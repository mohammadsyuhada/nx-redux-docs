// Handheld / Mobile header toggle. Switching keeps the page's path under the
// other platform when that page exists, else goes to its overview.
(function () {
  var PLATFORMS = ["handheld", "mobile"];
  var LABELS = { handheld: "Handheld", mobile: "Mobile" };

  function platformOf(pageUrl) {
    var first = pageUrl.split("/")[0];
    return PLATFORMS.indexOf(first) >= 0 ? first : null;
  }

  function counterpart(pageUrl, pages) {
    var from = platformOf(pageUrl);
    if (!from) return null;
    var to = from === "handheld" ? "mobile" : "handheld";
    var candidate = to + pageUrl.slice(from.length);
    return pages.indexOf(candidate) >= 0 ? candidate : to + "/";
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { counterpart: counterpart, platformOf: platformOf };
    return;
  }

  function mount() {
    var page = window.NX_PAGE_URL || "";
    var base = window.NX_BASE_URL || ".";
    var current = platformOf(page);
    var header = document.querySelector(".md-header__inner");
    if (!current || !header) return;

    var group = document.createElement("nav");
    group.className = "nx-platform";
    group.setAttribute("aria-label", "Platform");

    PLATFORMS.forEach(function (p) {
      var link = document.createElement("a");
      link.className = "nx-platform__option";
      link.textContent = LABELS[p];
      if (p === current) {
        link.href = base + "/" + page;
        link.setAttribute("aria-current", "page");
      } else {
        // Overview first, so the link works even if the page list never loads.
        link.href = base + "/" + p + "/";
        fetch(base + "/platform-pages.json")
          .then(function (r) { return r.json(); })
          .then(function (pages) { link.href = base + "/" + counterpart(page, pages); })
          .catch(function () {});
      }
      group.appendChild(link);
    });

    header.insertBefore(group, header.querySelector(".md-search"));
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();
