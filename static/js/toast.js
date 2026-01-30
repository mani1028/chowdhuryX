/**
 * Toast Notification System
 * Provides unified toast notifications for form submissions and user feedback
 */

class ToastNotification {
    constructor(title, message, type = 'info', duration = 3000) {
        this.title = title;
        this.message = message;
        this.type = type; // 'success', 'error', 'warning', 'info'
        this.duration = duration;
        this.element = null;
        this.show();
    }

    show() {
        // Create container if not exists
        let container = document.querySelector('.toast-container');
        if (!container) {
            container = document.createElement('div');
            container.className = 'toast-container';
            document.body.appendChild(container);
        }

        // Create toast element
        const toast = document.createElement('div');
        toast.className = `toast ${this.type}`;
        
        // Get icon based on type
        const icons = {
            success: 'fa-check-circle',
            error: 'fa-exclamation-circle',
            warning: 'fa-exclamation-triangle',
            info: 'fa-info-circle'
        };
        
        toast.innerHTML = `
            <div class="toast-icon">
                <i class="fas ${icons[this.type]}"></i>
            </div>
            <div class="toast-content">
                <div class="toast-title">${this.title}</div>
                <div class="toast-message">${this.message}</div>
            </div>
            <button class="toast-close" aria-label="Close notification">
                <i class="fas fa-times"></i>
            </button>
            <div class="toast-progress"></div>
        `;

        this.element = toast;

        // Add close functionality
        const closeBtn = toast.querySelector('.toast-close');
        closeBtn.addEventListener('click', () => this.hide());

        // Append to container
        container.appendChild(toast);

        // Auto-hide after duration
        if (this.duration > 0) {
            setTimeout(() => this.hide(), this.duration);
        }
    }

    hide() {
        if (this.element) {
            this.element.style.animation = 'slideInToast 0.3s ease-out reverse';
            setTimeout(() => {
                if (this.element && this.element.parentNode) {
                    this.element.parentNode.removeChild(this.element);
                }
            }, 300);
        }
    }
}

/**
 * Show success toast
 */
function showSuccessToast(title, message, duration = 3000) {
    return new ToastNotification(title, message, 'success', duration);
}

/**
 * Show error toast
 */
function showErrorToast(title, message, duration = 5000) {
    return new ToastNotification(title, message, 'error', duration);
}

/**
 * Show warning toast
 */
function showWarningToast(title, message, duration = 4000) {
    return new ToastNotification(title, message, 'warning', duration);
}

/**
 * Show info toast
 */
function showInfoToast(title, message, duration = 3000) {
    return new ToastNotification(title, message, 'info', duration);
}

/**
 * Form submission helper with CSRF and toast notifications
 */
function submitFormWithToast(formElement, endpoint, onSuccess = null, onError = null) {
    const formData = new FormData(formElement);
    
    // Show loading indicator
    const originalButton = formElement.querySelector('[type="submit"]');
    if (originalButton) {
        originalButton.disabled = true;
        originalButton.textContent = 'Submitting...';
    }

    fetch(endpoint, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': formData.get('csrf_token') || document.querySelector('[name="csrf_token"]').value
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showSuccessToast('Success', data.message || 'Operation completed successfully!');
            formElement.reset();
            if (onSuccess) onSuccess(data);
        } else {
            showErrorToast('Error', data.message || 'An error occurred. Please try again.');
            if (onError) onError(data);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showErrorToast('Error', 'Failed to submit form. Please try again.');
        if (onError) onError(error);
    })
    .finally(() => {
        // Restore button state
        if (originalButton) {
            originalButton.disabled = false;
            originalButton.textContent = 'Submit';
        }
    });
}

// Export for module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        ToastNotification,
        showSuccessToast,
        showErrorToast,
        showWarningToast,
        showInfoToast,
        submitFormWithToast
    };
}
