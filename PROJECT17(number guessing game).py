import random

a = random.choice([i for i in range(10)])
tries =0

while True:
    guess = int(input("Enter the number within range 10"))
    tries+=1
    if guess > a:
        print("Its smaller")

    elif guess < a:
        print("its bigger")

    elif guess == a:
        print(f"You got it!, tries = {tries}")
        break


    else:
        print("Enter within Range")