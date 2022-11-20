'''
final.py is my CS50 python course final project: A game that mimics the famous word guessing game "WORDLE"
'''
from termcolor import colored
import random
import re
import requests
def main():
    print("You have six guesses! Good luck..." )
    print(get_word())
    print(match_words(guess_word))
def get_word():
    global word_list
    global random_word
    '''
    get_word() function that donwloads a list of five letter word from a databases and generates a random word from that list
    source: https://gist.github.com/iancward/afe148f28c5767d5ced7a275c12816a3
    '''
    meaningpedia_resp = requests.get("https://meaningpedia.com/5-letter-words?show=all")
    # compile regex
    pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
    # find all matches
    word_list = pattern.findall(meaningpedia_resp.text)
    random_word = random.choice(word_list)
    return random_word
def guess_word():
    '''
    prompts the user for a five letter word and checks if the user enters five valid english letters,
    if the user enters less or more than 5 letters it re-prompts the user
    if the user enters a number in the word it captures a value error
    '''
    global word_list
    #The user enters the guess
    while True:
        try:
            guess = input("Enter guess: ")
            for i in range(len(guess)):
                if guess[i].isnumeric():
                    raise ValueError

            if guess not in word_list:

                print("Please enter a valid word")
            elif len(guess) != 5:
                print("Please enter a 5 letter word")
            else:
                return guess
        except ValueError:
            print("Please enter English letters only")
def match_words(guess_word):
    '''
    matches the random word generated to the guessed word by the user
    the user has only 6 tries
    '''
    global random_word
    tries = 0
    while tries <6:
        s = guess_word()
        match = ""
        tries +=1
        #Check how many times the char occurs in the word:
        for i in range(len(random_word)):
            if s == random_word:
                return f"Well done! {colored(s, 'green')}"
            if s[i] == random_word[i]:
                match += colored(s[i], 'green')
            elif s[i] != random_word[i]:
                if s[i] in random_word:
                    match += colored(s[i], 'yellow')
                elif s[i] not in random_word:
                    match += colored(s[i], 'grey')

        print(f"Trials left: {6 - tries}")
        print(match)
    return f"The word is: {random_word}\nbetter luck next time"

if __name__ == "__main__":
    main()