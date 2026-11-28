(function () {
  function fit() {
    document.querySelectorAll('.viewport').forEach(function (v) {
      var f = v.querySelector('.frame');
      var s = v.clientWidth / 1440;
      f.style.transform = 'scale(' + s + ')';
      v.style.height = Math.round(900 * s) + 'px';
    });
  }
  if (window.lucide) window.lucide.createIcons();
  fit();
  window.addEventListener('resize', fit);
  if (window.ResizeObserver) new ResizeObserver(fit).observe(document.body);
})();
