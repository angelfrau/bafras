(function(){
  var cab = document.getElementById('cabecera');
  var boton = document.getElementById('menuBoton');
  if (boton) boton.addEventListener('click', function(){
    var ab = cab.classList.toggle('abierta'); boton.setAttribute('aria-expanded', ab);
  });
  document.querySelectorAll('[data-foto]').forEach(function(caja){
    var nombres = caja.getAttribute('data-foto').split(','), exts = ['png', 'jpg', 'jpeg', 'webp', 'PNG', 'JPG', 'JPEG'], cand = [];
    nombres.forEach(function(n){ exts.forEach(function(e){ cand.push('/assets/images/team/' + n + '.' + e); }); });
    var i = 0;
    (function probar(){
      if (i >= cand.length) return;
      var im = new Image(); im.alt = '';
      im.onload = function(){ caja.classList.add('con-foto'); caja.appendChild(im); };
      im.onerror = probar;
      im.src = cand[i++];
    })();
  });
  var an = document.getElementById('anio'); if (an) an.textContent = new Date().getFullYear();
})();
