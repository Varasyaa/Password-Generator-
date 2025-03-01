import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    char_set = ""
    if use_letters:
        char_set += string.ascii_letters
    if use_numbers:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation

    if not char_set:
        raise ValueError("No character types selected for password generation!")

    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        use_letters = var_letters.get()
        use_numbers = var_numbers.get()
        use_symbols = var_symbols.get()
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def on_copy():
    password = entry_result.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")

# Length input
label_length = tk.Label(root, text="Password Length:")
label_length.pack(padx=5, pady=5)

entry_length = tk.Entry(root)
entry_length.pack(padx=5, pady=5)

# Character set options
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

checkbox_letters = tk.Checkbutton(root, text="Include Letters", variable=var_letters)
checkbox_letters.pack(padx=5, pady=5)

checkbox_numbers = tk.Checkbutton(root, text="Include Numbers", variable=var_numbers)
checkbox_numbers.pack(padx=5, pady=5)

checkbox_symbols = tk.Checkbutton(root, text="Include Symbols", variable=var_symbols)
checkbox_symbols.pack(padx=5, pady=5)

# Generate button
btn_generate = tk.Button(root, text="Generate Password", command=on_generate)
btn_generate.pack(padx=5, pady=10)

# Result field
label_result = tk.Label(root, text="Generated Password:")
label_result.pack(padx=5, pady=5)

entry_result = tk.Entry(root)
entry_result.pack(padx=5, pady=5)

# Copy to clipboard button
btn_copy = tk.Button(root, text="Copy to Clipboard", command=on_copy)
btn_copy.pack(padx=5, pady=10)

root.mainloop()
