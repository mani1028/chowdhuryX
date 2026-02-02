/* ========================================
   CAREERS PAGE JAVASCRIPT
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {
    const applyButtons = document.querySelectorAll('.apply-btn');
    const applicationModal = document.getElementById('applicationModal');
    const closeBtn = document.querySelector('.modal-close');
    const applicationForm = document.getElementById('applicationForm');
    const positionInput = document.getElementById('positionInput');
    const modalPositionName = document.getElementById('modalPositionName');
    const fileInput = document.getElementById('resume');
    const fileLabel = document.querySelector('.file-label');

    // Update file label when file is selected
    if (fileInput && fileLabel) {
        fileInput.addEventListener('change', (e) => {
            const fileName = e.target.files[0]?.name;
            if (fileName) {
                fileLabel.textContent = fileName;
                fileLabel.style.color = 'var(--brand-primary)';
            } else {
                fileLabel.textContent = 'Choose file...';
                fileLabel.style.color = '#64748b';
            }
        });
    }

    // Open modal and set position
    applyButtons.forEach(button => {
        button.addEventListener('click', () => {
            const position = button.dataset.position;
            positionInput.value = position;
            if (modalPositionName) {
                modalPositionName.textContent = position;
            }
            applicationModal.classList.add('show');
            document.body.style.overflow = 'hidden'; // Prevent background scroll
        });
    });

    // Close modal
    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            applicationModal.classList.remove('show');
            document.body.style.overflow = ''; // Restore scroll
        });
    }

    // Close modal when clicking outside
    window.addEventListener('click', (event) => {
        if (event.target === applicationModal) {
            applicationModal.classList.remove('show');
            document.body.style.overflow = '';
        }
    });

    // Handle form submission
    if (applicationForm) {
        applicationForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(applicationForm);
            const submitButton = applicationForm.querySelector('button[type="submit"]');
            const originalText = submitButton.innerHTML;
            const position = positionInput.value;
            
            try {
                submitButton.disabled = true;
                submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';
                
                const response = await fetch('/apply-job', {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': formData.get('csrf_token')
                    }
                });
                
                const data = await response.json();
                
                if (data.success) {
                    // Show success message
                    if (typeof showSuccessToast === 'function') {
                        showSuccessToast('Application Submitted', `Your application for ${position} has been submitted successfully!`);
                    } else {
                        alert(`Application submitted successfully for ${position}!`);
                    }
                    
                    applicationForm.reset();
                    fileLabel.textContent = 'Choose file...';
                    fileLabel.style.color = '#64748b';
                    applicationModal.classList.remove('show');
                    document.body.style.overflow = '';
                } else {
                    // Show error message
                    if (typeof showErrorToast === 'function') {
                        showErrorToast('Submission Error', data.message || 'An error occurred. Please try again.');
                    } else {
                        alert(data.message || 'An error occurred. Please try again.');
                    }
                }
            } catch (error) {
                console.error('Error:', error);
                if (typeof showErrorToast === 'function') {
                    showErrorToast('Error', 'An error occurred while submitting your application. Please try again.');
                } else {
                    alert('An error occurred while submitting your application. Please try again.');
                }
            } finally {
                submitButton.disabled = false;
                submitButton.innerHTML = originalText;
            }
        });
    }
});
