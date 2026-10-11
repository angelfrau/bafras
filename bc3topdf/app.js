/* BAFRAS · BC3 a PDF: formulario, portada (plantilla de presupuesto), cuerpo A4 y documentos de trabajo.
   El BC3 se lee en el navegador. Nada se envía a ningún servidor. */
(function () {
  'use strict';

  var BC3 = window.BC3;
  var LOGO = '../images/BAFRAS_logo_horizontal_deep_corregido.svg';
  var ANCHO_HOJA = 793.7; // 210 mm en píxeles CSS
  var $ = function (id) { return document.getElementById(id); };
  var datos = null;       // BC3 leído (null hasta que se carga un archivo)

  // Anchos de columna del cuerpo: código, descripción, ud, cantidad, precio, importe.
  var COLS = '<colgroup><col class="c-cod"><col><col class="c-ud"><col class="c-cant">' +
    '<col class="c-pre"><col class="c-imp"></colgroup>';

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  function estado(texto, error) {
    var el = $('estado');
    el.textContent = texto;
    el.className = 'estado' + (error ? ' error' : '');
  }

  function pad2(n) { return (n < 10 ? '0' : '') + n; }

  // El BC3 ya trae los precios de venta (el margen va dentro del BC3). Aquí solo se toma el IVA.
  function ajustesVenta() {
    var iva = parseFloat($('iva').value);
    return { iva: iva >= 0 ? iva : 21 };
  }

  // Cantidad: entero con separador de miles; si no es entero, dos decimales.
  function cantTxt(n) {
    var r = Math.round(n * 100) / 100;
    if (Number.isInteger(r)) return String(r).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    return BC3.euros(Math.round(r * 100));
  }

  // En el presupuesto no existen lotes: cualquier «lote» se presenta como «ud».
  function unidadTxt(u) {
    return /^lote$/i.test(u || '') ? 'ud' : (u || '');
  }

  function fechaTxt(iso) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso || '');
    return m ? m[3] + '/' + m[2] + '/' + m[1] : '';
  }

  function leerCampos() {
    return {
      titulo: $('titulo').value.trim(),
      cliente: $('cliente').value.trim(),
      rev: $('rev').value.trim(),
      fecha: fechaTxt($('fecha').value),
      emplazamiento: $('emplazamiento').value.trim(),
      expediente: $('expediente').value.trim()
    };
  }

  // ---------- portada: misma composición que la plantilla (logo arriba, bloque centrado, datos abajo) ----------
  function portadaHtml(m) {
    return '<section class="portada">' +
      '<img class="p-logo" src="' + LOGO + '" alt="BAFRAS Engineering">' +
      '<div class="p-medio"><p class="p-etiqueta">Presupuesto</p>' +
      '<h1 class="p-titulo" id="p-titulo">' + esc(m.titulo) + '</h1></div>' +
      '<dl class="p-datos">' +
      '<div><dt>Cliente</dt><dd>' + esc(m.cliente || '—') + '</dd></div>' +
      '<div><dt>Emplazamiento</dt><dd>' + esc(m.emplazamiento || '—') + '</dd></div>' +
      '<div><dt>Expediente</dt><dd>' + esc(m.expediente || '—') + '</dd></div>' +
      '<div><dt>Revisión · fecha</dt><dd>' + esc(m.rev + ' · ' + m.fecha) + '</dd></div>' +
      '</dl></section>';
  }

  // Tamaño del título según el número de líneas: 38 / 37 / 35 / 30 pt.
  function ajustarTitulo() {
    var el = $('p-titulo');
    if (!el) return;
    el.className = 'p-titulo t1';
    var cs = getComputedStyle(el);
    var lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.05;
    var lineas = Math.max(1, Math.round(el.getBoundingClientRect().height / lh));
    el.className = 'p-titulo t' + Math.min(lineas, 4);
  }

  // En pantalla, la hoja se reduce si no cabe en el ancho de la página. La impresión no se toca.
  function ajustarZoom() {
    var vista = $('vista');
    var z = vista.clientWidth > 0 ? Math.min(1, vista.clientWidth / ANCHO_HOJA) : 1;
    vista.style.setProperty('--zoom', String(z));
  }

  // ---------- cuerpo ----------
  function filaPartida(p, codigo) {
    return '<tr>' +
      '<td class="cod">' + esc(codigo) + '</td>' +
      '<td class="desc"><strong>' + esc(p.resumen) + '</strong>' +
      (p.texto ? '<span>' + esc(p.texto) + '</span>' : '') + '</td>' +
      '<td class="c">' + esc(unidadTxt(p.unidad)) + '</td>' +
      '<td class="c">' + cantTxt(p.cantidad) + '</td>' +
      '<td class="c">' + BC3.euros(p.pvpUd) + '</td>' +
      '<td class="c">' + BC3.euros(p.centimos) + '</td>' +
      '</tr>';
  }

  // Código de cada partida: capítulo y orden (09.01) o subcapítulo y orden (04.01.01).
  // Si el capítulo tiene subcapítulos, la fila de suma se llama «Partidas»; si no, «Subtotal».
  function tablaPartidas(partidas, base, nombre, conSubcapitulos) {
    var html = '<table>' + COLS + '<thead><tr>' +
      '<th class="c-cod">Código</th><th>Descripción</th><th class="c c-ud">Ud</th>' +
      '<th class="c c-cant">Cant.</th><th class="c c-pre">Precio (€)</th><th class="c c-imp">Importe (€)</th>' +
      '</tr></thead><tbody>';
    var suma = 0;
    partidas.forEach(function (p, i) {
      html += filaPartida(p, base + '.' + pad2(i + 1));
      suma += p.centimos;
    });
    html += '<tr class="subtotal"><td colspan="5">' + (conSubcapitulos ? 'Partidas ' : 'Subtotal ') +
      esc(base) + ' · ' + esc(nombre) + '</td><td class="c">' + BC3.euros(suma) + '</td></tr>';
    return html + '</tbody></table>';
  }

  // Capítulo: título, tabla de partidas, subcapítulos y, si los tiene, el total del capítulo.
  function capituloHtml(c, nivel) {
    var h = nivel === 2 ? 'h2' : 'h3';
    var base = c.code.replace('#', '');
    var partidas = c.hijos.filter(function (x) { return x.tipo === 'partida'; });
    var subcapitulos = c.hijos.filter(function (x) { return x.tipo === 'capitulo'; });
    var html = '<' + h + '>' + esc(base) + ' · ' + esc(c.nombre) + '</' + h + '>';
    if (partidas.length) html += tablaPartidas(partidas, base, c.nombre, subcapitulos.length > 0);
    subcapitulos.forEach(function (s) { html += capituloHtml(s, nivel + 1); });
    if (subcapitulos.length) {
      html += '<table>' + COLS + '<tbody><tr class="total"><td colspan="5">Total ' + esc(base) +
        ' · ' + esc(c.nombre) + '</td><td class="c">' + BC3.euros(c.centimos) + '</td></tr></tbody></table>';
    }
    return html;
  }

  function resumenHtml(r) {
    var html = '<div class="bloque-resumen"><h2>Resumen</h2><table class="resumen"><thead><tr><th>Capítulo</th>' +
      '<th class="c">Importe (€)</th></tr></thead><tbody>';
    r.capitulos.forEach(function (c) {
      html += '<tr><td>' + esc(c.code.replace('#', '')) + ' · ' + esc(c.nombre) + '</td>' +
        '<td class="c">' + BC3.euros(c.centimos) + '</td></tr>';
    });
    html += '<tr class="subtotal"><td>Total sin IVA</td><td class="c">' + BC3.euros(r.subtotal) + '</td></tr>';
    html += '<tr><td>IVA ' + r.ivaPct + ' %</td><td class="c">' + BC3.euros(r.iva) + '</td></tr>';
    html += '<tr class="total"><td>Total con IVA</td><td class="c">' + BC3.euros(r.total) + '</td></tr>';
    return html + '</tbody></table></div>';
  }

  function cuerpoHtml(r, m) {
    var meta = 'Revisión ' + esc(m.rev) + ' · ' + esc(m.fecha);
    var html = '<section class="cuerpo hoja"><h1>' + esc(m.titulo) + '</h1><p class="meta">' + meta + '</p>';
    r.capitulos.forEach(function (c) { html += capituloHtml(c, 2); });
    return html + resumenHtml(r) + '</section>';
  }

  // ---------- carga del BC3 (clic o arrastrar) ----------
  function cargar(f) {
    datos = null;
    $('generar').disabled = true;
    $('imprimir').hidden = true;
    $('descargar').hidden = true;
    listo = null;
    generacion++;
    invalidarDocs();
    $('archivo').textContent = f.name;
    estado('Leyendo el BC3…');
    f.arrayBuffer().then(function (buf) {
      datos = BC3.parsear(BC3.decodificar(buf));
      var raiz = datos.conceptos[datos.raiz];
      if (!$('titulo').value.trim()) $('titulo').value = raiz.resumen || '';
      var r = BC3.calcular(datos, 1, ajustesVenta().iva); // precios de venta tal cual vienen en el BC3
      $('generar').disabled = false;
      $('preparar-docs').disabled = false;
      estado('BC3 leído: ' + r.numPartidas + ' partidas. Venta sin IVA ' + BC3.euros(r.subtotal) +
        ' €; con IVA ' + BC3.euros(r.total) + ' €.');
    }).catch(function (e) {
      estado('No se pudo leer el BC3: ' + e.message, true);
    });
  }

  var zona = $('soltar');
  ['dragenter', 'dragover'].forEach(function (ev) {
    zona.addEventListener(ev, function (e) { e.preventDefault(); zona.classList.add('activa'); });
  });
  ['dragleave', 'drop'].forEach(function (ev) {
    zona.addEventListener(ev, function (e) { e.preventDefault(); zona.classList.remove('activa'); });
  });
  zona.addEventListener('drop', function (e) {
    var f = e.dataTransfer && e.dataTransfer.files[0];
    if (f) cargar(f);
  });
  $('bc3').addEventListener('change', function () {
    if (this.files[0]) cargar(this.files[0]);
  });

  var generacion = 0; // una vista previa antigua no sobrescribe a la nueva
  var listo = null;   // { bytes, nombre } del último PDF del presupuesto

  function descargarArchivo(bytes, nombre) {
    var url = URL.createObjectURL(new Blob([bytes], { type: 'application/pdf' }));
    var a = document.createElement('a');
    a.href = url;
    a.download = nombre;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 60000);
  }

  // Prefijo_<cliente>_rev<revisión>.pdf (o título si no hay cliente), sin tildes ni espacios.
  // El prefijo por defecto es «Presupuesto».
  function nombreArchivo(m, prefijo) {
    var base = (m.cliente || m.titulo || 'presupuesto').normalize('NFD').replace(/[̀-ͯ]/g, '')
      .replace(/[^A-Za-z0-9]+/g, '_').replace(/^_+|_+$/g, '');
    var rev = (m.rev || '01').replace(/[^A-Za-z0-9]+/g, '');
    return (prefijo || 'Presupuesto') + '_' + (base || 'presupuesto') + '_rev' + rev + '.pdf';
  }

  $('generar').addEventListener('click', function () {
    if (!datos) return;
    if (!$('formulario').reportValidity()) return;
    var iva = parseFloat($('iva').value);
    if (!(iva >= 0)) {
      estado('Revisa el IVA.', true);
      return;
    }
    var r = BC3.calcular(datos, 1, iva); // precios de venta tal cual vienen en el BC3
    var m = leerCampos();
    var id = ++generacion;
    listo = null;
    $('descargar').hidden = true;
    $('vista').style.setProperty('--zoom', '1'); // se mide a escala 1 y después se ajusta
    $('vista').innerHTML = portadaHtml(m) + cuerpoHtml(r, m);
    ajustarTitulo();
    ajustarZoom();
    $('imprimir').hidden = false;
    var resumen = 'Listo: ' + r.numPartidas + ' partidas. Venta sin IVA ' + BC3.euros(r.subtotal) +
      ' €; con IVA ' + BC3.euros(r.total) + ' €.';
    estado(resumen + ' Preparando el PDF…');
    window.BC3PDF.generar(r, m).then(function (bytes) {
      if (id !== generacion) return;
      listo = { bytes: bytes, nombre: nombreArchivo(m) };
      $('descargar').hidden = false;
      estado(resumen + ' PDF listo para descargar.');
    }).catch(function (e) {
      if (id !== generacion) return;
      estado('No se pudo preparar el PDF: ' + e.message, true);
    });
  });

  // Se descarga en el mismo gesto del usuario: el PDF ya está preparado.
  $('descargar').addEventListener('click', function () {
    if (!listo) return;
    descargarArchivo(listo.bytes, listo.nombre);
    estado('Descarga iniciada: ' + listo.nombre + '.');
  });

  window.addEventListener('resize', ajustarZoom);
  $('imprimir').addEventListener('click', function () { window.print(); });

  // ---------- documentos de trabajo ----------
  // Se preparan los siete a la vez y cada uno se descarga con su botón, en el mismo gesto
  // del usuario (como el presupuesto). Si cambia algún dato de la portada, lo preparado ya no vale.
  var docsPreparados = {};   // clave → { bytes, nombre }
  var generacionDocs = 0;    // una preparación antigua no sobrescribe a la nueva
  var botonPreparar = $('preparar-docs');
  var botonesDocs = document.querySelectorAll('[data-doc]');

  function estadoDocs(texto, error) {
    var el = $('estado-docs');
    el.textContent = texto;
    el.className = 'estado' + (error ? ' error' : '');
  }

  function invalidarDocs() {
    generacionDocs++;
    docsPreparados = {};
    botonesDocs.forEach(function (b) { b.disabled = true; });
    estadoDocs('');
  }

  $('formulario').addEventListener('input', function () {
    if (Object.keys(docsPreparados).length === 0) return;
    invalidarDocs();
    estadoDocs('Has cambiado algún dato. Vuelve a preparar los documentos.');
  });

  botonPreparar.addEventListener('click', function () {
    if (!datos) return;
    if (!$('formulario').reportValidity()) return;
    var r = BC3.calcular(datos, 1, ajustesVenta().iva); // precios de venta tal cual vienen en el BC3
    var m = leerCampos();
    invalidarDocs();
    var id = generacionDocs;
    botonPreparar.disabled = true;
    estadoDocs('Preparando los documentos…');

    // Uno detrás de otro, para no tener varias copias del BC3 en memoria a la vez.
    window.BC3PDFDocs.claves.reduce(function (antes, clave) {
      return antes.then(function () {
        if (id !== generacionDocs) return null;
        return window.BC3PDFDocs.generar(clave, datos, r, m).then(function (bytes) {
          if (id !== generacionDocs) return;
          docsPreparados[clave] = { bytes: bytes, nombre: nombreArchivo(m, window.BC3PDFDocs.archivo(clave)) };
          document.querySelector('[data-doc="' + clave + '"]').disabled = false;
        });
      });
    }, Promise.resolve()).then(function () {
      if (id !== generacionDocs) return;
      botonPreparar.disabled = false;
      estadoDocs('Documentos listos para descargar.');
    }).catch(function (e) {
      if (id !== generacionDocs) return;
      botonPreparar.disabled = false;
      estadoDocs('No se pudieron preparar los documentos: ' + e.message, true);
    });
  });

  botonesDocs.forEach(function (boton) {
    boton.addEventListener('click', function () {
      var clave = boton.getAttribute('data-doc');
      var preparado = docsPreparados[clave];
      if (!preparado) return;
      descargarArchivo(preparado.bytes, preparado.nombre);
      estadoDocs('Descarga iniciada: ' + preparado.nombre + '.');
    });
  });

  var hoy = new Date();
  $('fecha').value = hoy.getFullYear() + '-' + pad2(hoy.getMonth() + 1) + '-' + pad2(hoy.getDate());
})();
