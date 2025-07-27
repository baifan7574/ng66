var monetag = monetag || {};
monetag.cmd = monetag.cmd || [];
monetag.cmd.push(function() {
    monetag.fantasticTag.init({
        zoneId: 9632429,
    });
});

var s = document.createElement("script");
s.type = "text/javascript";
s.src = "https://a.monetag.com/fantastic-tag.min.js";
s.async = true;
document.head.appendChild(s);
