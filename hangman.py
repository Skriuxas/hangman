import random
# Settings
failed_attempts = 0
tried_letters = []
print("Hello there. This is Hangman game.")
print("You have maximum of 7 tries to guess the word.")
while True:
    print("What theme do you want to play?")
    try:
        words_file_input = input("--> ")
    except(KeyboardInterrupt):
        print("\nThanks for playing!")
        break
    words_file = "themes/" + words_file_input + ".txt"
    try:
        words_file = open(words_file)
    except:
        print("You've entered wrong file name, please try again.")
        continue
    wordlist = words_file.read().split()
    secret_word = wordlist[random.randint(0, len(wordlist) - 1)]
    secret_word = secret_word.replace(",", "").lower().replace(".","")
    guessed = [""] * len(secret_word)
    while True:
        if failed_attempts < 7:
            guessed_str = ''.join(guessed)
            count_loop = 0
            print(guessed_str)
            print("So far you've tried " + str(tried_letters))
            if failed_attempts == 1:
                print('''
 +---+
 |   |
     |        
     |
     |
     |
    ''')
            elif failed_attempts == 2:
                print('''
 +---+
 |   |
 O   |        
     |
     |
     |
    ''')
            elif failed_attempts == 3:
                print('''
 +---+
 |   |
 O   |        
 |   |
     |
     |
    ''')
            elif failed_attempts == 4:
                print('''
 +---+
 |   |
 O   |        
/|   |
     |
     |
    ''')
            elif failed_attempts == 5:
                print('''
 +---+
 |   |
 O   |        
/|\  |
     |
     |
    ''')
            elif failed_attempts == 6:
                print('''
 +---+
 |   |
 O   |        
/|\  |
/    |
     |
    ''')
            if secret_word == guessed_str:
                print("\nYou won!")
                break
            try:
                guess = input("--> ").lower()
            except(KeyboardInterrupt):
                break
            if len(guess) > 1:
                print("You've listed a word, but not a character.")
                continue
            if guess == "" or guess == " ":
                print("You've entered nothing.")
                continue
            if guess in secret_word:
                if guess not in tried_letters:
                    tried_letters.append(guess)
                    for char in secret_word:
                        if guess == char:
                            guessed[count_loop] = guess
                        else:
                            if guessed[count_loop] == "":
                                guessed[count_loop] = "_"
                        count_loop += 1
                        if count_loop >= len(secret_word):
                            count_loop = 0
                else:
                    print("You've already guessed this letter.")
                    continue
            else:
                if guess not in tried_letters:
                    print("You've guessed wrong")
                    failed_attempts+= 1
                    tried_letters.append(guess)
                else:
                    print("You've already guessed this letter.") 
        else:
            print('''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
    ''')
            print("\nYou've lost.")
            break
    print(f"\nWord was {secret_word}.")
    print("\nThanks for playing!")
    break
