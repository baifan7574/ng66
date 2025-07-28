// 加载 Adcash 主脚本
var adcashLib = document.createElement("script");
adcashLib.src = "https://acdn.adnxs.com/adcash/autotag.min.js";
adcashLib.async = true;

// 当主脚本加载完成后再执行 AutoTag
adcashLib.onload = function () {
  if (typeof aclib !== "undefined") {
    aclib.runAutoTag({
      zoneId: "jqeh7xu71d",
    });
  } else {
    console.error("Adcash script not loaded properly.");
  }
};

// 插入到 <head> 里
document.head.appendChild(adcashLib);
