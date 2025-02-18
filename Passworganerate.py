import random
import string

def generate_password(length):
    if length < 6 or length > 32:
        print("Довжина пароля повинна бути від 6 до 32 символів.")
        return None

    all_characters = string.ascii_letters + string.digits + "!@#$%^&*()-_+="
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()-_+=")
    ]

    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

def main():
    length = int(input("Введіть довжину пароля (6-32): "))
    password = generate_password(length)
    if password:
        print("Ваш пароль:", password)

if __name__ == "__main__":
    main()