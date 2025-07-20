TrustVault is a modern, regex-powered password strength checker that helps you evaluate and improve your passwords. It provides clear feedback on password strength and suggests ways to strengthen weak or moderate passwords. Plus, it can generate strong, secure password recommendations for you!

Features
Regex-based password strength evaluation

Categorizes passwords as Weak, Moderate, or Strong

Provides actionable recommendations for improvement

Suggests strong password generation on demand

Easy command-line interface

Installation
Simply clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/0xTorque/trustvault.git
cd trustvault
Make sure you have Python installed (version 3.6+ recommended). No additional dependencies needed.

Usage
Run the script in your terminal:

bash
Copy
Edit
python trustvault.py
You will be prompted to enter a password. The program will then:

Display the strength of your password

Give recommendations if it’s weak or moderate

Offer to generate a strong password suggestion

How It Works
The password strength is checked by matching regex patterns for:

Minimum length (8 characters)

Uppercase letters

Lowercase letters

Digits

Special characters (!@#$%^&*()_+=-)

Based on these checks, it scores your password and provides feedback.

Example
sql
Copy
Edit
Enter your password: MyPass123
Password Strength: ⚠️ Moderate
Recommendations to improve your password:
- Add at least one special character (!@#$%^&*()_+=-).
Would you like a strong password suggestion? (y/n): y
Suggested strong password: Pw9$Ab2@TqZ
Contributing
Contributions are welcome! Feel free to fork, submit issues, or send pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.
