import tkinter as tk
from tkinter import font
from tkinter import messagebox
import pygame
import threading
import time
import os
import re
import sys

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', ':': '---...',
    '"': '.-..-.', '\'': '.----.', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.', ' ': '/'

}

REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

EXTENDED_LATIN_MAP = {
    'Š': 'S', 'š': 's', 'Đ': 'Dj', 'đ': 'dj', 'Č': 'C', 'č': 'c', 'Ć': 'C', 'ć': 'c', 'Ž': 'Z', 'ž': 'z'
}

pygame.mixer.init()
volume = 0.5
speed = 0.5
gap = 0
playing = False
stop_signal = threading.Event()

def resource_path(relative_path):
    # Get absolute path to resource, works for dev and PyInstaller
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

dot_sound = pygame.mixer.Sound(resource_path("dot.wav"))
dash_sound = pygame.mixer.Sound(resource_path("dash.wav"))

def play_beep(symbol):
    if symbol == '.':
        dot_sound.set_volume(volume)
        dot_sound.play()
        time.sleep(0.1 * speed)
    elif symbol == '-':
        dash_sound.set_volume(volume)
        dash_sound.play()
        time.sleep(0.3 * speed)

def play_morse(morse_code):
    global playing
    playing = True
    for symbol in morse_code:
        if stop_signal.is_set():
            break
        if symbol in ['.', '-']:
            play_beep(symbol)
        elif symbol == ' ':
            time.sleep(0.3 * speed + gap)
        elif symbol == '/':
            time.sleep(0.7 * speed + gap)
        elif symbol == '\n':
            time.sleep(1 * speed + gap * 1.1)
        time.sleep(0.1 * speed)
    playing = False

def convert_text_to_morse(text):
    text = text.upper()
    text = ''.join(EXTENDED_LATIN_MAP.get(ch, ch) for ch in text)
    lines = text.splitlines()
    converted = []
    for line in lines:
        converted.append(' '.join(MORSE_CODE_DICT.get(char, '') for char in line))
    return '\n'.join(converted)

def convert_morse_to_text(morse):
    words = morse.split('\n')
    decoded_lines = []
    for word in words:
        characters = word.split(' ')
        decoded_line = ''.join(REVERSE_MORSE_CODE_DICT.get(char, '') for char in characters)
        decoded_lines.append(decoded_line)
    return '\n'.join(decoded_lines)

def run_conversion():
    input_val = input_text.get("1.0", tk.END).strip()
    if var_mode.get() == "text_to_morse":
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, convert_text_to_morse(input_val))
    else:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, convert_morse_to_text(input_val))

def toggle_play():
    global playing
    if playing:
        return
    stop_signal.clear()
    if var_mode.get() == "text_to_morse":
        source = output_text.get("1.0", tk.END).strip()
    else:  # morse_to_text mode plays input box content (Morse code)
        source = input_text.get("1.0", tk.END).strip()
    if not source:
        return
    thread = threading.Thread(target=play_morse, args=(source,))
    thread.start()


def stop_play():
    global playing
    stop_signal.set()
    playing = False

def update_volume(val):
    global volume
    volume = float(val)

def update_speed(val):
    global speed
    speed = float(val)

def update_gap(val):
    global gap
    gap = float(val)

def select_all(event):
    event.widget.tag_add("sel", "1.0", "end")
    return "break"

def custom_paste(event):
    widget = event.widget
    try:
        clipboard = widget.clipboard_get()
    except:
        return "break"
    try:
        widget.delete("sel.first", "sel.last")
    except:
        pass
    widget.insert("insert", clipboard)
    return "break"

def clear_and_set_mode():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    if var_mode.get() == "morse_to_text":
        def only_morse_input(event):
            if event.char not in ".-/ /\\n\\r\\t\\b":  # add space ' ' here explicitly
                return "break"
        input_text.bind("<Key>", only_morse_input)
    else:
        input_text.unbind("<Key>")


# GUI setup
root = tk.Tk()
root.title("Variant - Morse Code Converter")
root.geometry("900x700")
root.configure(bg="#1e1e1e")

font_main = font.Font(family="Consolas", size=12)
bg_color = "#1e1e1e"
input_bg = "#252526"
fg_color = "#d4d4d4"
highlight_color = "#007acc"

var_mode = tk.StringVar(value="text_to_morse")
frame_mode = tk.Frame(root, bg=bg_color)
tk.Radiobutton(frame_mode, text="Text to Morse", variable=var_mode, value="text_to_morse",
               bg=bg_color, fg=fg_color, selectcolor=input_bg, font=font_main,
               command=clear_and_set_mode).pack(side="left", padx=10)
tk.Radiobutton(frame_mode, text="Morse to Text", variable=var_mode, value="morse_to_text",
               bg=bg_color, fg=fg_color, selectcolor=input_bg, font=font_main,
               command=clear_and_set_mode).pack(side="left", padx=10)
frame_mode.pack(pady=10)

