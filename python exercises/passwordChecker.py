# Password Strength Checker

# Ask the user for a password.
# Check if it contains:

# At least 8 characters

# At least one number

# At least one uppercase letter

# At least one lowercase letter

# Tell the user if it is Strong, Medium, or Weak

def password_check(password):
    if len(password) > 8:
        print("Weak password, add a number ,an uppercase")
    