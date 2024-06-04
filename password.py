import random
import tkinter as tk
from tkinter import font, IntVar, StringVar

def generate_password():
    en = int(entry1.get())
    allowed_chars = ""
    if option_lower.get():
        allowed_chars += "abcdefghijklmnopqrstuvwxyz"
    if option_upper.get():
        allowed_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if option_digits.get():
        allowed_chars += "0123456789"
    if option_special.get():
        allowed_chars += "!@#$%^&*()"

    if allowed_chars:
        password = ''.join(random.choice(allowed_chars) for i in range(en))
        pass_ent.delete(0, tk.END)
        pass_ent.insert(tk.END, password)
    else:
        pass_ent.delete(0, tk.END)
        pass_ent.insert(tk.END, "Please select at least one character type")
def reset():
    user_entry.delete(0, tk.END)
    entry1.delete(0, tk.END)
    pass_ent.delete(0, tk.END)
    option_lower.set(0)
    option_upper.set(0)
    option_digits.set(0)
    option_special.set(0)

window = tk.Tk()
window.title("Password Generator")
p = tk.Label(window, text="Password Generator", fg="blue", font=("Arial", 12, "bold"))
custom_font = font.Font(p, p.cget("font"))
custom_font.configure(underline=True, size=10)
p.configure(font=custom_font)
p.grid(row=0, column=1)

user_name = tk.Label(window, text="Enter user name:")
user_entry = tk.Entry(window)
user_name.grid(row=4, column=0, padx=10, pady=5)
user_entry.grid(row=4, column=1)

pass_len = tk.Label(window, text="Password length:")
entry1 = tk.Entry(window)
pass_len.grid(row=5, column=0, padx=10, pady=5)
entry1.grid(row=5, column=1)

l=tk.Label(window,text="Type of character for password")
l.grid(row=6,column=1,padx=10,pady=5)

option_lower = IntVar()
option_upper = IntVar()
option_digits = IntVar()
option_special = IntVar()

lowercase_check = tk.Checkbutton(window, text="Lowercase", variable=option_lower)
uppercase_check = tk.Checkbutton(window, text="Uppercase", variable=option_upper)
digits_check = tk.Checkbutton(window, text="Digits", variable=option_digits)
special_check = tk.Checkbutton(window, text="Special Characters", variable=option_special)

lowercase_check.grid(row=7, column=1, sticky="w")
uppercase_check.grid(row=8, column=1, sticky="w")
digits_check.grid(row=9, column=1, sticky="w")
special_check.grid(row=10, column=1, sticky="w")

pass_label = tk.Label(window, text="Generated Password:")
pass_ent = tk.Entry(window)
pass_label.grid(row=11, column=0, padx=10, pady=5)
pass_ent.grid(row=11, column=1)

gen_pass = tk.Button(window, text="Generate", fg="white", bg="blue", command=generate_password)
gen_pass.grid(row=12, column=1, sticky="nsew", padx=14, pady=6)



reset = tk.Button(window, text="Reset", command=reset)
reset.grid(row=13, column=1, sticky="nsew", padx=18, pady=6)

window.mainloop()