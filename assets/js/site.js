// Menú móvil accesible (mejora progresiva): sin JS la navegación permanece visible.
(function () {
  "use strict";
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("site-nav");
  if (!toggle || !nav) return;

  var mobile = window.matchMedia("(max-width: 760px)");
  document.documentElement.classList.add("js");

  function setOpen(open) {
    toggle.setAttribute("aria-expanded", String(open));
    nav.classList.toggle("is-open", open);
  }

  function sync() {
    toggle.hidden = !mobile.matches;
    if (!mobile.matches) setOpen(false);
  }

  toggle.addEventListener("click", function () {
    setOpen(toggle.getAttribute("aria-expanded") !== "true");
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
      setOpen(false);
      toggle.focus();
    }
  });

  if (mobile.addEventListener) mobile.addEventListener("change", sync);
  else mobile.addListener(sync);
  sync();
})();

// Cartera BAFRAS (WEB-EXPERIENCE-04): carril con desplazamiento propio. Sin JS, el carril se desplaza de forma nativa
// (táctil, rueda, teclado sobre el carril enfocable). Los botones solo se muestran si hay desplazamiento efectivo,
// se deshabilitan en los extremos y no mueven el foco. Sin autoplay.
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

  Array.prototype.forEach.call(document.querySelectorAll("[data-portfolio]"), function (root) {
    var track = root.querySelector(".portfolio__track");
    var controls = root.querySelector(".portfolio__controls");
    var prev = root.querySelector("[data-portfolio-prev]");
    var next = root.querySelector("[data-portfolio-next]");
    if (!track || !controls || !prev || !next) return;

    // aria-disabled (no `disabled`): el botón conserva el foco al llegar a un extremo.
    function setEnabled(button, enabled) {
      button.setAttribute("aria-disabled", String(!enabled));
    }

    function update() {
      var max = track.scrollWidth - track.clientWidth;
      var scrollable = max > 1;
      controls.hidden = !scrollable;
      setEnabled(prev, scrollable && track.scrollLeft > 1);
      setEnabled(next, scrollable && track.scrollLeft < max - 1);
    }

    function step(direction) {
      if ((direction < 0 ? prev : next).getAttribute("aria-disabled") === "true") return;
      var card = track.querySelector(".portfolio-card");
      var gap = parseFloat(getComputedStyle(track).columnGap) || 0;
      var amount = card ? card.getBoundingClientRect().width + gap : track.clientWidth;
      track.scrollBy({ left: direction * amount, behavior: reduce.matches ? "auto" : "smooth" });
    }

    prev.addEventListener("click", function () { step(-1); });
    next.addEventListener("click", function () { step(1); });
    track.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
  });
})();
