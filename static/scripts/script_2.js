import { animateSpeedometer } from './utils/animateSpeedometer.js';


const   changePictureBtn = document.getElementById('change-picture'),
        protectImage = document.getElementById('start-now_img'),
        line1 = document.getElementById('line_1'),
        line2 = document.getElementById('line_2'),
        speedometer = document.querySelector('.speedometer'),
        targetSpeeds = [
            { target: 325, time: 70 },
            { target: 360, time: 60 },
            { target: 430, time: 52 },
            { target: 435, time: 51 },
            { target: 455, time: 47 },
            { target: 470, time: 45 },
            { target: 510, time: 43 },
            { target: 540, time: 40 },
            { target: 630, time: 37.5 },
            { target: 650, time: 35.6 },
            { target: 670, time: 33 },
        ];

        
//Start Speedometer
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            animateSpeedometer(targetSpeeds);
            observer.unobserve(speedometer); 
        }
    });
}, { threshold: 1.0 }); 

observer.observe(speedometer);
    
// Start now section
changePictureBtn.addEventListener("mouseenter", () => {
    protectImage.style.opacity = '0'; 
    setTimeout(() => {
        protectImage.src = "../assets/images/light-tg-replace.png";
        protectImage.style.opacity = '1'; 
    }, 500); 
    line1.style.backgroundColor = '#DADADA';
    line2.style.backgroundColor = '#000';
})



// Dropdown
document.querySelectorAll('.dropdown_pictures > li').forEach(item => {
    item.addEventListener('click', () => {
        const video = item.nextElementSibling;
        const arrowIcon = item.querySelector('button img');

        if (!video.classList.contains('show')) {
            video.classList.add('show');
            arrowIcon.src = '../assets/images/icons/light-open-arrow.svg'; 
        } else {
            video.classList.remove('show');
            arrowIcon.src = '../assets/images/icons/light-close-arrow.svg'; 
        }
    });
});


// Burger menu
const burgerBtn = document.querySelector('.burger-menu');
const navItems = document.querySelector('.nav_items');
const btnImg = burgerBtn.firstChild;
// Stop scroll function
const scrollHandler = () => {
    window.scrollTo({ top: 0 });
};

burgerBtn?.addEventListener('click', () => {
    navItems.classList.toggle('open'); 
        
    if(navItems.classList.contains('open')){
        btnImg.src ='../assets/images/icons/light-krestik.svg';
        window.addEventListener('scroll', scrollHandler)
    } else{
        btnImg.src ='../assets/images/icons/light-burger-menu.svg'
        window.removeEventListener('scroll', scrollHandler)
    }
})
 
document.querySelectorAll('.nav_items > li').forEach(item => {
    item.addEventListener('click', () => {
        navItems.classList.remove('open');
        btnImg.src ='../assets/images/icons/light-burger-menu.svg'
        window.removeEventListener('scroll', scrollHandler)
    })
})