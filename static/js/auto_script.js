tabs = ["eng-button", "fr-button", "esp-button", "ara-button"] // languages
i=1
// changes the active
setInterval(function(){
  // simulate a click on the html button for the new language
    document.getElementById(tabs[i]).click();
    // looping
    i = (i +1) % 4;
}, 10000);
