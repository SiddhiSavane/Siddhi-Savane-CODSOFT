import tkinter as tk

def click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

display = tk.Entry(root, font=("Arial", 22), justify="right")
display.pack(fill="both", padx=10, pady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for btn in buttons:
    action = lambda x=btn: click(x) if x != "=" else calculate()
    tk.Button(frame, text=btn, width=6, height=3, font=("Arial", 14),
              command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 4:
        col = 0
        row += 1

tk.Button(root, text="Clear", width=25, height=2, command=clear).pack(pady=10)

root.mainloop()
