import random

n = random.randint(1, 99)
min, max, count, guess_chances = 1, 99, 1, 5
player_name = input("Hello, What's your name? ")

print("Hello," + player_name)

while 1 <= guess_chances:
    num = int(input(f"Enter an integer from {min} to {max}: "))
    if num > n:
        if num > max:
            print("Your guess is out of range. Try guess something lower than", max)
        else:
            print("Your guess is too high. Try guess something lower than", num)
            max = num
    elif num < n:
        if num < min:
            print("Your guess is out of range. Try guess something higher than", min)
        else:
            print("Your guess is too low. Try guess something higher than", num)
            min = num
    else:
        print("You guessed it!")
        print("You took", str(count), "tries to guess the number")
        break
    guess_chances -= 1
    print("you have", str(guess_chances), "chances left")
    count += 1

if guess_chances == 0:
    print("Game Over")
    print("The number is", str(n))
    print("Thanks for playing")