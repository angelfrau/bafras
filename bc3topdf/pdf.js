/* BAFRAS · presupuesto en PDF: portada a sangre (logo, título y datos), cuerpo A4 y resumen.
   Las medidas, los colores, las fuentes y las tablas básicas están en pdf-base.js.
   El BC3 no sale del dispositivo: la librería va incluida en vendor/. */
(function () {
  'use strict';

  var B = window.BC3PDFBase;
  var BC3 = window.BC3;
  var MM = B.MM, W = B.W, H = B.H, LAT = B.LAT, ANCHO = B.ANCHO, LIMITE = B.LIMITE;
  var CAB = B.CAB, PAL = B.PAL, COLS = B.COLS;
  var escribir = B.escribir, escribirCentrado = B.escribirCentrado, escribirEspaciado = B.escribirEspaciado;
  var envolver = B.envolver, bl = B.bl, rect = B.rect, filete = B.filete;
  var asegurar = B.asegurar, nuevaPagina = B.nuevaPagina;

  // Cabeceras de las partidas: código, descripción, ud, cantidad, precio e importe.
  var COLUMNAS_PARTIDAS = [
    { w: COLS[0], alin: 'L', t: 'Código' }, { w: COLS[1], alin: 'L', t: 'Descripción' },
    { w: COLS[2], alin: 'C', t: 'Ud' }, { w: COLS[3], alin: 'C', t: 'Cant.' },
    { w: COLS[4], alin: 'C', t: 'Precio (€)' }, { w: COLS[5], alin: 'C', t: 'Importe (€)' }
  ];

  function pad2(n) { return (n < 10 ? '0' : '') + n; }

  // Cantidad del presupuesto: entero, o dos decimales con coma.
  function cantTxt(n) {
    var r = Math.round(n * 100) / 100;
    if (Number.isInteger(r)) return String(r).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    return BC3.euros(Math.round(r * 100));
  }

  function logoBytes() { return B.bytesDe(window.BAFRAS_LOGO_PNG); }

  // Celdas de una partida del presupuesto: código, descripción, ud, cantidad, precio e importe.
  function celdasPartida(ctx, p, codigo) {
    return [
      B.celdaTxt(codigo, ctx.r, 7.5, PAL.gris, COLS[0]),
      B.celdaDescripcion(ctx, p.resumen, p.texto, COLS[1]),
      B.celdaTxt(B.unidadTxt(p.unidad), ctx.r, 8.5, PAL.tinta, COLS[2]),
      B.celdaTxt(cantTxt(p.cantidad), ctx.r, 8.5, PAL.tinta, COLS[3]),
      B.celdaTxt(BC3.euros(p.pvpUd), ctx.r, 8.5, PAL.tinta, COLS[4]),
      B.celdaTxt(BC3.euros(p.centimos), ctx.r, 8.5, PAL.tinta, COLS[5])
    ];
  }

  // Tabla de partidas de un capítulo. El código es capítulo y orden: 09.01, 04.01.01...
  // Si el capítulo tiene subcapítulos, la suma se llama «Partidas»; si no, «Subtotal».
  function tablaPartidas(ctx, partidas, base, nombre, conSub) {
    var repetir = function () { B.cabecera(ctx, LAT, COLUMNAS_PARTIDAS); };
    repetir();
    partidas.forEach(function (p, i) {
      var fila = { celdas: celdasPartida(ctx, p, base + '.' + pad2(i + 1)), filete: true, fondo: null };
      B.filaTabla(ctx, COLUMNAS_PARTIDAS, fila, repetir);
    });
    var suma = partidas.reduce(function (s, p) { return s + p.centimos; }, 0);
    var etiqueta = (conSub ? 'Partidas ' : 'Subtotal ') + base + ' · ' + nombre;
    B.filaTabla(ctx, COLUMNAS_PARTIDAS, B.filaSuma(ctx, COLUMNAS_PARTIDAS, etiqueta, BC3.euros(suma), PAL.papel, true), repetir);
  }

  // Capítulo (nivel 2) o subcapítulo (nivel 3): título, tabla de partidas, subcapítulos y,
  // si los tiene, el total del capítulo.
  function capitulo(ctx, c, nivel) {
    var base = c.code.replace('#', '');
    var partidas = c.hijos.filter(function (x) { return x.tipo === 'partida'; });
    var subs = c.hijos.filter(function (x) { return x.tipo === 'capitulo'; });

    // Espacio que debe quedar libre tras el título: la cabecera y la primera fila de partidas.
    var primeraFila = partidas.length
      ? CAB + B.alturaDeFila(COLUMNAS_PARTIDAS, { celdas: celdasPartida(ctx, partidas[0], base + '.01'), filete: true, fondo: null })
      : 20 * MM;
    B.tituloCapitulo(ctx, base + ' · ' + c.nombre, nivel, primeraFila);

    if (partidas.length) tablaPartidas(ctx, partidas, base, c.nombre, subs.length > 0);
    subs.forEach(function (s) { capitulo(ctx, s, nivel + 1); });
    if (subs.length) {
      var total = B.filaSuma(ctx, COLUMNAS_PARTIDAS, 'Total ' + base + ' · ' + c.nombre, BC3.euros(c.centimos), PAL.beige, false);
      B.filaTabla(ctx, COLUMNAS_PARTIDAS, total, null);
    }
  }

  // Resumen por capítulos: bloque que no se parte entre páginas, alineado a la derecha (110 mm).
  function entradasResumen(ctx, fila) {
    var f = fila.negrita ? ctx.b : ctx.r;
    return [
      { w: 84 * MM, alin: 'L', celda: B.celdaTxt(fila.t1, f, 8.5, PAL.tinta, 84 * MM) },
      { w: 26 * MM, alin: 'C', celda: B.celdaTxt(fila.t2, f, 8.5, PAL.tinta, 26 * MM) }
    ];
  }

  function bloqueResumen(ctx, r) {
    var lhT = 10.5 * 1.35, xRes = LAT + ANCHO - 110 * MM;
    var filas = r.capitulos.map(function (c) {
      return { t1: c.code.replace('#', '') + ' · ' + c.nombre, t2: BC3.euros(c.centimos), negrita: false, fondo: null, filete: true };
    });
    filas.push({ t1: 'Total sin IVA', t2: BC3.euros(r.subtotal), negrita: true, fondo: PAL.papel, filete: true });
    filas.push({ t1: 'IVA ' + r.ivaPct + ' %', t2: BC3.euros(r.iva), negrita: false, fondo: null, filete: true });
    filas.push({ t1: 'Total con IVA', t2: BC3.euros(r.total), negrita: true, fondo: PAL.beige, filete: false });

    var total = 10 * MM + lhT + 8 * MM + CAB;
    filas.forEach(function (f) { total += B.alturaFila(entradasResumen(ctx, f), f.filete); });
    if (ctx.y + total > LIMITE) nuevaPagina(ctx); else ctx.y += 10 * MM;

    escribir(ctx, 'Resumen', LAT, bl(ctx.y, lhT, 10.5), ctx.b, 10.5, PAL.pino);
    ctx.y += lhT;
    filete(ctx, LAT, LAT + ANCHO, ctx.y + 1.15 * MM, 0.3 * MM, PAL.linea);
    ctx.y += 8 * MM; // aire entre el filete del resumen y la tabla
    B.cabecera(ctx, xRes, [{ w: 84 * MM, alin: 'L', t: 'Capítulo' }, { w: 26 * MM, alin: 'C', t: 'Importe (€)' }]);
    filas.forEach(function (f) {
      var e = entradasResumen(ctx, f);
      B.dibujarFila(ctx, xRes, e, B.alturaFila(e, f.filete), f.fondo, f.filete);
    });
  }

  function cuerpo(ctx, r, m) {
    var lhT = 15 * 1.35, lhM = 8.5 * 1.35;
    envolver(ctx.b, m.titulo, 15, ANCHO).forEach(function (l) {
      asegurar(ctx, lhT, null);
      escribir(ctx, l, LAT, bl(ctx.y, lhT, 15), ctx.b, 15, PAL.pino);
      ctx.y += lhT;
    });
    ctx.y += 1 * MM;
    // Cabecera del cuerpo: revisión · fecha (el título va arriba).
    envolver(ctx.r, 'Revisión ' + m.rev + ' · ' + m.fecha, 8.5, ANCHO).forEach(function (l) {
      asegurar(ctx, lhM, null);
      escribir(ctx, l, LAT, bl(ctx.y, lhM, 8.5), ctx.r, 8.5, PAL.gris);
      ctx.y += lhM;
    });
    ctx.y += 5 * MM;
    r.capitulos.forEach(function (c) { capitulo(ctx, c, 2); });
    bloqueResumen(ctx, r);
  }

  // Portada: página completa en beige, logo arriba (47,33 mm), datos abajo (47,33 mm) y el bloque
  // del rótulo y el título centrado entre ambos, igual que en style.css.
  function portada(ctx, m, logo) {
    rect(ctx, 0, 0, W, H, PAL.beige);

    var anchoLogo = 134 * MM, altoLogo = anchoLogo * 273 / 1281, topLogo = 47.33 * MM;
    ctx.pg.drawImage(logo, { x: (W - anchoLogo) / 2, y: H - topLogo - altoLogo, width: anchoLogo, height: altoLogo });
    var finLogo = topLogo + altoLogo;

    // Datos: rejilla de 150 mm, columnas de 65 mm separadas 20 mm, filas separadas 16 mm.
    var x0 = (W - 150 * MM) / 2, cx = [x0 + 32.5 * MM, x0 + 117.5 * MM];
    var dtLH = 6.5 * 1.2, ddLH = 10 * 1.2, dtMB = 1.2 * MM;
    var datos = [
      { dt: 'Cliente', dd: m.cliente || '—' },
      { dt: 'Emplazamiento', dd: m.emplazamiento || '—' },
      { dt: 'Expediente', dd: m.expediente || '—' },
      { dt: 'Revisión · fecha', dd: m.rev + ' · ' + m.fecha }
    ];
    datos.forEach(function (d) {
      d.lineas = envolver(ctx.r, d.dd, 10, 65 * MM);
      d.alto = dtLH + dtMB + d.lineas.length * ddLH;
    });
    var fila1 = Math.max(datos[0].alto, datos[1].alto), fila2 = Math.max(datos[2].alto, datos[3].alto);
    var topDatos = H - 47.33 * MM - (fila1 + 16 * MM + fila2);
    var topFila = [topDatos, topDatos + fila1 + 16 * MM];
    datos.forEach(function (d, i) {
      var x = cx[i % 2], y = topFila[i >> 1], yy;
      escribirEspaciado(ctx, d.dt.toUpperCase(), x, bl(y, dtLH, 6.5), ctx.b, 6.5, PAL.grisSuave, 0.2 * 6.5);
      yy = y + dtLH + dtMB;
      d.lineas.forEach(function (l) {
        escribirCentrado(ctx, l, x, bl(yy, ddLH, 10), ctx.r, 10, PAL.pino);
        yy += ddLH;
      });
    });

    // Título: máximo 160 mm; el tamaño depende del número de líneas (38/37/35/30 pt), como en la web.
    var n = Math.max(1, Math.min(envolver(ctx.b, m.titulo, 38, 160 * MM).length, 4));
    var tam = [38, 37, 35, 30][n - 1], lhT = tam * (n === 4 ? 0.95 : 1.05);
    var lineas = envolver(ctx.b, m.titulo, tam, 160 * MM);
    var lhE = 10.5 * 1.3, mbE = 4 * MM;
    var altoBloque = lhE + mbE + lineas.length * lhT;
    var topBloque = (finLogo + topDatos) / 2 - altoBloque / 2;
    escribirEspaciado(ctx, 'PRESUPUESTO', W / 2, bl(topBloque, lhE, 10.5), ctx.b, 10.5, PAL.grisSuave, 0.14 * 10.5);
    var y = topBloque + lhE + mbE;
    lineas.forEach(function (l) {
      escribirCentrado(ctx, l, W / 2, bl(y, lhT, tam), ctx.b, tam, PAL.pino);
      y += lhT;
    });
  }

  // r: resultado de BC3.calcular (precios de venta). m: datos de portada del formulario.
  // Devuelve una promesa con los bytes del PDF.
  function generar(r, m) {
    return B.abrirDocumento(m.titulo).then(function (ctx) {
      // La portada es la primera página; el pie aparece desde la segunda (índice 1).
      return ctx.doc.embedPng(logoBytes()).then(function (logo) {
        nuevaPagina(ctx);
        portada(ctx, m, logo);
        nuevaPagina(ctx);
        cuerpo(ctx, r, m);
        B.pies(ctx, 1);
        return ctx.doc.save();
      });
    });
  }

  window.BC3PDF = { generar: generar };
})();
