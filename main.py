import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog

import sys
import webbrowser

window = tk.Tk()
window.geometry('400x300')
window.title("Notepad Deluxe")
window.resizable(0,0)

def about_app():
    messagebox.showinfo("Notepad Deluxe", "Notepad Deluxe, Est. August 2025. Notepad Deluxe is an open-source version of Notepad made in Python with more features. Notepad Deluxe is made off of Notepad Lite, a repository on GitHub made by Mancol001.")

textZone = tk.Text(master=window)
menu_up = Menu(window)
menuButton = Menu(menu_up, tearoff=0)
menuFileButton = Menu(menu_up, tearoff=0)

menuButton.add_command(label="Exit", command=sys.exit)
menuButton.add_command(label="About", command=about_app)
menuButton.add_command(label="Creator's GitHub", command=lambda: webbrowser.open("https://github.com/Moomerator46"))
menuButton.add_command(label="Notepad Lite's Creator Github", command=lambda: webbrowser.open("https://www.github.com/Mancol001/"))

def save_as_func():
    text_inputed = textZone.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files (.txt)", "*.txt"), ("Markdown (.md)", "*.md"), ("Python Programming Language (.py)", "*.py"), ("Hypertext Markup Language (.html)", "*.html"), ("Cascading Style Sheet (.css)", "*.css"), ("Javascript Programming Language (.js)", "*.js"), ("Hypertext Preprocessor (.php)", "*.php"), ("Structured Query Language (.sql)", "*.sql"), ("Typescript Programming Language (.ts)", "*.ts"), ("Hypertext Application (.hta)", "*.hta"), ("INPOS Addfirun Application (.inpaa)", "*.inpaa"), ("MoreApps INPOS Mod (.mam)", "*.mam"), ("All Files", "*.*")])

    with open(file_path, "w") as file:
        file.write(text_inputed)
        print("Notepad Framework: File has been saved")
        messagebox.showinfo("Notepad Deluxe")

def open_file_func():
    text_inputed = textZone.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files (.txt)", "*.txt"), ("Markdown (.md)", "*.md"), ("Python Programming Language (.py)", "*.py"), ("Hypertext Markup Language (.html)", "*.html"), ("Cascading Style Sheet (.css)", "*.css"), ("Javascript Programming Language (.js)", "*.js"), ("Hypertext Preprocessor (.php)", "*.php"), ("Structured Query Language (.sql)", "*.sql"), ("Typescript Programming Language (.ts)", "*.ts"), ("Hypertext Application (.hta)", "*.hta"), ("INPOS Addfirun Application (.inpaa)", "*.inpaa"), ("MoreApps INPOS Mod (.mam)", "*.mam"), ("All Files", "*.*")])

    with open(file_path, "r") as file:
        text_cont = file.read()
        textZone.delete("1.0", tk.END)
        textZone.insert(tk.END, text_cont)

def save_open_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files (.txt)", "*.txt"), ("Markdown (.md)", "*.md"), ("Python Programming Language (.py)", "*.py"), ("Hypertext Markup Language (.html)", "*.html"), ("Cascading Style Sheet (.css)", "*.css"), ("Javascript Programming Language (.js)", "*.js"), ("Hypertext Preprocessor (.php)", "*.php"), ("Structured Query Language (.sql)", "*.sql"), ("Typescript Programming Language (.ts)", "*.ts"), ("Hypertext Application (.hta)", "*.hta"), ("INPOS Addfirun Application (.inpaa)", "*.inpaa"), ("MoreApps INPOS Mod (.mam)", "*.mam"), ("All Files", "*.*")])

    if file_path:
        with open(file_path, "w") as file:
            target_text = textZone.get("1.0", tk.END)
            file.write(target_text)
            messagebox.showinfo("Notepad Deluxe", "Notepad Framework: File has been saved")

menuFileButton.add_command(label="Save As", command=save_as_func)
menuFileButton.add_command(label="Save", command=save_open_file)

menuFileButton.add_command(label="Open", command=open_file_func)

menu_up.add_cascade(label="Menu", menu=menuButton)
menu_up.add_cascade(label="File", menu=menuFileButton)

textZone.pack()

window.config(menu=menu_up)
window.mainloop()