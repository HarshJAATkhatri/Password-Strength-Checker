import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r'[A-Z]', password)
    lowercase_error = not re.search(r'[a-z]', password)
    digit_error = not re.search(r'\d', password)
    special_char_error = not re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Count how many criteria are met
    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    # Evaluate strength
    if score == 5:
        strength = "Very Strong 💪"
    elif score >= 4:
        strength = "Strong ✅"
    elif score >= 3:
        strength = "Moderate ⚠️"
    elif score >= 2:
        strength = "Weak ❗"
    else:
        strength = "Very Weak ❌"

    # Report
    result = {
        "Password": password,
        "Length >= 8": not length_error,
        "Has Uppercase": not uppercase_error,
        "Has Lowercase": not lowercase_error,
        "Has Digit": not digit_error,
        "Has Special Char": not special_char_error,
        "Score (0-5)": score,
        "Strength": strength
    }

    return result


# Example usage
if __name__ == "__main__":
    password = input("Enter your password to check: ")
    result = check_password_strength(password)
    print("\nPassword Strength Report:")
    for k, v in result.items():
        print(f"{k}: {v}")
