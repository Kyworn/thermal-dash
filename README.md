# 🌡️ Temperature Monitoring Dashboard

## Overview

This is a sleek, real-time temperature monitoring web application designed to display CPU and GPU temperatures with a dynamic video background. Perfect for monitoring system temperatures with a modern, minimalist interface.

## 🚀 Features

- **Real-time Temperature Tracking**
  - Live CPU and GPU temperature display
  - Interactive temperature chart with historical data
  - Automatic updates every 2 seconds

- **Dynamic Background**
  - Customizable video background
  - Admin panel for video management
  - Supports multiple video files

## 🛠 Technologies Used

- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS3, JavaScript
- **Charting**: Chart.js
- **Video Management**: Custom Flask routes

## 📦 Prerequisites

- Python 3.8+
- pip (Python package manager)

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone the repository
   cd temperature-monitor
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎬 Setup Video Background

1. Place your video files in `static/videos/` or use the admin panel for uploading new videos
2. Use the admin panel to select and manage background videos

## 🚀 Running the Application

Launch launch_all_background_admin.sh with admin privileges to run the application and the temperature server.

Navigate to `http://localhost:5000` to view the dashboard
Admin panel: `http://localhost:5000/admin`

## 🛑 Stopping the Server

### Killing Python Processes

If the server doesn't stop properly, you may need to manually kill the Python processes in Task Manager:

1. Open Windows Task Manager (Ctrl + Shift + Esc)
2. Go to the "Processes" tab
3. Look for and end ALL Python processes:
   - Look for processes named `python.exe`
   - Pay special attention to `python (2)` and other Python instances
   - Ensure you end ALL related Python processes

**Warning**: 
- Be careful to only kill Python processes related to this application
- If unsure, note the Process ID (PID) before ending tasks

## 🖥️ Screenshots

[Add screenshots of your application here]

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.


---

**Note**: This project is a work in progress. Contributions and suggestions are welcome! 🌟
