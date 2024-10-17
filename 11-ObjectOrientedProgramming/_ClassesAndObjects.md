# CLASSES AND OBJECTS

1. Object-Oriented Programming (OOP) is a programming paradigm that is based on the concept of "objects." In OOP, software is designed by defining objects, which represent real-world entities. These objects can contain both data (attributes or properties) and methods (functions or behaviors) that operate on the data. The main goal of OOP is to make program code more modular, reusable, and easier to maintain.

   Watch the video (from the beginning to 3:42) on explaining the concepts of object, class and virtualization.

   <https://youtu.be/m_MQYyJpIjg?feature=shared>

1. In Python, a class is a construct that allows you to define custom data types. It is a fundamental concept of Object-Oriented Programming, enabling the creation of objects that bundle data (`attributes`) and behaviors (`methods`) together.

   **Features of a Class:**

   * **Attributes**: Variables that store data related to an object. These can represent the state of an object, such as name, age, price, etc.
   * **Methods**: Functions defined inside a class that operate on objects of that class. Methods can modify the state of an object, retrieve information, or perform specific actions.

   **Defining a Class:**

   To define a class in Python, we use the class keyword. Example:

   ```python
   class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Object attribute
        self.model = model  # Object attribute
        self.year = year    # Object attribute

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")
   ```

   **In the example above:**

   * **Car** is a class that describes cars.
   * **Constructor** `__init__()` is a special method called when a new object is created. It initializes the object and assigns values to the object's attributes.
   * `display_info` is a method that prints out the car's information.

   **Creating an Object:**

   An object is an instance of a class, which means a specific example described by the class. We create an object by calling the class as if it were a function.

   ```python
   my_car = Car("Toyota", "Corolla", 2021)  # Creating an object of the Car class
   my_car.display_info()  # Calling a method on the object
   ```

1. Learn on how to use classes and objects in Python:

   <https://youtu.be/f0TrMH9s-VE?feature=shared>

## Class and Object Creation

1. The file student.py contains the definition of a class that contains attributes describing a student. Modify the class by adding a third attribute. Then make changes to the program by adding a third student. Assign values ​​of all available attributes to all students. Finally, print information about all students.

1. The Square class represents objects describing a geometric figure (square). Complete the class by adding a method to calculate the perimeter of a square. Then write a program that creates two squares with sides of 4 and 6, respectively. Calculate the areas and perimeters of these squares. Print the results.

   ```python
   class Square:
      def __init__(self, a):
         self.a = a
      def area(self):
         return self.a * self.a

   square1 = Square(4)
   square2 = ...

   print('Square with side 4:')
   print('Area is ..., Perimeter is ....')
   print ('Square with side 6:')
   ...
   ...
   ```

1. The file `taxi.py` contains the definition of a class describing taxi rides. Complete the class by adding a method `print_receipt(self)` that prints receipt. It should contain all the information about the ride: distance, rate, and fare. Then write a program in which you create two objects representing two different taxi rides. Calculate the fares for the two rides and print receipts.

1. A class contained in the `socialmedia.py` models a social media profile, allowing users to add posts and display their timeline. Add a `display_timeline(self)` method to the class that prints the user's name along with a list of posts. Number the list items. Then write a program that creates a user 'johndoe'. Add the following posts. Print the user's name and posts.

   * Hello, world! 
   * Had a great day at the park!
   * What's up, Natalie? How are you?

1. The `Book` class, available in the `book.py` file, contains a collection of attributes and methods describing a book. Make changes so that the class also includes information about the book's price, which can be specified when it is created (specify a price of `48`). Print the price information along with other printed data.

1. Identify at least 3 states and 3 behaviors for your smartphone. Then, for the listed states and behaviors, create a class with attributes and methods. Try to use verbs in method names as they describe activities. Finally, create a smartphone object, call its methods and display object’s properties.

   ```python
      class Phone():
         ...
         ...
         ...
   ```

## String Representation of Object

1. In Python, `__str__()` is a special method that is used to define how an object should be represented as a string. This method is called when you use the `str()` function or `print()` function on an instance of a class. It allows you to control the human-readable string representation of your objects.

   The `__str__()` method should return a string that is a readable or meaningful representation of the object. It is mainly used for displaying the object to users. When you pass the object to `str()` or `print()`, Python internally calls `__str__()` to get a string representation of the object. Look at the example below. Then run this program.

   ```python
   class Car:
      def __init__(self, brand, model, year):
         self.brand = brand
         self.model = model
         self.year = year

      def __str__(self):
         return f"{self.year} {self.brand} {self.model}"

   # Creating an instance of the Car class
   my_car = Car("Toyota", "Corolla", 2021)

   # Print the object
   print(my_car)  # Output: 2021 Toyota Corolla
   ```

   You can also find additional information about the `__str__` method on the Internet:

   <https://www.pythontutorial.net/python-oop/python-__str__/>

