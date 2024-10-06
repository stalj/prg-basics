<!--
(c) Janusz Stal
Krakow University of Economics
Department of Informatics
stalj@uek.krakow.pl
-->

# FILE HANDLING

## 1. Reading from File

1. A file is a named location on disk to store data permanently. It is used to store information in a format that can be read by Python, other programs, or even a human. Python provides built-in functions and libraries to interact with files, allowing you to create, read, write, and manipulate them.

   Notice that files can be of various types, but the most common are:

   * Text files (e.g., .txt, .csv, .py): Store plain text data that is human-readable.
   
   * Binary files (e.g., images, videos, executable files): Contain data in binary format, which is not human-readable directly.

1. Watch the video on how to deal with text files in Python:

   <https://youtu.be/4mX0uPQFLDU?feature=shared>

1. Pay attention to the program below that opens and reads the contents of a text file. It is recommended to open the file in a 'with' statement. The open file is then closed automatically after executing all the statements contained in the 'with' statement block.

   > The 'r' (read) parameter in the open() function means to open the file for reading only. This is the default setting.

   ```python
   with open('example.txt', 'r') as file:
      content = file.read()
   # The file is automatically closed when the block is exited
   ```

1. To read the contents of a file, you must first open it. You can read the contents of a text file line by line, or you can read the entire contents of the file at once.

   The program print_countries.py opens a text file, reads its contents line by line, and prints the contents of each line. Analize the program code. Then, run the program.

   > If the program can't open the file 'countries.txt', look in the VSCode terminal to see what the current folder is. If it's 'ClassMaterials', change the current folder to the one that contains both the program and the file 'countries.txt' (08-FileHandling) by running the command below. Then run the program again.

      ```
      cd 08-FileHandling
      ```
   
   Notice the use of the print() statement with the end="" parameter. Its use is due to the existence of end-of-line characters at the end of lines in the text file.

   <https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/>

1. Modify the program print_countries.py so that the printed list of countries is numbered. Sample result:

   ```
   1. Poland, Warsaw, 38265000
   2. Germany, Berlin, 83240000
   3. France, Paris, 67850000
   4. Japan, Tokyo, 125800000
   5. Canada, Ottawa, 38250000
   ```

1. The following program prints a list of countries from 'countries.txt' file.Modify the program to print a list of countries sorted alphabetically.

   > Tip. Before printing the contents of the array, sort it alphabetically using the built-in function sorted()

   ```python
   ###
   # Reads the entire contents of a file
   #
   def read_from_file(name):
      with open(name, 'r') as file:
         content = file.read()
      return content

   # reads the entire file
   file_content = read_from_file('countries.txt')

   # splits the entire contents into lines
   # and stores them in an array
   file_lines = file_content.splitlines()

   # prints the array
   for line in file_lines:
      print(line)
   ```


1. The file car_park.txt contains data on the number of parked cars for the last five days. Complete the following program to calculate the total number of parked cars.

   ```python
   ###
   # Reads the entire contents of a file
   #
   def read_from_file(name):
      with open(name) as file:
         content = file.read()
      return content

   # reads the entire file and splits lines into array
   file_content = read_from_file('car_park.txt')
   file_lines = file_content.splitlines()

   # calculates the total number of cars parked
   total = 0
   for line in ...:
      total += ...

   print('Total cars parked:', ...)
   ```

1. The file pets.txt contains humorous text about animals. Write a program that prints the text and counts the number of words in the text.

   > To calculate the number of words in a line, use the split() method, which splits a string into a list where each word is a list item. Then read the length of this list. Use the len() function. Finally, sum the number of words in each line.\
   <https://www.w3schools.com/python/ref_string_split.asp>

1. The file it_company.csv contains a list of employees. Write a program that displays only employees with the position "Software Engineer".

   > Hint: You can check if a substring is contained within another string using the 'in' operator.

   ```python
   ###
   # Prints employees employed in a specified position.
   #

   # Employee List
   file_name = 'it_company.txt'

   # Position
   job_title = 'Software Engineer'

   with ... as ...:
      for line in ...:
         if ... in ...:
            print ...
   ```


## 2. Writing to File

1. Here's a program that writes data containing the title of a movie, its director, and the lead actor to a text file. Copy the program to the movie.py file, then run the program. Finally, open the created text file in an editor and check its contents.

   > To write data to a file, you need to open it with the 'w' (write) parameter. The write() method writes one line of data to the file. Note the '\n' character. It means to move the cursor to the next line. If you don't add it, all subsequent data will be placed on one line.

   ```python
   # Program to write movie details to a text file

   # Variables containing movie details
   movie_title = "Inception"
   director = "Christopher Nolan"
   lead_actor = "Leonardo DiCaprio"

   # Name of the file to write to
   file_name = 'movie_details.txt'

   # Writing movie details to the file
   with open(file_name, 'w') as file:
      file.write(f"Movie Title: {movie_title}\n")
      file.write(f"Director: {director}\n")
      file.write(f"Lead Actor: {lead_actor}\n")

   print(f"Movie details have been written to {file_name}.")
   ```

   Program explanation:

   * Variables: movie_title, director, and lead_actor hold the details of the movie.
   * Opening the file: with open(file_name, 'w') opens the file in write mode ('w'), creating or overwriting the file.
   * Writing details: Uses the write() method to write each movie detail to the file, adding \n at the end of each line for formatting.
   * Automatic file closing: The with statement ensures the file is properly closed after writing.

