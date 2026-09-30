(function(){
  var f = document.getElementById('formulario');
  if (f) f.addEventListener('submit', function(e){
    e.preventDefault();
    var aviso = document.getElementById('avisoForm'), btn = f.querySelector('button[type=submit]');
    btn.disabled = true; btn.textContent = 'Enviando…';
    fetch('https://formsubmit.co/ajax/info@bafras.com', {method:'POST', headers:{'Accept':'application/json'}, body:new FormData(f)})
      .then(function(r){ if(!r.ok) throw 0; aviso.textContent = 'Consulta enviada. Te responderemos lo antes posible.'; f.reset(); })
      .catch(function(){ aviso.innerHTML = 'No se ha podido enviar. Escríbenos directamente a <a href="mailto:info@bafras.com">info@bafras.com</a>.'; })
      .then(function(){ aviso.classList.add('visible'); btn.disabled = false; btn.textContent = 'Enviar consulta'; });
  });})();
