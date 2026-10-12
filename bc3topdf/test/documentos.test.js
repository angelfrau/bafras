// Pruebas de bc3.js, documentos.js y el formato de números de pdf-base.js. Sin navegador.
// Ejecutar desde bc3topdf/:  node --test test/
//
// El BC3 de prueba va escrito aquí, con datos inventados. Para probar con un BC3 real:
//   BC3_PRUEBA=/ruta/al/presupuesto.bc3 node --test test/
// (ese archivo no se guarda en el repositorio: son datos de un cliente).
'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');

const BC3 = require('../bc3.js');
const Docs = require('../documentos.js');

global.window = {};
require('../pdf-base.js');
const Base = window.BC3PDFBase;

// Un registro ~D: hijos como [codigo, factor, cantidad].
function descomposicion(padre, hijos) {
  return '~D|' + padre + '|' + hijos.flat().join('\\') + '|';
}

// Obra de prueba (datos inventados):
//   P.1 (55,00 €/ud)  = 1 MAT.1 + 0,5 h MO.01 + 0,25 h MQ.1
//   P.2 (10,02 €/m)   = 4 m MAT.2 (1,755 €/m) + 0,1 h REF.MO.02
//   P.3 (50,00 €/ud)  sin descomponer
// Capítulo 01#: P.1 × 2, P.2 × 3, P.3 × 1. Capítulo 02#: P.2 × 1 (la misma partida, otro capítulo).
const FIXTURE = [
  '~V|PRUEBA|FIEBDC-3/2016|||ANSI|Prueba|2|',
  '~C|RAIZ##||Obra de prueba|0|091026|0|',
  '~C|01#||Capitulo uno|0|091026|0|',
  '~C|02#||Capitulo dos|0|091026|0|',
  '~C|P.1|ud|Partida uno|55.00|091026|0|',
  '~C|P.2|m|Partida dos|10.02|091026|0|',
  '~C|P.3|ud|Partida tres sin descomponer|50.00|091026|0|',
  '~C|MO.01|h|Mano de obra oficial|40.00|091026|0|',
  '~C|REF.MO.02|h|Mano de obra ayudante|30.00|091026|0|',
  '~C|MAT.1|ud|Material uno|20.00|091026|0|',
  '~C|MAT.2|m|Material dos|1.755|091026|0|',
  '~C|MQ.1|h|Grua|60.00|091026|0|',
  '~T|P.1|Texto de la partida uno|',
  descomposicion('RAIZ##', [['01#', 1, 1], ['02#', 1, 1]]),
  descomposicion('01#', [['P.1', 1, 2], ['P.2', 1, 3], ['P.3', 1, 1]]),
  descomposicion('02#', [['P.2', 1, 1]]),
  descomposicion('P.1', [['MAT.1', 1, 1], ['MO.01', 1, 0.5], ['MQ.1', 1, 0.25]]),
  descomposicion('P.2', [['MAT.2', 1, 4], ['REF.MO.02', 1, 0.1]]),
].join('\r\n');

const datos = BC3.parsear(FIXTURE);
const r = BC3.calcular(datos, 1, 21);

test('calcular: importes de capítulos y presupuesto', () => {
  // 01#: 2 × 5.500 + 3 × 1.002 + 1 × 5.000 = 19.006 c. · 02#: 1 × 1.002 c.
  assert.equal(r.capitulos[0].hijos.length, 3);
  assert.equal(r.capitulos[0].centimos, 2 * 5500 + 3 * 1002 + 5000);
  assert.equal(r.capitulos[1].centimos, 1002);
  assert.equal(r.subtotal, 2 * 5500 + 4 * 1002 + 5000);
  assert.equal(r.iva, Math.round(r.subtotal * 0.21));
});

test('partidasUnicas: cada partida una vez, en orden de aparición', () => {
  const codigos = Docs.partidasUnicas(r).map((p) => p.code);
  assert.deepEqual(codigos, ['P.1', 'P.2', 'P.3']);
});

