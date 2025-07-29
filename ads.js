(function () {
  // === Monetag - Vignette Banner
  var vignette = document.createElement("script");
  vignette.src = "https://fpyf8.com/88/tag.min.js";
  vignette.async = true;
  vignette.setAttribute("data-zone", "9625896");
  vignette.setAttribute("data-cfasync", "false");
  document.head.appendChild(vignette);

  // === Monetag - In-Page Push
  var push = document.createElement("script");
  push.src = "https://fpyf8.com/88/tag.min.js";
  push.async = true;
  push.setAttribute("data-zone", "9625893");
  push.setAttribute("data-cfasync", "false");
  document.body.appendChild(push);

  // === AdCash - AutoTag
  var aclibScript = document.createElement("script");
  aclibScript.id = "aclib";
  aclibScript.type = "text/javascript";
  aclibScript.src = "//acscdn.com/script/aclib.js";
  aclibScript.async = true;
  aclibScript.onload = function () {
    if (typeof aclib !== 'undefined') {
      aclib.runAutoTag({
        zoneId: "jqeh7xui71d"
      });
    } else {
      console.error("AdCash AutoTag 未加载成功");
    }
  };
  document.head.appendChild(aclibScript);
})();