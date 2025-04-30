
import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
from gtts import gTTS
import pygame
import os
import threading
import time
import tempfile
import uuid
import queue

class FileMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TTS Monitor (gTTS + pygame with queue + controls)")
        self.file_path = ""
        self.monitoring = False
        self.last_size = 0
        self.speech_queue = queue.Queue()

        pygame.mixer.init()

        threading.Thread(target=self.speech_loop, daemon=True).start()

        tk.Label(root, text="Select a text file:").pack(pady=5)
        tk.Button(root, text="Browse", command=self.select_file).pack(pady=5)

        self.language = tk.StringVar(value="en")
        tk.Label(root, text="Language Code (e.g., en, es, fr):").pack(pady=5)
        tk.Entry(root, textvariable=self.language).pack(pady=5)

        tk.Label(root, text="Volume (0 to 100):").pack(pady=5)
        self.volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
        self.volume_slider.set(100)
        self.volume_slider.pack(pady=5)

        tk.Label(root, text="Pitch (simulated by speed):").pack(pady=5)
        self.pitch_slider = tk.Scale(root, from_=50, to=150, orient=tk.HORIZONTAL)
        self.pitch_slider.set(100)
        self.pitch_slider.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Monitoring", command=self.start_monitoring, state='disabled')
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Monitoring", command=self.stop_monitoring, state='disabled')
        self.stop_button.pack(pady=5)

        self.text_area = scrolledtext.ScrolledText(root, width=60, height=15)
        self.text_area.pack(pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.file_path:
            self.text_area.insert(tk.END, f"Selected file: {self.file_path}\n")
            self.start_button.config(state='normal')

    def start_monitoring(self):
        if not self.monitoring:
            self.monitoring = True
            self.start_button.config(state='disabled')
            self.stop_button.config(state='normal')

            if os.path.isfile(self.file_path):
                with open(self.file_path, 'rb') as f:
                    f.seek(0, os.SEEK_END)
                    self.last_size = f.tell()
            else:
                self.last_size = 0

            threading.Thread(target=self.monitor_file, daemon=True).start()

    def stop_monitoring(self):
        self.monitoring = False
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
        self.text_area.insert(tk.END, "Monitoring stopped.\n")

    def monitor_file(self):
        self.text_area.insert(tk.END, "Started monitoring...\n")
        while self.monitoring:
            try:
                if not os.path.isfile(self.file_path):
                    time.sleep(1)
                    continue

                current_size = os.path.getsize(self.file_path)
                if current_size < self.last_size:
                    self.last_size = 0

                with open(self.file_path, 'r', encoding='utf-8') as f:
                    f.seek(self.last_size)
                    new_lines = f.readlines()
                    self.last_size = f.tell()

                    for line in new_lines:
                        if '#' in line:
                            spoken = line.split('#', 1)[1].strip()
                            if ':' in spoken:
                                parts = spoken.split(':', 1)
                                speaker = parts[0].strip()
                                message = parts[1].strip()
                                spoken_text = f"{speaker} says {message}"
                            else:
                                spoken_text = spoken

                            if spoken_text:
                                self.text_area.insert(tk.END, f"Queued: {spoken_text}\n")
                                self.text_area.see(tk.END)
                                self.speech_queue.put(spoken_text)
            except Exception as e:
                self.text_area.insert(tk.END, f"Error: {e}\n")
            time.sleep(1)

    def speech_loop(self):
        while True:
            text = self.speech_queue.get()
            try:
                temp_path = os.path.join(tempfile.gettempdir(), f"tts_{uuid.uuid4().hex}.mp3")
                tts = gTTS(text=text, lang=self.language.get(), slow=self.pitch_slider.get() < 100)
                tts.save(temp_path)

                pygame.mixer.music.set_volume(self.volume_slider.get() / 100.0)
                pygame.mixer.music.load(temp_path)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

                time.sleep(0.5)
                for _ in range(5):
                    try:
                        os.remove(temp_path)
                        break
                    except PermissionError:
                        time.sleep(0.2)
            except Exception as e:
                print(f"TTS Error: {e}")
            self.speech_queue.task_done()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileMonitorApp(root)
    root.mainloop()
