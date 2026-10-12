// BAFRAS · construir-html.js
// Genera bc3topdf.html: una sola página con el CSS, las librerías y el código de bc3topdf/ incrustados.
// Uso desde la raíz del repositorio:
//   node bc3topdf/construir-html.js                     escribe bc3topdf.html en la raíz
//   node bc3topdf/construir-html.js <carpeta> <salida>  para generarlo en otro sitio
'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');

const carpeta = path.resolve(process.argv[2] || __dirname);
const salida = path.resolve(process.argv[3] || path.join(carpeta, '..', 'bc3topdf.html'));

const leer = (f) => fs.readFileSync(path.join(carpeta, f), 'utf8');
// Desde bc3topdf/ el logotipo está en ../images/; desde la raíz del sitio, en images/.
const rutas = (texto) => texto.replace(/\.\.\/images\//g, 'images/');
// Un </script> dentro del código cerraría la etiqueta antes de tiempo.
const enScript = (texto) => texto.replace(/<\/script/gi, '<\\/script');
// Dentro de un comentario HTML no puede aparecer "--".
const enComentario = (texto) => texto.replace(/--/g, '- -').trim();

let commit = 'sin git';
try {
  commit = execFileSync('git', ['rev-parse', '--short', 'HEAD'], { cwd: carpeta, encoding: 'utf8' }).trim();
} catch (e) {
  // Sin repositorio se genera igual; solo falta el número de commit en la cabecera.
}

const licencias = ['vendor/LICENSE-pdf-lib.md', 'vendor/LICENSE-fontkit.txt', 'vendor/LICENSE-Liberation.txt']
  .map((f) => `${f}\n${enComentario(leer(f))}`)
  .join('\n\n');

const cabecera = `<!--
BAFRAS · bc3topdf.html: archivo único generado por construir-html.js a partir de bc3topdf/ (commit ${commit}).
No se edita a mano: para cambiarlo, edita bc3topdf/ y vuelve a generarlo.

Librerías y fuentes incrustadas, con sus licencias:

${licencias}
-->`;

const original = leer('index.html');
const hojasLocales = (original.match(/<link rel="stylesheet" href="(?!https?:)[^"]+">/g) || []).length;
const scriptsLocales = (original.match(/<script src="[^"]+"><\/script>/g) || []).length;

let html = rutas(original);
html = html.replace('<!doctype html>', (m) => `${m}\n${cabecera}`);

let hojas = 0;
html = html.replace(/<link rel="stylesheet" href="(?!https?:)([^"]+)">/g, (_, f) => {
  hojas++;
  return `<style>\n${rutas(leer(f))}\n</style>`;
});

let scripts = 0;
html = html.replace(/<script src="([^"]+)"><\/script>/g, (_, f) => {
  scripts++;
  return `<script>\n${enScript(rutas(leer(f)))}\n</script>`;
});

if (hojas !== hojasLocales || scripts !== scriptsLocales || /<script src=|href="style\.css"/.test(html)) {
  throw new Error('Quedan archivos locales sin incrustar en index.html');
}

fs.writeFileSync(salida, html, 'utf8');
const mb = (Buffer.byteLength(html, 'utf8') / 1048576).toFixed(2);
console.log(`Escrito ${salida}: ${mb} MB, ${scripts} scripts y ${hojas} hoja de estilos incrustados (commit ${commit}).`);
