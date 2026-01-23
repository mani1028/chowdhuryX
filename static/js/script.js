// Initialize Icons
document.addEventListener("DOMContentLoaded", function() {
    if (typeof lucide !== 'undefined') lucide.createIcons();
});

// Like Logic
function likeItem(type, id) {
    fetch(`/like/${type}/${id}`, { 
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(res => res.json())
    .then(data => {
        const element = document.getElementById(`${type}-likes-${id}`);
        if (element) element.innerText = data.likes;
    })
    .catch(error => console.error('Error:', error));
}

// Share Logic (with Count Increment)
function sharePost(title, id) {
    const url = window.location.origin + '/?search=' + encodeURIComponent(title);
    
    // 1. Increment Share Count in Database
    fetch(`/share/${id}`, { method: 'POST' })
        .then(res => res.json())
        .then(data => {
            // Update UI
            const display = document.getElementById(`share-count-display-${id}`);
            if(display) display.innerText = data.shares;
        });

    // 2. Perform Native Share or Copy
    if (navigator.share) {
        navigator.share({
            title: title,
            text: `Check out this insight from ChowdhuryX: ${title}`,
            url: url,
        }).catch((error) => console.log('Error sharing', error));
    } else {
        navigator.clipboard.writeText(url).then(() => {
            alert('Link copied to clipboard!');
        });
    }
}