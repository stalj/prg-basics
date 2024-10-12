import stack

# some previously visited websites
stack.push('instagram.com')
stack.push('uek.krakow.pl')
stack.push('microsoft.com')

while True:
   website = input('Enter website name (0 for back): ')

   # if entered 0
   #  break if empty stack
   # else
   #  read previous website name from stack

   # if entered website name
   #  add website name to stack

   # print name of website you are currently viewing
   print('\nYou are currently viewing:', website)
   print()
