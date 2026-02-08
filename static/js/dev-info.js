/**
 * Developer Info Easter Egg
 * Press Ctrl+Shift+D to open hidden dev info modal
 * Name encoded in Base64
 */

// Base64 encoded name: MANIKANTA CH
const ENCODED_NAME = 'TUFOSUtBTlRBIENI';

function decodeDevInfo() {
    try {
        return atob(ENCODED_NAME);
    } catch (e) {
        return 'Developer';
    }
}

function showDevInfoModal() {
    // Check if modal already exists
    let existingModal = document.getElementById('devInfoModal');
    if (existingModal) {
        existingModal.classList.add('closing');
        setTimeout(() => existingModal.parentElement.remove(), 300);
        return;
    }

    const developerName = decodeDevInfo();

    // Create modal overlay (transparent)
    const overlay = document.createElement('div');
    overlay.id = 'devInfoOverlay';
    overlay.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 99999;
    `;

    // Create modal content - matches website design
    const modal = document.createElement('div');
    modal.id = 'devInfoModal';
    modal.style.cssText = `
        background: linear-gradient(135deg, #0f1f38 0%, #1a365d 100%);
        border: 1px solid rgba(8, 145, 178, 0.35);
        border-radius: 12px;
        padding: 20px;
        color: white;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        animation: slideIn 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(8, 145, 178, 0.2), 0 0 40px rgba(8, 145, 178, 0.08);
        min-width: 320px;
        position: relative;
        backdrop-filter: blur(10px);
    `;

    modal.innerHTML = `
        <style>
            @keyframes slideIn {
                from {
                    transform: translateY(30px);
                    opacity: 0;
                }
                to {
                    transform: translateY(0);
                    opacity: 1;
                }
            }
            
            @keyframes slideOut {
                from {
                    transform: translateY(0);
                    opacity: 1;
                }
                to {
                    transform: translateY(30px);
                    opacity: 0;
                }
            }
            
            #devInfoModal.closing {
                animation: slideOut 0.3s ease-in forwards;
            }
            
            .dev-header {
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 18px;
                position: relative;
            }
            
            .dev-status-badge {
                width: 28px;
                height: 28px;
                background: linear-gradient(135deg, #0891b2 0%, #0369a1 100%);
                border-radius: 6px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 14px;
                box-shadow: 0 4px 12px rgba(8, 145, 178, 0.4);
            }
            
            .dev-title-section h3 {
                margin: 0;
                font-size: 14px;
                font-weight: 700;
                color: #fff;
                letter-spacing: 0.3px;
            }
            
            .dev-title-section p {
                margin: 3px 0 0 0;
                font-size: 10px;
                color: rgba(8, 145, 178, 0.9);
                text-transform: uppercase;
                letter-spacing: 0.4px;
                font-weight: 600;
            }
            
            .close-btn {
                position: absolute;
                top: -8px;
                right: -8px;
                background: rgba(8, 145, 178, 0.15);
                color: rgba(8, 145, 178, 0.9);
                border: 1px solid rgba(8, 145, 178, 0.3);
                width: 28px;
                height: 28px;
                border-radius: 6px;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 0;
                font-size: 16px;
                transition: all 0.25s ease;
                font-family: inherit;
            }
            
            .close-btn:hover {
                background: rgba(8, 145, 178, 0.25);
                color: #0891b2;
                border-color: rgba(8, 145, 178, 0.5);
                transform: rotate(90deg);
            }
            
            .dev-divider {
                height: 1px;
                background: linear-gradient(90deg, transparent, rgba(8, 145, 178, 0.2), transparent);
                margin: 14px 0;
            }
            
            .dev-info-item {
                margin-bottom: 12px;
                display: flex;
                flex-direction: column;
                gap: 3px;
            }
            
            .dev-info-label {
                display: flex;
                align-items: center;
                gap: 6px;
                font-size: 10px;
                font-weight: 700;
                color: rgba(209, 213, 219, 0.6);
                text-transform: uppercase;
                letter-spacing: 0.4px;
            }
            
            .dev-info-label i {
                color: #0891b2;
                font-size: 11px;
                width: 12px;
                text-align: center;
            }
            
            .dev-info-value {
                color: #0891b2;
                font-weight: 600;
                font-size: 12px;
                font-family: 'Monaco', 'Courier New', monospace;
                margin-left: 18px;
            }
            
            .dev-info-value.secondary {
                color: rgba(209, 213, 219, 0.85);
                font-weight: 500;
            }
            
            .dev-tech-stack {
                display: flex;
                flex-wrap: wrap;
                gap: 6px;
                margin-top: 6px;
                margin-left: 18px;
            }
            
            .dev-tech-tag {
                background: rgba(8, 145, 178, 0.15);
                color: #0891b2;
                padding: 3px 8px;
                border-radius: 4px;
                font-size: 10px;
                font-weight: 600;
                border: 1px solid rgba(8, 145, 178, 0.2);
            }
            
            .dev-footer {
                margin-top: 14px;
                padding-top: 12px;
                border-top: 1px solid rgba(8, 145, 178, 0.15);
                font-size: 10px;
                color: rgba(209, 213, 219, 0.5);
                text-align: center;
                letter-spacing: 0.3px;
            }
        </style>
        
        <div class="dev-header">
            <div class="dev-status-badge">&lt;/&gt;</div>
            <div class="dev-title-section">
                <h3>Developer Info</h3>
                <p>System Status</p>
            </div>
            <button class="close-btn" onclick="closeDevInfo()">✕</button>
        </div>
        
        <div class="dev-divider"></div>
        
        <div class="dev-info-item">
            <div class="dev-info-label"><i class="fas fa-user-code"></i> Developer</div>
            <div class="dev-info-value">${developerName}</div>
        </div>
        
        <div class="dev-info-item">
            <div class="dev-info-label"><i class="fas fa-building"></i> Organization</div>
            <div class="dev-info-value secondary">ChowdhuryX Organization LLC</div>
        </div>
        
        <div class="dev-info-item">
            <div class="dev-info-label"><i class="fas fa-project-diagram"></i> Project</div>
            <div class="dev-info-value secondary">Enterprise Web Platform</div>
        </div>
        
        <div class="dev-divider"></div>
        
        <div class="dev-info-item">
            <div class="dev-info-label"><i class="fas fa-code-branch"></i> Version</div>
            <div class="dev-info-value">v1.2.8 (AT Update)</div>
        </div>
        
        <div class="dev-info-item">
            <div class="dev-info-label"><i class="fas fa-calendar"></i> Year</div>
            <div class="dev-info-value">2025-2026</div>
        </div>
        
        <div class="dev-divider"></div>
        
        <div class="dev-info-item">
            <div class="dev-info-label"><i class="fas fa-server"></i> Tech Stack</div>
            <div class="dev-tech-stack">
                <span class="dev-tech-tag">Python</span>
                <span class="dev-tech-tag">Flask</span>
                <span class="dev-tech-tag">PostgreSQL</span>
                <span class="dev-tech-tag">JavaScript</span>
                <span class="dev-tech-tag">React</span>
            </div>
        </div>
        
        <div class="dev-divider"></div>
        
        <div class="dev-info-item">
            <div class="dev-info-label"><i class="fas fa-envelope"></i> Contact</div>
            <div class="dev-info-value" style="font-size: 11px; color: rgba(209, 213, 219, 0.85);">chellamalla.manikanta2@gmail.com</div>
        </div>
        
        <div class="dev-footer">
            🔐 Hidden Easter Egg • Press Ctrl+Shift+D to toggle • Esc to close
        </div>
    `;


    overlay.appendChild(modal);
    document.body.appendChild(overlay);

    // Close on escape key
    const closeHandler = function(e) {
        if (e.key === 'Escape') {
            closeDevInfo();
        }
    };
    
    document.addEventListener('keydown', closeHandler);
    overlay._closeHandler = closeHandler;
}

function closeDevInfo() {
    const modal = document.getElementById('devInfoModal');
    const overlay = document.getElementById('devInfoOverlay');
    
    if (modal) {
        modal.classList.add('closing');
        setTimeout(() => {
            if (overlay && overlay.parentElement) {
                // Remove event listeners
                if (overlay._closeHandler) {
                    document.removeEventListener('keydown', overlay._closeHandler);
                }
                overlay.remove();
            }
        }, 300);
    }
}

// Listen for Ctrl+Shift+D
document.addEventListener('keydown', function(e) {
    // Ctrl (or Cmd on Mac) + Shift + D
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key.toUpperCase() === 'D') {
        e.preventDefault();
        showDevInfoModal();
    }
});

// Also log to console when page loads
console.log(
    '%c🔧 ChowdhuryX Developer Info',
    'font-size: 20px; font-weight: bold; color: #0891b2;'
);
console.log(
    '%cDeveloper: ' + decodeDevInfo(),
    'font-size: 14px; color: #1a365d; font-weight: bold;'
);
console.log(
    '%cPress Ctrl+Shift+D to open hidden developer panel',
    'font-size: 12px; color: #999; font-style: italic;'
);
