import random


def get_random_word():
    words = ["python", "pakistan", "programming", "hangman", "challenge"]
    return random.choice(words)


# Get a random word for the game
word = get_random_word()

print("Welcome to Hangman Game!")
print("enter the 1 for easy level")
print("enter the 2 for medium level")
print("enter the 3 for hard level")
level = int(input("enter your choice(1-3): "))

if level == 1:
    attempts = 6
    print("you have 6 attempts to guess the word")
elif level == 2:
    attempts = 4
    print("you have 4 attempts to guess the word")
elif level == 3:
    attempts = 2
    print("you have 2 attempts to guess the word")
else:
    attempts = 6
    print("invalid choice, defaulting to 6 attempts")

guessed_letters = []

while attempts > 0:
    # Display the word with revealed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Attempts remaining:", attempts)

    # Check if player won
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ")

    if guess in guessed_letters:
        print("You already guessed that letter!")
    elif guess in word:
        print("Correct guess!")
        guessed_letters.append(guess)
    else:
        print("Oops! Wrong guess, please try again")
        attempts -= 1

# Check if player lost
if attempts == 0:
    print("Sorry, you ran out of attempts. The word was:", word)



          







    

