<!--
(c) Janusz Stal
Krakow University of Economics
Department of Informatics
stalj@uek.krakow.pl
-->

# DICTIONARIES, STACKS AND QUEUES

## 1. Dictionary

1. A dictionary is a built-in data structure that stores data in key-value pairs. Each key is unique, and it maps to a specific value, allowing you to efficiently retrieve, update, and manage data. Dictionaries are mutable, meaning you can modify their content after they are created.

   Look at the dictionary below. It contains three elements, separated by commas. Each element in a dictionary consists of a key and a value, where the key acts as an identifier for accessing the associated value.

   ```python
   student = {'name':'John', 'age':25, 'major':'Computer Science'}
   ```

1. Familiarize yourself with the basic operations you can perform on a dictionary.


   **Basic Dictionary Operations**

   ```python
   # Create a dictionary
   student = {
      'name': 'John',
      'age': 22,
      'major': 'Computer Science'
   }

   # Accessing a value
   print(student['name'])

   # Adding a new key-value pair
   student['grade'] = 'A'

   # Modifying an existing value
   student['age'] = 23

   # Deleting a key-value pair
   del student['major']
   print(student)
   ```

   **Iterating Over a Dictionary**

   ```python
   # Create a dictionary
   fruits = {'apple': 3, 'banana': 5, 'orange': 2}

   # Iterating over keys
   for fruit in fruits:
      print(fruit)

   # Iterating over values
   for count in fruits.values():
      print(count)

   # Iterating over key-value pairs
   for fruit, count in fruits.items():
      print(f"The count of {fruit} is {count}")
   ```

   **Checking if a Key Exists**

   ```python
   # Create a dictionary
   person = {'name': 'Alice', 'age': 30}

   # Check if a key exists
   if 'name' in person:
      print("Name is present in the dictionary.")
   else:
      print("Name is not present.")
   ```

1. Create a dictionary describing your mobile phone. Use 6 key-value pairs of data. Then, using 'for' loop, display the contents of the dictionary. To read a key and value, use the items() method. Sample result:

   ```python
   mobile = {
   "OS":"Android",
      …
      …
      …
      …
      …
   }
   for key,value in mobile.items():
      print(f"{key} : {…}")
   ```

1. Create a dictionary as in the example below. Do you know what type of value was used in each of the six key-value pairs?

   ```python
   person = {
      "name": "Marek",
      "surname": "Banach",
      "age": 25,
      "hobby": ["swimming","excursions"],
      "married": True,
      "phone":{"landline":"123444321","mobile":"777888999"}
   }
   ```

   Then, create a program that:

   1. Displays name
   1. Displays hobby
   1. Displays the entire contents of the dictionary
   1. Changes surname to 'Nowak'
   1. Changes person's marriage status
   1. Adds gender: 'male'
   1. Adds a new hobby: 'bicycle'
   1. Adds work phone to existing phones: '313131444'
   1. Displays the entire contents of the dictionary (iterate over dictionary items)


1. Create an array with 5 dictionaries, each containing a country and its population. Then, print the array contents. Sample result:

   ```
   COUNTRY  POPULATION
   Poland   38000000
   …        …
   …        …
   …        …
   …        …
   ```

   ```python
   countries = [
   {"name":"Poland", "population":38000000},
      …
      …
      …
      …
   ]
   ```

1. Write a program that prints details of people from the phone book whose names start with the letter 'D'.

   ```python
   phone_book = {
      'John': '555-1234',
      'David': '555-5678',
      'Bob': '555-8765',
      'Charlie': '555-4321',
      'Diana': '555-9876',
      'Eve': '555-6543',
      'Frank': '555-3456',
      'Grace': '555-7890',
      'Hank': '555-1111',
      'Ivy': '555-2222',
      'Jack': '555-3333',
      'Daniel': '555-4444',
      'Liam': '555-5555',
      'Mia': '555-6666',
      'Nina': '555-7777',
      'Oscar': '555-8888',
      'Paul': '555-9999',
      'Dominic': '555-1010',
      'Rachel': '555-2020',
      'Sam': '555-3030'
   }

   ...
   ...
   ...
   ```

1. The following data contains information about the number of products available in a computer store. Write a program that prints:

   * a list of products and the quantity
   * the total number of products in the store

   ```python
   {
   'Laptop': 15,
   'Desktop PC': 10,
   'Monitor': 25,
   'Keyboard': 50,
   'Mouse': 60,
   'External Hard Drive': 30,
   'Printer': 12,
   'Router': 20,
   'USB Flash Drive': 100,
   'Graphics Card': 8
   }
   ```

