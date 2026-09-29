// Marks the sidebar category that is pinned while its pages scroll
// underneath, so CSS can turn its pill into a bar as wide as the sidebar.
// Categories pin just below the tab's own title at the top of the sidebar.
(function () {
  function watch() {
    var wrap = document.querySelector(".md-sidebar--primary .md-sidebar__scrollwrap");
    if (!wrap) return;
    var labels = Array.prototype.slice.call(wrap.querySelectorAll(
      ".md-nav--primary .md-nav__item--section .md-nav__item--section > .md-nav__link"
    ));
    if (!labels.length) return;
    var title = wrap.querySelector(".md-nav--primary > .md-nav__list > .md-nav__item--section > .md-nav__link");
    var ticking = false;

    function layout() {
      var pinTop = title ? title.getBoundingClientRect().height : 0;
      labels.forEach(function (label) { label.style.setProperty("--nx-pin-top", pinTop + "px"); });
      update();
    }

    function update() {
      ticking = false;
      var box = wrap.getBoundingClientRect();
      labels.forEach(function (label) {
        var pinTop = box.top + (parseFloat(getComputedStyle(label).top) || 0);
        var labelTop = label.getBoundingClientRect().top;
        var groupTop = label.parentElement.getBoundingClientRect().top;
        // Pinned: held in place while its group has already scrolled past.
        var stuck = Math.abs(labelTop - pinTop) < 1 && groupTop < labelTop - 1;
        if (stuck) {
          var shift = box.left - label.parentElement.getBoundingClientRect().left;
          label.style.setProperty("--nx-bar-shift", shift + "px");
          label.style.setProperty("--nx-bar-width", wrap.clientWidth + "px");
        }
        label.classList.toggle("is-stuck", stuck);
      });
    }

    wrap.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    window.addEventListener("resize", layout);
    layout();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", watch);
  else watch();
})();
