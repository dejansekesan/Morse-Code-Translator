import tkinter as tk
from tkinter import font
import subprocess
import os

def run_conversion():
    mode = var_mode.get()
    with open("input.txt", "w", encoding="utf-8") as f:
        f.write(input_text.get("1.0", tk.END))

    os.system(f"./variant {'1' if mode == 'text_to_morse' else '2'} < input.txt > output.txt")

    with open("output.txt", "r", encoding="utf-8") as f:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f.read())

def select_all(event):
    widget = event.widget
    widget.tag_add(tk.SEL, "1.0", tk.END)
    widget.mark_set(tk.INSERT, "1.0")
    widget.see(tk.INSERT)
    return "break"

root = tk.Tk()
root.title("Variant - Morse Code Converter")
root.geometry("900x700")
root.configure(bg="#1e1e1e")  # night theme

font_main = font.Font(family="Consolas", size=12)
bg_color = "#1e1e1e"
input_bg = "#252526"
fg_color = "#d4d4d4"
highlight_color = "#007acc"

# Mode selection
var_mode = tk.StringVar(value="text_to_morse")
frame_mode = tk.Frame(root, bg=bg_color)
tk.Radiobutton(frame_mode, text="Text to Morse", variable=var_mode, value="text_to_morse", 
               bg=bg_color, fg=fg_color, selectcolor=input_bg, font=font_main).pack(side="left", padx=10)
tk.Radiobutton(frame_mode, text="Morse to Text", variable=var_mode, value="morse_to_text", 
               bg=bg_color, fg=fg_color, selectcolor=input_bg, font=font_main).pack(side="left", padx=10)
frame_mode.pack(pady=10)

# Input frame with scrollbar
input_label = tk.Label(root, text="Input:", bg=bg_color, fg=fg_color, font=font_main)
input_label.pack(anchor="w", padx=10)
input_frame = tk.Frame(root, bg=bg_color)
input_scroll = tk.Scrollbar(input_frame)
input_text = tk.Text(input_frame, wrap="word", font=font_main, height=12, width=100,
                     bg=input_bg, fg=fg_color, insertbackground=fg_color,
                     undo=True, autoseparators=True, maxundo=-1, yscrollcommand=input_scroll.set)
input_scroll.config(command=input_text.yview)
input_scroll.pack(side="right", fill="y")
input_text.pack(side="left", expand=True, fill="both")
input_frame.pack(fill="both", expand=True, padx=10)

# Output frame with scrollbar
output_label = tk.Label(root, text="Output:", bg=bg_color, fg=fg_color, font=font_main)
output_label.pack(anchor="w", padx=10, pady=(10, 0))
output_frame = tk.Frame(root, bg=bg_color)
output_scroll = tk.Scrollbar(output_frame)
output_text = tk.Text(output_frame, wrap="word", font=font_main, height=12, width=100,
                      bg=input_bg, fg=fg_color, insertbackground=fg_color,
                      undo=True, autoseparators=True, maxundo=-1, yscrollcommand=output_scroll.set)
output_scroll.config(command=output_text.yview)
output_scroll.pack(side="right", fill="y")
output_text.pack(side="left", expand=True, fill="both")
output_frame.pack(fill="both", expand=True, padx=10)

# Convert button
tk.Button(root, text="Convert", command=run_conversion, font=font_main, bg=highlight_color, fg="white").pack(pady=10)

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

# Assuming your Text widget is called 'text_input' or similar



# Shortcuts and bindings
for widget in [input_text, output_text]:
    widget.bind("<Control-a>", select_all)
    widget.bind("<Control-A>", select_all)
    widget.bind("<Control-z>", lambda e, w=widget: w.edit_undo())
    widget.bind("<Control-y>", lambda e, w=widget: w.edit_redo())
    widget.bind("<Control-c>", lambda e, w=widget: w.event_generate("<<Copy>>"))
    widget.bind("<Control-v>", custom_paste)
    widget.bind("<Control-V>", custom_paste)
   # widget.bind("<Control-v>", lambda e, w=widget: w.event_generate("<<Paste>>"))
    widget.bind("<Control-x>", lambda e, w=widget: w.event_generate("<<Cut>>"))

root.mainloop()