1. The data below contains a price list of items from a clothing store along with their prices. Due to a seasonal sale, the store is reducing the price of each item by 10%. Write a program that:

   * prints a list of products and their prices before the discount
   * prints the total value of the products before the discount
   * modifies the price list according to the discount (round prices to two decimal places)
   * prints a list of products and their prices after the 10% discount
   * prints the total value of the products after the discount

   ```python
   price_list = {
      'T-shirt': 19.99,
      'Jeans': 49.99,
      'Jacket': 89.99,
      'Sneakers': 59.99,
      'Hat': 15.99
   }
   ```

## 2. JSON

1. JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is often used to transmit data between a server and a web application, as well as to store structured data.

   Note the key characteristics of JSON:

   * Readability: JSON is text-based, so it can be easily read by humans.
   * Simplicity: It is built on key-value pairs.
   * Language Agnostic: Although it derives from JavaScript, JSON is supported by many programming languages like Python, Java, PHP, C#, and more.

1. The computer.json file contains sample computer data. Open the json file in an editor and review its contents. Notice that the file contains a single dictionary of data.

   Then, write a program that prints information about a computer.

   ```python
   import json

   # Open the JSON file in read mode
   with open('computer.json', 'r', encoding='utf-8') as file:
      # Load the data from the JSON file into a variable
      data = json.load(file)

   # Print the JSON data
   for ... , ... in data.items():
      print(...,':',value)
   ```

1. The cities.json file contains data about selected cities in Poland. Open the json file in an editor and review its contents. Notice that the file contains an array of dictionaries.

   Then, write a program that prints information about cities.

   > Note: using the encoding='utf-8' parameter when opening the file is necessary because the json file also contains Polish characters in city names that must be processed correctly. Remember to always use this parameter when opening files that contain characters other than those in the Latin alphabet.

   ```python
   import json

   # Open the JSON file in read mode
   with open('cities.json', 'r', encoding='utf-8') as file:
      # Load the data from the JSON file into a variable
      data = json.load(file)

   # Print the JSON data
   for city in data:
      for ... , ... in city. ...():
         print(key,':',value)
      print()
   ```

1. The file dogs.json contains data about dogs. Write a program that prints information about dogs younger than 5 years.

1. The hotel's IT system contains a list of reserved rooms. The data is contained in the reservations.json file. Write a program that prints the summary information as stated below. Break your program into smaller parts defining functions.

   * number of rooms
   * number of paid reservations
   * number of unpaid reservations
   * total value of paid reservations
   * total value of unpaid reservations

1. The following program writes data to a json file. Analyze this program. Then, run the program and see if the json file is created. Display the created json file in the editor.

   ```python
   import json

   data = {
      "patient_record": {
         "patient_id": "P001234",
         "first_name": "John",
         "last_name": "Doe",
         "date_of_birth": "1985-05-15",
         "gender": "Male",
         "contact_info": {
               "phone_number": "+1-555-123-4567",
               "email": "johndoe@example.com",
               "address": {
                  "street": "123 Main St",
                  "city": "New York",
                  "state": "NY",
                  "postal_code": "10001",
                  "country": "USA"
               }
         },
         "medical_history": {
               "allergies": ["Penicillin", "Peanuts"],
               "current_medications": ["Lisinopril 10mg", "Metformin 500mg"],
               "past_illnesses": ["Hypertension", "Type 2 Diabetes"],
               "surgeries": [
                  {
                     "surgery_type": "Appendectomy",
                     "date": "2015-08-20"
                  }
               ]
         }
      }
   }

   # Specify the file path and name
   file_name = "patient.json"

   # Open the file in write mode and use json.dump() to write the data to the file
   with open(file_name, 'w') as file:
      json.dump(data, file, indent=4)

   print("Data has been written to", file_name)
   ```

1. Create a dictionary that describes your favorite book or movie with at least five key-value pairs. Then, create a program that writes the dictionary data to the favourite.json file.

1. Write a program that takes data from the keyboard about a purchased product:

   * name
   * price (real number with two decimal places)
   * paid (yes/no)

   The program then saves the product data in the product.json file. Pay attention to the correct data types describing the product (string, float, bool).

   ```python
   product = {}
   
   # read product data from keyboard
   ...

   # save product data to json file
   ...
   ```

## 3, Stack

