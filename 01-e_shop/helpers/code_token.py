import random
import string

def generate_code_token(length=32):
    code_token = ''.join(random.choice(string.ascii_letters) for i in range(length))

    return code_token