/**
 * ChowdhuryX Home Page Interactions
 * Enterprise-grade micro-interactions
 */

(function() {
    'use strict';
    
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    function init() {
        setupScrollAnimations();
        setupStatsAnimation();
        setupSmoothScroll();
    }
    
    // Intersection Observer for scroll animations
    function setupScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-fade-in-up');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        
        // Observe capability cards and other elements
        document.querySelectorAll('.capability-card, .why-item, .industry-card, .location-card').forEach(el => {
            observer.observe(el);
        });
    }
    
    // Smooth scroll for anchor links
    function setupSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href !== '#' && href !== '#!') {
                    e.preventDefault();
                    const target = document.querySelector(href);
                    if (target) {
                        const headerHeight = document.querySelector('.site-header')?.offsetHeight || 0;
                        const targetPosition = target.offsetTop - headerHeight - 20;
                        
                        window.scrollTo({
                            top: targetPosition,
                            behavior: 'smooth'
                        });
                    }
                }
            });
        });
    }
    
    // Stat counter animation
    function animateValue(element, start, end, duration) {
        const range = end - start;
        let current = start;
        const increment = range / (duration / 16);
        
        const timer = setInterval(() => {
            current += increment;
            if ((increment > 0 && current >= end) || (increment < 0 && current <= end)) {
                element.textContent = end + (element.dataset.suffix || '');
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current) + (element.dataset.suffix || '');
            }
        }, 16);
    }
    
    // Animate stats when visible
    function setupStatsAnimation() {
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                    const statValue = entry.target.querySelector('.stat-value');
                    if (statValue) {
                        const text = statValue.textContent;
                        const value = parseInt(text.replace(/\D/g, ''));
                        if (!isNaN(value)) {
                            statValue.dataset.suffix = text.replace(value.toString(), '');
                            animateValue(statValue, 0, value, 1500);
                            entry.target.classList.add('animated');
                        }
                    }
                }
            });
        }, { threshold: 0.5 });
        
        document.querySelectorAll('.stat-item, .hero-stats .stat-item').forEach(el => {
            statsObserver.observe(el);
        });
    }
    
})();
