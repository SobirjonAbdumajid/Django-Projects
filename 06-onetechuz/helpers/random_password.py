import random
import string


def random_password(x):
    password = random.randint(10 ** (x - 1), (10 ** x) - 1)
    return password


def generate_code_token(length):
    password = ''.join(random.choice(string.ascii_letters) for i in range(length))

    return password