test('códigos de presupuesto: capítulo y orden, como en el presupuesto', () => {
  // Capítulo 01#: P.1, P.2 y P.3 → 01.01, 01.02, 01.03. Capítulo 02#: P.2 (otra aparición) → 02.01.
  const mapa = Docs.codigosPresupuesto(r);
  assert.deepEqual(r.capitulos[0].hijos.map((x) => mapa.get(x)), ['01.01', '01.02', '01.03']);
  assert.equal(mapa.get(r.capitulos[1].hijos[0]), '02.01');
  // Cuadros nº 1 y nº 2: cada partida una vez, con todos sus códigos. P.2 está en 01# y en 02#.
  assert.deepEqual(Docs.cuadroPrecios1(r).map((p) => p.codigos), [['01.01'], ['01.02', '02.01'], ['01.03']]);
  assert.deepEqual(Docs.cuadroPrecios2(r, datos).map((p) => p.codigos), [['01.01'], ['01.02', '02.01'], ['01.03']]);
});

test('códigos de presupuesto en subcapítulos y con partidas repetidas', () => {
  // 04.01# (X.1, X.2) y 04.02# (X.2 otra vez, Y.1): el subcapítulo añade su código al de la partida.
  const txt = [
    '~V|SUB|FIEBDC-3/2016|||ANSI|Subcapitulos|2|',
    '~C|RAIZ##||Obra|0|091026|0|',
    '~C|04#||Instalacion|0|091026|0|',
    '~C|04.01#||Subcapitulo uno|0|091026|0|',
    '~C|04.02#||Subcapitulo dos|0|091026|0|',
    '~C|X.1|ud|Partida X1|10.00|091026|0|',
    '~C|X.2|ud|Partida X2|20.00|091026|0|',
    '~C|Y.1|ud|Partida Y1|30.00|091026|0|',
    descomposicion('RAIZ##', [['04#', 1, 1]]),
    descomposicion('04#', [['04.01#', 1, 1], ['04.02#', 1, 1]]),
    descomposicion('04.01#', [['X.1', 1, 1], ['X.2', 1, 1]]),
    descomposicion('04.02#', [['X.2', 1, 1], ['Y.1', 1, 1]]),
  ].join('\r\n');
  const d = BC3.parsear(txt);
  const rr = BC3.calcular(d, 1, 21);
  const mapa = Docs.codigosPresupuesto(rr);
  const [sub1, sub2] = rr.capitulos[0].hijos;
  assert.deepEqual(sub1.hijos.map((x) => mapa.get(x)), ['04.01.01', '04.01.02']);
  assert.deepEqual(sub2.hijos.map((x) => mapa.get(x)), ['04.02.01', '04.02.02']);
  // X.2 aparece en 04.01 y en 04.02: en el cuadro nº 1, una vez, con sus dos códigos.
  assert.deepEqual(Docs.cuadroPrecios1(rr).map((p) => p.codigos), [['04.01.01'], ['04.01.02', '04.02.01'], ['04.02.02']]);
});

test('cuadro nº 1: precio unitario de cada partida', () => {
  const lista = Docs.cuadroPrecios1(r);
  assert.deepEqual(lista.map((p) => p.pvpUd), [5500, 1002, 5000]);
  assert.equal(lista[0].texto, 'Texto de la partida uno');
});

test('cuadro nº 2: líneas de descomposición que suman el precio', () => {
  const cuadro = Docs.cuadroPrecios2(r, datos);

  const p1 = cuadro[0];
  assert.equal(p1.descompuesta, true);
  assert.deepEqual(p1.lineas.map((l) => l.codigo), ['MAT.1', 'MO.01', 'MQ.1']);
  assert.deepEqual(p1.lineas.map((l) => l.importe), [2000, 2000, 1500]);
  assert.equal(p1.lineas.reduce((s, l) => s + l.importe, 0), p1.pvpUd);
  assert.equal(p1.redondeo, 0);

  const p2 = cuadro[1];
  assert.deepEqual(p2.lineas.map((l) => l.importe), [702, 300]);
  assert.equal(p2.lineas.reduce((s, l) => s + l.importe, 0), p2.pvpUd);
  assert.equal(p2.redondeo, 0);

  const p3 = cuadro[2];
  assert.equal(p3.descompuesta, false);
  assert.deepEqual(p3.lineas, []);
  assert.equal(p3.redondeo, 0);
});

