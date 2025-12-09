# Installation Guide

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Step-by-Step Installation

### 1. Clone the Repository
```bash
git clone https://github.com/vermarudransh/Qr-Code-Reader-Generator.git
cd Qr-Code-Reader-Generator
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install ZBar Library (Required for Scanning)

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install libzbar0
```

**macOS:**
```bash
brew install zbar
```

**Windows:**
ZBar DLLs are automatically included with the pyzbar package.

### 4. Verify Installation
```bash
python qr_tool.py
```

You should see the main menu if everything is installed correctly.

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'qrcode'"

**Solution:**
```bash
pip install qrcode[pil]
```

### Issue: "Unable to find zbar shared library"

**Solution:**

**Linux:**
```bash
sudo apt-get install libzbar0
```

**macOS:**
```bash
brew install zbar
pip install pyzbar
```

**Windows:**
Reinstall pyzbar:
```bash
pip uninstall pyzbar
pip install pyzbar
```

### Issue: "No module named 'cv2'"

**Solution:**
```bash
pip install opencv-python
```

## Virtual Environment 
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
