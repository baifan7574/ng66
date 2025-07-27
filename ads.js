// === Vignette Banner 1 (Anti-AdBlock)
var s1 = document.createElement("script");
s1.src = "https://a.monetag.com/fantastic-tag.min.js";
s1.async = true;
s1.onload = function() {
  var monetag = monetag || {};
  monetag.cmd = monetag.cmd || [];
  monetag.cmd.push(function () {
    monetag.fantasticTag.init({
      zoneId: 9632429,
    });
  });
};
document.head.appendChild(s1);

// === Vignette Banner 2
var s2 = document.createElement("script");
s2.src = "https://a.monetag.com/fantastic-tag.min.js";
s2.async = true;
s2.onload = function() {
  var monetag = monetag || {};
  monetag.cmd = monetag.cmd || [];
  monetag.cmd.push(function () {
    monetag.fantasticTag.init({
      zoneId: 9632428,
    });
  });
};
document.head.appendChild(s2);

// === In-Page Push 1 (Anti-AdBlock)
var s3 = document.createElement("script");
s3.src = "https://a.monetag.com/tag.min.js";
s3.async = true;
s3.onload = function() {
  var monetag = monetag || {};
  monetag.cmd = monetag.cmd || [];
  monetag.cmd.push(function () {
    monetag.inPagePushTag.init({
      zoneId: 9632411,
    });
  });
};
document.head.appendChild(s3);

// === In-Page Push 2
var s4 = document.createElement("script");
s4.src = "https://a.monetag.com/tag.min.js";
s4.async = true;
s4.onload = function() {
  var monetag = monetag || {};
  monetag.cmd = monetag.cmd || [];
  monetag.cmd.push(function () {
    monetag.inPagePushTag.init({
      zoneId: 9632410,
    });
  });
};
document.head.appendChild(s4);
