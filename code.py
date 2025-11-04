import re
import tkinter as tk

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[@$!%*?&#^()_+\-=\[\]{};':\"\\|,.<>\/?]", password) is None

    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    if score == 5:
        strength = "Very Strong 💪"
        color = "green"
    elif score == 4:
        strength = "Strong ✅"
        color = "lime green"
    elif score == 3:
        strength = "Moderate ⚠"
        color = "orange"
    else:
        strength = "Weak ❌"
        color = "red"

    feedback = []
    if length_error:
        feedback.append("• At least 8 characters required.")
    if lowercase_error:
        feedback.append("• Add lowercase letters (a-z).")
    if uppercase_error:
        feedback.append("• Add uppercase letters (A-Z).")
    if digit_error:
        feedback.append("• Add at least one digit (0-9).")
    if special_char_error:
        feedback.append("• Add special characters (@, #, $, etc).")

    return strength, color, feedback


def evaluate_password():
    password = entry.get()
    strength, color, feedback = check_password_strength(password)

    result_label.config(text=f"Strength: {strength}", fg=color)
    if feedback:
        feedback_text = "\n".join(feedback)
        feedback_label.config(text=f"Suggestions:\n{feedback_text}", fg="white", justify="left")
    else:
        feedback_label.config(text="All good! ✅", fg="white")


root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("400x300")
root.config(bg="#1e1e1e")

title_label = tk.Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold"), bg="#1e1e1e", fg="cyan")
title_label.pack(pady=15)

entry_label = tk.Label(root, text="Enter Password:", bg="#1e1e1e", fg="white")
entry_label.pack()

# Password visible while typing
entry = tk.Entry(root, width=30, font=("Helvetica", 12))
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Strength", command=evaluate_password, bg="cyan", fg="black", font=("Helvetica", 10, "bold"))
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#1e1e1e")
result_label.pack(pady=5)

feedback_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#1e1e1e", justify="left")
feedback_label.pack(pady=5)

root.mainloop()
