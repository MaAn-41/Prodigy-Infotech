import re

def check_password_strength(password):
    # Criteria checks
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+{}[]\\|:;\"'<>,.?/" for c in password)
    
    # Calculate score based on criteria
    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    
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

def get_password_from_user():
    while True:
        password = input("Enter your password (at least 8 characters): ")
        if len(password) < 8:
            print("Password should be at least 8 characters long. Try again.")
        else:
            return password

def main():
    print("\nWelcome to Password Strength Checker!\n")
    
    password = get_password_from_user()
    strength = check_password_strength(password)
    
    print(f"\nYour password strength is: {strength}")

if __name__ == "__main__":
    main()
