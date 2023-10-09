"""Muhammad Talha"""
import tkinter as tk
import string
import random

def generate():
    try:
        # Get the password length from the input field
        plength = int(entry_box2.get())
    except ValueError:
        result_label.config(text="Invalid password length. Please enter a valid number.")
        return
    
    if plength <= 0:
        result_label.config(text="Password length must be greater than 0.")
        return
    
    if plength > 100:
        result_label.config(text="Password length is too long.")
        return

    ll = string.ascii_lowercase
    ul = string.ascii_uppercase
    dig = string.digits
    spec_char = string.punctuation
    characters = ll + ul + dig + spec_char

    if plength > len(characters):
        result_label.config(text=f"Password length exceeds available characters ({len(characters)} characters).")
        return

    password = ''.join(random.choice(characters) for _ in range(plength))
    entry_box3.delete(0, tk.END)
    entry_box3.insert(0, password)
    
def reset():
    entry_box1.delete(0, tk.END)
    entry_box2.delete(0, tk.END)
    entry_box3.delete(0, tk.END)

def accept():
    name = entry_box1.get()
    generated_password = entry_box3.get()
    
    result_label.config(text=f"Name: {name}\nGenerated Password: {generated_password}")

root = tk.Tk()
root.title("Password Generator")
root.geometry('600x400')

result_label = tk.Label(root, text="", font=("bold", 12))
result_label.pack()

txt = tk.Label(root, text="Password Generator", font=("bold", 25), fg="red", bg="#000000")
txt.pack()

frame = tk.Frame(root)
frame.pack()

t1 = tk.Label(frame, text="Enter your Name:", font=("bold", 15))
t1.grid(row=0, column=0, padx=10)
entry_box1 = tk.Entry(frame, text="", width=50)
entry_box1.grid(row=0, column=1, padx=10)

t2 = tk.Label(frame, text="Password Length:", font=("bold", 15))
t2.grid(row=1, column=0, padx=10)
entry_box2 = tk.Entry(frame, text="", width=50)
entry_box2.grid(row=1, column=1, padx=10)

t3 = tk.Label(frame, text="Generated Password:", font=("bold", 15))
t3.grid(row=2, column=0, padx=10)
entry_box3 = tk.Entry(frame, text="", width=50)
entry_box3.grid(row=2, column=1, padx=10)

frame = tk.Frame(root)
frame.pack()

bt1 = tk.Button(frame, text="Generate Password", font=("bold", 11), width=20, height=1, command=generate, relief="solid", bg="blue", fg="white")
bt1.grid(pady=10)

bt3 = tk.Button(frame, text="Accept", width=7, height=1, command=accept, relief="solid")
bt3.grid(pady=10)

bt2 = tk.Button(frame, text="Reset", width=7, height=1, command=reset, relief="solid")
bt2.grid(pady=10)

root.mainloop()
