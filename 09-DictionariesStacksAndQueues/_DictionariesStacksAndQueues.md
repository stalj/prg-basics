<!--
(c) Janusz Stal
Krakow University of Economics
Department of Informatics
stalj@uek.krakow.pl
-->

# DICTIONARIES, STACKS AND QUEUES

## 1. Dictionary

1. Watch the video on using dictionaries in Python:

   <https://youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-> 

1. Sprawdź w3schools jak wykonuje się następujące operacja na słowniku:


Basic Dictionary Operations

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

Iterating Over a Dictionary
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

Checking if a Key Exists

   ```python
   # Create a dictionary
   person = {'name': 'Alice', 'age': 30}

   # Check if a key exists
   if 'name' in person:
      print("Name is present in the dictionary.")
   else:
      print("Name is not present.")
   ```

1. Create a dictionary as in the example below. Note the structure of the dictionary (key-value) and the value types in the example below. What type of value was used in each of the six key-value pairs?

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

   1. Displays contents of the dictionary
   1. Displays name
   1. Displays hobby
   1. Changes surname to 'Nowak'
   1. Changes person's marriage status
   1. Adds gender: 'male'
   1. Adds a new hobby: 'bicycle'
   1. Adds work phone to existing phones: '313131444'

1. Create a dictionary describing your mobile phone. Use at least 6 key-value pairs of data of different types. Then, using 'for' loop, display the contents of the dictionary. To read a key and value, use the items() method. Sample result:

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

1. Create an array with 5 dictionaries, each containing a country and its population. Then, using a ‘while’ loop, display the array contents. Sample result:

   ```python
   countries = [
   {"name":"Poland", "population":38000000},
      …
      …
      …
      …
   ]
   ```

   ```
   COUNTRY  POPULATION
   Poland   38000000
   …        …
   …        …
   …        …
   …        …
   ```

## 2. JSON

1. 1. Watch the video on how to deal with JSON files in Python:

   <https://youtu.be/pTT7HMqDnJw?feature=shared> 

1. Find any JSON file on the Internet and download it to your computer. Open the file in any character editor and read its contents. Then, write a program that displays the contents of the JSON file. Sample result:

   import json

   with open("filename.json") as file:
   `    `data = json.load(file)

   for key,value in data.items():
   `    `print(f"{key} : {value}")


1. Create a dictionary that describes your favorite book or movie with at least five key-value pairs. Then, create a program that writes the dictionary data to the favourite.json file. Use the dump() method. Pay attention to the formatting of the data in the json file. Use the 'indent' parameter in the dump() method. Sample result:

   ```python
   movie = {
      "title":"…",
      "year": …,
      "actor":{"leading":"…","supporting":"…"},
      "oscar":False,
      …
      …
      …
   }
   ```

1. Write a program in which you create a dictionary containing student data. Try to describe a student in detail, using different data types that can be used in the dictionary. Then, save the data about student in the file student.json, in a readable form.

## 3, Stack

1. A stack is a linear data structure in which data is added to the top of the stack and is retrieved from the top of the stack. Familiarize yourself in more detail with this data structure. Explain the concept of LIFO.

1. Video explaining stacks !!!!!!!!!

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


## 4. Queue

1. A queue is a linear data structure in which new data is added to the end of the queue, and data is retrieved from the beginning of the queue for further processing. Familiarize yourself in more detail with this data structure. Explain the concept of FIFO.

1. Video explaining queues !!!!!!!!!

1. Following the example of stack.py, create a queue.py module in which define queue handling. Then write a program that imports the queue.py module. Add and remove values from the queue. Display its content.

## 5. Practice Makes Perfect

1. A dictionary contains course names along with the number of hours. Write a program that calculates and displays the total number of hours. Sample results:

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

   Write a program that creates a dictionary called ‘person’ containing data from the two given dictionaries (five key-value pairs). Display the contents of the ‘person’ dictionary.

1. A program contains two functions:
   1. hotel\_list(hotels) that returns a list of hotels names, separated by a comma sign
   1. avg\_price(hotels) that returns the average room price for a given list of hotels, rounded to an integer value

Write a program that calculates and displays the average price for a room in hotels in Krakow and Sopot and indicates in which cities hotels are cheaper.

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

   Sample result:

   ```
   Hotels in Krakow: …,…,…,…
   Average hotel price in Krakow: …
   Hotels in Sopot: …,…,…,…
   Average hotel price in Sopot: …
   Cheaper hotels in: …
   ```

1. The website http://api.nbp.pl contains data on exchange rates published by the National Bank of Poland. The service provides data in json or xml formats. Display the last ten Euro exchange rates in json format in the browser window. Save the data to the euro.json file. Then, write a program that displays the data from the euro.json file in the following format:

   ```
   Date            Buying Rate     Selling Rate
   ============================================
   2019-10-25      3.8150          3.9820
   ...
   ```             ...             ...

