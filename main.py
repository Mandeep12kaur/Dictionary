from tkinter import *
from tkinter import messagebox
import pyttsx3
from dict_logic import Dictionary

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

dictionary = Dictionary()

def search():
    word = word_entry.get()
    meanings, word, suggestion = dictionary.get_meaning(word)
    result_text.delete(1.0, END)

    if meanings:
        for meaning in meanings:
            result_text.insert(END, f'• {meaning}\n\n')
    elif suggestion:
        if messagebox.askyesno('Did You Mean?', f'Did you mean "{suggestion}"?'):
            word_entry.delete(0, END)
            word_entry.insert(END, suggestion)
            search()
        else:
            messagebox.showerror('Not Found', 'Word not found. Try again.')
    else:
        messagebox.showerror('Not Found', 'Word not found. Try again.')

def clear():
    word_entry.delete(0, END)
    result_text.delete(1.0, END)

def iexit():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()

def speak_word():
    engine.say(word_entry.get())
    engine.runAndWait()

def speak_meaning():
    engine.say(result_text.get(1.0, END))
    engine.runAndWait()

root = Tk()
root.title("Talking Dictionary")
root.geometry("700x500")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

Label(root, text="Talking Dictionary", font=("Helvetica", 28, "bold"), bg="#f4f4f4", fg="#333").pack(pady=20)

Label(root, text="Enter Word", font=("Helvetica", 16), bg="#f4f4f4").pack()
word_entry = Entry(root, font=("Helvetica", 16), width=30, bd=2, relief=FLAT, justify=CENTER)
word_entry.pack(pady=10)

btn_frame = Frame(root, bg="#f4f4f4")
btn_frame.pack(pady=10)

Button(btn_frame, text="🔍 Search", font=("Helvetica", 12), command=search, width=10).grid(row=0, column=0, padx=5)
Button(btn_frame, text="🔊 Word", font=("Helvetica", 12), command=speak_word, width=10).grid(row=0, column=1, padx=5)
Button(btn_frame, text="🔈 Meaning", font=("Helvetica", 12), command=speak_meaning, width=12).grid(row=0, column=2, padx=5)
Button(btn_frame, text="🧹 Clear", font=("Helvetica", 12), command=clear, width=10).grid(row=0, column=3, padx=5)
Button(btn_frame, text="❌ Exit", font=("Helvetica", 12), command=iexit, width=10).grid(row=0, column=4, padx=5)

Label(root, text="Meaning", font=("Helvetica", 16), bg="#f4f4f4").pack(pady=(20, 5))
result_text = Text(root, font=("Helvetica", 14), height=8, width=60, bd=2, relief=FLAT, wrap=WORD)
result_text.pack()

root.bind('<Return>', lambda event: search())

root.mainloop()
