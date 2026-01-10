#Imports the random library
import random

print("Welcome to the Number Guessing Game!")
print("I thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.")

#Receive the attempt number
choiceDifficulty = int(input("""Please select the difficulty level: 
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice: """))

#Generate the random number
randomNumber = random.randint(1,100)

attempts = 0

match choiceDifficulty:
#Executes a specific block according to the selected option.
    case 1:
        print("Great! You have selected de easy difficulty level")
        print("Let's start the game!")

        for i in range(10):
            
            choiceNumber = int(input("Enter your guess: "))
            attempts += 1

            if choiceNumber == randomNumber:
                print("Congratulations! You guessed the correct number in {} attempts".format(attempts))
            else:
                meter = "less" if choiceNumber > randomNumber else "greater"
                print("Incorret! The number is {} than {}".format(meter,choiceNumber))
        else:
            print("Your attempts are over!")
    case 2:
        print("Great! You have selected de medium difficulty level")
        print("Let's start the game!")

        for i in range(5):
            
            choiceNumber = int(input("Enter your guess: "))
            attempts += 1

            if choiceNumber == randomNumber:
                print("Congratulations! You guessed the correct number in {} attempts".format(attempts))
            else:
                meter = "less" if choiceNumber > randomNumber else "greater"
                print("Incorret! The number is {} than {}".format(meter,choiceNumber))
        else:
            print("Your attempts are over!")
    case 3:
        print("Great! You have selected de hard difficulty level")
        print("Let's start the game!")

        for i in range(3):
            
            choiceNumber = int(input("Enter your guess: "))
            attempts += 1

            if choiceNumber == randomNumber:
                print("Congratulations! You guessed the correct number in {} attempts".format(attempts))
            else:
                meter = "less" if choiceNumber > randomNumber else "greater"
                print("Incorret! The number is {} than {}".format(meter,choiceNumber))
        else:
            print("Your attempts are over!")
    case _:
        print("Invalid option!")
