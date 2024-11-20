export function animateSpeedometer(targetSpeeds) {
    const speedDisplay = document.getElementById('speed');

    const randomTarget = targetSpeeds[Math.floor(Math.random() * targetSpeeds.length)];
    const targetSpeed = randomTarget.target;
    const intervalTime = randomTarget.time;

    let currentSpeed = 0;
    const speedInterval = setInterval(() => {
        if (currentSpeed >= targetSpeed) {
            clearInterval(speedInterval);
        } else {
            currentSpeed += 5;  
            speedDisplay.firstElementChild.textContent = currentSpeed;
        }
    }, intervalTime);  

    const style = document.createElement('style');
    style.type = 'text/css';

    const keyframes = `
    @keyframes rotateNeedle {
        0% {
            transform: rotate(-142deg);
        }
        100% {
            transform:  rotate(142deg);     
        }
    }
    `;

    style.innerHTML = keyframes;
    document.head.appendChild(style);
}