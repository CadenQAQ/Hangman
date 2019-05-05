import string
letters_guessed = ['a','p']
secret_word = 'ap'


def get_available_letters(letters_guessed):
    avalable_letters = string.ascii_lowercase
    remain_letter = " "
    for letter in avalable_letters:
        if letter not in letters_guessed:
            remain_letter = remain_letter+letter


    return remain_letter

print(get_available_letters(letters_guessed))


print("I am thinking of a word that is %s letters long" %(len(secret_word)))
letters_guessed = input("Please guess a letter:")
print(input("Please guess a letter:"))


