document.getElementById('video-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const selectedVideo = document.querySelector('input[name="video"]:checked').value;
    const statusMessage = document.getElementById('status-message');
    
    fetch('/update_background', {
        method: 'POST',
        body: new FormData(e.target)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            statusMessage.textContent = `Background video updated to ${selectedVideo}`;
            statusMessage.className = 'success';
        } else {
            statusMessage.textContent = data.message;
            statusMessage.className = 'error';
        }
    })
    .catch(error => {
        statusMessage.textContent = 'Error updating background';
        statusMessage.className = 'error';
        console.error('Error:', error);
    });
});

document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const statusMessage = document.getElementById('status-message');
    
    fetch('/upload_video', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            statusMessage.textContent = `Video uploaded: ${data.filename}`;
            statusMessage.className = 'success';
            
            // Refresh the page to show new video
            setTimeout(() => {
                location.reload();
            }, 1500);
        } else {
            statusMessage.textContent = data.message;
            statusMessage.className = 'error';
        }
    })
    .catch(error => {
        statusMessage.textContent = 'Error uploading video';
        statusMessage.className = 'error';
        console.error('Error:', error);
    });
});
