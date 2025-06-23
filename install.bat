@echo off
echo ========================================
echo Advanced Online Exam System Installer
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://python.org
    pause
    exit /b 1
)

echo Python found. Checking version...
python -c "import sys; print('Python version:', sys.version)"
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv exam_env
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call exam_env\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation completed successfully!
echo ========================================
echo.
echo To run the application:
echo 1. Activate virtual environment: exam_env\Scripts\activate.bat
echo 2. Run the application: python run.py
echo.
echo Make sure to configure MongoDB connection in config.py
echo.
pause 