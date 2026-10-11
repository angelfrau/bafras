/* BAFRAS · documentos de trabajo en PDF: mediciones, mediciones ciegas, cuadros de precios
   nº 1 y nº 2, y cuadros de materiales, maquinaria y mano de obra.
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
    mediciones: {
      titulo: 'Mediciones', archivo: 'Mediciones',
      nota: 'Cantidad de cada partida en el presupuesto, sin precios.'
    },
    ciegas: {
      titulo: 'Mediciones ciegas', archivo: 'Mediciones_ciegas',
      nota: 'Para pedir ofertas: rellene el precio unitario y el importe de cada partida. Las cantidades son las del presupuesto.'
    },
    precios1: {
      titulo: 'Cuadro de precios nº 1', archivo: 'Cuadro_precios_1',
      nota: 'Precio unitario de venta de cada partida, sin IVA.'
    },
    precios2: {
      titulo: 'Cuadro de precios nº 2', archivo: 'Cuadro_precios_2',
      nota: 'Recursos, rendimientos y precios de cada partida, sin IVA. Cada importe de línea es rendimiento × precio, a céntimo: puede haber 0,01 € de diferencia con el precio de la partida.'
    },
    materiales: {
      titulo: 'Cuadro de materiales', archivo: 'Cuadro_materiales', grupo: 'materiales',
      total: 'Total materiales',
      nota: 'Cantidad total y precio de venta de cada material, sin IVA.'
    },
    maquinaria: {
      titulo: 'Cuadro de maquinaria', archivo: 'Cuadro_maquinaria', grupo: 'maquinaria',
      total: 'Total maquinaria', vacio: 'En este presupuesto no hay maquinaria.',
      nota: 'Cantidad total y precio de venta de cada máquina, sin IVA.'
    },
    mano: {
      titulo: 'Cuadro de mano de obra', archivo: 'Cuadro_mano_de_obra', grupo: 'mano',
      total: 'Total mano de obra',
      nota: 'Horas totales y precio de venta de cada categoría, sin IVA.'
    }
  };

  // Columnas de cada tabla: [ancho en mm, alineación, cabecera]. Todas suman 178 mm.
  function columnas(defs) {
    return defs.map(function (d) { return { w: d[0] * MM, alin: d[1], t: d[2] }; });
  }
  var COL_MEDICIONES = columnas([[22, 'L', 'Código'], [110, 'L', 'Descripción'], [11, 'C', 'Ud'], [35, 'C', 'Cantidad']]);
  var COL_PRECIOS1 = columnas([[22, 'L', 'Código'], [110, 'L', 'Descripción'], [11, 'C', 'Ud'], [35, 'C', 'Precio (€)']]);
  var COL_CIEGAS = columnas([[22, 'L', 'Código'], [66, 'L', 'Descripción'], [11, 'C', 'Ud'], [19, 'C', 'Cant.'], [28, 'C', 'Precio (€)'], [32, 'C', 'Importe (€)']]);
  var COL_DESCOMPOSICION = columnas([[22, 'L', 'Código'], [78, 'L', 'Descripción'], [11, 'C', 'Ud'], [19, 'C', 'Rend.'], [22, 'C', 'Precio (€)'], [26, 'C', 'Importe (€)']]);
  var COL_RECURSOS = columnas([[22, 'L', 'Código'], [78, 'L', 'Descripción'], [11, 'C', 'Ud'], [19, 'C', 'Cantidad'], [22, 'C', 'Precio (€)'], [26, 'C', 'Importe (€)']]);

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

  function sinDescomponerTxt(n) {
    var txt = n === 1 ? '1 partida sin descomposición' : n + ' partidas sin descomposición';
    return 'No incluye ' + txt + ' (precio directo), que no tienen recursos.';
  }

  // ---------- filas ----------

  // Partida en las mediciones: código, descripción y cantidad.
  function filaMedicion(ctx, p) {
    var c = COL_MEDICIONES;
    return {
      celdas: [
        B.celdaTxt(p.code, ctx.r, 7.5, PAL.gris, c[0].w),
        B.celdaDescripcion(ctx, p.resumen, p.texto, c[1].w),
        B.celdaTxt(B.unidadTxt(p.unidad), ctx.r, 8.5, PAL.tinta, c[2].w),
        B.celdaTxt(B.formatoNumero(p.cantidad, 0, 2), ctx.r, 8.5, PAL.tinta, c[3].w)
      ],
      filete: true, fondo: null
    };
  }

  // Partida en las mediciones ciegas: lo mismo, con precio e importe en blanco y más altura.
  function filaCiega(ctx, p) {
    var c = COL_CIEGAS;
    return {
      celdas: [
        B.celdaTxt(p.code, ctx.r, 7.5, PAL.gris, c[0].w),
        B.celdaDescripcion(ctx, p.resumen, p.texto, c[1].w),
        B.celdaTxt(B.unidadTxt(p.unidad), ctx.r, 8.5, PAL.tinta, c[2].w),
        B.celdaTxt(B.formatoNumero(p.cantidad, 0, 2), ctx.r, 8.5, PAL.tinta, c[3].w),
        B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[4].w),
        B.celdaTxt('', ctx.r, 8.5, PAL.tinta, c[5].w)
      ],
      filete: true, fondo: null, minAlto: 7 * MM
    };
  }

  // Partida en el cuadro nº 1: código, descripción, unidad y precio.
  function filaPrecio1(ctx, p) {
    var c = COL_PRECIOS1;
    return {
      celdas: [
        B.celdaTxt(p.codigo, ctx.r, 7.5, PAL.gris, c[0].w),
        B.celdaDescripcion(ctx, p.resumen, p.texto, c[1].w),
        B.celdaTxt(B.unidadTxt(p.unidad), ctx.r, 8.5, PAL.tinta, c[2].w),
        B.celdaTxt(BC3.euros(p.pvpUd), ctx.r, 8.5, PAL.tinta, c[3].w)
      ],
      filete: true, fondo: null
    };
  }

  // Recurso en un cuadro de recursos: cantidad total, precio e importe.
  function filaRecurso(ctx, x) {
    var c = COL_RECURSOS;
    return {
      celdas: [
        B.celdaTxt(x.codigo, ctx.r, 7.5, PAL.gris, c[0].w),
        B.celdaTxt(x.resumen, ctx.r, 8.5, PAL.tinta, c[1].w),
        B.celdaTxt(B.unidadTxt(x.unidad), ctx.r, 8.5, PAL.tinta, c[2].w),
        B.celdaTxt(B.formatoNumero(x.cantidad, 0, 4), ctx.r, 8.5, PAL.tinta, c[3].w),
        B.celdaTxt(B.formatoNumero(x.precio, 2, 4), ctx.r, 8.5, PAL.tinta, c[4].w),
        B.celdaTxt(BC3.euros(x.importe), ctx.r, 8.5, PAL.tinta, c[5].w)
      ],
      filete: true, fondo: null
    };
  }

  // Bloque de una partida en el cuadro nº 2: cabecera de la partida, sus líneas y su precio total.
  // Devuelve la lista de filas del bloque.
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
      d.lineas.forEach(function (l) {
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

    filas.push(B.filaSuma(ctx, c, 'Precio de la partida', BC3.euros(d.pvpUd), PAL.beige, false));
    return filas;
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

  function dibujarMediciones(ctx, r, ciega) {
    var cols = ciega ? COL_CIEGAS : COL_MEDICIONES;
    var filaDe = function (p) { return ciega ? filaCiega(ctx, p) : filaMedicion(ctx, p); };
    r.capitulos.forEach(function (c) { capituloConTabla(ctx, c, 2, cols, filaDe); });
    if (ciega) {
      // Total para que el proveedor lo rellene.
      var total = B.filaSuma(ctx, cols, 'Total sin IVA', '', PAL.beige, false);
      total.minAlto = 7 * MM;
      B.filaTabla(ctx, cols, total, function () { B.cabecera(ctx, LAT, cols); });
    }
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

  // Cuadro de materiales, maquinaria o mano de obra. lista: recursos de ese tipo.
  function dibujarRecursos(ctx, info, rec) {
    var lista = rec[info.grupo];
    if (!lista.length) {
      parrafo(ctx, info.vacio || 'No hay recursos de este tipo en el presupuesto.', ctx.r, 9, PAL.tinta);
    } else {
      var repetir = function () { B.cabecera(ctx, LAT, COL_RECURSOS); };
      repetir();
      lista.forEach(function (x) { B.filaTabla(ctx, COL_RECURSOS, filaRecurso(ctx, x), repetir); });
      var total = B.filaSuma(ctx, COL_RECURSOS, info.total, BC3.euros(Datos.totalImporte(lista)), PAL.beige, false);
      B.filaTabla(ctx, COL_RECURSOS, total, repetir);
    }
    if (rec.numSinDescomponer) {
      ctx.y += 4 * MM;
      parrafo(ctx, sinDescomponerTxt(rec.numSinDescomponer), ctx.r, 8, PAL.gris);
    }
  }

  // ---------- generación ----------

  function contenido(ctx, clave, datos, r) {
    var info = DOCUMENTOS[clave];
    if (clave === 'mediciones') return dibujarMediciones(ctx, r, false);
    if (clave === 'ciegas') return dibujarMediciones(ctx, r, true);
    if (clave === 'precios1') return dibujarPrecios1(ctx, Datos.cuadroPrecios1(r));
    if (clave === 'precios2') return dibujarPrecios2(ctx, Datos.cuadroPrecios2(r, datos));
    return dibujarRecursos(ctx, info, Datos.cuadrosRecursos(r, datos));
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
    claves: ['mediciones', 'ciegas', 'precios1', 'precios2', 'materiales', 'maquinaria', 'mano'],
    generar: generar,
    titulo: function (clave) { return DOCUMENTOS[clave].titulo; },
    archivo: function (clave) { return DOCUMENTOS[clave].archivo; }
  };
})();
