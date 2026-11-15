import random
r = random.randint(1,100)
take = 0
while True:
    take += 1
    n = int(input("Guess the number from 1 to 100 :- "))
    if n == r:
        print(f"Your number is correct. Your Takes {take}")
        break
    elif n > r:
        print("Your number is higher.")
    elif n < r:
        print("Your number is lower.")
