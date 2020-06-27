import random

print('H A N G M A N')
words = ['python', 'java', 'kotlin', 'javascript']
choice = list(random.choice(words))
dashes = '-' * len(choice)
stored = []
tries = 8
menu = input("""Type "play" to play the game, "exit" to quit: """)
while menu == 'play':
    while tries > 0:
        if choice == list(dashes):
            break
        counter = 0
        letter = input('\n' + dashes + '\nInput a letter:')

        if len(letter) > 1:
            print("You should input a single letter")
        elif letter.isupper():
            print("It is not an ASCII lowercase letter")
        elif letter.isalpha() == False:
            print("It is not an ASCII lowercase letter")
        elif letter in dashes or letter in stored:
            print("You already typed this letter")
        elif letter not in choice:
            print('No such letter in the word')
            tries -= 1
        else:
            while counter < len(choice):
                if choice[counter] == letter:
                    dashes = list(dashes)
                    dashes[counter] = letter
                    if dashes == choice:
                        dashes = ''.join(dashes)
                        print(f"You guessed the word {dashes}!\nYou survived!")
                        break
                    dashes = ''.join(dashes)
                    counter += 1
                else:
                    dashes = ''.join(dashes)
                    counter += 1

        stored.append(letter)
        dashes = ''.join(dashes)
    
    if list(dashes) != choice:
        print("You are hanged!\n")
    menu = input("""Type "play" to play the game, "exit" to quit: """)
