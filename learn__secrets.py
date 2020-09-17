import secrets
import string


def generate_password(length=32):
    symbols = string.ascii_letters + string.digits
    return "".join(secrets.choice(symbols) for _ in range(length))


if __name__ == "__main__":
    print(generate_password())
