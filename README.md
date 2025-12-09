# 🔲 QR Code Generator & Scanner

A simple, offline Python tool for generating and scanning QR codes. No internet required, completely private.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## ✨ Features

- **Generate QR Codes** - Create QR codes from any text or URL
- **Scan QR Codes** - Decode QR codes from image files
- **Simple Interface** - User-friendly command-line menu
- **Offline & Private** - Works completely offline, no data sharing
- **Fast** - Instant generation, sub-second scanning
- **Cross-Platform** - Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/vermarudransh/Qr-Code-Reader-Generator.git
cd Qr-Code-Generator

# Install dependencies
pip install -r requirements.txt

# Install zbar library (required for scanning)
# Ubuntu/Debian:
sudo apt-get install libzbar0

# macOS:
brew install zbar

# Windows: Already included with pyzbar
```

### Usage
```bash
# Run the tool
python qr_tool.py
```

## 📖 How to Use

### Generate QR Code

1. Run the program: `python qr_tool.py`
2. Select option `1` (Generate QR Code)
3. Enter your data (text, URL, etc.)
4. Optionally provide a filename (default: qr_code.png)
5. QR code is generated and saved!

### Scan QR Code

1. Run the program: `python qr_tool.py`
2. Select option `2` (Scan QR Code)
3. Enter the image filename
4. View the decoded data!

