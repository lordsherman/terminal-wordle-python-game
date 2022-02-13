import random
import sty

gameOver = False
max_guesses = 6

def getWord():
    global game_word
    global word_list
    # Generates a list of words from the text file.
    words = []
    with open("mediumwords.txt", "r") as f:
        lines = f.readlines()
        for word in lines:
            words.append(word.strip())
    # Alter list to only use 5 character words.
    word_list = []
    for word in words:
        if len(word) == 5:
            word_list.append(word)
        else:
            continue
    game_word = random.choice(word_list)
getWord()

# Process the users guess based on common wordle logic
def processGuess(guess):
    global gameOver
    global max_guesses

    game_word_list = list(game_word)
    guess_list = list(guess)

    for i in range(len(game_word_list)):
        for x in guess_list[i]:
            if x == game_word_list[i]:
                print("Correct Letter Correct Place: " + x)
                break
            elif x in game_word_list:
                if x not in game_word_list[i]:
                    print("Correct Letter Wrong Place: " + x)
                    break
            else:
                print("Incorrect Letter: " + x)
                break

    if len(guess) != 5 and guess not in word_list:
        # Guess must be a five letter word and not gibberish.
        print("Please enter a valid guess. (5 letters only)")
    elif guess != game_word and max_guesses != 0:
        max_guesses -= 1
        if max_guesses == 0:
            print("You have ran out of guesses! You lose :(\nThe Correct word was: " + game_word)
            gameOver = True
        else:
            print("That is not correct, try again")
    elif guess == game_word:
        print("You guessed the word! You win!")
        gameOver = True

# Main Game Loop
while gameOver == False and max_guesses > 0:
    guess = input("Make a guess: ")
    processGuess(guess)