frame_input_area = tk.Frame(root, bg=bg_color)
frame_input_area.pack(fill="both", expand=True, padx=10)

input_label = tk.Label(frame_input_area, text="Input:", bg=bg_color, fg=fg_color, font=font_main)
input_label.grid(row=0, column=0, sticky="w", pady=(0, 2))

input_frame = tk.Frame(frame_input_area, bg=bg_color)
input_frame.grid(row=1, column=0, sticky="nsew")

frame_input_area.grid_rowconfigure(1, weight=1)
frame_input_area.grid_columnconfigure(0, weight=1)

input_scroll = tk.Scrollbar(input_frame)
input_text = tk.Text(input_frame, wrap="word", font=font_main, height=12,
                     bg=input_bg, fg=fg_color, insertbackground=fg_color,
                     undo=True, autoseparators=True, maxundo=-1, yscrollcommand=input_scroll.set)
input_scroll.config(command=input_text.yview)
input_scroll.pack(side="right", fill="y")
input_text.pack(side="left", expand=True, fill="both")

frame_output_area = tk.Frame(root, bg=bg_color)
frame_output_area.pack(fill="both", expand=True, padx=10, pady=(10, 0))

output_label = tk.Label(frame_output_area, text="Output:", bg=bg_color, fg=fg_color, font=font_main)
output_label.grid(row=0, column=0, sticky="w", pady=(0, 2))

output_frame = tk.Frame(frame_output_area, bg=bg_color)
output_frame.grid(row=1, column=0, sticky="nsew")

frame_output_area.grid_rowconfigure(1, weight=1)
frame_output_area.grid_columnconfigure(0, weight=1)

output_scroll = tk.Scrollbar(output_frame)
output_text = tk.Text(output_frame, wrap="word", font=font_main, height=12,
                      bg=input_bg, fg=fg_color, insertbackground=fg_color,
                      undo=True, autoseparators=True, maxundo=-1, yscrollcommand=output_scroll.set)
output_scroll.config(command=output_text.yview)
output_scroll.pack(side="right", fill="y")
output_text.pack(side="left", expand=True, fill="both")

controls_frame = tk.Frame(root, bg=bg_color)
controls_frame.pack(pady=10)

convert_button = tk.Button(controls_frame, text="Convert", command=run_conversion,
                           font=font_main, bg="#007acc", fg="white")
convert_button.grid(row=0, column=0, padx=5)

play_button = tk.Button(controls_frame, text="Play", command=toggle_play,
                        font=font_main, bg="#28a745", fg="white")  # green
play_button.grid(row=0, column=1, padx=5)

stop_button = tk.Button(controls_frame, text="Stop", command=stop_play,
                        font=font_main, bg="#dc3545", fg="white")  # red
stop_button.grid(row=0, column=2, padx=5)

volume_label = tk.Label(controls_frame, text="Volume", bg=bg_color, fg=fg_color, font=font_main)
volume_label.grid(row=0, column=3, padx=(20, 5))
volume_slider = tk.Scale(controls_frame, from_=0, to=1, resolution=0.01, orient="horizontal",
                         command=update_volume, bg=bg_color, fg=fg_color, font=font_main,
                         troughcolor=input_bg)
volume_slider.set(volume)
volume_slider.grid(row=0, column=4, padx=5)

speed_label = tk.Label(controls_frame, text="Speed (s)", bg=bg_color, fg=fg_color, font=font_main)
speed_label.grid(row=0, column=5, padx=(20, 5))
speed_slider = tk.Scale(controls_frame, from_=0.1, to=2.0, resolution=0.1, orient="horizontal",
                        command=update_speed, bg=bg_color, fg=fg_color, font=font_main,
                        troughcolor=input_bg)
speed_slider.set(speed)
speed_slider.grid(row=0, column=6, padx=5)


gap_label = tk.Label(controls_frame, text="Gap (in seconds)", bg=bg_color, fg=fg_color, font=font_main)
gap_label.grid(row=0, column=7, padx=(20, 5))
gap_slider = tk.Scale(controls_frame, from_=0, to=3.0, resolution=0.1, orient="horizontal",
                        command=update_gap, bg=bg_color, fg=fg_color, font=font_main,
                        troughcolor=input_bg)
gap_slider.set(gap)
gap_slider.grid(row=0, column=8, padx=5)

for widget in [input_text, output_text]:
    widget.bind("<Control-a>", select_all)
    widget.bind("<Control-A>", select_all)
    widget.bind("<Control-z>", lambda e, w=widget: w.edit_undo())
    widget.bind("<Control-y>", lambda e, w=widget: w.edit_redo())
    widget.bind("<Control-c>", lambda e, w=widget: w.event_generate("<<Copy>>"))
    widget.bind("<Control-v>", custom_paste)
    widget.bind("<Control-V>", custom_paste)
    widget.bind("<Control-x>", lambda e, w=widget: w.event_generate("<<Cut>>"))

root.mainloop()
