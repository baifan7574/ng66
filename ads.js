
// Adcash AutoTag script
(function() {
  var adcash = document.createElement('script');
  adcash.type = 'text/javascript';
  adcash.innerHTML = `
    aclib.runAutoTag({
      zoneId: 'jqeh7xu71d',
    });
  `;
  document.body.appendChild(adcash);
})();
