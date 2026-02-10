import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordEngine:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+=-{}[]<>?/"

    def generate_password(self, length, use_upper, use_digits, use_symbols):
        if length < 4:
            return None

        characters = self.lowercase

        if use_upper:
            characters += self.uppercase
        if use_digits:
            characters += self.digits
        if use_symbols:
            characters += self.symbols

        if not characters:
            return None

        password = ""
        for _ in range(length):
            password += random.choice(characters)

        return password



class PasswordGeneratorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Advanced Password Generator")
        self.root.geometry("450x450")
        self.root.resizable(False, False)

        self.engine = PasswordEngine()

        self.title_label = tk.Label(
            self.root,
            text="Password Generator",
            font=("Arial", 18, "bold")
        )
        self.title_label.pack(pady=15)

        self.length_label = tk.Label(self.root, text="Enter Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(self.root, width=10, justify="center")
        self.length_entry.pack(pady=5)

        self.upper_var = tk.IntVar()
        self.digit_var = tk.IntVar()
        self.symbol_var = tk.IntVar()

        self.upper_check = tk.Checkbutton(
            self.root, text="Include Uppercase Letters", variable=self.upper_var
        )
        self.upper_check.pack()

        self.digit_check = tk.Checkbutton(
            self.root, text="Include Numbers", variable=self.digit_var
        )
        self.digit_check.pack()

        self.symbol_check = tk.Checkbutton(
            self.root, text="Include Symbols", variable=self.symbol_var
        )
        self.symbol_check.pack()

        self.generate_button = tk.Button(
            self.root, text="Generate Password", width=20, command=self.generate
        )
        self.generate_button.pack(pady=15)

        self.result_entry = tk.Entry(
            self.root, width=35, justify="center", font=("Arial", 12)
        )
        self.result_entry.pack(pady=10)

        self.copy_button = tk.Button(
            self.root, text="Copy to Clipboard", command=self.copy_password
        )
        self.copy_button.pack(pady=5)

        self.clear_button = tk.Button(
            self.root, text="Clear", command=self.clear_all
        )
        self.clear_button.pack(pady=5)

        self.footer = tk.Label(
            self.root,
            text="CODSOFT Python Internship - Task 3",
            font=("Arial", 9)
        )
        self.footer.pack(side="bottom", pady=10)

    def generate(self):
        try:
            length = int(self.length_entry.get())
        except:
            messagebox.showerror("Error", "Please enter a valid number")
            return

        password = self.engine.generate_password(
            length,
            self.upper_var.get(),
            self.digit_var.get(),
            self.symbol_var.get()
        )

        if password is None:
            messagebox.showerror(
                "Error", "Password length must be at least 4"
            )
            return

        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, password)

    def copy_password(self):
        pwd = self.result_entry.get()
        if pwd == "":
            messagebox.showwarning("Warning", "No password to copy")
        else:
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

    def clear_all(self):
        self.length_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)
        self.upper_var.set(0)
        self.digit_var.set(0)
        self.symbol_var.set(0)

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.root.mainloop()
