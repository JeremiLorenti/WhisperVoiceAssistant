main.py
import keyboard
import pyaudio
import io
from api import speech_to_text
from gui import create_gui

def record_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    frames = []
    try:
        while True:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        print("Recording stopped.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    buf = io.BytesIO()
    for frame in frames:
        buf.write(frame)
    buf.seek(0)
    return buf.read()

def on_hotkey():
    audio_data = record_audio()
    text = speech_to_text(audio_data)
    text_box.insert(tk.END, text)

window, text_box = create_gui()
keyboard.add_hotkey('ctrl+alt+a', on_hotkey)
keyboard.wait()
window.mainloop()
