import tkinter as tk
from tkinter import messagebox

def click_me():
    messagebox.showinfo("Info", "Button Clicked!")
def submit_text():
    texto = entry.get()
    messagebox.showinfo("Submitted Text", f"Você digitou: {texto}")
def select_option():
    selected = listbox.get(tk.ACTIVE)
    messagebox.showinfo("Selected", f"Você selecionou: {selected}")
root = tk.Tk()
root.title("tk")
root.geometry("250x400")
# Label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=(10,5))
# Button "Click Me"
btn_click = tk.Button(root, text="Click Me", command=click_me)
btn_click.pack(pady=5)
# Entry e botão Submit
entry = tk.Entry(root, width=20)
entry.pack(pady=(15,5))
btn_submit = tk.Button(root, text="Submit", command=submit_text)
btn_submit.pack(pady=5)
# Checkbox
check_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Check Me", variable=check_var)
checkbox.pack(pady=10)
# Radio Buttons
radio_var = tk.IntVar(value=2)
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value=1)
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value=2)
radio1.pack()
radio2.pack()
# Listbox
listbox = tk.Listbox(root, height=6)
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.insert(3, "Option 3")
listbox.pack(pady=10)

btn_select = tk.Button(root, text="Select", command=select_option)
btn_select.pack()

root.mainloop()