1. A stack is a linear data structure in which data is added to the top of the stack and is retrieved from the top of the stack. Familiarize yourself in more detail with this data structure. Explain the concept of LIFO.

   ![Stack Data Structure](https://media.geeksforgeeks.org/wp-content/uploads/20240606180325/What-is-Stack-(1).webp)

1. The following functions are necessary to handle the stack:

   ```
   push() - to put an item on the stack
   pop() - to pull an item from the stack
   empty()  - to remove all items from the stack
   ```

   In the stack.py file you can find a simple implementation of the stack using a Python list. Note the definition of the defined functions. What actions do these functions perform? Then write a program, in which, import the module stack.py and do the following:
   
      1. Display stack
      1. Put the number 2 on the stack
      1. Put the number 14 on the stack
      1. Put the number 9 on the stack
      1. Display stack
      1. Get element from stack
      1. Display stack
      1. Put the number 31 on the stack
      1. Put the number 6 on the stack
      1. Display stack
      1. Get two elements from stack
      1. Display stack

1. Write a program that converts any natural number to a binary number. Use the stack. To convert a number, divide the number by 2, each time taking the remainder of the division and putting the remainder on the stack. Repeat the division until the number you are dividing is zero. Then pop and display all values from the stack. Sample result for number 18:

   |Division|Remainder|
   | :-: | :-: |
   |18 / 2 = 9|0|
   |9 / 2 = 4|1|
   |4 / 2 = 2|0|
   |2 / 2 = 1|0|
   |1  / 2 = 0|1|

   ```
   Natural number: 18
   Binary number: 10010 
   ```

1. A back.py program simulates the Back key in a web browser (displaying the previously viewed web site). Complete the program.

## 5. Practice Makes Perfect

1. Read the chapter in your class textbook that covers the topics in this section.

1. Watch the video on using dictionaries in Python:

   <https://youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-> 

1. Write a program to translate words from English to Polish. The user enters a word in English from the keyboard. The program displays the translation of the word or information that the translation is unavailable.

   ```python
   translations = {
      'computer': 'komputer',
      'mouse': 'myszka',
      'keyboard': 'klawiatura',
      'printer': 'drukarka'
   }
   ...
   ...
   ...
   ```

1. A dictionary contains course names along with the number of hours. Write a program that calculates and prints the total number of hours. Sample results:

   ```
   The total number of hours in the winter semester is …
   ```

   ```python
   winter_semester = {
      "math":60,
      "programming":30,
      "history":15
   }
   ```

1. Write a program that counts how many times each word appears in a paragraph. 

   > Hint: Check the dictionary to see if the next word appears in it. If so, increase the number of times the word appears by 1. You can easily split a paragraph into individual words using the split() method. Search the Internet for how to use it.

   ```python
   paragraph = "cat dog mouse cat rat cat mouse"
   ...
   ...
   ```

1. The program contains two dictionaries with personal data:

   ```python
   basic_data = {
      "name":"Barbara",
      "age":21
   }

   advanced_data = {
      "status":"student",
      "married":False,
      "interest":["reading","swimming"]
   }
   ```

   Write a program that creates a dictionary called ‘person’ containing data from the two other dictionaries (five key-value pairs). Print the contents of the ‘person’ dictionary.

1. A program contains two functions:
   1. hotel_list(hotels) that returns a list of hotel names, separated by a comma sign
   1. avg_price(hotels) that returns the average room price for a given list of hotels, rounded to an integer value

   Write a program that calculates and displays the average price for a room in hotels in Krakow and Sopot and indicates in which cities hotels are cheaper. Sample result:

   ```
   Hotels in Krakow: …,…,…,…
   Average hotel price in Krakow: …
   Hotels in Sopot: …,…,…,…
   Average hotel price in Sopot: …
   Cheaper hotels in: …
   ```

   ```python
   hotels_in_Krakow = [
      {"name":"Sky","price":320.00},
      {"name":"Metropol","price":480.00},
      {"name":"New Port","price":420.00},
      {"name":"Aparthotel","price":390.00}
   ]

   hotels_in_Sopot = [
      {"name":"Focus","price":510.00},
      {"name":"Aqua","price":345.00},
      {"name":"La Boutique","price":390.00},
      {"name":"Marina","price":410.00}
   ]
   ```

1. Write a program to calculate the total cost of a shopping cart using a price list.

   ```python
   # Price list
   prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

   # Shopping cart with quantities
   cart = {'juice': 3, 'bread': 1, 'milk': 2}

   # Calculate total cost
   ...
   ...
   ```

1. A traffic camera records passing vehicles. The camera saves their registration numbers in the file vehicle.txt. Write a program that calculates and prints how many registered cars come from each province of Poland. The list of provinces and the corresponding first letters of the vehicle registration numbers are contained in the file province.csv.

   > Hint: use the dictionary containing the letters corresponding to the provinces and the numbers of vehicles whose first letters of the registration number match the letters of the province.

1. Watch the video on how to deal with JSON files in Python:

   <https://youtu.be/pTT7HMqDnJw?feature=shared> 


1. The website <https://api.nbp.pl/en.html> contains data on exchange rates published by the National Bank of Poland. The service provides data both in json and xml formats. Display the last ten Euro exchange rates in json format in a web browser. Then, save the data to the euro.json file. Finally, write a program that displays the data from the euro.json file in the following format:

   ```
   Date            Buying Rate     Selling Rate
   ============================================
   2019-10-25      3.8150          3.9820
   ...
   ...
   ...
   ```

1. Write a program to record voting. Voting results are saved in the voting.json file with the structure below. The program takes a person's name from the keyboard and increases the number of votes for that person by 1. If this is a new person, they are added to the list with a vote count of 1. You can run the program multiple times to add additional votes to the json file.

   ```python
   {
      person_name: number of votes,
      person_name: number of votes,
      ...
      ...
   }

   # Read the contents of the json file
   ...
   
   # Vote for a person
   person_name = input('Name of the person you are voting for:')
   ...
 
   # Save voting data to json file
   ...
   ```

1. Define a function that takes a string as input and uses a stack to reverse it. Then, write a program to reverse any text entered from the keyboard.
   
   > Hint: Push each character of the string onto the stack, then pop characters to form the reversed string.

1. Search the Internet and familiarise yourself with RPN (Reverse Polish Notation). Then, write a program that calculates RPN expressions. RPN can be conveniently evaluated using a stack structure. A user can enter from the keyboard any number, an operator (+ - \* / ) or the equal sign (=).

   1. If the entered value is a number, push the number on to the stack
   1. If the entered value is an operator, pop two items from the top of the stack, do the calculation, and push the result of the operation on to the stack.
   1. If the entered value is an equal sign, pop the final result from the stack and display the result of calculation.

   Then, using the program, calculate the value of RPN expressions:

   |Expression|RPN (Reverse Polish Notation)|
   | :- | :- |
   |2 + 3 =|2 3 + =|
   |2 \* (4 + 1)|2 4 1 + \* =|
   |(2 + 3) \* ( 4 + 5) =|2 3 + 4 5 + \* =|
   |8 / (3 + 1) \* (3 - 2 + 4) = |8 3 1 + / 3 2 – 4 + \* =|

1. Define a function that returns true if the brackets `()`, `{}`, `[]` are used correctly in the given expression. Otherwise, the function returns false. Then write a program that checks the correctness of the expressions given below.

   ```python
   [(2+3)*4+5]/6-{(7*8)+[4]}=
   [(2+3]/4)
   ```

   > Use a stack. Read the next characters of the expression. Skip all but the brackets. If it is an opening bracket, put it on the stack. If it is a closing bracket, pop the item from the stack and compare whether it is a matching opening bracket.

1. A queue is a linear data structure in which new data is added to the end of the queue, and data is retrieved from the beginning of the queue for further processing. Familiarize yourself in more detail with this data structure. 

   ![Queue Data Structure](https://media.geeksforgeeks.org/wp-content/uploads/20240606165428/Introduction-to-Queue-(2).webp)


1. Following the example of stack.py, create a queue.py module in which define queue handling. Then, write a program that imports the queue.py module. Add and remove values from the queue. Display its content.

1. Using the queue.py module you created, write a program that manages a queue of files to print.

   ```python
   import queue

   while True:
      print('1. Add file to print')
      print('2. Print file')
      print('3. View list of files to print')
      print('0. Quit')
      menu = input('Select an option: ')
      ...
      ...
      if menu == '1':
         file_name = input('\nEnter file name to print: ')
         # add new file to the end of the queue 
      ...
      ...
      ...

      elif menu == '0':
         break
   ```

1. Write a program that supports customer service in an office. Use the queue module. Each new customer receives a ticket with an automatically assigned consecutive number and is added to the end of the queue. The next customer to be served is taken from the beginning of the queue.