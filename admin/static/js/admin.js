/* ========================================
   CHOWDHURYX ADMIN PANEL - JAVASCRIPT
   Enterprise-Grade Admin Panel Features
   ======================================== */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize mobile menu toggle
    initializeMobileMenu();
    
    // Initialize alerts
    initializeAlerts();
    
    // Initialize form validation
    initializeFormValidation();
    
    // Initialize delete confirmations
    initializeDeleteConfirmations();
    
    // Initialize table features
    initializeTableFeatures();
    
    // Initialize tooltips
    initializeTooltips();
});

/**
 * Initialize mobile menu toggle functionality
 */
function initializeMobileMenu() {
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (!mobileToggle || !navMenu) {
        return;
    }
    
    mobileToggle.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        const isActive = mobileToggle.classList.contains('active');
        
        mobileToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        
        // Update aria attributes
        mobileToggle.setAttribute('aria-expanded', !isActive);
    });
    
    // Close menu when a link is clicked
    const navLinks = navMenu.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            mobileToggle.classList.remove('active');
            navMenu.classList.remove('active');
            mobileToggle.setAttribute('aria-expanded', 'false');
        });
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        const isClickInsideNav = navMenu.contains(event.target);
        const isClickInsideToggle = mobileToggle.contains(event.target);
        
        if (!isClickInsideNav && !isClickInsideToggle && navMenu.classList.contains('active')) {
            mobileToggle.classList.remove('active');
            navMenu.classList.remove('active');
            mobileToggle.setAttribute('aria-expanded', 'false');
        }
    });
}

/**
 * Initialize alert auto-dismiss functionality
 */
function initializeAlerts() {
    const alerts = document.querySelectorAll('.alert-dismissible');
    
    alerts.forEach(alert => {
        const closeBtn = alert.querySelector('.alert-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                alert.remove();
            });
        }
        
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            if (alert.parentElement) {
                const closeBtn = alert.querySelector('.alert-close');
                if (closeBtn) {
                    closeBtn.click();
                }
            }
        }, 5000);
    });
}

/**
 * Initialize form validation
 */
function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const inputs = form.querySelectorAll('[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.classList.add('error');
                    input.style.borderColor = '#dc2626';
                    isValid = false;
                } else {
                    input.classList.remove('error');
                    input.style.borderColor = '';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showAlert('Please fill in all required fields', 'warning');
            }
        });
    });
}

/**
 * Initialize delete confirmation dialogs
 */
function initializeDeleteConfirmations() {
    const deleteButtons = document.querySelectorAll('[data-confirm-delete]');
    
    deleteButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            const message = this.getAttribute('data-confirm-delete') || 'Are you sure you want to delete this item?';
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    });
}

/**
 * Initialize table features (selection, sorting, etc.)
 */
function initializeTableFeatures() {
    const selectAllCheckbox = document.querySelector('[data-select-all]');
    const tableCheckboxes = document.querySelectorAll('table input[type="checkbox"]:not([data-select-all])');
    
    if (selectAllCheckbox) {
        selectAllCheckbox.addEventListener('change', function() {
            tableCheckboxes.forEach(checkbox => {
                checkbox.checked = selectAllCheckbox.checked;
            });
            updateSelectedCount();
        });
    }
    
    tableCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateSelectedCount);
    });
}

/**
 * Update selected item count
 */
function updateSelectedCount() {
    const checkboxes = document.querySelectorAll('table input[type="checkbox"]:checked:not([data-select-all])');
    const countElement = document.querySelector('.selected-count');
    
    if (countElement) {
        countElement.textContent = checkboxes.length + ' selected';
    }
}

/**
 * Initialize tooltip functionality
 */
function initializeTooltips() {
    const tooltips = document.querySelectorAll('[data-tooltip]');
    
    tooltips.forEach(tooltip => {
        tooltip.addEventListener('mouseenter', function() {
            showTooltip(this);
        });
        tooltip.addEventListener('mouseleave', function() {
            hideTooltip(this);
        });
    });
}

/**
 * Show toast/alert notification
 */
