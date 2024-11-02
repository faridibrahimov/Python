import random

def gen_pass(pass_length):
    elements = "()+-/*!&$#?=@<>123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
print(gen_pass(14))