# Installation Guide

## Overview
This project requires the following dependencies to run:
- `tkinter` (for GUI development)
- `pyttsx3` (for text-to-speech functionality)

Some modules used in the project (`json`, `difflib`) are built into Python and do not require installation.

## Installation Steps

### 1. Clone or Download the Repository
If you haven't already, clone this repository or download the files.
```bash
git clone <repository_url>
cd <project_directory>
```

### 2. Install Dependencies
Run the following command to install required packages:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
After installation, execute the Python script to start the application:
```bash
python main.py
```
(Replace `main.py` with the actual filename of your script.)

## Notes
- `tkinter` is included with most Python distributions, so installation might not be necessary.
- Ensure Python is installed and `pip` is up to date (`pip install --upgrade pip`).

## Troubleshooting
- If `pyttsx3` doesn't work on your system, try installing additional dependencies:
  ```bash
  pip install pypiwin32 pyobjc
  ```
  (Windows users may need `pypiwin32`, and macOS users may need `pyobjc`).
- If you encounter errors, check the package documentation or reinstall dependencies.
