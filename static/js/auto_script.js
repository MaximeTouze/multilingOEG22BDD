tabs = ["eng-button", "fr-button", "esp-button", "ara-button"]
i=1
setInterval(function(){ 
    document.getElementById(tabs[i]).click()
    console.log(document.getElementById(tabs[i]))
    i++
    if(i == 4){
        i = 0
    }
}, 10000);
