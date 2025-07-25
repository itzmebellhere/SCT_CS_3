def check_password_strength(password):
    length = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    score = sum([length, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

# Main program
print("=== Password Strength Checker ===")
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password Strength:", strength)
