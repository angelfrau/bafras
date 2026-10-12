// Pruebas del importe en letra del cuadro nº 1 (documentos.js). Sin navegador.
// Ejecutar desde bc3topdf/:  node --test test/letras.test.js
'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const Docs = require('../documentos.js');

const L = Docs.importeEnLetra;

test('importeEnLetra: euros enteros', () => {
  assert.equal(L(0), 'Cero euros');
  assert.equal(L(100), 'Un euro');
  assert.equal(L(1600), 'Dieciséis euros');
  assert.equal(L(2200), 'Veintidós euros');
  assert.equal(L(3100), 'Treinta y un euros');
  assert.equal(L(10000), 'Cien euros');
  assert.equal(L(10100), 'Ciento un euros');
  assert.equal(L(100000), 'Mil euros');
  assert.equal(L(100100), 'Mil un euros');
  assert.equal(L(194400), 'Mil novecientos cuarenta y cuatro euros');
  assert.equal(L(2100000), 'Veintiún mil euros');
});

test('importeEnLetra: céntimos', () => {
  assert.equal(L(1), 'Cero euros con un céntimo');
  assert.equal(L(5), 'Cero euros con cinco céntimos');
  assert.equal(L(275), 'Dos euros con setenta y cinco céntimos');
  assert.equal(L(1905), 'Diecinueve euros con cinco céntimos');
  assert.equal(L(2175), 'Veintiún euros con setenta y cinco céntimos');
  assert.equal(L(7020), 'Setenta euros con veinte céntimos');
});

test('importeEnLetra: millones, con «de» cuando no hay más cifras', () => {
  assert.equal(L(100000000), 'Un millón de euros');
  assert.equal(L(150000000), 'Un millón quinientos mil euros');
  assert.equal(L(200000000), 'Dos millones de euros');
  assert.equal(L(2100000000), 'Veintiún millones de euros');
});
