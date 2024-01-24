import random

passWord = "!#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
passwordLen = int(input("Please enter the length of the password: "))
x = "".join(random.sample(passWord,passwordLen))
print(f"Your new generated password is {x}")


