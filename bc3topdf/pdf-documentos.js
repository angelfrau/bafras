/* BAFRAS · documentos de trabajo en PDF: mediciones ciegas y cuadros de precios nº 1 y nº 2.
   Los datos salen de documentos.js (BC3Docs); el dibujo, de pdf-base.js (BC3PDFBase).
   Cada documento es un PDF aparte, con la misma letra, colores y tablas que el presupuesto. */
(function () {
  'use strict';

  var B = window.BC3PDFBase;
  var Datos = window.BC3Docs;
  var BC3 = window.BC3;
  var MM = B.MM, LAT = B.LAT, ANCHO = B.ANCHO, PAL = B.PAL;

  // Título, nombre de archivo y texto de cada documento.
  var DOCUMENTOS = {
    ciegas: {
      titulo: 'Mediciones ciegas', archivo: 'Mediciones_ciegas',
      nota: 'Para pedir ofertas: rellene el precio unitario y el importe de cada partida. Las cantidades son las del presupuesto.'
    },
    precios1: {
      titulo: 'Cuadro de precios nº 1', archivo: 'Cuadro_precios_1',
      nota: 'Precio unitario de venta de cada unidad de obra, sin IVA, en cifra y en letra. Tiene carácter contractual.'
    },
    precios2: {
      titulo: 'Cuadro de precios nº 2', archivo: 'Cuadro_precios_2',
      nota: 'Descomposición de cada partida en materiales, mano de obra, maquinaria y otros servicios, con su rendimiento y su precio por unidad, sin IVA. Sirve para calcular y abonar partes de obra en caso de rescisión o de contratos incompletos. Cada importe es rendimiento × precio, a céntimo; si los recursos no suman el precio de la partida, la diferencia aparece como redondeo.'
    }
  };

  // Columnas de cada tabla: [ancho en mm, alineación, cabecera]. Todas suman 178 mm.
  function columnas(defs) {
    return defs.map(function (d) { return { w: d[0] * MM, alin: d[1], t: d[2] }; });
  }
  var COL_PRECIOS1 = columnas([[22, 'L', 'Código'], [110, 'L', 'Descripción'], [11, 'C', 'Ud'], [35, 'C', 'Precio (€)']]);
  var COL_CIEGAS = columnas([[22, 'L', 'Código'], [66, 'L', 'Descripción'], [11, 'C', 'Ud'], [19, 'C', 'Cant.'], [28, 'C', 'Precio (€)'], [32, 'C', 'Importe (€)']]);
  var COL_DESCOMPOSICION = columnas([[22, 'L', 'Código'], [78, 'L', 'Descripción'], [11, 'C', 'Ud'], [19, 'C', 'Rend.'], [22, 'C', 'Precio (€)'], [26, 'C', 'Importe (€)']]);

  // ---------- texto ----------

  // Párrafo envuelto en el ancho útil; avanza ctx.y.
  function parrafo(ctx, texto, f, tam, hex) {
    var lh = tam * 1.35;
    B.envolver(f, texto, tam, ANCHO).forEach(function (l) {
      B.asegurar(ctx, lh, null);
      B.escribir(ctx, l, LAT, B.bl(ctx.y, lh, tam), f, tam, hex);
      ctx.y += lh;
    });
  }

  // Primera página de cada documento: título, obra y revisión, y una nota corta.
  function cabeceraDocumento(ctx, info, m) {
    parrafo(ctx, info.titulo, ctx.b, 15, PAL.pino);
    ctx.y += 1 * MM;
    parrafo(ctx, m.titulo + ' · Revisión ' + m.rev + ' · ' + m.fecha, ctx.r, 8.5, PAL.gris);
    ctx.y += 3 * MM;
    parrafo(ctx, info.nota, ctx.r, 8, PAL.tinta);
    ctx.y += 6 * MM;
  }

  // ---------- filas ----------

  // Partida en las mediciones ciegas: lo mismo, con precio e importe en blanco y más altura.
  // «codigo» es el código de presupuesto de esta aparición de la partida (01.01).
  function filaCiega(ctx, p, codigo) {
    var c = COL_CIEGAS;
    return {
      celdas: [
        B.celdaTxt(codigo, ctx.r, 7.5, PAL.gris, c[0].w),
        B.celdaDescripcion(ctx, p.resumen, p.texto, c[1].w),
        B.celdaTxt(B.unidadTxt(p.unidad), ctx.r, 8.5, PAL.tinta, c[2].w),
        B.celdaTxt(B.formatoNumero(p.cantidad, 0, 2), ctx.r, 8.5, PAL.tinta, c[3].w),
        B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[4].w),
        B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[5].w)
      ],
      filete: true, fondo: null, minAlto: 7 * MM
    };
  }

  // Partida en el cuadro nº 1: código, descripción (con el precio en letra), unidad y precio.
  function filaPrecio1(ctx, p) {
    var c = COL_PRECIOS1;
    var descripcion = B.celdaDescripcion(ctx, p.resumen, p.texto, c[1].w);
    descripcion.bloques.push({
      lineas: B.envolver(ctx.r, 'Precio en letra: ' + Datos.importeEnLetra(p.pvpUd), 8, c[1].w - 2 * B.PAD_H),
      f: ctx.r, tam: 8, lh: 8 * 1.35, hex: PAL.gris, mt: 0.6 * MM
    });
    return {
      celdas: [
        B.celdaTxt(p.codigo, ctx.r, 7.5, PAL.gris, c[0].w),
        descripcion,
        B.celdaTxt(B.unidadTxt(p.unidad), ctx.r, 8.5, PAL.tinta, c[2].w),
        B.celdaTxt(BC3.euros(p.pvpUd), ctx.r, 8.5, PAL.tinta, c[3].w)
      ],
      filete: true, fondo: null
    };
  }

  // Grupos de recursos de una partida del cuadro nº 2, en el orden del pliego: [tipo, rótulo].
  var GRUPOS_RECURSOS = [['materiales', 'Materiales'], ['mano', 'Mano de obra'], ['maquinaria', 'Maquinaria'], ['otros', 'Otros (servicios)']];

  // Bloque de una partida en el cuadro nº 2: cabecera de la partida, sus recursos agrupados por tipo
  // (con el subtotal de cada grupo), el redondeo y su precio total. Devuelve la lista de filas del bloque.
  function filasDescomposicion(ctx, d) {
    var c = COL_DESCOMPOSICION;
    var filas = [{
      celdas: [
        B.celdaTxt(d.codigo, ctx.r, 7.5, PAL.gris, c[0].w),
        B.celdaTxt(d.resumen, ctx.b, 8.5, PAL.pino, c[1].w),
        B.celdaTxt(B.unidadTxt(d.unidad), ctx.r, 8.5, PAL.tinta, c[2].w),
        B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[3].w),
        B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[4].w),
        B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[5].w)
      ],
      filete: true, fondo: PAL.papel
    }];

    if (d.descompuesta) {
      GRUPOS_RECURSOS.forEach(function (g) {
        var lineas = d.lineas.filter(function (l) { return l.tipo === g[0]; });
        if (!lineas.length) return;
        var subtotal = lineas.reduce(function (s, l) { return s + l.importe; }, 0);
        filas.push({
          celdas: [
            B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[0].w),
            B.celdaTxt(g[1], ctx.b, 8.5, PAL.pino, c[1].w),
            B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[2].w),
            B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[3].w),
            B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[4].w),
            B.celdaTxt(BC3.euros(subtotal), ctx.b, 8.5, PAL.pino, c[5].w)
          ],
          filete: false, fondo: null
        });
        lineas.forEach(function (l) {
          filas.push({
            celdas: [
              B.celdaTxt(l.codigo, ctx.r, 7.5, PAL.gris, c[0].w),
              B.celdaTxt(l.resumen, ctx.r, 8.5, PAL.tinta, c[1].w),
              B.celdaTxt(B.unidadTxt(l.unidad), ctx.r, 8.5, PAL.tinta, c[2].w),
              B.celdaTxt(B.formatoNumero(l.rendimiento, 0, 4), ctx.r, 8.5, PAL.tinta, c[3].w),
              B.celdaTxt(B.formatoNumero(l.precio, 2, 4), ctx.r, 8.5, PAL.tinta, c[4].w),
              B.celdaTxt(BC3.euros(l.importe), ctx.r, 8.5, PAL.tinta, c[5].w)
            ],
            filete: true, fondo: null
          });
        });
      });
    } else {
      filas.push({
        celdas: [
          B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[0].w),
          B.celdaTxt('Partida de precio directo, sin descomposición.', ctx.r, 8, PAL.gris, c[1].w),
          B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[2].w),
          B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[3].w),
          B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[4].w),
          B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[5].w)
        ],
        filete: true, fondo: null
      });
    }

    if (d.redondeo) {
      filas.push({
        celdas: [
          B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[0].w),
          B.celdaTxt('Redondeo a céntimo', ctx.r, 8, PAL.gris, c[1].w),
          B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[2].w),
          B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[3].w),
          B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[4].w),
          B.celdaTxt(BC3.euros(d.redondeo), ctx.r, 8.5, PAL.tinta, c[5].w)
        ],
        filete: true, fondo: null
      });
    }
    filas.push(B.filaSuma(ctx, c, 'Precio de la partida', BC3.euros(d.pvpUd), PAL.beige, false));
    return filas;
  }

  // Conciliación con el presupuesto, al final del cuadro nº 2: recursos + partidas directas +
  // redondeos = presupuesto sin IVA. Cada fila es una línea de importe; la última, el total.
  function filaConciliacion(ctx, etiqueta, importe, negrita, fondo) {
    var c = COL_DESCOMPOSICION, f = negrita ? ctx.b : ctx.r;
    var ancho = c.slice(0, -1).reduce(function (s, col) { return s + col.w; }, 0);
    return {
      total: true,
      celdas: [
        B.celdaTxt(etiqueta, f, 8.5, PAL.tinta, ancho),
        B.celdaTxt(importe, f, 8.5, PAL.tinta, c[c.length - 1].w)
      ],
      fondo: fondo, filete: true
    };
  }

  function dibujarConciliacion(ctx, con) {
    var filas = [
      filaConciliacion(ctx, 'Materiales', BC3.euros(con.materiales), false, null),
      filaConciliacion(ctx, 'Mano de obra', BC3.euros(con.mano), false, null),
      filaConciliacion(ctx, 'Maquinaria', BC3.euros(con.maquinaria), false, null),
      filaConciliacion(ctx, 'Otros (servicios)', BC3.euros(con.otros), false, null),
      filaConciliacion(ctx, 'Partidas de precio directo', BC3.euros(con.directas), false, null),
      filaConciliacion(ctx, 'Redondeo del precio de cada partida', BC3.euros(con.redondeoPartidas), false, null),
      filaConciliacion(ctx, 'Redondeo a céntimo de los importes', BC3.euros(con.redondeoImportes), false, null),
      filaConciliacion(ctx, 'Presupuesto sin IVA', BC3.euros(con.total), true, PAL.beige)
    ];
    var alto = filas.reduce(function (s, f) { return s + B.alturaDeFila(COL_DESCOMPOSICION, f); }, 0);
    ctx.y += 6 * MM;
    B.asegurarBloque(ctx, 14 * MM + alto, null);
    parrafo(ctx, 'Conciliación con el presupuesto', ctx.b, 10, PAL.pino);
    parrafo(ctx, 'El presupuesto redondea a céntimo el precio de cada partida; los recursos se valoran con su precio exacto. La diferencia es el redondeo.', ctx.r, 8, PAL.gris);
    ctx.y += 2 * MM;
    filas.forEach(function (f) { B.filaTabla(ctx, COL_DESCOMPOSICION, f, null); });
  }

  // ---------- contenido de cada documento ----------

  // Un capítulo con su tabla de partidas. filaDe(p) devuelve la fila de cada partida.
  // Después vienen los subcapítulos, con el mismo formato y un nivel más abajo.
  function capituloConTabla(ctx, c, nivel, cols, filaDe) {
    var base = c.code.replace('#', '');
    var partidas = c.hijos.filter(function (x) { return x.tipo === 'partida'; });
    var subs = c.hijos.filter(function (x) { return x.tipo === 'capitulo'; });
    var filas = partidas.map(filaDe);

    // Como en el presupuesto: el título no se queda solo al final de una página.
    var primera = filas.length ? B.CAB + B.alturaDeFila(cols, filas[0]) : 20 * MM;
    B.tituloCapitulo(ctx, base + ' · ' + c.nombre, nivel, primera);
    if (filas.length) B.tabla(ctx, cols, filas);
    subs.forEach(function (s) { capituloConTabla(ctx, s, nivel + 1, cols, filaDe); });
  }

  // Mediciones ciegas: capítulos con su tabla y, al final, el total para que el proveedor lo rellene.
  function dibujarCiegas(ctx, r) {
    var cols = COL_CIEGAS, codigos = Datos.codigosPresupuesto(r);
    r.capitulos.forEach(function (c) {
      capituloConTabla(ctx, c, 2, cols, function (p) { return filaCiega(ctx, p, codigos.get(p)); });
    });
    var total = B.filaSuma(ctx, cols, 'Total sin IVA', '', PAL.beige, false);
    total.minAlto = 7 * MM;
    B.filaTabla(ctx, cols, total, function () { B.cabecera(ctx, LAT, cols); });
  }

  function dibujarPrecios1(ctx, lista) {
    B.tabla(ctx, COL_PRECIOS1, lista.map(function (p) { return filaPrecio1(ctx, p); }));
  }

  // Cada bloque (una partida y sus líneas) no se parte entre páginas si cabe en una.
  function dibujarPrecios2(ctx, lista) {
    var repetir = function () { B.cabecera(ctx, LAT, COL_DESCOMPOSICION); };
    repetir();
    lista.forEach(function (d) {
      var filas = filasDescomposicion(ctx, d);
      var alto = filas.reduce(function (s, f) { return s + B.alturaDeFila(COL_DESCOMPOSICION, f); }, 0);
      B.asegurarBloque(ctx, alto, repetir);
      filas.forEach(function (f) { B.filaTabla(ctx, COL_DESCOMPOSICION, f, repetir); });
    });
  }

  // ---------- generación ----------

  function contenido(ctx, clave, datos, r) {
    if (clave === 'ciegas') return dibujarCiegas(ctx, r);
    if (clave === 'precios1') return dibujarPrecios1(ctx, Datos.cuadroPrecios1(r));
    dibujarPrecios2(ctx, Datos.cuadroPrecios2(r, datos));
    return dibujarConciliacion(ctx, Datos.conciliacion(r, datos));
  }

  // Devuelve una promesa con los bytes del PDF del documento «clave».
  //   datos: BC3 leído (parsear). r: resultado de BC3.calcular. m: datos de portada del formulario.
  function generar(clave, datos, r, m) {
    var info = DOCUMENTOS[clave];
    if (!info) return Promise.reject(new Error('documento desconocido: ' + clave));
    return B.abrirDocumento(info.titulo + ' · ' + m.titulo).then(function (ctx) {
      B.nuevaPagina(ctx);
      cabeceraDocumento(ctx, info, m);
      contenido(ctx, clave, datos, r);
      B.pies(ctx, 0);
      return ctx.doc.save();
    });
  }

  window.BC3PDFDocs = {
    claves: ['ciegas', 'precios1', 'precios2'],
    generar: generar,
    archivo: function (clave) { return DOCUMENTOS[clave].archivo; }
  };
})();