1. Write a program that writes a list of the Seven Wonders of the World to a text file, in alphabetical order, with each name on a separate line. Then check in which folder the text file was created. See if its contents match the task.

   ```python
   ###
   # Writes Seven Wonders of the World to a file
   #
   seven_wonders = [
      "Great Wall of China",
      "Petra",
      "Christ the Redeemer",
      "Machu Picchu",
      "Chichen Itza",
      "Roman Colosseum",
      "Taj Mahal"
   ]

   # Name of the file to write to
   file_name = 'seven_wonders.txt'

   # Sort data alphabetically
   ...

   # Write data to the file
      with ...(file_name, 'w') as ...:
         for item in ...:
            ... .write(...)
   ```

1. Write a program that copies the contents of the file 'healthy_lifestyle.txt' to the file copy_healthy_lifestyle.txt'.

   > Hint: Read the entire contents of the original file and write them to the target file (copy).

   ```python
   ###
   # Makes a copy of a text file
   #

   # file names
   original_file = 'healthy_lifestyle.txt'
   target_file = 'copy_healthy_lifestyle.txt'

   # read the content of the original file
   with ... as ...:
      content = ... .read()
   ...
   ...

   # write the content to the target file (copy)
   with ... as ...:
      ... .write(...)
   ```

1. Write a program that saves data of employees employed in the position of 'Software Engineer' to the file 'software_engineer.txt'. Data is available in the file 'it_company.csv'.

   > Hint: Read employee data line by line. For each line, check if it contains the name of the indicated position. If so, write this line to the output file.

   ```python
   ###
   # Saves to a file a list of employees working at a specified position.
   #

   # file names
   employees_file = 'it_company.csv'
   position_file = 'software_engineer.txt'

   # Position
   job_title = 'Software Engineer'

   # write selected employees to a file
   with ... as ...:
      with ... as ...:
         for line in ...:
            if ... in ...:
               ... .write(...)
   ```

1. Write a program that allows you to create a shopping list. The program takes user input from the keyboard until the user enters 0. Each value taken is saved to a text file 'shopping_list.txt'.

   > Hint: Open the file in append mode using the 'a' (append) parameter in the open() function.

   ```python
   ###
   # Creates a shopping list based on product names
   # entered from the keyboard.
   #

   # shopping list file name
   shopping_list = 'shopping_list.txt'

   # adds product name at the end of a shopping list
   def add_product(file_name, product_name):
      with open(...,'a') as ...:
         ... .write(...)

   # Takes next product name from the keyboard
   product = ""
   while product != "0":
      product = input('Enter product name (0 stops): ')
      if product == '0':
         ... # stops entering food names
      else:
         add_...
   ```

## 3. Using Regular Expressions

1. Regular expressions (regex) are sequences of characters that define a search pattern. They are used to find, match, and manipulate text. Regular expressions provide a powerful way to perform complex text processing, such as searching for specific patterns in a string, validating input, replacing text, or extracting information from large volumes of data.

   ![Regular Expression Example](re.png)

1. Use the interactive regular expression tutorial below to complete all the tasks in it.

   <https://regexone.com/>


1. Copy the text below into the Regex101 online editor:

   <https://regex101.com/>

   Then, for each of the following tasks, create a pattern that identifies the text chunks as described in the task.

   * Find all dates in the format "month day, year" (e.g., "March 12, 1992")
   * Locate all phone numbers in the format "XXX-XXX-XXXX" (e.g., "555-123-4567")
   * Find all numbers written with commas as thousand separators (e.g., "1,234")
   * Identify all fragments containing names starting with a capital letter (e.g., "Alice", "John", "Mike")
   * Find whole numbers in the text (e.g., "30")

   ```
   Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988. They have a mutual friend named Mike, whose phone number is 555-123-4567. In their hometown, which has a population of 1,234 or 1,235 people, a holiday festival is held every year on December 25. Alice works in an office with 30 employees. Her phone number is 555-765-4321.
   ```

1. A file shopping.txt contains an email with shopping report. Write a program that calculates the total value of money spent.

   ```python
   ###
   # Calculates the total value of money spent
   #
   import re # module for regular expressions

   # file name with shopping report
   email_file = 'shopping_email.txt'

   # read the content of email
   ...
   ...
   email = ... (email content)

   # regular expression pattern
   # for amounts
   pattern = '....'

   # extract numbers from email
   # tip: findall() method returns an array
   amounts = re.findall(pattern, email)

   # calculate the total purchases
   ...
   for amount in amounts:
      ...
   
   # print result
   print(...)
   ```