1. The products.csv file contains data about the products sold. Create the file in a text editor.

   ```
   Product,Quantity,Price
   milk,8,4.25
   cheese,5,17.90
   bread,21,6.15
   juice,12,5.90
   ```

   Then, write a program to convert data from CSV to JSON. The program reads product data from the CSV file and writes the data to a JSON file.

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



--------------------
--------------------
--------------------



Here are the 10 real-life tasks with their corresponding Python code examples that use dictionaries:

### 1. **Store and Access Employee Information**

**Task:** Create a dictionary to store employee details such as name, position, and salary. Retrieve and display the position of a specific employee.

```python
# Dictionary storing employee details
employees = {
    'John': {'position': 'Manager', 'salary': 60000},
    'Alice': {'position': 'Engineer', 'salary': 50000},
    'Bob': {'position': 'Intern', 'salary': 20000}
}

# Accessing the position of a specific employee
employee_name = 'Alice'
if employee_name in employees:
    print(f"{employee_name}'s position is {employees[employee_name]['position']}.")
else:
    print(f"No details available for {employee_name}.")
```

### 2. **Count Word Frequency in a Text**

**Task:** Count how many times each word appears in a paragraph.

```python
text = "the cat and the dog the cat"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
```

### 3. **Product Price List**

**Task:** Create a dictionary that stores product prices, update a product's price, and look up the price by product name.

```python
# Product price list
products = {
    'apple': 1.2,
    'banana': 0.5,
    'orange': 0.8
}

# Update price of an existing product
products['banana'] = 0.6

# Look up the price of a product
product_name = 'apple'
if product_name in products:
    print(f"The price of {product_name} is ${products[product_name]:.2f}.")
else:
    print(f"{product_name} is not available.")
```

### 4. **Phone Book Application**

**Task:** Build a phone book with contacts, allowing adding, removing, and searching contacts.

```python
# Phone book dictionary
phone_book = {'John': '555-1234', 'Alice': '555-5678'}

# Add a new contact
phone_book['Bob'] = '555-8765'

# Remove a contact
phone_book.pop('Alice', None)

# Search for a contact
contact_name = 'John'
if contact_name in phone_book:
    print(f"{contact_name}'s phone number is {phone_book[contact_name]}.")
else:
    print(f"{contact_name} is not found.")
```

### 5. **Group Students by Grade**

**Task:** Group students into a dictionary where the grade is the key and the value is a list of students with that grade.

```python
students = [('John', 'A'), ('Alice', 'B'), ('Bob', 'A'), ('Mary', 'C')]

# Group students by grade
grades = {}
for name, grade in students:
    if grade not in grades:
        grades[grade] = []
    grades[grade].append(name)

print(grades)
```

### 6. **Shopping Cart Total**

**Task:** Calculate the total cost of a shopping cart using a separate price dictionary.

```python
# Price dictionary
prices = {'apple': 1.2, 'banana': 0.5, 'orange': 0.8}

# Shopping cart with quantities
cart = {'apple': 3, 'banana': 2}

# Calculate total cost
total_cost = sum(prices[item] * quantity for item, quantity in cart.items())
print(f"Total cost: ${total_cost:.2f}")
```

### 7. **Track Inventory Levels**

**Task:** Create an inventory dictionary and update it when items are added or sold.

```python
# Inventory dictionary
inventory = {'apple': 50, 'banana': 100, 'orange': 75}

# Add stock
inventory['apple'] += 10

# Sell stock
inventory['banana'] -= 5

# Display current inventory
print(inventory)
```

### 8. **Translate Words Using a Dictionary**

**Task:** Create a translation dictionary and allow users to input an English word to get its French translation.

```python
# Dictionary of translations (English to French)
translations = {'apple': 'pomme', 'banana': 'banane', 'orange': 'orange'}

# Input word to translate
word = input("Enter an English word: ").lower()

# Get the French translation
translation = translations.get(word, 'Translation not available')
print(f"The French word for {word} is {translation}.")
```

### 9. **Voting System**

**Task:** Simulate a simple voting system where candidates are the keys, and vote counts are the values.

```python
# Voting system
votes = {'John': 0, 'Alice': 0, 'Bob': 0}

# Cast a vote
vote = 'Alice'
if vote in votes:
    votes[vote] += 1

# Display vote counts
print(votes)
```

### 10. **Store Weather Data**

**Task:** Store weather data in a dictionary and allow users to look up the temperature by city.

```python
# Weather data dictionary
weather = {'New York': 22, 'London': 18, 'Paris': 20, 'Berlin': 16}

# User input for city
city = input("Enter a city name: ").title()

# Get temperature for the city
temperature = weather.get(city, 'City not found')
print(f"The temperature in {city} is {temperature}°C.")
```

These examples illustrate various real-life scenarios where dictionaries can be used effectively in Python.





Here are 10 more real-life examples with Python code to practice using dictionaries:

### 11. **Track Attendance of Students**

