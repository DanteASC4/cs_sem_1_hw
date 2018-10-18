#CSci 127 Teaching Staff
#October 2017
#A program that converts hex numbers to decimal, but filled with errors...
#Modified by:  Dante Rivera

def convert(s):
     """ Takes a hex string as input.
     Returns decimal equivalent.
     """

     # total = 0
     # st = int(s)
     # for i in range(st):
     #      total = total * 16
     #      ascii = ord(s)
     #      if ord('0') <= ascii <= ord('9'):
     #           #It's a decimal number, and return it as decimal:
     #           total = total + ascii - ord('0')
     #      elif ord('A') <= ascii <= ord('F'):
     #           #It's a hex number between 10 and 15, convert and return:
     #           total = total + ascii - ord('A') + 10
     #      elif ord('a') <= ascii <= ord('f'):
     #           #Check if they used lower case:
     #           #It's a hex number between 10 and 15, convert and return:
     #           total = total + ascii - ord('a') + 10
     #      else:
     #           #Not a valid number!
     #           return(-1)
     i = int(s, 16)
     b = str(i)
     return(b)

def main():
    hexString = input('Enter a number in hex: ')
    print("The number in decimal is", convert(hexString))


#Allow script to be run directly:
if __name__ == "__main__":
     main()
