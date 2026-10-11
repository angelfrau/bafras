/* BAFRAS · piezas comunes de los PDF (pdf-lib): medidas, colores, fuentes, texto y tablas.
   Las usan el presupuesto (pdf.js) y los documentos de trabajo (pdf-documentos.js).

   Medidas: todo se dibuja en puntos PDF. La posición vertical «y» se cuenta desde arriba
   de la página, como en un documento de texto, y se convierte en cada dibujo (H − y). */
(function () {
  'use strict';

  var MM = 72 / 25.4;                          // puntos por milímetro
  var W = 210 * MM, H = 297 * MM;              // A4
  var LAT = 16 * MM, ANCHO = W - 2 * LAT;      // margen lateral y ancho útil (178 mm)
  var SUP = 22 * MM;                           // margen superior del cuerpo
  var LIMITE = H - 20 * MM;                    // hasta aquí llega el texto (medido desde arriba)
  var PAD_V = 1.6 * MM, PAD_H = 1.5 * MM;      // relleno de celdas (igual que style.css)
  var CAB = 2 * 1.2 * MM + 8.5 * 1.35 + 0.4 * MM; // altura de la cabecera de una tabla

  // Anchos de columna del presupuesto: código, descripción, ud, cantidad, precio, importe (mm).
  var COLS = [19, 84, 11, 16, 22, 26].map(function (v) { return v * MM; });

  var PAL = {
    beige: '#ECE8DD', papel: '#F7F5F0', pino: '#0E2B25', verde: '#1A7A5A',
    tinta: '#2A2A2A', gris: '#4A5550', grisSuave: '#7A8580', linea: '#D8D2C3'
  };

  // Caracteres de Windows-1252 fuera de Latin-1 (la fuente incrustada también los tiene).
  var EXTRA = '€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ';

  // ---------- formatos ----------

  // Un «lote» no existe en el presupuesto: se muestra como «ud».
  function unidadTxt(u) { return /^lote$/i.test(u || '') ? 'ud' : (u || ''); }

  // Número con coma decimal y separador de miles. Muestra entre minDec y maxDec decimales
  // y quita los ceros sobrantes: 40,5 → "40,50"; 0,0244897959 → "0,0245"; 12 → "12".
  function formatoNumero(n, minDec, maxDec) {
    var signo = n < 0 ? '-' : '';
    var partes = Math.abs(n).toFixed(maxDec).split('.');
    var entero = partes[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    var decimales = partes[1] || '';
    while (decimales.length > minDec && decimales.charAt(decimales.length - 1) === '0') {
      decimales = decimales.slice(0, -1);
    }
    return signo + entero + (decimales ? ',' + decimales : '');
  }

  // ---------- texto y colores ----------

  // Bytes de un data: URI en base64 (las fuentes y el logotipo van dentro del propio script).
  function bytesDe(uri) {
    var b64 = String(uri || '').split(',')[1] || '';
    var bin = atob(b64), out = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
    return out;
  }

  function rgb(hex) {
    var n = parseInt(hex.slice(1), 16);
    return window.PDFLib.rgb(((n >> 16) & 255) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255);
  }

  // Deja solo los caracteres que la fuente puede escribir; tabuladores y saltos pasan a espacio.
  function limpiar(s) {
    return Array.from(String(s == null ? '' : s)).map(function (ch) {
      var c = ch.codePointAt(0);
      if (c === 9 || c === 10 || c === 13) return ' ';
      if (c < 32 || (c >= 127 && c < 160)) return '';
      if (c <= 255 || EXTRA.indexOf(ch) !== -1) return ch;
      return '?';
    }).join('');
  }

  // Línea base (medida desde arriba) de un texto centrado en una línea de altura lh.
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

  // ---------- dibujo sobre la página actual (ctx.pg) ----------

  function escribir(ctx, s, x, base, f, tam, hex) {
    if (!s) return;
    ctx.pg.drawText(s, { x: x, y: H - base, size: tam, font: f, color: rgb(hex) });
  }

  function escribirCentrado(ctx, s, cx, base, f, tam, hex) {
    if (!s) return;
    escribir(ctx, s, cx - f.widthOfTextAtSize(s, tam) / 2, base, f, tam, hex);
  }

  // Interletrado (letter-spacing de CSS): el espacio va tras cada letra, también tras la última.
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

  // Si el bloque no cabe, pasa a la página siguiente y repite la cabecera de la tabla (si la hay).
  function asegurar(ctx, alto, repetir) {
    if (ctx.y + alto <= LIMITE) return;
    nuevaPagina(ctx);
    if (repetir) repetir();
  }

  // Igual que asegurar, pero para un bloque que debe ir entero: si cabe en una página
  // nueva, se pasa a ella; si es más alto que una página, se parte fila a fila.
  function asegurarBloque(ctx, alto, repetir) {
    if (ctx.y + alto <= LIMITE) return;
    if (alto <= LIMITE - SUP) {
      nuevaPagina(ctx);
      if (repetir) repetir();
    }
  }

  // ---------- celdas ----------
  // Una celda es una lista de bloques de texto; cada bloque tiene sus líneas, su letra y su color.

  function celda(lineas, f, tam, lh, hex, mt) {
    return { bloques: [{ lineas: lineas, f: f, tam: tam, lh: lh, hex: hex, mt: mt || 0 }] };
  }

  // Celda de una sola letra y color (códigos, cantidades, precios...).
  function celdaTxt(s, f, tam, hex, ancho) {
    return celda(envolver(f, s, tam, ancho - 2 * PAD_H), f, tam, tam * 1.35, hex, 0);
  }

  // Descripción de una partida: resumen en negrita y, debajo, el texto largo en letra menor.
  function celdaDescripcion(ctx, resumen, texto, ancho) {
    var anchoTxt = ancho - 2 * PAD_H;
    var bloques = [{ lineas: envolver(ctx.b, resumen, 8.5, anchoTxt), f: ctx.b, tam: 8.5, lh: 8.5 * 1.35, hex: PAL.pino, mt: 0 }];
    if (texto) bloques.push({ lineas: envolver(ctx.r, texto, 7.8, anchoTxt), f: ctx.r, tam: 7.8, lh: 7.8 * 1.35, hex: PAL.tinta, mt: 0.6 * MM });
    return { bloques: bloques };
  }

  function alturaCelda(c) {
    return c.bloques.reduce(function (h, b) { return h + b.mt + b.lineas.length * b.lh; }, 0);
  }

  // Altura de una fila: la celda más alta, más el relleno y, si lleva filete, su grosor.
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

  // Dibuja una fila en la posición actual. entradas: [{w, alin, celda}] desde xIni.
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

  // Cabecera de tabla: texto en negrita pino y filete inferior de 0,4 mm. columnas: [{w, alin, t}].
  function cabecera(ctx, xIni, columnas) {
    var x = xIni, base = bl(ctx.y + 1.2 * MM, 8.5 * 1.35, 8.5);
    columnas.forEach(function (col) {
      if (col.alin === 'C') escribirCentrado(ctx, col.t, x + col.w / 2, base, ctx.b, 8.5, PAL.pino);
      else escribir(ctx, col.t, x + PAD_H, base, ctx.b, 8.5, PAL.pino);
      x += col.w;
    });
    filete(ctx, xIni, x, ctx.y + CAB - 0.2 * MM, 0.4 * MM, PAL.pino);
    ctx.y += CAB;
  }

  // ---------- filas de tabla genéricas ----------
  // Una fila tiene una celda por columna (fila.celdas), o, si es de suma (fila.total),
  // dos celdas: la etiqueta ocupa todas las columnas menos la última, que lleva el importe.
  //   fila = { celdas: [...], fondo: hex|null, filete: bool, minAlto: pt (opcional), total: bool }

  function entradasDe(columnas, fila) {
    if (!fila.total) {
      return columnas.map(function (col, i) { return { w: col.w, alin: col.alin, celda: fila.celdas[i] }; });
    }
    var ultima = columnas[columnas.length - 1];
    var anchoEtiqueta = columnas.slice(0, -1).reduce(function (s, col) { return s + col.w; }, 0);
    return [
      { w: anchoEtiqueta, alin: 'L', celda: fila.celdas[0] },
      { w: ultima.w, alin: ultima.alin, celda: fila.celdas[1] }
    ];
  }

  function alturaDeFila(columnas, fila) {
    return Math.max(alturaFila(entradasDe(columnas, fila), fila.filete), fila.minAlto || 0);
  }

  // Dibuja una fila; si no cabe, pasa de página (y repite la cabecera con repetir()).
  function filaTabla(ctx, columnas, fila, repetir) {
    var entradas = entradasDe(columnas, fila), alto = alturaDeFila(columnas, fila);
    asegurar(ctx, alto, repetir);
    dibujarFila(ctx, LAT, entradas, alto, fila.fondo, fila.filete);
  }

  // Tabla completa: cabecera y filas, con la cabecera repetida en cada página nueva.
  function tabla(ctx, columnas, filas) {
    var repetir = function () { cabecera(ctx, LAT, columnas); };
    cabecera(ctx, LAT, columnas);
    filas.forEach(function (f) { filaTabla(ctx, columnas, f, repetir); });
  }

  // Fila de suma (subtotal o total): etiqueta y importe en negrita. La etiqueta ocupa las
  // columnas menos la última, que lleva el importe. ctx.b es la fuente en negrita.
  function filaSuma(ctx, columnas, etiqueta, importe, fondo, conFilete) {
    var ancho = columnas.slice(0, -1).reduce(function (s, col) { return s + col.w; }, 0);
    var ultima = columnas[columnas.length - 1];
    return {
      total: true,
      celdas: [celdaTxt(etiqueta, ctx.b, 8.5, PAL.tinta, ancho), celdaTxt(importe, ctx.b, 8.5, PAL.tinta, ultima.w)],
      fondo: fondo, filete: conFilete
    };
  }

  // ---------- títulos de capítulo ----------
  // Título de capítulo (nivel 2) o de subcapítulo (nivel 3). «restoReserva» es el espacio que
  // debe quedar libre tras el título (la cabecera y la primera fila), para que no se quede solo
  // al final de una página. Devuelve nada; deja ctx.y justo debajo del título.
  function tituloCapitulo(ctx, texto, nivel, restoReserva) {
    var h2 = nivel === 2;
    var tam = h2 ? 10.5 : 9, lh = tam * 1.35;
    var mt = (h2 ? 7 : 4) * MM, mb = (h2 ? 2 : 1.5) * MM;
    var pb = h2 ? 1.3 * MM : 0;          // h2: relleno inferior de 1,3 mm y filete de 0,3 mm
    var lineas = envolver(ctx.b, texto, tam, ANCHO);
    var alto = mt + lineas.length * lh + pb + mb + (restoReserva || 0);
    if (ctx.y + alto > LIMITE) nuevaPagina(ctx); else ctx.y += mt;
    lineas.forEach(function (l) {
      escribir(ctx, l, LAT, bl(ctx.y, lh, tam), ctx.b, tam, h2 ? PAL.pino : PAL.verde);
      ctx.y += lh;
    });
    if (h2) filete(ctx, LAT, LAT + ANCHO, ctx.y + 1.15 * MM, 0.3 * MM, PAL.linea);
    ctx.y += pb + mb;
  }

  // ---------- pies y documento nuevo ----------

  // Pie «BAFRAS Engineering» y «Página N de M» en cada página desde la índice «desde».
  // La numeración cuenta todas las páginas, también las que no llevan pie.
  function pies(ctx, desde) {
    var paginas = ctx.doc.getPages(), total = paginas.length, y = H - 287.8 * MM;
    paginas.forEach(function (pg, i) {
      if (i < desde) return;
      pg.drawText('BAFRAS Engineering', { x: LAT, y: y, size: 7.5, font: ctx.r, color: rgb(PAL.gris) });
      var t = 'Página ' + (i + 1) + ' de ' + total;
      pg.drawText(t, { x: W - LAT - ctx.r.widthOfTextAtSize(t, 7.5), y: y, size: 7.5, font: ctx.r, color: rgb(PAL.gris) });
    });
  }

  // Documento nuevo con las fuentes incrustadas (Liberation Sans, métricas de Arial) y sus metadatos.
  // Con las fuentes estándar, cada visor sustituye la letra por la suya: el € se veía mal en el móvil.
  // Devuelve una promesa con ctx = { doc, r (regular), b (negrita) }.
  function abrirDocumento(titulo) {
    if (!window.PDFLib || !window.fontkit || !window.BAFRAS_FUENTES) {
      return Promise.reject(new Error('no se cargaron las librerías del PDF'));
    }
    return window.PDFLib.PDFDocument.create().then(function (doc) {
      doc.registerFontkit(window.fontkit);
      return Promise.all([
        doc.embedFont(bytesDe(window.BAFRAS_FUENTES.regular), { subset: true }),
        doc.embedFont(bytesDe(window.BAFRAS_FUENTES.bold), { subset: true })
      ]).then(function (fuentes) {
        var ahora = new Date();
        doc.setTitle(titulo || 'Presupuesto');
        doc.setAuthor('BAFRAS Engineering');
        doc.setCreator('BAFRAS · BC3 a PDF');
        doc.setCreationDate(ahora);
        doc.setModificationDate(ahora);
        return { doc: doc, r: fuentes[0], b: fuentes[1] };
      });
    });
  }

  window.BC3PDFBase = {
    MM: MM, W: W, H: H, LAT: LAT, ANCHO: ANCHO, SUP: SUP, LIMITE: LIMITE,
    PAD_V: PAD_V, PAD_H: PAD_H, CAB: CAB, COLS: COLS, PAL: PAL,
    unidadTxt: unidadTxt, formatoNumero: formatoNumero, bytesDe: bytesDe, rgb: rgb,
    limpiar: limpiar, bl: bl, envolver: envolver,
    escribir: escribir, escribirCentrado: escribirCentrado, escribirEspaciado: escribirEspaciado,
    rect: rect, filete: filete, nuevaPagina: nuevaPagina, asegurar: asegurar, asegurarBloque: asegurarBloque,
    celda: celda, celdaTxt: celdaTxt, celdaDescripcion: celdaDescripcion,
    alturaCelda: alturaCelda, alturaFila: alturaFila, dibujarFila: dibujarFila, cabecera: cabecera,
    entradasDe: entradasDe, alturaDeFila: alturaDeFila, filaTabla: filaTabla, tabla: tabla,
    filaSuma: filaSuma, tituloCapitulo: tituloCapitulo, pies: pies, abrirDocumento: abrirDocumento
  };
})();
