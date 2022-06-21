let modifieur = document.querySelector('select'),
    zone_name = document.querySelector(".changename"),
    zone_mail = document.querySelector(".changemail"),
    zone_pwd = document.querySelector(".changepassword"),
    zone_img = document.querySelector(".changeimage");

modifieur.addEventListener('change', function () {
    if (this.value == '') {
        zone_name.classList.remove("open")
        zone_mail.classList.remove("open")
        zone_pwd.classList.remove("open")
        zone_img.classList.remove("open")
    }
    if (this.value == 'name') {
        zone_name.classList.add("open")
        zone_mail.classList.remove("open")
        zone_pwd.classList.remove("open")
        zone_img.classList.remove("open")
    }
    if (this.value == 'mail') {
        zone_name.classList.remove("open")
        zone_mail.classList.add("open")
        zone_pwd.classList.remove("open")
        zone_img.classList.remove("open")
    }
    if (this.value == 'password') {
        zone_name.classList.remove("open")
        zone_pwd.classList.add("open")
        zone_mail.classList.remove("open")
        zone_img.classList.remove("open")
    }
    if (this.value == 'image') {
        zone_name.classList.remove("open")
        zone_pwd.classList.remove("open")
        zone_img.classList.remove("open")
        zone_img.classList.add("open")
    }
})