// ✅ 正确完整的 Adcash 广告脚本（可放在 ads.js 中统一调用）
document.write(`
  <script id="aclib" type="text/javascript" src="https://acdn.adnxs.com/script/aclib.js"></script>
  <script type="text/javascript">
    window.addEventListener('DOMContentLoaded', function () {
      if (typeof aclib !== 'undefined' && aclib.runAutoTag) {
        aclib.runAutoTag({
          zoneId: 'jqeh7xu71d',
        });
      }
    });
  </script>
`);
