#  Project '4' : "Random password generation"

import random
from string import ascii_letters,ascii_lowercase,digits,punctuation

symbols = ascii_letters+ascii_lowercase+digits+punctuation

secure_password = random.SystemRandom()
password = ''.join(secure_password.choice(symbols)   for pswd in range(12))
print(password)
