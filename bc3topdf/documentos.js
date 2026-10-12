/* BAFRAS · datos de los documentos de trabajo: cuadros de precios nº 1 y nº 2, recursos totales
   y conciliación con el presupuesto. Parte del árbol que devuelve BC3.calcular y del BC3 leído (datos.conceptos).
   No dibuja nada: así se puede probar en Node (test/documentos.test.js).

   Importes en céntimos (enteros), igual que bc3.js. */
(function (raiz, fabrica) {
  var api = fabrica();
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else raiz.BC3Docs = api;
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  // Euros a céntimos. Se redondea primero con 6 decimales para que el error de coma flotante
  // no cambie un céntimo (1,755 × 4 = 7,02, no 7,01).
  function aCentimos(euros) { return Math.round(Math.round(euros * 1e6) / 1e4); }

  function concepto(datos, codigo) {
    var c = datos.conceptos[codigo];
    if (!c) throw new Error('Concepto sin definir en el BC3: ' + codigo);
    return c;
  }

  // Precio de venta de un concepto en euros, sin redondear: el del BC3 por el coeficiente.
  // (En la web el coeficiente es 1: el BC3 ya trae los precios de venta.)
  function precioVenta(datos, codigo, coef) {
    return concepto(datos, codigo).precio * coef;
  }

  // Precio exacto por unidad, sin redondear (euros). Un recurso vale su precio de venta.
  // Una partida, o un auxiliar con descomposición, vale lo que suman sus componentes
  // multiplicados por su rendimiento. Así es como el BC3 llega al precio de cada partida.
  function precioExacto(datos, codigo, coef) {
    var c = concepto(datos, codigo);
    if (!c.hijos.length) return c.precio * coef;
    return c.hijos.reduce(function (s, h) {
      return s + h.factor * h.cantidad * precioExacto(datos, h.code, coef);
    }, 0);
  }

  // Una partida con descomposición tiene registro ~D. Sin ~D, es un recurso si cuelga
  // de otra partida, o una partida de precio directo si cuelga de un capítulo.
  function tieneDescomposicion(datos, codigo) {
    return concepto(datos, codigo).hijos.length > 0;
  }

  // Visita cada partida del árbol. Una partida puede estar en dos capítulos: se visita dos veces.
  function recorrerPartidas(nodos, visitar) {
    nodos.forEach(function (n) {
      if (n.tipo === 'capitulo') recorrerPartidas(n.hijos, visitar);
      else visitar(n);
    });
  }

  // Partidas sin repetir, en el orden del presupuesto (la primera vez que aparecen).
  function partidasUnicas(r) {
    var vistas = {}, lista = [];
    recorrerPartidas(r.capitulos, function (p) {
      if (vistas[p.code]) return;
      vistas[p.code] = true;
      lista.push(p);
    });
    return lista;
  }

  // Código de presupuesto de cada partida, igual que en el presupuesto: capítulo y orden (01.01) o
  // subcapítulo y orden (04.01.01). El código sale del capítulo (01# → 01) y del orden de la partida
  // entre las de su capítulo. Devuelve un Map de cada partida del árbol a su código: una partida que
  // está en dos capítulos tiene un código en cada uno; partidasUnicas da el de la primera aparición.
  function codigosPresupuesto(r) {
    var mapa = new Map();
    function capitulo(c) {
      var base = c.code.replace('#', ''), orden = 0;
      c.hijos.forEach(function (x) {
        if (x.tipo === 'capitulo') {
          capitulo(x);
        } else {
          orden += 1;
          mapa.set(x, base + '.' + (orden < 10 ? '0' : '') + orden);
        }
      });
    }
    r.capitulos.forEach(function (c) { capitulo(c); });
    return mapa;
  }

  // Todos los códigos de presupuesto de cada partida, por código BC3: una lista con un código por
  // aparición, en el orden del presupuesto. Una partida que está en dos capítulos tiene dos códigos.
  function codigosDePartida(r) {
    var mapa = codigosPresupuesto(r), porCodigo = new Map();
    recorrerPartidas(r.capitulos, function (p) {
      if (!porCodigo.has(p.code)) porCodigo.set(p.code, []);
      porCodigo.get(p.code).push(mapa.get(p));
    });
    return porCodigo;
  }

  // Tipo de un recurso según su código. En estos BC3 el campo «tipo» viene a 0 en todos los
  // conceptos, así que se mira el código: REF.MO.010 es mano de obra; MQ o MAQ, maquinaria;
  // PRU (pruebas y ensayos, servicios de empresa especializada), otros; el resto, materiales.
  function tipoRecurso(codigo) {
    var partes = codigo.toUpperCase().split('.');
    if (partes.indexOf('MO') !== -1) return 'mano';
    if (partes.indexOf('MQ') !== -1 || partes.indexOf('MAQ') !== -1) return 'maquinaria';
    if (partes.indexOf('PRU') !== -1) return 'otros';
    return 'materiales';
  }

  // Cuadro nº 1: una línea por partida, con sus códigos de presupuesto y su precio unitario.
  function cuadroPrecios1(r) {
    var codigos = codigosDePartida(r);
    return partidasUnicas(r).map(function (p) {
      return { codigos: codigos.get(p.code), unidad: p.unidad, resumen: p.resumen, texto: p.texto, pvpUd: p.pvpUd };
    });
  }

  // Líneas de la descomposición de una partida, por unidad de partida. Cada línea lleva el
  // tipo de recurso, el rendimiento, el precio del recurso y el importe (rendimiento × precio, a céntimo).
  function lineasDescomposicion(datos, codigo, coef) {
    return concepto(datos, codigo).hijos.map(function (h) {
      var hijo = concepto(datos, h.code);
      var rendimiento = h.factor * h.cantidad;
      var precio = precioVenta(datos, h.code, coef);
      return {
        codigo: h.code, unidad: hijo.unidad, resumen: hijo.resumen, tipo: tipoRecurso(h.code),
        rendimiento: rendimiento, precio: precio, importe: aCentimos(rendimiento * precio)
      };
    });
  }

  // Cuadro nº 2: cada partida (sin repetir) con las líneas de su descomposición. La partida lleva sus
  // códigos de presupuesto (01.01; dos si está en dos capítulos); sus líneas, el código del recurso
  // (REF.MO.020...). «redondeo» es lo que falta para que las líneas sumen el precio de la partida (céntimos).
  function cuadroPrecios2(r, datos) {
    var codigos = codigosDePartida(r);
    return partidasUnicas(r).map(function (p) {
      var descompuesta = tieneDescomposicion(datos, p.code);
      var lineas = descompuesta ? lineasDescomposicion(datos, p.code, r.coef) : [];
      var suma = lineas.reduce(function (s, l) { return s + l.importe; }, 0);
      return {
        codigos: codigos.get(p.code), unidad: p.unidad, resumen: p.resumen, pvpUd: p.pvpUd,
        descompuesta: descompuesta, lineas: lineas,
        redondeo: descompuesta ? p.pvpUd - suma : 0
      };
    });
  }

  // Suma en «acum» la cantidad de cada recurso que hay dentro de una partida. Si un hijo
  // tiene descomposición propia, se baja a sus recursos multiplicando los rendimientos.
  function sumarRecursos(datos, codigo, cantidad, acum) {
    var c = concepto(datos, codigo);
    if (!c.hijos.length) {
      acum[codigo] = (acum[codigo] || 0) + cantidad;
      return;
    }
    c.hijos.forEach(function (h) {
      sumarRecursos(datos, h.code, cantidad * h.factor * h.cantidad, acum);
    });
  }

  // Cuadros de recursos: cantidad total de cada recurso en el presupuesto, con su precio y su importe.
  // Las partidas sin descomposición no tienen recursos: se cuentan aparte.
  function cuadrosRecursos(r, datos) {
    var acum = {}, sinDescomponer = {};
    recorrerPartidas(r.capitulos, function (p) {
      if (tieneDescomposicion(datos, p.code)) sumarRecursos(datos, p.code, p.cantidad, acum);
      else sinDescomponer[p.code] = true;
    });

    var grupos = { mano: [], maquinaria: [], materiales: [], otros: [] };
    Object.keys(acum).sort().forEach(function (codigo) {
      var c = concepto(datos, codigo);
      var precio = precioVenta(datos, codigo, r.coef);
      var cantidad = acum[codigo];
      grupos[tipoRecurso(codigo)].push({
        codigo: codigo, unidad: c.unidad, resumen: c.resumen,
        cantidad: cantidad, precio: precio, importe: aCentimos(cantidad * precio)
      });
    });

    return {
      mano: grupos.mano,
      maquinaria: grupos.maquinaria,
      materiales: grupos.materiales,
      otros: grupos.otros,
      numSinDescomponer: Object.keys(sinDescomponer).length
    };
  }

  // Suma de los importes (céntimos) de una lista de recursos.
  function totalImporte(lista) {
    return lista.reduce(function (s, x) { return s + x.importe; }, 0);
  }

  // Lo que el presupuesto gana o pierde por redondear cada partida a céntimo:
  // suma de (precio redondeado − precio exacto) × cantidad. Céntimos, redondeados al final.
  function redondeoPartidas(r, datos) {
    var total = 0;
    recorrerPartidas(r.capitulos, function (p) {
      if (!tieneDescomposicion(datos, p.code)) return;
      total += (p.pvpUd - precioExacto(datos, p.code, r.coef) * 100) * p.cantidad;
    });
    return Math.round(total);
  }

  // Conciliación con el presupuesto: recursos por tipo + partidas de precio directo + redondeos
  // = presupuesto sin IVA. El redondeo de importes es lo que queda: el de cada importe a céntimo.
  function conciliacion(r, datos) {
    var rec = cuadrosRecursos(r, datos);
    var directas = 0;
    recorrerPartidas(r.capitulos, function (p) {
      if (!tieneDescomposicion(datos, p.code)) directas += p.centimos;
    });
    var materiales = totalImporte(rec.materiales);
    var mano = totalImporte(rec.mano);
    var maquinaria = totalImporte(rec.maquinaria);
    var otros = totalImporte(rec.otros);
    var rPartidas = redondeoPartidas(r, datos);
    return {
      materiales: materiales,
      mano: mano,
      maquinaria: maquinaria,
      otros: otros,
      directas: directas,
      redondeoPartidas: rPartidas,
      redondeoImportes: r.subtotal - (materiales + mano + maquinaria + otros + directas + rPartidas),
      total: r.subtotal
    };
  }

  // ---------- importes en letra (cuadro nº 1) ----------
  // Español: «Mil novecientos cuarenta y cuatro euros con cincuenta céntimos». Hasta 999.999.999 €.
  var UNIDADES = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'];
  var DIEZ_A_DIECINUEVE = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve'];
  var VEINTE_A_VEINTINUEVE = ['veinte', 'veintiuno', 'veintidós', 'veintitrés', 'veinticuatro', 'veinticinco', 'veintiséis', 'veintisiete', 'veintiocho', 'veintinueve'];
  var DECENAS = ['', '', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'];
  var CENTENAS = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos'];

  // De 1 a 999, sin apócope.
  function hastaMil(n) {
    if (n === 100) return 'cien';
    var partes = [], c = Math.floor(n / 100), r = n % 100;
    if (c) partes.push(CENTENAS[c]);
    if (r >= 30) partes.push(DECENAS[Math.floor(r / 10)] + (r % 10 ? ' y ' + UNIDADES[r % 10] : ''));
    else if (r >= 20) partes.push(VEINTE_A_VEINTINUEVE[r - 20]);
    else if (r >= 10) partes.push(DIEZ_A_DIECINUEVE[r - 10]);
    else if (r > 0) partes.push(UNIDADES[r]);
    return partes.join(' ');
  }

  // Delante de un sustantivo masculino, «uno» pasa a «un» y «veintiuno», a «veintiún».
  function apocope(texto) {
    return texto.replace(/veintiuno$/, 'veintiún').replace(/uno$/, 'un');
  }

  // Entero de 0 a 999.999.999, sin apócope.
  function enteroEnLetras(n) {
    if (n === 0) return 'cero';
    var partes = [], millones = Math.floor(n / 1e6), resto = n % 1e6;
    if (millones === 1) partes.push('un millón');
    else if (millones) partes.push(apocope(hastaMil(millones)) + ' millones');
    var miles = Math.floor(resto / 1000), cientos = resto % 1000;
    if (miles === 1) partes.push('mil');
    else if (miles) partes.push(apocope(hastaMil(miles)) + ' mil');
    if (cientos) partes.push(hastaMil(cientos));
    return partes.join(' ');
  }

  // Importe en céntimos → texto: «Un euro», «Veintiún euros con cinco céntimos», «Un millón de euros».
  function importeEnLetra(centimos) {
    var euros = Math.floor(centimos / 100), cent = centimos % 100;
    if (euros > 999999999) return (centimos / 100).toFixed(2).replace('.', ',') + ' €';
    var txt = apocope(enteroEnLetras(euros));
    if (euros === 1) txt += ' euro';
    else txt += (euros >= 1e6 && euros % 1e6 === 0) ? ' de euros' : ' euros';
    if (cent) txt += ' con ' + apocope(enteroEnLetras(cent)) + (cent === 1 ? ' céntimo' : ' céntimos');
    return txt.charAt(0).toUpperCase() + txt.slice(1);
  }

  return {
    partidasUnicas: partidasUnicas,
    codigosPresupuesto: codigosPresupuesto,
    tipoRecurso: tipoRecurso,
    cuadroPrecios1: cuadroPrecios1,
    cuadroPrecios2: cuadroPrecios2,
    cuadrosRecursos: cuadrosRecursos,
    totalImporte: totalImporte,
    conciliacion: conciliacion,
    importeEnLetra: importeEnLetra
  };
});
