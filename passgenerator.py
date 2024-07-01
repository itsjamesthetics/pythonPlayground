import string
import random

def generate_password(length):
    if length < 4:  # ensure the password is long enough to include all types
        raise ValueError("Password length must be at least 4 characters.")

    # Combine all letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password includes at least one of each character type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random characters
    password += [random.choice(characters) for _ in range(length - 4)]

    # Shuffle to avoid predictable sequences
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

# Example usage
password_length = 12  # Specify the desired length
password = generate_password(password_length)
print(f"Generated password: {password}")
