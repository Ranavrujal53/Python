// TYPEWRITER EFFECT
const text = "Welcome to Rana Vrujal Website 🚀";
let i = 0;

function typeEffect() {
    let el = document.getElementById("typing");
    if (el && i < text.length) {
        el.innerHTML += text.charAt(i);
        i++;
        setTimeout(typeEffect, 70);
    }
}

typeEffect();


// NAVBAR SHADOW ON SCROLL
window.addEventListener("scroll", function () {
    let navbar = document.querySelector(".navbar");

    if (window.scrollY > 50) {
        navbar.style.boxShadow = "0 4px 10px rgba(0,0,0,0.5)";
    } else {
        navbar.style.boxShadow = "none";
    }
});