1. Create a class that represents pieces of music. Define a class constructor that allows you to set the initial values of the music piece (artist, track title, album, year) when the object is created. Complete the class with the `__str__` method returning the song data as a string, in the format as below (4 lines). Then, create two objects that represent two pieces of music and print their data. Sample result:

   ```
   Performer: Ed Sheeran
   Title:     Hearts Don't Break Around Here
   Album:     Divide
   Year:      2017

   Performer: Queen
   Title:     Bohemian Rhapsody
   Album:     A Night at the Opera
   Year:      1975
   ```

   ```python
   # class definition
   class Song:
      def __...___(self,...,...,...,...):
         ...
         ...
         ...
         ...
      def __str.............
         ...
         ...
         ...
   
   # object creation
   song1 = ...
   song2 = ...

   ## object usage
   print(song1)
   ...
   ```

## Class with Multiple Components

1. In a `tv.py` file create a TV class that describes a TV set. The class should contain one boolean attribute called `is_on` that specifies whether the TV set is turned on. Initially, the TV is turned off. Add `turn_on()` and `turn_off()` methods in the class to turn the TV on and off, respectively. Also, add a `show_status()` method to print whether the TV is on or off. Then, in a tv_show.py, write a main program, in which try to create and use the TV set. Sample message:

   ```
   TV is on
   ```

   Then, try using the TV set in the program:

   1. Create TV set
   1. Show TV status
   1. Turn TV on
   1. Show TV status
   1. Turn TV off
   1. Show TV status

   ```python
   # tv.py file
   # class definition
   class TV:
      def __init__(self):
         self.is_on = False
      def turn_off(self):
         ...
      def turn_on ...
         ...
      ... show_status ...
   ```

   ```python
   # tv_show.py file
   # main program
   import ...

   def main():
      # object creation
      ...

      # object usage
      ...
   
   if __name__ == "__main__":
      main() 
   ```

1. In the TV class, add the `channel_no` attribute indicating the number of the current TV channel displayed by the TV set. Initially, the TV is set to channel 1. Modify the `show_status()` method so that it also prints the TV channel number, but only if the TV is turned on:

   ```
   TV is on, channel 1
   TV is off
   ```

   Then, try using the TV set. Print TV status both when switched on and off. See if the channel number is printed only when the TV is switched on.

1. Add the `set_channel(new_channel_no)` method in the TV class to set the TV channel number. Then try using the TV set.

   1. Create a TV set
   1. Show TV status
   1. Turn TV on
   1. Show TV status
   1. Change TV channel to 5
   1. Show TV status
   1. Turn TV off
   1. Show TV status 

1. In the TV class, add the channels attribute containing a list of available TV channel names (use an array). Initially, the array should be empty (TV not programmed, no available channels). Add `set_channels(channels_list)` and `show_channels()` methods in the TV class, which allows you to set channels on the TV and print the list of available channels. Sample list of available channels:

   ```
   Channel list:
   1. TVP1
   2. TVP2
   3. Polsat
   4. TVN
   5. Filmbox
   6. Discovery
   ```

   Then, try using the TV set:

   1. Create a TV set
   1. Show TV status
   1. Turn TV on
   1. Show TV status
   1. Display the list of available channels
   1. Set TV channels: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery
   1. Display the list of available channels
   1. Show TV status
   1. Turn TV offs

1. In the TV class, make changes to the `show_status()` method so that it prints not only the selected channel number but also its name. When the selected channel number exceeds the list of available channels, the channel name is not displayed.

   ```
   TV is on, channel 4 (TVN)
   ```

   Then, try using the TV. Set at least 7 channels (seven TV stations), change channel numbers a number of times and print TV status every time.

1. In the TV class, add support for volume adjustment in the range 0 to 10. The initial value of the volume level is 0. Add two methods to increase and decrease the TV volume level by one. Note that you cannot increase or decrease the volume beyond the specified range. Display the current volume level in the `show_status()` method. Then check the operation of the TV by adjusting and displaying its volume level.

## Practice Makes Perfect

1. From the course textbook, read chapter dealing with Object-Oriented Programming.

1. Watch the video on how Python classes are defined:

   <https://youtu.be/apACNr7DC_s?feature=shared>

1. Familiarise yourself with tutorials available on w3schools which deals with class creation and their components (fields and methods).

   <https://www.w3schools.com/python/python_classes.asp>

1. E-book is a digital book that can be read using a computer or other electronic devices (electronic book readers). Write a program in which define a class that describes states and behaviors of an  e-book. Each book has a title, author, number of pages and the current page number that is currently being read. It is possible to open a book - then we can read it. If a book is open, it is possible to go to the next or previous page.

   Place the class describing e-books in a separate file/module. In the main program file, try using the e-book:

   1. Create a book with a title, author, number of pages (check how to set the initial values of the fields at the time of creating the object using the `__init__` method / constructor and passing the initial values as arguments to the method call)
   1. Open a book
   1. Display a book status (title, author, page numbers, current page no)
   1. Read a few pages
   1. Display a book status
   1. Close a book
   1. Read a few pages (it should not be possible to perform this operation - display the message that the book is closed).

