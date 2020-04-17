import random


def wellcome():
    print("********************************")
    print("  WELCOME TO THE HANGMAN GAME! ")
    print("********************************")
    print()


def load_secret_word():
    archive = open('words.txt', 'r')
    words = []

    for line in archive:
        line = line.strip()
        words.append(line)

    archive.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word

    
def play():

    wellcome()

    secret_word = load_secret_word()
    hit_letter = ["_" for letter in secret_word] 

    hanged = False
    hit = False
    error = 0
    print(hit_letter)

    while not hanged and not hit:

        shot = input('type a letter: ')
        shot = shot.strip().upper()

        if shot in secret_word:
            index = 0
            for letter in secret_word:
                if shot == letter:
                    hit_letter[index] = letter
                index += 1

        else:
            error += 1

        hanged = error == 6  
        hit = "_" not in hit_letter
        print(hit_letter)

    print('End of the game')


if __name__ == "__main__":
    play()