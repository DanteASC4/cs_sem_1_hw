a = True

while a:
 str = input('Enter a string:   ') 
 if str != '':
  a = False
  print('You entered: ' + str)
 else: 
  print('That was empty, try again')
