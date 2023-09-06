const header = document.querySelector('.navbar');

window.onscroll = function() {
    var top = window.scrollY;
    if(top >=100) {
        header.classList.add('navbarDark');
    }
    else {
        header.classList.remove('navbarDark');
    }
}

const emailIcon = document.getElementById("email-icon");
const emailText = document.getElementById("email-text");
const phoneIcon = document.getElementById("phone-icon");
const phoneText = document.getElementById("phone-text");

emailIcon.addEventListener("mouseenter", () => {
    emailText.style.opacity = 1;
});

phoneIcon.addEventListener("mouseenter", () => {
    phoneText.style.opacity = 1;
});