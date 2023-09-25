import random
import string

def generate_strong_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)
        ):
            return password

password_length = int(input("Enter the length of the strong password: "))
strong_password = generate_strong_password(password_length)
print("Generated Strong Password: ", strong_password)
