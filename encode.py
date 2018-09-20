#Name: Dante Rivera
#Date: August 27th, 2018
#This program returns an encoded version of a string by shifting each letter one place to the left in the alphabet



msg = input('Enter a word or phrase: \n')   # User input

def semi_encode(string):
    string.lower()  # Forcing lowercase
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Char set
    encoded = ''     # Empty string to be the encoded message
    for i in string:    #Looping through given string
        char_pos = alphabet.find(i) - 1      # Get char position of given string in char set, shift to the left one
        encoded += alphabet[char_pos]   # Add shifted char to empty string
    print(encoded)  # Print encoded string



semi_encode(msg)    # Invoke function
