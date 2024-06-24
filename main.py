import tkinter as tk

root = tk.Tk()
root.title("Calculator")

root.geometry("300x450")
root.configure(bg='#2c3e50')

root.resizable(False, False)

entry = tk.Entry(root, width=16, font=('Arial', 30), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_clear():
    entry.delete(0, tk.END)

def create_button(text, row, column, command, rowspan=1, columnspan=1, bg='#ecf0f1', fg='#2c3e50'):
    button = tk.Button(root, text=text, padx=20, pady=20, command=command, bg=bg, fg=fg, font=('Arial', 14))
    button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew", padx=5, pady=5)
    return button

create_button("C", 1, 0, button_clear, bg='#e74c3c')
create_button("/", 1, 1, lambda: button_click('/'), bg='#f39c12')
create_button("*", 1, 2, lambda: button_click('*'), bg='#f39c12')
create_button("-", 1, 3, lambda: button_click('-'), bg='#f39c12')

create_button("7", 2, 0, lambda: button_click(7))
create_button("8", 2, 1, lambda: button_click(8))
create_button("9", 2, 2, lambda: button_click(9))
create_button("+", 2, 3, lambda: button_click("+"), bg='#f39c12', rowspan=2)

create_button("4", 3, 0, lambda: button_click(4))
create_button("5", 3, 1, lambda: button_click(5))
create_button("6", 3, 2, lambda: button_click(6))
create_button("=", 4, 3, button_equal, rowspan=2, bg='#27ae60')

create_button("1", 4, 0, lambda: button_click(1))
create_button("2", 4, 1, lambda: button_click(2))
create_button("3", 4, 2, lambda: button_click(3))

create_button("0", 5, 0, lambda: button_click(0), columnspan=2)
create_button(".", 5, 2, lambda: button_click('.'))

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

    

