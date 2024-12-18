import os
import json
from flask import Flask, render_template, request, jsonify, send_from_directory, redirect, url_for
import requests
import secrets

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/videos'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.secret_key = secrets.token_hex(16)

# Allowed video file extensions
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'wmv'}

def allowed_file(filename):
    """Check if the file has an allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Configuration file for video backgrounds
CONFIG_FILE = 'video_config.json'

def load_video_config():
    """Load video configuration"""
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'background_video': 'default.mp4'}

def save_video_config(config):
    """Save video configuration"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

@app.route('/')
def index():
    """Main display page"""
    config = load_video_config()
    return render_template('index.html', background_video=config['background_video'])

@app.route('/admin')
def admin_panel():
    """Admin panel to select video background"""
    # Get list of videos in the videos directory
    videos = [f for f in os.listdir('static/videos') if f.endswith(tuple(f'.{ext}' for ext in ALLOWED_EXTENSIONS))]
    config = load_video_config()
    return render_template('admin.html', videos=videos, current_video=config['background_video'])

@app.route('/update_background', methods=['POST'])
def update_background():
    """Update background video"""
    video = request.form.get('video')
    if video:
        config = load_video_config()
        config['background_video'] = video
        save_video_config(config)
        return jsonify({'status': 'success', 'video': video})
    return jsonify({'status': 'error', 'message': 'No video selected'})

@app.route('/upload_video', methods=['POST'])
def upload_video():
    """Handle video file upload"""
    if 'video' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file uploaded'})
    
    file = request.files['video']
    
    # Check if filename is empty
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})
    
    # Check if file is allowed
    if file and allowed_file(file.filename):
        # Sanitize filename
        filename = secrets.token_hex(8) + '.' + file.filename.rsplit('.', 1)[1].lower()
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Ensure videos directory exists
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        # Save the file
        file.save(file_path)
        
        return jsonify({
            'status': 'success', 
            'message': 'File uploaded successfully', 
            'filename': filename
        })
    
    return jsonify({'status': 'error', 'message': 'File type not allowed'})

@app.route('/temperatures')
def get_temperatures():
    """Proxy temperatures from temperature server"""
    try:
        response = requests.get('http://localhost:5000/temperatures', timeout=5)
        data = response.json()
        # Ensure temperatures are numbers
        return jsonify({
            'cpu': round(data['cpu']) if data['cpu'] is not None else None,
            'gpu': round(data['gpu']) if data['gpu'] is not None else None
        })
    except requests.RequestException:
        return jsonify({'cpu': 'N/A', 'gpu': 'N/A'})

@app.route('/static/videos/<path:filename>')
def serve_video(filename):
    """Serve video files"""
    return send_from_directory('static/videos', filename)

if __name__ == '__main__':
    # Ensure videos directory exists
    os.makedirs('static/videos', exist_ok=True)
    
    # Run the app
    app.run(host='0.0.0.0', port=8000, debug=True)
