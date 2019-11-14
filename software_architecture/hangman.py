list_with_super_words = ['happy', 'hello', 'tinkoff', 'computer', 'apple', 'tiger', 'betman', 'hello', 'robot']
count_if_mistakes = 5

def guess_word(super_word):
    user_world = ''
    mistake = 0

    for k in range(len(super_word)):
        user_world += '*'

    while mistake < count_if_mistakes:
        user_letter = input("Guess a letter:")
        is_success_letter = False

        for j in range(len(super_word)):
            if user_letter == super_word[j]:
                user_world = user_world[:j] + user_letter + user_world[j+1:]
                is_success_letter = True

        if is_success_letter:
            print("Hit!")
        else:
            mistake += 1
            print("Missed, mistake {0} out of {1}".format(mistake, count_if_mistakes))

        print("The word: ", user_world)

        if mistake+1 == count_if_mistakes:
            print('You lost!')
        elif user_world == super_word:
            print("You won!")
            exit()

if __name__ == "__main__":
    print("Hello, dear friend! We will play the game Hangman!")
    print("Please, choose the super word (input 0 out of 9 number): ")
    super_word = list_with_super_words[int(input())]
    guess_word(super_word)

