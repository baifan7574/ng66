(function () {
  // 广告 1：Vignette banner（Anti-AdBlock）
  var vignette = document.createElement("script");
  vignette.src = "https://fpyf8.com/88/tag.min.js";
  vignette.async = true;
  vignette.setAttribute("data-zone", "9625896");  // Vignette Banner
  vignette.setAttribute("data-cfasync", "false");
  document.head.appendChild(vignette);

  // 广告 2：In-Page Push（Anti-AdBlock）
  var push = document.createElement("script");
  push.src = "https://fpyf8.com/88/tag.min.js";
  push.async = true;
  push.setAttribute("data-zone", "9625893");  // In-Page Push Banner
  push.setAttribute("data-cfasync", "false");
  document.body.appendChild(push);  // 放 body 避免冲突
})();
