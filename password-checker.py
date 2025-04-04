import re

# Load common passwords
def load_common_passwords(filename="common_passwords.txt"):
    try:
        with open(filename, "r") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        print("Common password file not found! Skipping dictionary check.")
        return set()

# Check password strength
def check_password_strength(password, common_passwords):
    score = 0

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    # Complexity check
    if re.search(r"\d", password):  # Contains numbers
        score += 1
    if re.search(r"[A-Z]", password):  # Contains uppercase letters
        score += 1
    if re.search(r"[a-z]", password):  # Contains lowercase letters
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # Contains symbols
        score += 1

    # Common password check
    if password in common_passwords:
        return "❌ Very Weak (Common Password)"

    # Assign strength levels
    if score >= 6:
        return "✅ Strong"
    elif score >= 4:
        return "🟡 Moderate"
    else:
        return "⚠️ Weak"

# Run the checker
if __name__ == "__main__":
    common_passwords = load_common_passwords()
    user_password = input("Enter a password to check: ")
    result = check_password_strength(user_password, common_passwords)
    print("Password Strength:", result)