test('cuadros de recursos: cantidades totales, con P.2 en dos capítulos', () => {
  const rec = Docs.cuadrosRecursos(r, datos);

  // Mano de obra: MO.01 = 2 × 0,5 h; REF.MO.02 = 3 × 0,1 h + 1 × 0,1 h
  assert.deepEqual(rec.mano.map((x) => x.codigo), ['MO.01', 'REF.MO.02']);
  assert.ok(Math.abs(rec.mano[0].cantidad - 1) < 1e-9);
  assert.ok(Math.abs(rec.mano[1].cantidad - 0.4) < 1e-9);
  assert.deepEqual(rec.mano.map((x) => x.importe), [4000, 1200]);

  // Maquinaria: MQ.1 = 2 × 0,25 h
  assert.deepEqual(rec.maquinaria.map((x) => x.codigo), ['MQ.1']);
  assert.ok(Math.abs(rec.maquinaria[0].cantidad - 0.5) < 1e-9);
  assert.deepEqual(rec.maquinaria.map((x) => x.importe), [3000]);

  // Materiales: MAT.1 = 2 × 1; MAT.2 = 3 × 4 + 1 × 4 = 16 m
  assert.deepEqual(rec.materiales.map((x) => x.codigo), ['MAT.1', 'MAT.2']);
  assert.deepEqual(rec.materiales.map((x) => x.cantidad), [2, 16]);
  assert.deepEqual(rec.materiales.map((x) => x.importe), [4000, 2808]);

  assert.equal(rec.numSinDescomponer, 1);
});

test('cuadros de recursos suman lo mismo que las partidas descompuestas', () => {
  const rec = Docs.cuadrosRecursos(r, datos);
  const total = Docs.totalImporte(rec.mano) + Docs.totalImporte(rec.maquinaria) + Docs.totalImporte(rec.materiales) + Docs.totalImporte(rec.otros);
  // P.1 × 2 = 11.000 c. · P.2 × 4 = 4.008 c.
  assert.equal(total, 2 * 5500 + 4 * 1002);
});

test('conciliación: recursos + partidas directas + redondeos = presupuesto', () => {
  const con = Docs.conciliacion(r, datos);
  assert.equal(con.materiales, 4000 + 2808);
  assert.equal(con.mano, 4000 + 1200);
  assert.equal(con.maquinaria, 3000);
  assert.equal(con.directas, 5000);
  // Las partidas de la obra de prueba tienen precios exactos: no hay redondeo.
  assert.equal(con.redondeoPartidas, 0);
  assert.equal(con.redondeoImportes, 0);
  assert.equal(con.total, r.subtotal);
});

test('cuadro nº 2: si las líneas no suman el precio de la partida, la diferencia es el redondeo', () => {
  // Tres recursos de 0,333 € por unidad suman 0,999 €; la partida, redondeada, vale 1,00 €.
  const txt = [
    '~V|REDONDEO|FIEBDC-3/2016|||ANSI|Redondeo|2|',
    '~C|RAIZ##||Obra|0|091026|0|',
    '~C|01#||Capitulo|0|091026|0|',
    '~C|PR|ud|Partida redondeada|1.00|091026|0|',
    '~C|A.1|ud|Recurso A|0.333|091026|0|',
    '~C|A.2|ud|Recurso B|0.333|091026|0|',
    '~C|A.3|ud|Recurso C|0.333|091026|0|',
    descomposicion('RAIZ##', [['01#', 1, 1]]),
    descomposicion('01#', [['PR', 1, 1]]),
    descomposicion('PR', [['A.1', 1, 1], ['A.2', 1, 1], ['A.3', 1, 1]]),
  ].join('\r\n');
  const d = BC3.parsear(txt);
  const rr = BC3.calcular(d, 1, 21);

  const p = Docs.cuadroPrecios2(rr, d)[0];
  assert.deepEqual(p.lineas.map((l) => l.importe), [33, 33, 33]);
  assert.equal(p.redondeo, 1);

  const con = Docs.conciliacion(rr, d);
  assert.equal(con.total, 100);
  assert.equal(con.materiales, 99);
  assert.equal(con.redondeoPartidas, 0);
  assert.equal(con.redondeoImportes, 1);
});

test('maquinaria vacía: lista vacía y sin error', () => {
  // Quita MQ.1 de la descomposición de P.1 (el concepto puede seguir definido).
  const sinMaquinaria = BC3.parsear(FIXTURE.replace('\\MQ.1\\1\\0.25|', '|'));
  const rr = BC3.calcular(sinMaquinaria, 1, 21);
  const rec = Docs.cuadrosRecursos(rr, sinMaquinaria);
  assert.deepEqual(rec.maquinaria, []);
  assert.equal(rec.mano.length, 2);
});

