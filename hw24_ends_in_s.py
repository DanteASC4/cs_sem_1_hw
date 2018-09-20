#Name: Dante Rivera
#Date:  August 28th
#Simulates a nand gate

count = 0

words = input('Enter a bunch of nouns:    ')

wordL = words.split(' ')


def end_checker(word):
    global count
    if word[len(word) - 1] == 's':
        count += 1



wordS = list(map(end_checker, wordL))
print('Number of words: ', len(wordL))
print('Fraction of your list that is plural is: ', round(count / len(wordL), 2))
