import random
import string

random_string = string.ascii_letters + string.digits + string.ascii_uppercase
key = "".join(random.choice(random_string) for i in range(12))

SECRET_KEY = "setsecret"