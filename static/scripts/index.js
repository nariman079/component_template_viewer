import { animateSpeedometer } from './utils/animateSpeedometer.js';

const   changePictureBtn = document.getElementById('change-picture'),
        protectImage = document.getElementById('start-now_img'),
        line1 = document.getElementById('line_1'),
        line2 = document.getElementById('line_2');
        
    
// Start now section
changePictureBtn.addEventListener("mouseenter", () => {
    protectImage.style.opacity = '0'; 
    setTimeout(() => {
        protectImage.src = "//img/tg-replace.png";
        protectImage.style.opacity = '1'; 
    }, 500); 
    line1.style.backgroundColor = '#212121';
    line2.style.backgroundColor = '#fff';
})

window.onload = function() {
    animateSpeedometer(500);  
};


// Dropdown
document.querySelectorAll('.dropdown_pictures > li').forEach(item => {
    item.querySelector('button').addEventListener('click', () => {
        const image = item.nextElementSibling;
        const arrowIcon = item.querySelector('button img');

        if (!image.classList.contains('show')) {
            image.classList.add('show');
            arrowIcon.src = '../assets/images/icons/open-arrow.svg'; 
        } else {
            image.classList.remove('show');
            arrowIcon.src = '../assets/images/icons/close-arrow.svg'; 
        }
    });
});


// Burger menu
// const burgerBtn = document.querySelector('.burger-menu');

// burgerBtn?.addEventListener('click', () => {

// })
