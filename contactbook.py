import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

contacts = load_contacts()

root = tk.Tk()
root.title("Contact Book")
root.geometry("650x500")
root.resizable(False, False)

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()


def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")

def refresh_list():
    listbox.delete(0, tk.END)
    for c in contacts:
        listbox.insert(tk.END, f"{c['name']} - {c['phone']}")

def add_contact():
    if name_var.get() == "" or phone_var.get() == "":
        messagebox.showerror("Error", "Name and Phone are required")
        return

    contact = {
        "name": name_var.get(),
        "phone": phone_var.get(),
        "email": email_var.get(),
        "address": address_var.get()
    }
    contacts.append(contact)
    save_contacts()
    refresh_list()
    clear_fields()
    messagebox.showinfo("Success", "Contact added successfully!")

def select_contact(event):
    try:
        index = listbox.curselection()[0]
        selected = contacts[index]

        name_var.set(selected["name"])
        phone_var.set(selected["phone"])
        email_var.set(selected["email"])
        address_var.set(selected["address"])
    except:
        pass

def update_contact():
    try:
        index = listbox.curselection()[0]
        contacts[index]["name"] = name_var.get()
        contacts[index]["phone"] = phone_var.get()
        contacts[index]["email"] = email_var.get()
        contacts[index]["address"] = address_var.get()
        save_contacts()
        refresh_list()
        clear_fields()
        messagebox.showinfo("Updated", "Contact updated successfully!")
    except:
        messagebox.showerror("Error", "Select a contact to update")

def delete_contact():
    try:
        index = listbox.curselection()[0]
        del contacts[index]
        save_contacts()
        refresh_list()
        clear_fields()
        messagebox.showinfo("Deleted", "Contact deleted successfully!")
    except:
        messagebox.showerror("Error", "Select a contact to delete")

def search_contact():
    keyword = search_var.get().lower()
    listbox.delete(0, tk.END)
    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            listbox.insert(tk.END, f"{c['name']} - {c['phone']}")

title = tk.Label(root, text="CONTACT BOOK", font=("Arial", 20, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(frame, textvariable=name_var, width=30).grid(row=0, column=1)

tk.Label(frame, text="Phone").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(frame, textvariable=phone_var, width=30).grid(row=1, column=1)

tk.Label(frame, text="Email").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(frame, textvariable=email_var, width=30).grid(row=2, column=1)

tk.Label(frame, text="Address").grid(row=3, column=0, padx=10, pady=5)
tk.Entry(frame, textvariable=address_var, width=30).grid(row=3, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=12, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=12, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=12, command=delete_contact).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Clear", width=12, command=clear_fields).grid(row=0, column=3, padx=5)

search_frame = tk.Frame(root)
search_frame.pack(pady=5)

tk.Entry(search_frame, textvariable=search_var, width=30).grid(row=0, column=0)
tk.Button(search_frame, text="Search", command=search_contact).grid(row=0, column=1, padx=5)
tk.Button(search_frame, text="Show All", command=refresh_list).grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", select_contact)

refresh_list()
root.mainloop()