function showAlert(message, type = 'info') {
    const alertContainer = document.createElement('div');
    alertContainer.className = `alert alert-${type} alert-dismissible`;
    
    const iconMap = {
        'success': 'check-circle',
        'error': 'exclamation-circle',
        'danger': 'exclamation-circle',
        'warning': 'exclamation-triangle',
        'info': 'info-circle'
    };
    
    const icon = iconMap[type] || 'info-circle';
    
    alertContainer.innerHTML = `
        <i class="fas fa-${icon}"></i>
        <span>${message}</span>
        <button type="button" class="alert-close" onclick="this.parentElement.remove();">
            <i class="fas fa-times"></i>
        </button>
    `;
    
    const mainContent = document.querySelector('.admin-main') || document.body;
    mainContent.insertBefore(alertContainer, mainContent.firstChild);
    
    // Auto dismiss after 5 seconds
    setTimeout(() => {
        if (alertContainer.parentElement) {
            alertContainer.remove();
        }
    }, 5000);
}

/**
 * Show tooltip
 */
function showTooltip(element) {
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip-popup';
    tooltip.textContent = element.getAttribute('data-tooltip');
    tooltip.style.cssText = `
        position: absolute;
        background-color: #1a365d;
        color: #fff;
        padding: 8px 12px;
        border-radius: 6px;
        font-size: 12px;
        white-space: nowrap;
        z-index: 1000;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    `;
    
    document.body.appendChild(tooltip);
    
    const rect = element.getBoundingClientRect();
    tooltip.style.top = (rect.top + window.scrollY - tooltip.offsetHeight - 10) + 'px';
    tooltip.style.left = (rect.left + window.scrollX + rect.width / 2 - tooltip.offsetWidth / 2) + 'px';
    
    element._tooltip = tooltip;
}

/**
 * Hide tooltip
 */
function hideTooltip(element) {
    if (element._tooltip) {
        element._tooltip.remove();
        element._tooltip = null;
    }
}

/**
 * Format date to readable string
 */
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

/**
 * Copy text to clipboard
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showAlert('Copied to clipboard!', 'success');
    }).catch(() => {
        showAlert('Failed to copy to clipboard', 'error');
    });
}

/**
 * Export table data to CSV
 */
function exportTableToCSV(tableId, filename = 'export.csv') {
    const table = document.getElementById(tableId);
    if (!table) return;
    
    const csv = [];
    const rows = table.querySelectorAll('tr');
    
    rows.forEach(row => {
        const cols = row.querySelectorAll('td, th');
        const rowData = [];
        cols.forEach(col => {
            rowData.push('"' + col.textContent.replace(/"/g, '""') + '"');
        });
        csv.push(rowData.join(','));
    });
    
    const csvContent = csv.join('\n');
    const link = document.createElement('a');
    link.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csvContent);
    link.download = filename;
    link.click();
}

/**
 * Debounce function for search/filter
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Initialize table search/filter
 */
function initializeTableSearch(searchInputId, tableId) {
    const searchInput = document.getElementById(searchInputId);
    const table = document.getElementById(tableId);
    
    if (!searchInput || !table) return;
    
    const debouncedSearch = debounce(function() {
        const searchTerm = searchInput.value.toLowerCase();
        const rows = table.querySelectorAll('tbody tr');
        let visibleCount = 0;
        
        rows.forEach(row => {
            const text = row.textContent.toLowerCase();
            const isVisible = text.includes(searchTerm);
            row.style.display = isVisible ? '' : 'none';
            if (isVisible) visibleCount++;
        });
        
        // Show empty state if no results
        const emptyState = table.querySelector('.empty-state');
        if (emptyState) {
            emptyState.style.display = visibleCount === 0 ? '' : 'none';
        }
    }, 300);
    
    searchInput.addEventListener('input', debouncedSearch);
}

/**
 * Delete request handler
 */
async function deleteItem(url, confirmMessage = 'Are you sure?') {
    if (!confirm(confirmMessage)) return;
    
    try {
        const response = await fetch(url, { method: 'DELETE' });
        if (response.ok) {
            showAlert('Item deleted successfully', 'success');
            setTimeout(() => location.reload(), 1000);
        } else {
            showAlert('Failed to delete item', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showAlert('An error occurred', 'error');
    }
}

/**
 * Update item status
 */
async function updateStatus(itemId, newStatus) {
    try {
        const response = await fetch(`/admin/item/${itemId}/status`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRF-Token': document.querySelector('meta[name="csrf-token"]')?.content || ''
            },
            body: JSON.stringify({ status: newStatus })
        });
        
        if (response.ok) {
            showAlert('Status updated successfully', 'success');
        } else {
            showAlert('Failed to update status', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showAlert('An error occurred', 'error');
    }
}

// Export utilities for global access
window.admin = {
    showAlert,
    copyToClipboard,
    exportTableToCSV,
    initializeTableSearch,
    formatDate,
    deleteItem,
    updateStatus
};
