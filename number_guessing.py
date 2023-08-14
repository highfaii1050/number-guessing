import random

n = random.randint(1, 99)
count = 1
guess_chances = 5
player_name = input("Hello, What's your name? ")

print("Hello," + player_name)

while 1 <= guess_chances:
    num = int(input("Enter an integer from 1 to 99: "))
    if num > n:
        print("guess is too high. Try guess something lower than", num)
    elif num < n:
        print("guess is too low. Try guess something higher than", num)
    else:
        print("you guessed it!")
        print("you took ", str(count), " tries to guess the number")
        break
    guess_chances -= 1
    print("you have ", str(guess_chances), " chances left")
    count += 1

print("Game Over")
print("The number is ", str(n))
print("Thanks for playing")