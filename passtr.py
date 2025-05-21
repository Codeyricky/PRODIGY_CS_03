import tkinter as tk
import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[\W_]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = errors.count(False)

    if score == 5:
        return "Strong ", "green"
    elif score >= 3:
        return "Moderate ", "orange"
    else:
        return "Weak ", "red"

def on_check():
    password = entry.get()
    strength, color = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}", fg=color)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=30, show="*")
entry.pack()

check_btn = tk.Button(root, text="Check Strength", command=on_check)
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
