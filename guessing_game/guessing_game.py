from random import randint

play = True

while play:

    number = randint(0, 10)
    guess = int(input("Enter a number between 1 and 10:"))

    if guess == number:
        print "You guessed right!"
        answer = raw_input("Play again? (y/n)")
        if answer == "n":
            break
        elif answer == "y":
            play = True
        elif answer != "y" or answer != "n":
            print "Wrong input, try again."
            play = True
    else:
        print("Wrong guess")
        answer = raw_input("Play again? (y/n)")
        if answer == "n":
            break
        elif answer == "y":
            play = True
        elif answer != "y" or answer != "n":
            print "Wrong input, try again."
            play = True
        