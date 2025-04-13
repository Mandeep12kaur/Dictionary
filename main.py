import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
import pyttsx3
from dict_logic import Dictionary

dictionary = Dictionary()
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[0].id)

def search(event=None):
    word = word_entry.get()
    meanings, word, suggestion = dictionary.get_meaning(word)
    result_text.delete(1.0, 'end')
    if meanings:
        for meaning in meanings:
            result_text.insert('end', f'• {meaning}\n\n')
    elif suggestion:
        if messagebox.askyesno('Did You Mean?', f'Did you mean "{suggestion}"?'):
            word_entry.delete(0, 'end')
            word_entry.insert(0, suggestion)
            search()
        else:
            messagebox.showerror('Not Found', 'Word not found.')
    else:
        messagebox.showerror('Not Found', 'Word not found.')

def clear(event=None):
    word_entry.delete(0, 'end')
    result_text.delete(1.0, 'end')

def iexit(event=None):
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()

def speak_word():
    engine.say(word_entry.get())
    engine.runAndWait()

def speak_meaning():
    engine.say(result_text.get(1.0, 'end'))
    engine.runAndWait()

def update_autocomplete(*args):
    typed = word_entry.get().lower()
    suggestions = [word for word in dictionary.data if word.startswith(typed)][:5]
    if suggestions:
        suggestion_box.configure(values=suggestions)
        suggestion_box.current(0)
        suggestion_box.place(x=word_entry.winfo_x(), y=word_entry.winfo_y() + 35)
    else:
        suggestion_box.place_forget()

def fill_from_suggestion(event):
    word_entry.delete(0, 'end')
    word_entry.insert(0, suggestion_box.get())
    suggestion_box.place_forget()
    search()

root = tb.Window(themename="darkly")  # Try 'litera', 'superhero', 'morph', etc.
root.title("Dictionary")
root.geometry("650x460")
root.resizable(False, False)

tb.Label(root, text="Dictionary", font=("Helvetica", 22, "bold")).pack(pady=15)

word_var = tb.StringVar()
word_var.trace_add("write", update_autocomplete)

word_entry = tb.Entry(root, textvariable=word_var, font=("Helvetica", 14), width=30, justify='center')
word_entry.pack(pady=5)

suggestion_box = tb.Combobox(root, font=("Helvetica", 11), state="readonly")
suggestion_box.bind("<<ComboboxSelected>>", fill_from_suggestion)
suggestion_box.place_forget()

btn_frame = tb.Frame(root)
btn_frame.pack(pady=10)

tb.Button(btn_frame, text="Search", command=search, bootstyle=PRIMARY).grid(row=0, column=0, padx=5)
tb.Button(btn_frame, text="Speak Word", command=speak_word).grid(row=0, column=1, padx=5)
tb.Button(btn_frame, text="Speak Meaning", command=speak_meaning).grid(row=0, column=2, padx=5)
tb.Button(btn_frame, text="Clear", command=clear, bootstyle=SECONDARY).grid(row=0, column=3, padx=5)
tb.Button(btn_frame, text="Exit", command=iexit, bootstyle=DANGER).grid(row=0, column=4, padx=5)

result_text = tb.Text(root, font=("Helvetica", 13), wrap='word', height=8, width=60, bd=2, relief='flat')
result_text.pack(pady=10)

root.bind('<Control-Return>', search)
root.bind('<Escape>', clear)
root.bind('<Control-q>', iexit)

word_entry.focus()
root.mainloop()
