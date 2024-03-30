import random
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnñopqrstuvwxyz"
cap = minus.upper()
num = "0123456789"
sym = "@!()[]*#"
base = minus+cap+num+sym 
leng = 12

sample = random.sample(base, leng)
password = "".join(sample)
encrypted_password = generate_password_hash(password)
print(password, encrypted_password)