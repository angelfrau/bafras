(function(){
  var TITULOS = {
    "": {
      t: "BAFRAS Engineering · Ingeniería multidisciplinar en Mallorca",
      d: "Ingeniería multidisciplinar en Mallorca: infraestructura, sistemas energéticos, sistemas digitales y automatización."
    },
    "capacidades": {
      t: "Capacidades: Infraestructura e Ingeniería, Sistemas Energéticos y Sistemas Digitales y Automatización · BAFRAS Engineering",
      d: "Infraestructura e instalaciones, sistemas energéticos, sistemas digitales y automatización en un mismo despacho de ingeniería en Mallorca."
    },
    "capacidades/infrastructure": {
      t: "Infraestructura e Ingeniería: instalaciones MEP y dirección de obra en Mallorca · BAFRAS Engineering",
      d: "Diseño, coordinación y dirección de instalaciones eléctricas y térmicas, reformas y ampliaciones en Mallorca. Ingeniería con experiencia real en obra."
    },
    "capacidades/energy-systems": {
      t: "Sistemas Energéticos: fotovoltaica, almacenamiento y eficiencia energética en Mallorca · BAFRAS Engineering",
      d: "Estudio, diseño y optimización de sistemas energéticos: generación fotovoltaica, almacenamiento BESS, electrificación y eficiencia para edificios e industria en Mallorca."
    },
    "capacidades/digital-systems": {
      t: "Sistemas Digitales y Automatización: control y datos para edificios e industria · BAFRAS Engineering",
      d: "Monitorización, automatización, BMS/SCADA e integración de sistemas para edificios e industria en Mallorca, con análisis de datos y herramientas digitales de ingeniería."
    },
    "sectores": {
      t: "Sectores: hoteles y turismo, industria, centros deportivos, edificios y sector terciario e infraestructuras · BAFRAS Engineering",
      d: "Sectores de BAFRAS Engineering en Mallorca: hoteles y turismo, industria, centros deportivos, edificios y sector terciario, infraestructuras y sector público."
    },
    "proyectos": {
      t: "Proyectos y experiencia del equipo · BAFRAS Engineering",
      d: "Proyectos y experiencia del equipo de BAFRAS Engineering en energía fotovoltaica y almacenamiento, instalaciones MEP y automatización."
    },
    "proyectos/experiencia-del-equipo/campus-universitario": {
      t: "Campus universitario · Solar fotovoltaica y almacenamiento · BAFRAS Engineering",
      d: "Generación fotovoltaica, almacenamiento energético, infraestructura eléctrica, movilidad eléctrica y gestión de la energía en un campus universitario."
    },
    "proyectos/experiencia-del-equipo/mep-hoteles-colegios-residencial": {
      t: "Hoteles, colegios y residencial de alto nivel · BAFRAS Engineering",
      d: "Instalaciones eléctricas, mecánicas, de fontanería y protección contra incendios en hoteles, colegios y residencial de alto nivel en Mallorca e Ibiza."
    },
    "proyectos/experiencia-del-equipo/energia-offshore-internacional": {
      t: "Proyecto energético internacional · BAFRAS Engineering",
      d: "Participación en proyectos de energía eólica marina de gran escala, con sistemas eléctricos, automatización y control."
    },
    "conocimiento": {
      t: "Conocimiento técnico: artículos, casos de estudio y guías · BAFRAS Engineering",
      d: "Artículos técnicos, casos de estudio, guías e innovación en instalaciones, energía y sistemas digitales para edificios e industria."
    },
    "sobre-bafras": {
      t: "Sobre BAFRAS: quiénes somos, equipo y filosofía · BAFRAS Engineering",
      d: "BAFRAS Engineering reúne tres trayectorias complementarias en instalaciones MEP, sistemas energéticos y automatización, con experiencia en proyectos de distinta escala."
    },
    "contacto": {
      t: "Contacto · BAFRAS Engineering",
      d: "Contacta con BAFRAS Engineering en Mallorca por correo o formulario."
    }
  };
  var paginas = Array.prototype.slice.call(document.querySelectorAll('.pagina'));
  var cab = document.getElementById('cabecera');
  var boton = document.getElementById('menuBoton');
  var metaDesc = document.querySelector('meta[name="description"]');
  function leer(){
    var h = decodeURIComponent(location.hash.replace(/^#\/?/, ''));
    var partes = h.split('@');
    return { ruta: partes[0].replace(/\/$/, ''), ancla: partes[1] || '' };
  }
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function irAAncla(id, suave){
    var el = id && document.querySelector('.pagina.activa #' + id);
    if (el) { el.scrollIntoView({behavior: suave && !reduce ? 'smooth' : 'instant', block: 'start'}); return true; }
    return false;
  }
  function aplicar(ruta){
    paginas.forEach(function(p){ p.classList.toggle('activa', p.getAttribute('data-pagina') === ruta); });
    var raiz = ruta.split('/')[0];
    document.querySelectorAll('.nav > ul > li > a').forEach(function(a){
      var seg = (a.getAttribute('href') || '').replace(/^#\/?/, '').split('@')[0].split('/')[0];
      if (seg && seg === raiz) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    var t = TITULOS[ruta] || TITULOS[''];
    document.title = t.t; if (metaDesc) metaDesc.setAttribute('content', t.d);
  }
  function mostrar(){
    var x = leer(), ruta = x.ruta;
    if (!paginas.some(function(p){ return p.getAttribute('data-pagina') === ruta; })) ruta = '';
    cab.classList.remove('abierta'); if (boton) boton.setAttribute('aria-expanded', 'false');
    var actual = document.querySelector('.pagina.activa');
    var misma = actual && actual.getAttribute('data-pagina') === ruta;
    if (misma) {                                   // mismo apartado: desplazamiento suave, sin recargar
      if (!irAAncla(x.ancla, true)) window.scrollTo({top: 0, behavior: reduce ? 'auto' : 'smooth'});
      return;
    }
    function cambiar(){ aplicar(ruta); window.scrollTo({top: 0, behavior: 'instant'}); if (x.ancla) irAAncla(x.ancla, false); }
    if (reduce || !actual) { cambiar(); return; }
    if (document.startViewTransition) {            // fundido cruzado nativo
      document.startViewTransition(cambiar);
    } else {                                       // respaldo: sale, cambia, entra
      var main = document.querySelector('main');
      main.classList.add('saliendo');
      setTimeout(function(){ cambiar(); main.classList.remove('saliendo'); }, 220);
    }
  }
  window.addEventListener('hashchange', mostrar);
  mostrar();
})();
