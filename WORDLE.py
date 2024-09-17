import random

def load_words(file_path):
    with open(file_path, "r") as file:
        words = file.read().split()
    return words

def check_place(guess, wordle):
    feedback = []
    for i in range(5):
        if guess[i] == wordle[i]:
            feedback.append(f"{i+1}. letter - {guess[i].upper()}: RIGHT place")
        elif guess[i] in wordle:
            feedback.append(f"{i+1}. letter - {guess[i].upper()}: WRONG place.")
    return feedback

def get_valid_guess():
    while True:
        guess = input("Guess the word!: ").upper()
        if len(guess) != 5:
            print("That was not a five letter word!")
        else:
            return guess

def main():
    words = load_words("possible_words.txt")
    wordle = random.choice(words)
    attempts = 0
    
    while attempts < 6:  
        guess = get_valid_guess()
        attempts += 1
        
        if guess == wordle:
            print("You won!")
            break
        
        feedback = check_place(guess, wordle)
        for line in feedback:
            print(line)
        
    if guess != wordle:
        print("You lost!")
        print(f"The answer was: {wordle}")
        print("Try again next time!")

if __name__ == "__main__":
    main()