1. Write a program that reads a name from the keyboard. Then the program checks if the entered name is correct, according to the following requirements:

   * only letters
   * at least 3 letters
   * first letter uppercase, remaining lowercase

   ```python
   ###
   # Checks the correctness of the entered name
   #
   import re

   # read name from keyboard
   name = ...

   # pattern for a name
   pattern = ...

   # check if the name matches the pattern
   match = re.match(pattern,name)

   # print results
   if match:
      print(...)
   else:
      ... 
   ```


## 4. Practice Makes Perfect

1. Read the chapter in your class textbook that covers the topics in this section.



1. web scraping
pobrać oryginalną stronę z internetu, np. z danymi liczbowymi, zadanie to wydobyć te informacje

1. plik zawiera listę nazw plików, program zwracam pliki np. z podanym rozszerzeniem nazwy, albo ile jest plików zgodnych z wzorcem
(plik to nie lista nazw plików, każdy w oddzielnym wierszu, ale 2-3 paragrafy w których podane nazwy plików, po przecinku)

1. Zadanie 1-2 dot. obsługi plików CSV

1. 




1. Watch the video on how to deal with regular expressions:

   <https://youtu.be/nxjwB8up2gI?feature=shared> 

1. Write a program that calculates the number of lines for any text file. The user enters the name of the file from the keyboard. Display the result of the calculation (the file name and the number of lines). Do not display the contents of the file. Sample result:

   File name: countries.txt
   Number of lines: 14

1. Find any text file on the Internet that contains at least 30 lines of text and download that file to your computer. Then, write a program that displays the first five lines from the file and then waits for the Enter key to be pressed. The program repeats displaying the next five lines from the file, waiting for the Enter key to be pressed each time.

1. Find any text file on the Internet and download it to your computer. Then write a program that copies the contents of this file to the copy.txt file. Copy the contents of the file as a whole. Finally, open both files in any text editor and check that their contents are the same.

1. Find any text file on the Internet and download it to your computer. Then, write a program that copies the contents of this file to the copylines.txt file. Copy the contents of the file line by line. Finally, open both files in any text editor and check that their contents are the same.

1. Using any text editor, create the following two text files:

   ```
   MeatAndFish.txt

   Skinless white meat
   Tuna fish
   Luncheon meat
   Lean cuts of red meat

   GrainsAndBread.txt

   Bread
   Rice
   All purpose flour
   Breakfast cereal
   Pasta 
   ```

   Then, write a program that creates the allproducts.txt file, in which save the contents of the MeatAndFish.txt and the GrainsAndBread.txt files.

1. Create a program that writes to a text file integer numbers in the range <1,50>, every number in a separate line.

1. Create a program that writes 50 random integers between 100 and 999 to a text file, each number on a separate line.

1. Create a program that saves to a text file integer numbers in the range <1,10> with their second and third power. Sample result:

   ```
   1,1,1
   2,4,8
   3,9,27
   4,16,64
   …
   ```

1. In any text editor, create a text file studentslist.txt containing the following data in the CSV format:

   ```
   first\_name,last\_name,age,gender,email
   Decca,Blackstone,52,Male,dblackstone0@time.com
   Elena,Rechert,27,Female,erechert1@ucoz.com
   Bibbye,Norree,26,Female,bnorree2@reddit.com
   Alasdair,McCoole,53,Male,amccoole3@foxnews.com
   Hogan,Hatrey,26,Male,hhatrey4@zimbio.com
   ```

   Then, create a program that reads data from the CSV file and displays the first name, last name and email address of students under 30. Format the data as below. Sample result:

   ```
   Elena   Rechert  erechert1@ucoz.com
   Bibbye  Norree   bnorree2@reddit.com
   Hogan   Hatrey   hhatrey4@zimbio.com
   ```

   Tip: import and use the CSV module. 

1. The announcement regarding the temperature forecast in degrees Celsius for the next three days was published on the Internet:

   ```
   "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
   ```

   Create a program that calculates the average temperature. Use regular expressions to extract the values of temperatures from the message.

   ```python
   import re

   message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
   temperatures = re.findall("\d{2}",message)
   # complete the program code
   # ...
   ```

1. Write a program that calculates the number of vowels in the text:

   ```
   To be, or not to be, that is the question
   ```

   Use regular expressions and the findall() method.

1. Write a program that computes the number of words in the following text. Use regular expressions.

   ```
   To be, or not to be, that is the question
   ```

1. Find any text file on the Internet and download it to your computer. Then, write a program that displays all words with at least six letters from the file. Display each word on a separate line. Use regular expressions.

1. The grades.txt file contains student’s grades. Create the file in any text editor with the content as below:

   ```
   Name: Peter
   Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0
   ```

   Then, create a program that calculates the arithmetic mean of student’s grades.

