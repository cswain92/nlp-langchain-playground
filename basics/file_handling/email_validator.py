import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


if __name__ == "__main__":
    print(is_valid_email("test@example.com"))
    print(is_valid_email("invalid-email"))
