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
