/* BAFRAS · BC3 a PDF: genera el PDF en el propio navegador (pdf-lib).
   Replica la vista previa: portada a sangre (logo, título y datos), cuerpo A4 con márgenes
   de 22/16/20 mm, tablas con la cabecera repetida y pie «Página N de M».
   El BC3 no sale del dispositivo: la librería va incluida en vendor/. */
(function () {
  'use strict';

  var BC3 = window.BC3;
  var MM = 72 / 25.4;                          // puntos por milímetro
  var W = 210 * MM, H = 297 * MM;              // A4
  var LAT = 16 * MM, ANCHO = W - 2 * LAT;      // márgenes laterales y ancho útil (178 mm)
  var SUP = 22 * MM;                           // margen superior del cuerpo
  var LIMITE = H - 20 * MM;                    // límite inferior del texto, medido desde arriba
  var PAD_V = 1.6 * MM, PAD_H = 1.5 * MM;      // relleno de celdas (style.css)
  var COLS = [19, 84, 11, 16, 22, 26].map(function (v) { return v * MM; }); // c-cod, desc, c-ud, c-cant, c-pre, c-imp
  var CAB = 2 * 1.2 * MM + 8.5 * 1.35 + 0.4 * MM; // cabecera de tabla: relleno, texto y filete pino
  var PAL = {
    beige: '#ECE8DD', papel: '#F7F5F0', pino: '#0E2B25', verde: '#1A7A5A',
    tinta: '#2A2A2A', gris: '#4A5550', grisSuave: '#7A8580', linea: '#D8D2C3'
  };
  // Caracteres de Windows-1252 fuera de Latin-1 (la fuente estándar del PDF sí los escribe).
  var EXTRA = '€‚ƒ„…†‡ˆ‰Š‹ŒŽ' +
    '‘’“”•–—˜™š›œžŸ';

  function pad2(n) { return (n < 10 ? '0' : '') + n; }

  // Igual que app.js: un lote no existe en el presupuesto y se muestra como «ud».
  function unidadTxt(u) { return /^lote$/i.test(u || '') ? 'ud' : (u || ''); }
  function cantTxt(n) {
    var r = Math.round(n * 100) / 100;
    if (Number.isInteger(r)) return String(r).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    return BC3.euros(Math.round(r * 100));
  }

  function logoBytes() {
    var b64 = String(window.BAFRAS_LOGO_PNG || '').split(',')[1] || '';
    var bin = atob(b64), out = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
    return out;
  }

  function rgb(hex) {
    var n = parseInt(hex.slice(1), 16);
    return window.PDFLib.rgb(((n >> 16) & 255) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255);
  }

  // Solo caracteres que la fuente estándar escribe; los tabuladores y saltos pasan a espacio.
  function limpiar(s) {
    return Array.from(String(s == null ? '' : s)).map(function (ch) {
      var c = ch.codePointAt(0);
      if (c === 9 || c === 10 || c === 13) return ' ';
      if (c < 32 || (c >= 127 && c < 160)) return '';
      if (c <= 255 || EXTRA.indexOf(ch) !== -1) return ch;
      return '?';
    }).join('');
  }

  // Línea base (en puntos, medida desde arriba) de un texto centrado en su línea de altura lh.
  function bl(top, lh, tam) { return top + lh / 2 + 0.3465 * tam; }

  // Parte un texto en líneas de ancho máximo (en puntos), palabra a palabra.
  function envolver(f, s, tam, anchoMax) {
    var palabras = limpiar(s).split(/\s+/).filter(function (p) { return p !== ''; });
    var lineas = [], actual = null;
    palabras.forEach(function (p) {
      if (actual === null) { actual = p; return; }
      var prueba = actual + ' ' + p;
      if (f.widthOfTextAtSize(prueba, tam) <= anchoMax) actual = prueba;
      else { lineas.push(actual); actual = p; }
    });
    if (actual !== null) lineas.push(actual);
    return lineas;
  }

  // ---------- dibujo ----------
  function escribir(ctx, s, x, base, f, tam, hex) {
    if (!s) return;
    ctx.pg.drawText(s, { x: x, y: H - base, size: tam, font: f, color: rgb(hex) });
  }
  function escribirCentrado(ctx, s, cx, base, f, tam, hex) {
    if (!s) return;
    escribir(ctx, s, cx - f.widthOfTextAtSize(s, tam) / 2, base, f, tam, hex);
  }
  // Interletrado (letter-spacing de CSS): el espacio se suma tras cada carácter, también el último.
  function escribirEspaciado(ctx, s, cx, base, f, tam, hex, sp) {
    var letras = Array.from(s), total = 0, x;
    letras.forEach(function (ch) { total += f.widthOfTextAtSize(ch, tam) + sp; });
    x = cx - total / 2;
    letras.forEach(function (ch) {
      escribir(ctx, ch, x, base, f, tam, hex);
      x += f.widthOfTextAtSize(ch, tam) + sp;
    });
  }
  function rect(ctx, x, top, w, h, hex) {
    ctx.pg.drawRectangle({ x: x, y: H - top - h, width: w, height: h, color: rgb(hex) });
  }
  // Filete horizontal; y se mide desde arriba, en el centro del grosor.
  function filete(ctx, x1, x2, y, grosor, hex) {
    ctx.pg.drawLine({ start: { x: x1, y: H - y }, end: { x: x2, y: H - y }, thickness: grosor, color: rgb(hex) });
  }
  function nuevaPagina(ctx) {
    ctx.pg = ctx.doc.addPage([W, H]);
    ctx.y = SUP;
  }
  // Si el bloque no cabe en la página, pasa a la siguiente y repite la cabecera de la tabla si la hay.
  function asegurar(ctx, alto, repetir) {
    if (ctx.y + alto <= LIMITE) return;
    nuevaPagina(ctx);
    if (repetir) repetir();
  }

  // ---------- celdas y filas ----------
  function celda(lineas, f, tam, lh, hex, mt) {
    return { bloques: [{ lineas: lineas, f: f, tam: tam, lh: lh, hex: hex, mt: mt || 0 }] };
  }
  function celdaTxt(s, f, tam, hex, ancho) {
    return celda(envolver(f, s, tam, ancho - 2 * PAD_H), f, tam, tam * 1.35, hex, 0);
  }
  function alturaCelda(c) {
    return c.bloques.reduce(function (h, b) { return h + b.mt + b.lineas.length * b.lh; }, 0);
  }
  function alturaFila(entradas, conFilete) {
    var h = 0;
    entradas.forEach(function (e) { h = Math.max(h, alturaCelda(e.celda)); });
    return h + 2 * PAD_V + (conFilete ? 0.2 * MM : 0);
  }
  function pintarCelda(ctx, c, x, ancho, arriba, alin) {
    var y = arriba;
    c.bloques.forEach(function (b) {
      y += b.mt;
      b.lineas.forEach(function (l) {
        var base = bl(y, b.lh, b.tam);
        if (alin === 'C') escribirCentrado(ctx, l, x + ancho / 2, base, b.f, b.tam, b.hex);
        else escribir(ctx, l, x + PAD_H, base, b.f, b.tam, b.hex);
        y += b.lh;
      });
    });
  }
  // Dibuja una fila en la posición actual: entradas [{w, alin, celda}] desde xIni.
  function dibujarFila(ctx, xIni, entradas, alto, fondo, conFilete) {
    var ancho = entradas.reduce(function (s, e) { return s + e.w; }, 0), x = xIni;
    if (fondo) rect(ctx, xIni, ctx.y, ancho, alto - (conFilete ? 0.2 * MM : 0), fondo);
    entradas.forEach(function (e) {
      pintarCelda(ctx, e.celda, x, e.w, ctx.y + PAD_V, e.alin);
      x += e.w;
    });
    if (conFilete) filete(ctx, xIni, x, ctx.y + alto - 0.1 * MM, 0.2 * MM, PAL.linea);
    ctx.y += alto;
  }
  // Cabecera de tabla: negrita pino y filete inferior de 0,4 mm.
  function cabecera(ctx, xIni, entradas) {
    var x = xIni, base = bl(ctx.y + 1.2 * MM, 8.5 * 1.35, 8.5);
    entradas.forEach(function (e) {
      if (e.alin === 'C') escribirCentrado(ctx, e.t, x + e.w / 2, base, ctx.b, 8.5, PAL.pino);
      else escribir(ctx, e.t, x + PAD_H, base, ctx.b, 8.5, PAL.pino);
      x += e.w;
    });
    filete(ctx, xIni, x, ctx.y + CAB - 0.2 * MM, 0.4 * MM, PAL.pino);
    ctx.y += CAB;
  }
  function cabPartidas(ctx) {
    cabecera(ctx, LAT, [
      { w: COLS[0], alin: 'L', t: 'Código' }, { w: COLS[1], alin: 'L', t: 'Descripción' },
      { w: COLS[2], alin: 'C', t: 'Ud' }, { w: COLS[3], alin: 'C', t: 'Cant.' },
      { w: COLS[4], alin: 'C', t: 'Precio (€)' }, { w: COLS[5], alin: 'C', t: 'Importe (€)' }
    ]);
  }

  // Celdas de una partida: código, descripción (negrita + texto), ud, cantidad, precio y importe.
  function celdasPartida(ctx, p, codigo) {
    var anchoDesc = COLS[1] - 2 * PAD_H;
    var bloques = [{ lineas: envolver(ctx.b, p.resumen, 8.5, anchoDesc), f: ctx.b, tam: 8.5, lh: 8.5 * 1.35, hex: PAL.pino, mt: 0 }];
    if (p.texto) bloques.push({ lineas: envolver(ctx.r, p.texto, 7.8, anchoDesc), f: ctx.r, tam: 7.8, lh: 7.8 * 1.35, hex: PAL.tinta, mt: 0.6 * MM });
    return [
      { w: COLS[0], alin: 'L', celda: celdaTxt(codigo, ctx.r, 7.5, PAL.gris, COLS[0]) },
      { w: COLS[1], alin: 'L', celda: { bloques: bloques } },
      { w: COLS[2], alin: 'C', celda: celdaTxt(unidadTxt(p.unidad), ctx.r, 8.5, PAL.tinta, COLS[2]) },
      { w: COLS[3], alin: 'C', celda: celdaTxt(cantTxt(p.cantidad), ctx.r, 8.5, PAL.tinta, COLS[3]) },
      { w: COLS[4], alin: 'C', celda: celdaTxt(BC3.euros(p.pvpUd), ctx.r, 8.5, PAL.tinta, COLS[4]) },
      { w: COLS[5], alin: 'C', celda: celdaTxt(BC3.euros(p.centimos), ctx.r, 8.5, PAL.tinta, COLS[5]) }
    ];
  }

  // Fila de suma de una tabla de partidas: la etiqueta ocupa las cinco primeras columnas.
  function filaSuma(ctx, etiqueta, importe, fondo, conFilete, repetir) {
    var ancho5 = COLS[0] + COLS[1] + COLS[2] + COLS[3] + COLS[4];
    var entradas = [
      { w: ancho5, alin: 'L', celda: celdaTxt(etiqueta, ctx.b, 8.5, PAL.tinta, ancho5) },
      { w: COLS[5], alin: 'C', celda: celdaTxt(importe, ctx.b, 8.5, PAL.tinta, COLS[5]) }
    ];
    var alto = alturaFila(entradas, conFilete);
    asegurar(ctx, alto, repetir);
    dibujarFila(ctx, LAT, entradas, alto, fondo, conFilete);
  }

  function tablaPartidas(ctx, partidas, base, nombre, conSub) {
    var repetir = function () { cabPartidas(ctx); };
    cabPartidas(ctx);
    partidas.forEach(function (p, i) {
      var celdas = celdasPartida(ctx, p, base + '.' + pad2(i + 1));
      var alto = alturaFila(celdas, true);
      asegurar(ctx, alto, repetir);
      dibujarFila(ctx, LAT, celdas, alto, null, true);
    });
    var suma = partidas.reduce(function (s, p) { return s + p.centimos; }, 0);
    filaSuma(ctx, (conSub ? 'Partidas ' : 'Subtotal ') + base + ' · ' + nombre, BC3.euros(suma), PAL.papel, true, repetir);
  }

  // Capítulo (h2) o subcapítulo (h3): título, tabla de partidas, subcapítulos y total si los tiene.
  function capitulo(ctx, c, nivel) {
    var base = c.code.replace('#', ''), h2 = nivel === 2;
    var tam = h2 ? 10.5 : 9, lh = tam * 1.35;
    var mt = (h2 ? 7 : 4) * MM, mb = (h2 ? 2 : 1.5) * MM;
    var pb = h2 ? 1.3 * MM : 0;                   // h2: relleno inferior 1 mm y filete de 0,3 mm
    var lineas = envolver(ctx.b, base + ' · ' + c.nombre, tam, ANCHO);
    var partidas = c.hijos.filter(function (x) { return x.tipo === 'partida'; });
    var subs = c.hijos.filter(function (x) { return x.tipo === 'capitulo'; });
    // El título no se queda solo al final de la página: va con su cabecera y su primera fila.
    var reserva = mt + lineas.length * lh + pb + mb;
    if (partidas.length) reserva += CAB + alturaFila(celdasPartida(ctx, partidas[0], base + '.01'), true);
    else reserva += 20 * MM;
    if (ctx.y + reserva > LIMITE) nuevaPagina(ctx); else ctx.y += mt;
    lineas.forEach(function (l) {
      escribir(ctx, l, LAT, bl(ctx.y, lh, tam), ctx.b, tam, h2 ? PAL.pino : PAL.verde);
      ctx.y += lh;
    });
    if (h2) filete(ctx, LAT, LAT + ANCHO, ctx.y + 1.15 * MM, 0.3 * MM, PAL.linea);
    ctx.y += pb + mb;
    if (partidas.length) tablaPartidas(ctx, partidas, base, c.nombre, subs.length > 0);
    subs.forEach(function (s) { capitulo(ctx, s, nivel + 1); });
    if (subs.length) filaSuma(ctx, 'Total ' + base + ' · ' + c.nombre, BC3.euros(c.centimos), PAL.beige, false, null);
  }

  function entradasRes(ctx, fila) {
    var f = fila.negrita ? ctx.b : ctx.r;
    return [
      { w: 84 * MM, alin: 'L', celda: celdaTxt(fila.t1, f, 8.5, PAL.tinta, 84 * MM) },
      { w: 26 * MM, alin: 'C', celda: celdaTxt(fila.t2, f, 8.5, PAL.tinta, 26 * MM) }
    ];
  }

  // Resumen por capítulos: bloque que no se parte entre páginas, alineado a la derecha (110 mm).
  function bloqueResumen(ctx, r) {
    var lhT = 10.5 * 1.35, xRes = LAT + ANCHO - 110 * MM;
    var filas = r.capitulos.map(function (c) {
      return { t1: c.code.replace('#', '') + ' · ' + c.nombre, t2: BC3.euros(c.centimos), negrita: false, fondo: null, filete: true };
    });
    filas.push({ t1: 'Total sin IVA', t2: BC3.euros(r.subtotal), negrita: true, fondo: PAL.papel, filete: true });
    filas.push({ t1: 'IVA ' + r.ivaPct + ' %', t2: BC3.euros(r.iva), negrita: false, fondo: null, filete: true });
    filas.push({ t1: 'Total con IVA', t2: BC3.euros(r.total), negrita: true, fondo: PAL.beige, filete: false });

    var total = 7 * MM + lhT + 1.3 * MM + 2 * MM + CAB;
    filas.forEach(function (f) { total += alturaFila(entradasRes(ctx, f), f.filete); });
    if (ctx.y + total > LIMITE) nuevaPagina(ctx); else ctx.y += 7 * MM;

    escribir(ctx, 'Resumen', LAT, bl(ctx.y, lhT, 10.5), ctx.b, 10.5, PAL.pino);
    ctx.y += lhT;
    filete(ctx, LAT, LAT + ANCHO, ctx.y + 1.15 * MM, 0.3 * MM, PAL.linea);
    ctx.y += 1.3 * MM + 2 * MM;
    cabecera(ctx, xRes, [{ w: 84 * MM, alin: 'L', t: 'Capítulo' }, { w: 26 * MM, alin: 'C', t: 'Importe (€)' }]);
    filas.forEach(function (f) {
      var e = entradasRes(ctx, f);
      dibujarFila(ctx, xRes, e, alturaFila(e, f.filete), f.fondo, f.filete);
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
    var meta = 'Revisión ' + m.rev + ' · ' + m.fecha + ' · Precios de venta en euros · Cliente: ' + m.cliente;
    envolver(ctx.r, meta, 8.5, ANCHO).forEach(function (l) {
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

  // Pie «BAFRAS Engineering» y «Página N de M» en las páginas del cuerpo (no en la portada).
  function pies(ctx) {
    var paginas = ctx.doc.getPages(), total = paginas.length, y = H - 287.8 * MM;
    paginas.forEach(function (pg, i) {
      if (i === 0) return;
      pg.drawText('BAFRAS Engineering', { x: LAT, y: y, size: 7.5, font: ctx.r, color: rgb(PAL.gris) });
      var t = 'Página ' + (i + 1) + ' de ' + total;
      pg.drawText(t, { x: W - LAT - ctx.r.widthOfTextAtSize(t, 7.5), y: y, size: 7.5, font: ctx.r, color: rgb(PAL.gris) });
    });
  }

  // r: resultado de BC3.calcular (precios de venta). m: datos de portada del formulario.
  function generar(r, m) {
    if (!window.PDFLib) return Promise.reject(new Error('no se cargó la librería del PDF'));
    var PL = window.PDFLib;
    return PL.PDFDocument.create().then(function (doc) {
      // En pdf-lib, incrustar fuentes e imágenes devuelve promesas.
      return Promise.all([
        doc.embedFont(PL.StandardFonts.Helvetica),
        doc.embedFont(PL.StandardFonts.HelveticaBold),
        doc.embedPng(logoBytes())
      ]).then(function (v) {
        var ctx = { doc: doc, r: v[0], b: v[1] };
        var ahora = new Date();
        doc.setTitle(m.titulo || 'Presupuesto');
        doc.setAuthor('BAFRAS Engineering');
        doc.setCreator('BAFRAS · BC3 a PDF');
        doc.setCreationDate(ahora);
        doc.setModificationDate(ahora);
        nuevaPagina(ctx);
        portada(ctx, m, v[2]);
        nuevaPagina(ctx);
        cuerpo(ctx, r, m);
        pies(ctx);
        return doc.save();
      });
    });
  }

  window.BC3PDF = { generar: generar };
})();