test('tipoRecurso: mano de obra, maquinaria y materiales según el código', () => {
  assert.equal(Docs.tipoRecurso('REF.MO.010'), 'mano');
  assert.equal(Docs.tipoRecurso('MO.01'), 'mano');
  assert.equal(Docs.tipoRecurso('MQ.1'), 'maquinaria');
  assert.equal(Docs.tipoRecurso('GEN.MAQ.7'), 'maquinaria');
  assert.equal(Docs.tipoRecurso('FV.PAN.031'), 'materiales');
  assert.equal(Docs.tipoRecurso('BT.CCA.010'), 'materiales');
  assert.equal(Docs.tipoRecurso('ACT.PRU.011'), 'otros');
  assert.equal(Docs.tipoRecurso('ACT.IMP.011'), 'materiales');
});

test('formato de números: coma, miles, decimales mínimos y máximos', () => {
  assert.equal(Base.formatoNumero(40.5, 2, 4), '40,50');
  assert.equal(Base.formatoNumero(37.1115, 2, 4), '37,1115');
  assert.equal(Base.formatoNumero(62.397, 2, 4), '62,397');
  assert.equal(Base.formatoNumero(0.0244897959 * 490, 0, 4), '12');
  assert.equal(Base.formatoNumero(0.0244897959, 0, 4), '0,0245');
  assert.equal(Base.formatoNumero(247.1233, 0, 4), '247,1233');
  assert.equal(Base.formatoNumero(1234.5, 2, 2), '1.234,50');
  assert.equal(Base.formatoNumero(-3.5, 0, 2), '-3,5');
});

test('euros: céntimos a texto español', () => {
  assert.equal(BC3.euros(1234567), '12.345,67');
  assert.equal(BC3.euros(5), '0,05');
});

// ---- BC3 real, si se indica por variable de entorno (no se guarda en el repositorio) ----
const real = process.env.BC3_PRUEBA;
test('BC3 real (opcional): cuadros y conciliación con el presupuesto', { skip: !real || !fs.existsSync(real) }, () => {
  const d = BC3.parsear(BC3.decodificar(fs.readFileSync(real)));
  const rr = BC3.calcular(d, 1, 21);
  const cuadro1 = Docs.cuadroPrecios1(rr);
  const cuadro2 = Docs.cuadroPrecios2(rr, d);
  const con = Docs.conciliacion(rr, d);

  // Códigos de presupuesto: uno por aparición de cada partida, en los cuadros nº 1 y nº 2.
  // La bandeja BT.BAN.030 está en 04.01 y en 04.02: tiene dos códigos.
  assert.deepEqual(cuadro1.slice(0, 3).map((p) => p.codigos), [['00.01'], ['00.02'], ['01.01']]);
  const porCuadro1 = cuadro1.flatMap((p) => p.codigos);
  assert.equal(porCuadro1.length, rr.numPartidas);
  assert.equal(new Set(porCuadro1).size, porCuadro1.length);
  porCuadro1.forEach((c) => assert.match(c, /^\d{2}(\.\d{2}){1,2}$/, 'código ' + c));
  assert.equal(cuadro2.flatMap((p) => p.codigos).length, rr.numPartidas);
  const bandeja = 'Bandeja metálica 60×100 con tapa';
  assert.deepEqual(cuadro1.find((p) => p.resumen === bandeja).codigos, ['04.01.07', '04.02.09']);
  assert.deepEqual(cuadro2.find((p) => p.resumen === bandeja).codigos, ['04.01.07', '04.02.09']);

  // Cada partida descompuesta: sus líneas más su redondeo suman su precio.
  cuadro2.filter((p) => p.descompuesta).forEach((p) => {
    assert.equal(p.lineas.reduce((s, l) => s + l.importe, 0) + p.redondeo, p.pvpUd, 'bloque ' + p.codigos.join(' '));
  });

  // La conciliación cierra con el presupuesto, y los redondeos son pequeños.
  assert.equal(con.total, rr.subtotal);
  assert.ok(Math.abs(con.redondeoPartidas) < 500, 'redondeo de partidas mayor de 5 €');
  assert.ok(Math.abs(con.redondeoImportes) < 50, 'redondeo de importes mayor de 0,50 €');
  console.log('  Redondeo de partidas ' + (con.redondeoPartidas / 100).toFixed(2) +
    ' € · redondeo de importes ' + (con.redondeoImportes / 100).toFixed(2) +
    ' € · presupuesto ' + (rr.subtotal / 100).toFixed(2) + ' €');
});
