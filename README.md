
# Talking Dictionary App

## Overview
This project is a modern graphical dictionary application with voice support, autocomplete, and theme customization. Built using Python and `ttkbootstrap`, it offers a clean UI with a native feel across platforms.

### ✨ Features
- Search for word meanings
- Text-to-speech for both word and meaning
- Autocomplete suggestions as you type
- Dark/light theme support using `ttkbootstrap`
- Keyboard shortcuts:
  - `Ctrl + Enter` – Search
  - `Esc` – Clear
  - `Ctrl + Q` – Exit

## 🛠️ Requirements

### Python Packages
- `pyttsx3` – Text-to-speech engine
- `ttkbootstrap` – Enhanced UI theming based on ttk
- `tkinter` – Built-in GUI library (comes with most Python installations)

Modules like `json`, `difflib`, and `os` are part of Python’s standard library and need no installation.

## 🔧 Installation Steps

### 1. Clone the Repository
```bash
git clone <repository_url>
cd <project_directory>
```

### 2. Install Dependencies
Install required packages:
```bash
pip install -r requirements.txt
```

Your `requirements.txt` should contain:
```
pyttsx3
ttkbootstrap
```

### 3. Run the Application
Start the app:
```bash
python main.py
```

## 🧠 Notes
- You can change the theme in `main.py` by modifying:
  ```python
  root = tb.Window(themename="darkly")  # Options: "litera", "superhero", etc.
  ```
- `tkinter` usually comes preinstalled with Python.
- Use Python ≥ 3.7 for best compatibility.

## 🛠️ Troubleshooting

- If `pyttsx3` throws errors:
  ```bash
  pip install pypiwin32 pyobjc
  ```
  *(Windows: `pypiwin32`, macOS: `pyobjc`)*

- For missing GUI components, ensure `tkinter` is available on your Python installation:
  ```bash
  sudo apt install python3-tk  # Ubuntu/Debian
  ```

## 📁 Project Structure
```
project/
│
├── main.py
├── dictionary_logic.py
├── data/
│   └── data.json
├── requirements.txt
├── .gitignore
└── README.md
```
