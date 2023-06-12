import tkinter as tk

def create_gui():
    window = tk.Tk()
    text_box = tk.Text(window)
    text_box.pack()
    return window, text_box
