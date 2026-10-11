/* BAFRAS · lectura de BC3 (FIEBDC-3) y cálculo del presupuesto de venta.
   Sin dependencias. Funciona en el navegador y en Node (para pruebas).
   Importes en céntimos (enteros) para que las sumas cuadren exactamente. */
(function (raiz, fabrica) {
  var api = fabrica();
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else raiz.BC3 = api;
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  // El BC3 de Arquímedes va en Windows-1252 (ANSI).
  function decodificar(buffer) {
    return new TextDecoder('windows-1252').decode(buffer);
  }

  // Un registro empieza en una línea que comienza por "~". Las líneas que no
  // empiezan por "~" continúan el registro anterior (los ~D se parten en varias líneas).
  function registros(texto) {
    var out = [];
    texto.split(/\r\n|\r|\n/).forEach(function (linea) {
      if (linea === '') return;
      if (linea.charAt(0) === '~' || out.length === 0) out.push(linea);
      else out[out.length - 1] += linea;
    });
    return out;
  }

  function numero(s, defecto) {
    if (s === undefined || s === null || s === '') return defecto;
    var n = parseFloat(String(s).replace(',', '.'));
    return isFinite(n) ? n : defecto;
  }

  function concepto(conceptos, code) {
    return conceptos[code] || (conceptos[code] = {
      code: code, unidad: '', resumen: '', precio: 0, texto: '', hijos: []
    });
  }

  // ~C concepto · ~T texto largo · ~D descomposición CHILD\factor\cantidad\...
  function parsear(texto) {
    var conceptos = {}, raiz = null;
    registros(texto).forEach(function (r) {
      var p = r.split('|'), tipo = p[0];
      if (tipo === '~C') {
        var c = concepto(conceptos, p[1]);
        c.unidad = p[2] || '';
        c.resumen = p[3] || '';
        c.precio = numero(p[4], 0);
      } else if (tipo === '~T') {
        concepto(conceptos, p[1]).texto = p[2] || '';
      } else if (tipo === '~D') {
        var partes = (p[2] || '').split('\\'), hijos = [];
        for (var i = 0; i + 2 < partes.length; i += 3) {
          if (partes[i]) hijos.push({
            code: partes[i],
            factor: numero(partes[i + 1], 1),
            cantidad: numero(partes[i + 2], 1)
          });
        }
        concepto(conceptos, p[1]).hijos = hijos;
        if (raiz === null) raiz = p[1];
      }
    });
    if (raiz === null) throw new Error('El archivo no contiene un presupuesto (faltan registros ~D).');
    return { conceptos: conceptos, raiz: raiz };
  }

  // Los capítulos son los conceptos cuyo código acaba en "#" (01#, 04.01#...).
  function esCapitulo(code) {
    return code.charAt(code.length - 1) === '#';
  }

  function suma(lista, campo) {
    return lista.reduce(function (acc, x) { return acc + x[campo]; }, 0);
  }

  // coef: se multiplica por el precio del BC3 (1 si el BC3 ya trae precios de venta).
  // ivaPct: IVA en % (21). Precio unitario redondeado a céntimo; importe = precio × cantidad, a céntimo.
  function calcular(datos, coef, ivaPct) {
    var C = datos.conceptos, partidas = 0;

    function nodo(h, mult) {
      var c = C[h.code];
      if (!c) throw new Error('Concepto sin definir en el BC3: ' + h.code);
      var cant = mult * h.factor * h.cantidad;
      if (esCapitulo(h.code)) {
        var hijos = c.hijos.map(function (x) { return nodo(x, cant); });
        return {
          tipo: 'capitulo', code: h.code, nombre: c.resumen, hijos: hijos,
          centimos: suma(hijos, 'centimos')
        };
      }
      partidas += 1;
      var pvp = Math.round(c.precio * coef * 100);
      return {
        tipo: 'partida', code: h.code, unidad: c.unidad, resumen: c.resumen, texto: c.texto,
        cantidad: cant, pvpUd: pvp, centimos: Math.round(pvp * cant)
      };
    }

    var raiz = C[datos.raiz];
    var capitulos = raiz.hijos.map(function (h) { return nodo(h, 1); });
    var subtotal = suma(capitulos, 'centimos');
    return {
      titulo: raiz.resumen,
      capitulos: capitulos,
      subtotal: subtotal,
      iva: Math.round(subtotal * ivaPct / 100),
      total: subtotal + Math.round(subtotal * ivaPct / 100),
      numPartidas: partidas,
      coef: coef,
      ivaPct: ivaPct
    };
  }

  // 1234567 céntimos -> "12.345,67"
  function euros(c) {
    var neg = c < 0;
    c = Math.abs(c);
    var ent = Math.floor(c / 100), dec = c % 100;
    var s = String(ent).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    return (neg ? '-' : '') + s + ',' + (dec < 10 ? '0' : '') + dec;
  }

  return { decodificar: decodificar, registros: registros, parsear: parsear,
           calcular: calcular, euros: euros, esCapitulo: esCapitulo };
});
