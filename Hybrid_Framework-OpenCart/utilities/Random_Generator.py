import random
import string


def random_fname_generator(size=6, chars=string.ascii_uppercase+string.ascii_lowercase):
    return  ''.join(random.choice(chars) for x in range(size))
def random_lname_generator(size=6, chars=string.ascii_uppercase+string.ascii_lowercase):
    return  ''.join(random.choice(chars) for x in range(size))
def random_email_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return  ''.join(random.choice(chars) for x in range(size))