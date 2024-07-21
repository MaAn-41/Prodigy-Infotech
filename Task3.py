import tkinter as tk
from tkinter import ttk, messagebox

def check_password_strength(password):
    # Criteria checks
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+{}[]\\|:;\"'<>,.?/" for c in password)
    
    # Calculate score based on criteria
    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    
    # Determine strength level
    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score >= 2:
        return "Moderate"
    elif score >= 1:
        return "Weak"
    else:
        return "Very Weak"

def evaluate_password():
    password = entry_password.get()
    if len(password) < 8:
        messagebox.showwarning("Password Strength Checker", "Password should be at least 8 characters long.")
    else:
        strength = check_password_strength(password)
        messagebox.showinfo("Password Strength Checker", f"Your password strength is: {strength}")

# Create GUI window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)
root.configure(background="#f0f0f0")

# Create style for ttk widgets
style = ttk.Style()
style.configure("TLabel", background="#f0f0f0", font=("Times New Roman", 12))
style.configure("TButton", background="#4CAF50", font=(" Times New Roman", 12), foreground="Grey")
style.configure("TEntry", font=(" Times New Roman", 12))

# Create and place GUI elements
frame = ttk.Frame(root, padding=(20, 20))
frame.pack(fill=tk.BOTH, expand=True)

label_title = ttk.Label(frame, text="Password Strength Checker", style="TLabel")
label_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

label_prompt = ttk.Label(frame, text="Enter your password:", style="TLabel")
label_prompt.grid(row=1, column=0, pady=10, sticky=tk.W)

entry_password = ttk.Entry(frame, show="*", width=30)
entry_password.grid(row=1, column=1, padx=10, pady=10)

button_check = ttk.Button(frame, text="Check Password", command=evaluate_password, style="TButton")
button_check.grid(row=2, column=0, columnspan=2, pady=10)

# Function to handle Enter key press
def on_enter(event):
    evaluate_password()

# Bind Enter key to evaluate_password function
root.bind('<Return>', on_enter)

# Run the GUI application
root.mainloop()
