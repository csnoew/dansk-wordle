import random
import time

with open("wordlist.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))

    originwordle = random.choice(words).lower()
    wordle = originwordle.lower()

win = 0
f = 0
o = 0


def call():
    global g, wordle, guess
    if f != 5 and o != 6:
        g = 0
        guess = input("guess: ").lower()
        if len(guess) != 5:
            print("Invalid guess")
            time.sleep(1)
            open(__file__)
            exit()
        if 6 > g:
            g = g + 1
            test()
    elif wordle == guess:
        print("Correct, the word was", originwordle)
        input("Press enter to exit...")
        exit()
    else:
        print("Incorrect, the word was", originwordle)
        input("Press enter to exit...")
        exit()


def test():
    global f, o
    i = 0
    f = 0
    if win == 0:
        while 5 > i:
            if str(guess[i]) in wordle:
                if guess[i] == wordle[i]:
                    print("green ", end="")
                    i = i + 1
                    f = f + 1
                else:
                    print("yellow ", end="")
                    i = i + 1
            else:
                print("gray ", end="")
                i = i + 1
        i = 0
        o = o + 1
        print("  -  ", o, "/ 6")
        print("")
        print("")
        call()
    else:
        print("Incorrect, the word was", originwordle)
        input("Press enter to exit...")
        exit()


call()
