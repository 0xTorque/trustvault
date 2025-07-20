import re
import random
import string

print("Hello, Welcome to TrustVault!")  


def check_password_strength(password):
    score = 0
    recommendations = []

    if len(password) >= 8:
        score += 1
    else:
        recommendations.append("Make the password longer (at least 8 characters).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        recommendations.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        recommendations.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        recommendations.append("Add at least one digit.")

    if re.search(r"[!@#$%^&*()_+=-]", password):
        score += 1
    else:
        recommendations.append("Add at least one special character (!@#$%^&*()_+=-).")

    if score <= 2:
        strength = "❌ Weak"
    elif score <= 4:
        strength = "⚠️ Moderate"
    else:
        strength = "✅ Strong"

    return strength, recommendations


def recommend_password(length=12):
    if length < 8:
        length = 8  # Enforce minimum length

    # One character from each category
    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()_+=-"),
    ]

    # Fill the rest with random choices from all allowed chars
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+=-"
    password_chars += random.choices(all_chars, k=length - 4)

    random.shuffle(password_chars)
    return ''.join(password_chars)


# --- CLI Interface ---
password = input("Enter your password: ")
strength, recs = check_password_strength(password)
print("Password Strength:", strength)

if recs:
    print("Recommendations to improve your password:")
    for r in recs:
        print(f"- {r}")

    want_suggestion = input("Would you like a strong password suggestion? (y/n): ").lower()
    if want_suggestion == 'y':
        print("Suggested strong password:", recommend_password())
