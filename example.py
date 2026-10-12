import random 

number = random.randint(1, 100)
count = 0 

while True:
    guess = int(input("Enter your guess: "))
    count += 1

    if guess > number:
        print("Your guess is greater than the number.")
    elif guess < number:
        print("Your guess is lesser than the number.")
    else:
        print("you fount the correct answeer is",count, "🥳Correct!,Amasing")
