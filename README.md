# TTS File Monitor (gTTS + pygame)

A Python GUI app that monitors a `.txt` file and speaks any new lines containing `#` using Google Text-to-Speech (gTTS).

---

## ✨ Features
- ✅ Monitors a text file for updates
- 🗣️ Google Text-to-Speech (gTTS)
- 🔊 Volume control
- 🎵 Simulated pitch control (via speed)
- ⏱ Queued speech (no interruptions)
- 🎮 `pygame` for smooth playback

---

## 🧭 Step-by-Step Guide for First-Time Users

### ✅ Step 1: Install Python

1. Go to: https://www.python.org/downloads/
2. Download and install Python 3.10 or later
3. ✅ During installation, check the box: **"Add Python to PATH"**

---

### ✅ Step 2: Download and Extract This Project

- Download the ZIP or clone the repo:
  ```
  git clone https://github.com/yourusername/tts-monitor.git
  ```

- Or just extract the provided `.zip` containing:
  - `src/tts_gui_gtts_pygame_controls.py`
  - `build_exe_gtts_pygame_controls.bat`
  - `requirements.txt`
  - `README.md`

---

### ✅ Step 3: Install Dependencies

Open Command Prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

This installs:
- `gTTS` – Google Text-to-Speech
- `pygame` – Audio playback
- `pyinstaller` – For `.exe` building

---

### ✅ Step 4: Run the Program

```bash
python src/tts_gui_gtts_pygame_controls.py
```

The GUI will launch.

---

### ✅ Step 5: Using the App

1. Click **"Browse"** and select a `.txt` file
2. Adjust **volume** and **pitch** (simulated)
3. Press **Start Monitoring**
4. Add lines like:
   ```
   Narrator: #Welcome to the system
   User: #Hello!
   ```
5. It will speak any new lines with `#` after monitoring starts.

---

### 🛠 Optional: Build a Standalone .EXE

Run this in Command Prompt:

```bash
build_exe_gtts_pygame_controls.bat
```

The `.exe` will appear in the `dist/` folder.

---

## 🧾 License

MIT License
