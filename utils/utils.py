import random
import string


def generate_code(num: int = 6):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num))
