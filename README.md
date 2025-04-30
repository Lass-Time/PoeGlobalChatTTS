# TTS File Monitor

A Python GUI that monitors a `.txt` file and reads lines with `#` using text-to-speech (TTS).

## Features
- Voice selection
- Rate and volume control
- Text-to-speech with pyttsx3
- Speech queuing (no overlapping errors)

## How to Use
1. Select a `.txt` file with lines like:
   ```
   (Client.txt file under \Program Files (x86)\Steam\steamapps\common\Path of Exile\logs)
   Narrator: #Welcome to the system
   ```
2. Click "Start Monitoring"

## Build Instructions
- Requires Python 3.10+
- Install dependencies:
  ```
  pip install -r requirements.txt
  ```
- Build the .exe:
  ```
  build_exe_with_queue.bat
  ```

## License
MIT
