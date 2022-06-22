function checkfunctionpublic() {
    var check = document.getElementById("zonePublic");
    var zone = document.querySelectorAll('[id="zonepublic"]');
    if (check.checked == true) {
        for (var i = 0; i< zone.length; i++) {
            zone[i].disabled = false;
            console.log(zone[i])
        }        
    } 
    else {
        for (var i = 0; i< zone.length; i++) {
            zone[i].disabled = true;
        }   
    }
}

function checkfunctionproteger() {
    var check = document.getElementById("Proteger");
    var zone  = document.querySelectorAll('[id="zoneprotected"]');
    if (check.checked == true) {
        for (var i = 0; i< zone.length; i++) {
            zone[i].disabled = false;
        }        
    } 
    else {
        for (var i = 0; i< zone.length; i++) {
            zone[i].disabled = true;
        }   
    }
}

function checkfunctionprivate() {
    var check = document.getElementById("Private");
    var zone  = document.querySelectorAll('[id="zoneprivate"]');
    if (check.checked == true) {
        for (var i = 0; i< zone.length; i++) {
            zone[i].disabled = false;
        }        
    } 
    else {
        for (var i = 0; i< zone.length; i++) {
            zone[i].disabled = true;
        }   
    }
}

function checkfunctionattribue() {
    var check = document.getElementById('attribue');
    var liste = document.getElementsByClassName('Option-checkbox');
    var zone = liste[1];
    if(check.checked == true) {
        zone.classList.remove("close");
    }
    else {
        zone.classList.add("close");
    }
}

function checkfunctionmethode() {
    var check = document.getElementById('methode');
    var liste = document.getElementsByClassName('Option-checkbox');
    var zone_methode  = document.querySelectorAll('[id="zonemethode"]');
    var zone = liste[2];
    if(check.checked == true) {
        zone.classList.remove("close");
        for (var i = 0; i< zone_methode.length; i++) {
            zone_methode[i].disabled = false;
        }   
    }
    else {
        zone.classList.add("close");
        for (var i = 0; i< zone_methode.length; i++) {
            zone_methode[i].disabled = true;
        } 
    }
}

function checkfunctionComment() {
    var check = document.getElementById('comment');
    var zone = document.getElementsByClassName('Commentaire');
    if(check.checked == true) {
        zone[0].classList.remove("close");
    }
    else {
        zone[0].classList.add("close");
    }
}