**Task:** Create a dictionary to store students' attendance. Mark attendance as "Present" or "Absent" and allow updating for individual students.

```python
# Dictionary to track attendance
attendance = {'John': 'Present', 'Alice': 'Absent', 'Bob': 'Present'}

# Update attendance for a student
attendance['Alice'] = 'Present'

# Display attendance for all students
for student, status in attendance.items():
    print(f"{student}: {status}")
```

### 12. **Store and Update Bank Account Balances**

**Task:** Simulate a bank system where you store customer names as keys and their bank balances as values. Allow depositing and withdrawing amounts.

```python
# Dictionary storing bank balances
bank_accounts = {'John': 1000, 'Alice': 2000, 'Bob': 1500}

# Deposit money
bank_accounts['John'] += 500

# Withdraw money
bank_accounts['Alice'] -= 300

# Display all account balances
for customer, balance in bank_accounts.items():
    print(f"{customer}: ${balance}")
```

### 13. **Catalog of Books in a Library**

**Task:** Create a dictionary to store books in a library where the key is the book title, and the value is the status of whether the book is "Available" or "Checked Out."

```python
# Library book catalog
library = {
    'To Kill a Mockingbird': 'Available',
    '1984': 'Checked Out',
    'Moby Dick': 'Available'
}

# Check out a book
library['Moby Dick'] = 'Checked Out'

# Display all books and their availability
for book, status in library.items():
    print(f"'{book}' is {status}.")
```

### 14. **Store Movie Ratings**

**Task:** Create a dictionary where movie titles are the keys and their ratings (out of 10) are the values. Allow users to update the rating of a movie.

```python
# Movie ratings dictionary
movies = {'Inception': 9, 'Titanic': 8, 'Avatar': 7}

# Update rating for a movie
movies['Avatar'] = 8

# Display all movie ratings
for movie, rating in movies.items():
    print(f"{movie}: {rating}/10")
```

### 15. **Track Grocery Stock Levels**

**Task:** Store grocery items as keys and their stock levels as values. Allow updating stock when items are sold or restocked.

```python
# Grocery stock levels
grocery_stock = {'Milk': 20, 'Bread': 50, 'Eggs': 100}

# Restock an item
grocery_stock['Milk'] += 10

# Sell an item
grocery_stock['Bread'] -= 5

# Display current stock levels
for item, stock in grocery_stock.items():
    print(f"{item}: {stock} units")
```

### 16. **Store User Preferences for a Website**

**Task:** Create a dictionary that stores user preferences (e.g., dark mode, font size) for a website. Allow updating user preferences.

```python
# User preferences dictionary
user_preferences = {'theme': 'dark', 'font_size': 'medium'}

# Update user preference
user_preferences['font_size'] = 'large'

# Display current preferences
for setting, value in user_preferences.items():
    print(f"{setting}: {value}")
```

### 17. **Shopping Cart with Multiple Items per Product**

**Task:** Store items in a shopping cart where each item has multiple details (quantity and price). Calculate the total cost of the cart.

```python
# Shopping cart dictionary
cart = {
    'apple': {'quantity': 3, 'price': 1.2},
    'banana': {'quantity': 2, 'price': 0.5}
}

# Calculate total cost
total_cost = sum(item['quantity'] * item['price'] for item in cart.values())
print(f"Total cost: ${total_cost:.2f}")
```

### 18. **Store Favorite Sports Teams for Multiple People**

**Task:** Create a dictionary where people's names are keys, and their favorite sports teams are values. Allow updating their favorite teams.

```python
# Favorite sports teams dictionary
favorite_teams = {'John': 'Lakers', 'Alice': 'Patriots', 'Bob': 'Yankees'}

# Update favorite team for a person
favorite_teams['John'] = 'Warriors'

# Display favorite teams
for person, team in favorite_teams.items():
    print(f"{person}'s favorite team is {team}.")
```

### 19. **Store Shopping Wishlist**

**Task:** Create a dictionary to store a wishlist where item names are the keys, and the value is whether the item has been bought or not ("Yes" or "No").

```python
# Shopping wishlist dictionary
wishlist = {'Laptop': 'No', 'Phone': 'Yes', 'Headphones': 'No'}

# Mark an item as bought
wishlist['Laptop'] = 'Yes'

# Display wishlist status
for item, status in wishlist.items():
    print(f"{item}: Bought - {status}")
```

### 20. **Track Project Deadlines**

**Task:** Create a dictionary where the project names are the keys, and the deadlines are the values. Allow updating deadlines as the project progresses.

```python
# Project deadlines dictionary
projects = {'Project A': '2024-12-01', 'Project B': '2024-11-15'}

# Update deadline for a project
projects['Project A'] = '2024-12-15'

# Display project deadlines
for project, deadline in projects.items():
    print(f"{project} deadline is {deadline}.")
```

These examples cover a wide range of real-world scenarios that will help you get comfortable using dictionaries for various tasks in Python.