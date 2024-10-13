import queue

# create a visited_websites
visited_websites = queue.LifoQueue()

# some previously visited websites
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

while True:
   website = input('Enter website name (0 for back): ')

   if website == '0':
      if visited_websites.empty():
         break
      else:
         print('<-- Going back to a previously visited website')
         website = ...
   elif ... != "":
      ...

   # print name of website you are currently viewing
   print('You are currently viewing:', website)
   print()
