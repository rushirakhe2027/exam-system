#!/bin/bash

echo "========================================"
echo "Advanced Online Exam System Installer"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "Python found. Checking version..."
python3 --version
echo

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv exam_env
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source exam_env/bin/activate

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo
echo "========================================"
echo "Installation completed successfully!"
echo "========================================"
echo
echo "To run the application:"
echo "1. Activate virtual environment: source exam_env/bin/activate"
echo "2. Run the application: python run.py"
echo
echo "Make sure to configure MongoDB connection in config.py"
echo

# Make the script executable
chmod +x install.sh 