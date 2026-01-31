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
            const position = positionInput.value;
            
            try {
                submitButton.disabled = true;
                submitButton.textContent = 'Submitting...';
                
                const response = await fetch('/apply-job', {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': formData.get('csrf_token')
                    }
                });
                
                const data = await response.json();
                
                if (data.success) {
                    showSuccessToast('Application Submitted', `Your application for ${position} has been submitted successfully!`);
                    applicationForm.reset();
                    applicationModal.classList.remove('show');
                } else {
                    showErrorToast('Submission Error', data.message || 'An error occurred. Please try again.');
                }
            } catch (error) {
                console.error('Error:', error);
                showErrorToast('Error', 'An error occurred while submitting your application. Please try again.');
            } finally {
                submitButton.disabled = false;
                submitButton.textContent = originalText;
            }
        });
    }
});
