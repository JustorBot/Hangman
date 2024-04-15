import random

wordList = ["hi", "bye", "dumb", "poes", "bullshit", "simon", "hacker", "formula 1", "motogp", "naai", "bike", "scammer"]

pickedWord = wordList[random.randint(0, len(wordList)-1)]
print(pickedWord)

def guessing():
    guesses = 0
    while True:
        try:
            letter = input("Type a letter: ")
            if letter in pickedWord:
                guessed_letters = ["_" for _ in pickedWord]  
                guessed_letters[pickedWord.index(letter)] = letter  

                while "_" in guessed_letters: 
                    print(" ".join(guessed_letters))
                    guess = input("Guess a letter: ")

                    if guess in pickedWord and guess not in guessed_letters:  
                        for i, char in enumerate(pickedWord):
                            if char == guess:
                                guessed_letters[i] = guess
                    else:
                        print("Incorrect guess. Try again.")
                        guesses += 1
                        print("You have guessed: {}".format(guesses))
                        if guesses > 5:
                            print("Guesses greater than 5 so You lose!!")
                            main()

                print("Congratulations! You guessed the word:", pickedWord)
                break
        except:
            print("Try Again nothing entered")

def main():
    while True:
        try:
            choice = int(input("1 to play or 0 to exit: "))
            choicelist = [0, 1]
            if choice in choicelist and choice == 1:
                print("Welcome you have 5 Guesses to guess the word Selected at random!!!")
                guessing()
            elif choice in choicelist and choice == 0:
                print("Thanks for playing Dumb person!!")
                break
        except ValueError:
            print("Invalid enter either 1 or 0")
            
main()