1. The medical thermometer measures the patient's temperature in the range from 34.0 to 42.0 degrees Celsius, with an accuracy of 0.1 degrees. Write a program in which define a class that describes the states and behaviors of the thermometer. The thermometer should enable temperature measurement (do it by generating a random number from the 34.0 to 42.0 range) and display the measured value. If the temperature is at least 37 degrees Celsius, the thermometer should additionally display the 'Fever' message, e.g.

   ```
   Temperature: 37.2C (fever)
   ```

   When the temperature is at least 41.0, the thermometer should additionally print the message 'CRITICAL TEMPERATURE!!'. Place the class definition and the main program in separate files. Then use the program and:

   1. Create a thermometer
   1. Turn thermometer on
   1. Measure temperature
   1. Display temperature
   1. Turn thermometer off

1. The bank account has a 26-digit number assigned when creating an account. The initial account balance is PLN 0. You can deposit any amount on the account. You can also withdraw any amount from the account, provided that it does not exceed the account balance. If you try to withdraw a larger amount, the following message will be displayed: "Insufficient funds on the account". At any time, it is possible to display information about the number and balance of the bank account in the following format:

   ```
   Bank Account No: 11 1111 1111 1111 1111 1111 1111
   Balance: PLN 25,38
   ```

   Create a program that handles the bank account.

   1. Familiarises yourself with a problem.
   1. Identify an object
   1. Define the states and behaviors of the object.
   1. Transform the states and behaviors of the object into the fields and methods of the class that will serve as a pattern for creating an object.
   1. Create a sketch of the class without creating any method content.
   1. Create the content of each method.

   Then, use the program and:

   1. Create a bank account with the number 12 3456 5555 9090 1111 0000 7722
   1. Display account balance
   1. Deposit PLN 25,30
   1. Display account balance
   1. Withdraw PLN 31,70
   1. Display account balance
   1. Withdraw PLN 14
   1. Display account balance

1. Write a program containing a Statistics class that describes the properties of any set of numbers. The class should allow to:

   1. Add to the set of numbers, the next number read from the keyboard (store the numbers in the array)
   1. Display all numbers separated by a space
   1. Determine the greatest number
   1. Determine the smallest number
   1. Calculate the arithmetic mean of numbers
   1. Calculate of the median
   1. Print of calculated / determined statistical quantities (minimum, maximum, arithmetic mean, median)

   Then, use the program for numbers below to calculate and print the basic staticstics:

   ```
   12, 37, 6, 9, 17 
   ```

1. The `Contact` class contains the `name`, `email` and `telephone` fields enabling the description of a single contact on a smartphone. The `Contact_List` class allows you to store contacts (store objects describing contacts in an array) and perform the following operations:

   1. Add a new contact
   1. Display the contact list

   Write a program consisting of 3 files (`smartphone.py`, `contact.py`, `contact_list.py`). In the mail program (`smartphone.py`), create an object representing a contact list and add the following people data:

   ```
   John Brown     brown@onet.pl       555234000
   Anna May   	   am@o2.pl            232000199
   George Small   smallg@google.pl    222999100
   Paola Big      bigpaola@poczta.pl  100200300
   ```

   Then, display the contact list available on the smartphone.

1. An object representing an employee contains the following data: name, surname, age, and seniority (the number of years worked). Define a `C` class that allows you to create an object. Provide employee data at the time of creating the object, in the given order. Define a text representation of an object in the class that contains a string of last name, first letter of first name, and seniority. If the employee is an adult (at least 18 years old), use uppercase letters, otherwise lowercase letters. Sample result:

   ```
   C("Anna","May",17,7) returns "maya7"
   C("George","Brown",21,4) returns "BROWNG4"
   ```

1. An object contains a list of coordinates of points on the plane, as a two-dimensional array. Define a `C` class that allows you to create an object. Provide the list of coordinates of points at the time of creating the object. In the class `C`, define a method `m(n)` that returns true when at least `n` points are in the first quadrant of the coordinate system (both point coordinates are greater than 0), or false otherwise. Sample result:

   ```
   C([[2,3],[1,8],[-6,4],[3,-7]])
   m(2) returns True
   m(3) returns False
   ```

1. A stadium is divided into sectors, each marked with a letter. There is a certain number of fans in each sector. Define the class `C`, which allows you to create an object representing the stadium with a list of sectors and the number of fans in sectors. Data, as a dictionary, should be transferred to the object at the time of its creation. Define in the class a `method m1(s,n)` that allows you to change the number of fans `n` in sector `s` or add a new sector `s` with the given number of fans `n`. Define in the class a method `m2(s)` that returns the sum of fans in the sectors listed in the string `s`. Sample result:

   ```
   C({"A":120,"D":150,"G":90,"K":110})
   m1("G",130)
   m2("GD") returns 280
   m2("KEJ") returns 110
   ```
