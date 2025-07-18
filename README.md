# 🎓 Advanced Online Exam System with AI Proctoring

A comprehensive web-based examination platform with advanced AI-powered proctoring capabilities, real-time monitoring, and secure exam delivery.

## 📋 Table of Contents
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Testing the System](#testing-the-system)
- [User Roles & Access](#user-roles--access)
- [Troubleshooting](#troubleshooting)
- [Security Features](#security-features)
- [API Documentation](#api-documentation)

## ✨ Features

### 🔒 AI-Powered Proctoring
- **Real-time face detection** using MediaPipe and OpenCV
- **Gaze tracking** to detect looking away from screen
- **Multiple person detection** to prevent cheating
- **Phone/device detection** using computer vision
- **Automatic violation warnings** with configurable thresholds
- **Auto-submission** after violation limit exceeded

### 📝 Exam Management
- **Multiple question types**: Objective (MCQ) and Subjective
- **Random question selection** from question banks
- **Timed examinations** with countdown timers
- **Auto-save functionality** for student answers
- **Real-time progress tracking**
- **Flexible exam scheduling**

### 👥 User Management
- **Three-tier role system**: Teachers, Students, Proctors
- **Class-based organization** with student enrollment
- **Secure authentication** with password hashing
- **Session management** with automatic logout

### 📊 Analytics & Reporting
- **Detailed submission reports** with timestamps
- **Violation tracking** and analytics
- **Performance statistics** for teachers
- **Export capabilities** for results

### 🌐 Real-time Features
- **WebSocket communication** for live monitoring
- **Real-time notifications** and alerts
- **Live exam status updates**
- **Instant violation reporting**

## 🖥️ System Requirements

### Minimum Requirements
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux Ubuntu 18.04+
- **Python**: 3.11.x (Recommended and Tested)
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space
- **Internet**: Stable broadband connection
- **Camera**: Built-in or external webcam (for proctoring)
- **Browser**: Chrome 90+, Firefox 88+, Safari 14+

### Recommended Requirements
- **Python**: 3.11.x (Fully tested and optimized)
- **RAM**: 16GB for optimal performance
- **GPU**: NVIDIA GPU with CUDA support (for better AI performance)
- **Storage**: SSD with 5GB free space

## 🚀 Installation Guide

### Step 1: Extract Project Files
```bash
# If you have a ZIP file, extract it to your desired location
# Navigate to the project directory
cd exam-system
```

### Step 2: Set Up Python Environment
```bash
# Check Python version (must be 3.11.x)
python --version
# Should show: Python 3.11.x

# Create virtual environment
python -m venv exam_env

# Activate virtual environment
# On Windows:
exam_env\Scripts\activate
# On macOS/Linux:
source exam_env/bin/activate
```

### Step 3: Install Dependencies
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# If you encounter issues with TensorFlow, install CPU version:
pip install tensorflow-cpu==2.13.0
```

### Step 4: Set Up MongoDB Database

**Step-by-Step MongoDB Compass Setup:**

1. **Download MongoDB Community Server**
   - Go to [MongoDB Community Server Download](https://www.mongodb.com/try/download/community)
   - Select your operating system (Windows/macOS/Linux)
   - Choose the latest version
   - Download the installer

2. **Install MongoDB Community Server**
   
   **For Windows:**
   - Run the downloaded `.msi` installer
   - Choose "Complete" installation
   - **Important**: Check "Install MongoDB Compass" during installation
   - Check "Run service as Network Service user" 
   - Click "Install" and wait for completion
   - MongoDB will start automatically as a Windows service

   **For macOS:**
   ```bash
   # Install using Homebrew (recommended)
   brew tap mongodb/brew
   brew install mongodb-community
   
   # Start MongoDB service
   brew services start mongodb/brew/mongodb-community
   
   # Download MongoDB Compass separately
   # Go to https://www.mongodb.com/try/download/compass
   ```

   **For Linux (Ubuntu/Debian):**
   ```bash
   # Import MongoDB public GPG key
   wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | sudo apt-key add -
   
   # Create list file for MongoDB
   echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
   
   # Update package database
   sudo apt-get update
   
   # Install MongoDB
   sudo apt-get install -y mongodb-org
   
   # Start MongoDB service
   sudo systemctl start mongod
   sudo systemctl enable mongod
   
   # Install MongoDB Compass
   wget https://downloads.mongodb.com/compass/mongodb-compass_1.40.4_amd64.deb
   sudo dpkg -i mongodb-compass_1.40.4_amd64.deb
   ```

3. **Launch MongoDB Compass**
   - Open MongoDB Compass application
   - You should see a connection screen
   - Use the default connection string: `mongodb://localhost:27017`
   - Click "Connect"

4. **Create Database**
   - In MongoDB Compass, click "Create Database"
   - Database Name: `exam_system`
   - Collection Name: `users` (you can start with this)
   - Click "Create Database"

5. **Verify Connection**
   - You should see your `exam_system` database in the left sidebar
   - The connection string to use in your app: `mongodb://localhost:27017/exam_system`

### Step 5: Configure Environment
```bash
# Create .env file in project root (optional but recommended)
# Add the following variables:
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-super-secret-key-here
MONGODB_URI=mongodb://localhost:27017/exam_system
```

## ⚙️ Configuration

### 1. Update config.py
```python
# Edit config.py file with your settings
class Config:
    SECRET_KEY = 'your-super-secret-key-change-this-in-production'
    
    # MongoDB Compass (Local Database)
    MONGODB_URI = 'mongodb://localhost:27017/exam_system'
    
    # Other configurations
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
```

### 2. Initialize Database
   ```bash
# Run the application once to create database indexes and collections
python run.py

# You should see output like:
# MongoDB indexes initialized successfully
# 🚀 EXAM SYSTEM STARTING
# 🌐 Starting on http://127.0.0.1:5000

# Stop with Ctrl+C after seeing the initialization message
```

### 3. Load Sample Data (Optional)
   ```bash
# The system includes sample questions that will be automatically
# available when you create your first exam:
# - demo_objective_questions.json (45 MCQ questions)
# - subjective_questions.json (41 text-based questions)
   ```

## 🗄️ MongoDB Compass Management

### Using MongoDB Compass with Your Exam System

Once your application is running, you can use MongoDB Compass to:

#### 1. **Monitor Database Activity**
- Open MongoDB Compass
- Connect to `mongodb://localhost:27017`
- Navigate to `exam_system` database
- View real-time data changes as users interact with your system

#### 2. **View Collections**
Your exam system will create these collections automatically:
- **`users`** - Teacher, Student, and Proctor accounts
- **`classes`** - Class information and student enrollments
- **`exams`** - Exam configurations and settings
- **`questions`** - Question bank with objective and subjective questions
- **`submissions`** - Student exam submissions and answers
- **`violations`** - Proctoring violations and warnings

#### 3. **Database Operations**
- **View Data**: Click on any collection to see documents
- **Search**: Use the filter bar to find specific records
- **Export**: Export collections for backup or analysis
- **Import**: Import question banks or user data

#### 4. **Troubleshooting with Compass**
- **Check Connections**: Verify if data is being saved properly
- **Monitor Performance**: View query performance and indexes
- **Debug Issues**: Examine document structure and data types

#### 5. **Sample Queries for Testing**
```javascript
// Find all teachers
{"role": "teacher"}

// Find active exams
{"is_active": true}

// Find submissions for a specific exam
{"exam_id": ObjectId("your-exam-id-here")}

// Find violations for a specific student
{"student_id": ObjectId("your-student-id-here")}
```

### Backup and Restore
```bash
# Create backup using mongodump
mongodump --db exam_system --out ./backup

# Restore from backup
mongorestore --db exam_system ./backup/exam_system
```

## 🏃‍♂️ Running the Application

### Development Mode
   ```bash
# Activate virtual environment (if not already active)
# On Windows:
exam_env\Scripts\activate
# On macOS/Linux:
source exam_env/bin/activate

# Run the application
   python run.py
   ```

### Production Mode
```bash
# Using Gunicorn (Linux/macOS)
gunicorn -w 4 -b 0.0.0.0:8000 run:app

# Using Waitress (Windows)
pip install waitress
waitress-serve --host=0.0.0.0 --port=8000 run:app
```

The application will be available at:
- **Development**: http://localhost:5000
- **Production**: http://localhost:8000

## 🧪 Testing the System

### 1. Create Test Accounts

#### Teacher Account
1. Go to `/register`
2. Register as a Teacher
3. Create a class and add questions

#### Student Account
1. Register as a Student
2. Join the class created by teacher

### 2. Test Exam Flow
1. **Teacher**: Create an exam with questions
2. **Student**: Take the exam
3. **Monitor**: Check proctoring features work
4. **Review**: Check results and reports

### 3. Test Proctoring Features
- **Face Detection**: Ensure camera detects face
- **Gaze Tracking**: Look away to trigger warnings
- **Multiple Person**: Have someone else appear on camera
- **Phone Detection**: Show a phone to camera
- **Violation Limits**: Trigger 20 violations for auto-submit

### 4. Sample Test Data
The system includes sample questions in:
- `demo_objective_questions.json` - Multiple choice questions
- `subjective_questions.json` - Text-based questions

## 👤 User Roles & Access

### 🎓 Teacher
- Create and manage classes
- Add/edit questions and question banks
- Create and schedule exams
- View student submissions and results
- Access analytics and reports
- Monitor exam sessions

### 👨‍🎓 Student
- Join classes using class codes
- Take assigned examinations
- View personal results and history
- Access exam schedules
- Receive real-time notifications

### 👮‍♂️ Proctor
- Monitor live exam sessions
- View real-time violation reports
- Access proctoring dashboard
- Generate monitoring reports

## 🔧 Troubleshooting

### Common Issues

#### 1. Camera Not Working
```bash
# Check camera permissions in browser
# Try different browsers
# Update OpenCV: pip install --upgrade opencv-python
```

#### 2. MongoDB Connection Issues
```bash
# Check MongoDB service is running
# Verify connection string in config.py
# Check firewall settings
```

#### 3. TensorFlow Installation Issues
```bash
# Install CPU version if GPU issues:
pip uninstall tensorflow
pip install tensorflow-cpu==2.13.0
```

#### 4. Port Already in Use
```bash
# Kill existing processes:
# Windows: taskkill /F /IM python.exe
# Linux/macOS: pkill -f python
```

#### 5. Missing Dependencies
```bash
# Reinstall requirements:
pip install --force-reinstall -r requirements.txt
```

### Performance Optimization
- Use SSD storage for better I/O performance
- Increase RAM allocation for large exams
- Use CDN for static files in production
- Enable MongoDB indexing for faster queries

## 🔐 Security Features

### Authentication & Authorization
- **Secure password hashing** using bcrypt
- **Session management** with Flask-Login
- **Role-based access control**
- **CSRF protection** with Flask-WTF

### Exam Security
- **Browser lockdown** features
- **Copy-paste prevention**
- **Right-click disabling**
- **Developer tools blocking**
- **Tab switching detection**

### Data Protection
- **Encrypted data transmission**
- **Secure cookie handling**
- **Input validation and sanitization**
- **SQL injection prevention**

### Proctoring Security
- **Real-time violation detection**
- **Tamper-proof monitoring**
- **Encrypted video processing**
- **Secure violation reporting**

## 📡 API Documentation

### Authentication Endpoints
- `