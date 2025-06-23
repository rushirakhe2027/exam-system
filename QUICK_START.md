# 🚀 Quick Start Guide - Advanced Online Exam System

## 📦 For ZIP File Installation

If you received this project as a ZIP file, follow these steps to get it running quickly:

### Step 1: Extract Files
1. Extract the ZIP file to your desired location
2. Open terminal/command prompt in the extracted folder

### Step 2: Choose Installation Method

#### Option A: Automatic Installation (Recommended)

**Windows Users:**
```cmd
# Double-click install.bat or run in Command Prompt:
install.bat
```

**Linux/macOS Users:**
```bash
# Make script executable and run:
chmod +x install.sh
./install.sh
```

#### Option B: Manual Installation

1. **Create Virtual Environment:**
   ```bash
   # Windows:
   python -m venv exam_env
   exam_env\Scripts\activate
   
   # Linux/macOS:
   python3 -m venv exam_env
   source exam_env/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Step 3: Configure Database

#### Quick Setup with MongoDB Atlas (Cloud):
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create free account and cluster
3. Get connection string
4. Update `config.py`:
   ```python
   MONGODB_URI = "your-mongodb-connection-string"
   ```

#### Local MongoDB Setup:
1. Install [MongoDB Community Server](https://www.mongodb.com/try/download/community)
2. Start MongoDB service
3. Keep default settings in `config.py`

### Step 4: Run the Application
```bash
python run.py
```

### Step 5: Access the System
Open your browser and go to: http://localhost:5000

## 🧪 Quick Test

### Create Test Accounts:
1. **Register as Teacher**: Go to `/register` → Select Teacher
2. **Register as Student**: Go to `/register` → Select Student

### Test the System:
1. **Teacher**: Create a class and exam
2. **Student**: Join class and take exam
3. **Test Proctoring**: Ensure camera works and try triggering violations

## 📁 Project Structure Quick Reference

```
exam system/
├── 📄 README.md                    # Detailed documentation
├── 📄 PROJECT_DOCUMENTATION.md     # Complete project analysis
├── 📄 QUICK_START.md               # This quick start guide
├── 📄 requirements.txt             # Python dependencies
├── 📄 config.py                    # Configuration file
├── 📄 run.py                       # Application starter
├── 📄 install.bat                  # Windows installer
├── 📄 install.sh                   # Linux/macOS installer
├── 📄 setup.py                     # Python package setup
├── 📄 .gitignore                   # Git ignore file
├── 📄 demo_objective_questions.json # Sample MCQ questions
├── 📄 subjective_questions.json    # Sample text questions
└── 📁 app/                         # Main application code
    ├── 📁 models/                  # Data models
    ├── 📁 routes/                  # URL handlers
    ├── 📁 templates/               # HTML templates
    ├── 📁 static/                  # CSS, JS, AI models
    └── 📁 utils/                   # Utility functions
```

## ⚡ Key Features to Test

### 🔒 AI Proctoring Features:
- **Face Detection**: Camera should detect your face
- **Gaze Tracking**: Look away to trigger warnings
- **Multiple Person Detection**: Have someone else appear on camera
- **Violation Warnings**: System shows emoji warnings
- **Auto-submission**: Reaches limit after 20 violations

### 📝 Exam Features:
- **Auto-save**: Answers save automatically as you type
- **Green Checkmarks**: Question buttons turn green when answered
- **Progress Tracking**: Visual progress indicators
- **Timer**: Countdown timer for timed exams

### 👥 User Roles:
- **Teacher**: Create classes, exams, questions, view results
- **Student**: Take exams, view results
- **Proctor**: Monitor exam sessions (if implemented)

## 🔧 Common Issues & Solutions

### Issue: Camera Not Working
**Solution:**
- Check browser permissions for camera access
- Try different browsers (Chrome recommended)
- Ensure good lighting conditions

### Issue: MongoDB Connection Error
**Solution:**
- Verify MongoDB is running (local installation)
- Check connection string in `config.py`
- Ensure network connectivity (for Atlas)

### Issue: Dependencies Installation Failed
**Solution:**
```bash
# Try installing with specific versions:
pip install --force-reinstall -r requirements.txt

# For TensorFlow issues:
pip install tensorflow-cpu==2.13.0
```

### Issue: Port Already in Use
**Solution:**
```bash
# Windows:
taskkill /F /IM python.exe

# Linux/macOS:
pkill -f python
```

## 📱 Browser Compatibility

### Recommended Browsers:
- ✅ **Chrome 90+** (Best performance)
- ✅ **Firefox 88+** (Good performance)
- ✅ **Safari 14+** (macOS only)
- ⚠️ **Edge 90+** (Basic support)

### Required Browser Features:
- WebRTC support for camera access
- JavaScript enabled
- Local storage enabled
- WebSocket support

## 🎯 Default Login Credentials

After installation, you can create accounts by registering. The system includes:
- Sample objective questions in `demo_objective_questions.json`
- Sample subjective questions in `subjective_questions.json`

## 🔗 Important URLs

- **Home**: http://localhost:5000/
- **Login**: http://localhost:5000/login
- **Register**: http://localhost:5000/register
- **Teacher Dashboard**: http://localhost:5000/teacher/dashboard
- **Student Dashboard**: http://localhost:5000/student/dashboard

## 📞 Need Help?

1. Check `README.md` for detailed documentation
2. Review `PROJECT_DOCUMENTATION.md` for technical details
3. Ensure all system requirements are met
4. Verify MongoDB connection is working

## 🏆 Success Indicators

You know the system is working correctly when:
- ✅ Application starts without errors
- ✅ You can register and login
- ✅ Camera permission is granted
- ✅ Face detection shows green border around face
- ✅ Questions load and auto-save works
- ✅ Violation warnings appear when looking away

---

**Quick Start Version**: 1.0  
**Compatible with**: Windows 10+, macOS 10.14+, Linux Ubuntu 18.04+  
**Python Version**: 3.8+ 