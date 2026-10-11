/* BAFRAS · datos de los documentos de trabajo: cuadros de precios, cuadros de recursos
   y mediciones. Parte del árbol que devuelve BC3.calcular y del BC3 leído (datos.conceptos).
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

  // Tipo de un recurso según su código. En estos BC3 el campo «tipo» viene a 0 en todos los
  // conceptos, así que se mira el código: REF.MO.010 es mano de obra; MQ o MAQ, maquinaria;
  // el resto, materiales.
  function tipoRecurso(codigo) {
    var partes = codigo.toUpperCase().split('.');
    if (partes.indexOf('MO') !== -1) return 'mano';
    if (partes.indexOf('MQ') !== -1 || partes.indexOf('MAQ') !== -1) return 'maquinaria';
    return 'materiales';
  }

  // Cuadro nº 1: una línea por partida, con su precio unitario.
  function cuadroPrecios1(r) {
    return partidasUnicas(r).map(function (p) {
      return { codigo: p.code, unidad: p.unidad, resumen: p.resumen, texto: p.texto, pvpUd: p.pvpUd };
    });
  }

  // Líneas de la descomposición de una partida, por unidad de partida. Cada línea lleva el
  // rendimiento, el precio del recurso y el importe (rendimiento × precio, a céntimo).
  function lineasDescomposicion(datos, codigo, coef) {
    return concepto(datos, codigo).hijos.map(function (h) {
      var hijo = concepto(datos, h.code);
      var rendimiento = h.factor * h.cantidad;
      var precio = precioVenta(datos, h.code, coef);
      return {
        codigo: h.code, unidad: hijo.unidad, resumen: hijo.resumen,
        rendimiento: rendimiento, precio: precio, importe: aCentimos(rendimiento * precio)
      };
    });
  }

  // Cuadro nº 2: cada partida (sin repetir) con las líneas de su descomposición.
  // «redondeo» es lo que falta para que las líneas sumen el precio de la partida (céntimos).
  function cuadroPrecios2(r, datos) {
    return partidasUnicas(r).map(function (p) {
      var descompuesta = tieneDescomposicion(datos, p.code);
      var lineas = descompuesta ? lineasDescomposicion(datos, p.code, r.coef) : [];
      var suma = lineas.reduce(function (s, l) { return s + l.importe; }, 0);
      return {
        codigo: p.code, unidad: p.unidad, resumen: p.resumen, pvpUd: p.pvpUd,
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

    var grupos = { mano: [], maquinaria: [], materiales: [] };
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
    var maquinaria = totalImporte(rec.maquinaria);
    var mano = totalImporte(rec.mano);
    var rPartidas = redondeoPartidas(r, datos);
    return {
      materiales: materiales,
      maquinaria: maquinaria,
      mano: mano,
      directas: directas,
      redondeoPartidas: rPartidas,
      redondeoImportes: r.subtotal - (materiales + maquinaria + mano + directas + rPartidas),
      total: r.subtotal
    };
  }

  return {
    partidasUnicas: partidasUnicas,
    tipoRecurso: tipoRecurso,
    cuadroPrecios1: cuadroPrecios1,
    cuadroPrecios2: cuadroPrecios2,
    cuadrosRecursos: cuadrosRecursos,
    totalImporte: totalImporte,
    conciliacion: conciliacion
  };
});
