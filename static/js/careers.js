/* ========================================
   CAREERS PAGE JAVASCRIPT
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {
    const applyButtons = document.querySelectorAll('.apply-btn');
    const applicationModal = document.getElementById('applicationModal');
    const closeBtn = document.querySelector('.close');
    const applicationForm = document.getElementById('applicationForm');
    const positionInput = document.getElementById('positionInput');

    // Open modal and set position
    applyButtons.forEach(button => {
        button.addEventListener('click', () => {
            const position = button.dataset.position;
            positionInput.value = position;
            applicationModal.classList.add('show');
        });
    });

    // Close modal
    closeBtn.addEventListener('click', () => {
        applicationModal.classList.remove('show');
    });

    // Close modal when clicking outside
    window.addEventListener('click', (event) => {
        if (event.target === applicationModal) {
            applicationModal.classList.remove('show');
        }
    });

    // Handle form submission
    if (applicationForm) {
        applicationForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(applicationForm);
            const submitButton = applicationForm.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            
            try {
                submitButton.disabled = true;
                submitButton.textContent = 'Submitting...';
                
                const response = await fetch('/apply-job', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (data.success) {
                    showNotification(data.message, 'success');
                    applicationForm.reset();
                    applicationModal.classList.remove('show');
                } else {
                    showNotification(data.message, 'error');
                }
            } catch (error) {
                console.error('Error:', error);
                showNotification('An error occurred. Please try again.', 'error');
            } finally {
                submitButton.disabled = false;
                submitButton.textContent = originalText;
            }
        });
    }
});

function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background-color: ${type === 'success' ? '#28a745' : '#dc3545'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
        z-index: 9999;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}
