/**
 * Interactive Web Portfolio JavaScript
 * Handles scroll animations and 3D hover effects.
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Scroll Animations (Intersection Observer)
    // Elements fade in and slide up when they enter the viewport
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // Trigger when 15% of the element is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: Stop observing once it's visible if we only want it to animate once
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.fade-in');
    animatedElements.forEach(el => observer.observe(el));


    // 2. Interactive 3D Tilt Effect for Project Cards
    // Adds a premium, dynamic feel when hovering over cards
    const cards = document.querySelectorAll('[data-tilt]');

    cards.forEach(card => {
        card.addEventListener('mousemove', handleTilt);
        card.addEventListener('mouseleave', resetTilt);
    });

    function handleTilt(e) {
        const card = e.currentTarget;
        const cardRect = card.getBoundingClientRect();
        
        // Calculate mouse position relative to the center of the card
        const x = e.clientX - cardRect.left;
        const y = e.clientY - cardRect.top;
        
        const centerX = cardRect.width / 2;
        const centerY = cardRect.height / 2;
        
        // Calculate rotation degrees (max 5 degrees)
        const rotateX = ((y - centerY) / centerY) * -5;
        const rotateY = ((x - centerX) / centerX) * 5;
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        card.style.boxShadow = `
            ${(centerX - x) / 10}px 
            ${(centerY - y) / 10 + 20}px 
            30px rgba(0, 0, 0, 0.4),
            0 0 15px rgba(6, 182, 212, 0.1) inset
        `;
    }

    function resetTilt(e) {
        const card = e.currentTarget;
        card.style.transform = `perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)`;
        card.style.boxShadow = '0 8px 32px 0 rgba(0, 0, 0, 0.37)'; // Reset to CSS variable value
        
        // Add a smooth transition specifically for the reset
        card.style.transition = 'transform 0.5s ease-out, box-shadow 0.5s ease-out';
        
        // Remove the transition after it completes so mousemove is instantaneous again
        setTimeout(() => {
            card.style.transition = 'transform 0.1s, box-shadow 0.1s';
        }, 500);
    }
});
