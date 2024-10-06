<!--
(c) Janusz Stal
Krakow University of Economics
Department of Informatics
stalj@uek.krakow.pl
-->

# TYPES, VARIABLES AND OPERATORS

## 1. Interactive and Script Modes

1. In Python programming language, there are two ways in which you can run your code:

    * Interactive mode
    * Script mode

    Interactive mode is a feature that allows you to execute commands one at a time and see the output immediately. It is often used for testing small pieces of code, debugging, or learning the language. 
    
    Now, try to run Python in interactive mode:

    1. Open a command line (Terminal window) e.g. PowerShell for Windows. Search the Internet if you do not know how to do this.
    1. Type 'py', 'python' or 'python3' (depending on your operating system setup) and press Enter.
    1. You will enter the Python interactive shell where you can type and run Python commands interactively. The prompt usually looks like this:

        \>\>\>

1. In interactive mode, execute the following commands (enter a command and press Enter):

    1. 7 + 4
    1. (30 + 10) / 2
    1. 2 ** 3
    1. 7 > 5
    1. r = 4
    1. area = 3.14159 * r * r
    1. area
    1. round(area,2)
    1. first_name = "Mary"
    1. last_name = "Brown"
    1. full_name = first_name + ' ' + last_name
    1. full_name
    1. print(full_name)
    1. len(full_name)
    1. Enter commands to calculate and print the area of ​​a triangle with dimensions a=5 and h=4.
    1. Enter commands to calculate and print the arithmetic mean of the numbers: 7, 12 and 31. Print the result with an accuracy of 2 decimal places.

1. Script mode is used to write and execute program code from a file, instead of typing commands interactively. To write and run your program in script mode:

    1. Use any text editor to write your program code (e.g. Windows Notepad).
    1. Save the file with a .py extension (for example: myprogram.py).
    1. Open the terminal window in a folder where you saved your program file.
    1. Run the script by typing:

        ```
        py myprogram.py
        ```
    
    Below is a program to calculate Body Mass Index. Run the program in Script mode. 
    
    > Hint: create a text file bmi.py and copy and paste the program below. Please note that each program line must start in the first column. Remove unnecessary spaces if necessary.

    ```python
    ###
    # BMI Calculator
    #
    height = input('Enter your height in cm: ')
    weight = input('Enter your weight in kg: ')
    height = int(height)
    weight = int(weight)
    bmi = weight / (height/100)**2
    bmi = round(bmi,2)
    print('Your BMI is', bmi)
    print('Check on the Internet if your BMI is ok!!')
    ```

1. To create computer programs, it is most convenient to use an integrated environment (IDE). This tool allows you to both create a program and run it. One of the popular tools is Microsoft Visual Studio Code (VS Code).

    The program below simulates five dice rolls. In VS Code, create and run the program. 
    
    > Hint: on the Windows desktop, create a new folder called IDE. Then, open the folder in VS Code. Next, in VS Code, in the IDE folder, create a new dice.py file. Finally, run the created program.

    ```python
    ###
    # The program simulates five dice rolls.
    #
    import random
    print("Dice rolling simulator")
    for i in range(5):
        dice_roll = random.randint(1,6)
        print(dice_roll, end=" ")
    
    ```

## 2. Operators and Data Types

1. Operators in programming are symbols or keywords that perform operations on variables and values. They are essential in performing arithmetic calculations, comparisons, logical decisions, and more. Operators are crucial tools in programming that allow you to perform various operations on data. They are foundational elements in all programming languages, enabling everything from simple arithmetic to complex logic and data manipulation.

    Find a list of available operators in Python. You can use the following resource, for example:

    <https://www.w3schools.com/python/python_operators.asp>

    Then, explain what operation you can perform using the following operators:

    * \+
    * \*
    * \*\*
    * \/
    * \/\/
    * \%
    * \>
    * \<=

1. Count how many operators and arguments are included in each expression. Then, calculate values of the expressions. First, try to calculate every expression without using a computer or calculator. Then, check your results in interactive mode.

    1. 3 * 2 + 1
    1. 5 + 10 * 5
    1. 4 + 4 / 2 ** 2 
    1. 4 % 3 % 2 % 1 
    1. 1 + 2 % 3 ** 4 * 5
    1. True != False

1. A data type in programming defines the kind of data that can be stored and manipulated within a program. It specifies the type of value and what operations can be performed on it. Different programming languages have different data types. In Python, the built-in data types that you can consider basic are the following:

    * Integer (int): Represents whole numbers (e.g., 1, -5, 100).
    * Float (float): Represents decimal numbers (e.g., 3.14, -0.99, 7.0).
    * Boolean (bool): Represents truth values: True or False.
    * String (str): Represents a sequence of characters (e.g., "Hello, World!").

    In Python, you can check the data type of a value or variable using the built-in type() function. Here is how you can use it:

    ```python
    type(variable_or_value)
    ```
    
    Consider what data type the following values represent. Then, check your answers (run Python in interactive mode). Use the type(value) function.

    1. 50
    1. 149.17
    1. 4 * 7
    1. 4.0 * 7
    1. "Krakow University of Economics"
    1. True
    1. 2 > 5

## 3. Variables

1. In programming, a variable is a symbolic name or identifier that holds a value. It acts as a container for storing data, and the value stored in a variable can change during program execution. Variables are fundamental to programming because they allow you to store, retrieve, and manipulate data efficiently.

    Variables usually have descriptive names that reflect their purpose Each variable is characterized by:
    
    * its name
    * the value it stores
    * the type of the stored value

    Below is a short program that uses variables. Analyze the program code and count how many variables are used in the program. Then, for each variable, provide its name, value, and value type.

    ```python
    company = "ABC Data"
    phone = "555-123-009"
    employees = 25
    remote_work = True
    big_company = employees > 100
    income = 4500000
    income_per_person = income / employees
    ```

1. Below is a program that calculates the sum of two numbers. Modify the program to calculate the sum of three numbers. Notice the use of the function print(value1,value2,...), which allows the values to be printed on the monitor screen.

    ```python
    ###
    # A program that calculates the sum of two numbers.
    # Modify the program to calculate the sum of three numbers.
    #
    number1 = 71
    number2 = 14
    result = number1 + number2
    print('Number 1: ', number1)
    print('Number 2: ', number2)
    print('The result of summation: ', result)
    ```

1. Two variables x and y have values of 7 and 34. Write a program that swaps variable values (x should be 34 and y should be 7). Use an additional, auxiliary variable.

    > Hint: It is a good idea to always put a short description of the program in a comment at the beginning of the file. You can use the task text for this.

    > Hint: The program file name may contain the section number and task number, e.g. 3-7.py.


    ```python
    ###
    # A program for swapping two varable values
    #
    x = 7
    y = 34
    z = 0 # additional, auxiliary variable
    print("Before swapping: x=", x, "y=", y)

    # swap the values
    ...
    ...

    print("After swapping: x=", x, "y=", y)
    ```

1. Write a program that, for a given speed in km/h, prints the speed in m/s.

    ```python
    ###
    # A program that, for a given speed in km/h,
    # prints the speed in m/s
    #
    speed_kmh = 70
    speed_ms = ...
    print(speed_kmh, "km/h = ", speed_ms, "m/s")
    ```


1. Write a program that calculates the length of the diagonal of a rectangle with sides a=5 and b=8. To calculate the square root of a given value, use the sqrt function. The function is available in a module called math, which you must import into your program.

    ```python
    ###
    # A program that calculates the length of the diagonal
    # of a rectangle with sides a and b.
    #
    import math
    a = 5
    b = ...
    diagonal = math.sqrt(a**2 ...)
    print(...)
    ```

1. The distance to the horizon depends on the height of the observer above the ground. The higher you are, the farther away the horizon is. For most situations, you can use the following formula:

    d = 3.57 × √h

    Where:

    * d is the distance to the horizon in kilometers
    * h is the height of the observer in meters

    Write a program that calculates the distance to the horizon from a height given in meters from the keyboard. Then, using the program, calculate the distance to the horizon in km when:

    1. You are standing on a beach, by the sea, on the water line (calculate the distance for your height in m). You have probably been to the seaside many times. Can you believe that the horizon is only a few kilometers away?
    1. You are looking out of a hotel window located by the sea, the window is at a height of 20 meters.

1. In the year 2022, the world population was approximately 8 billion. The Northern Hemisphere has 7.2 billion people. Write a program that calculates and prints:

    1. The number of people and percentage of the total population living in the Northern Hemisphere
    1. The number of people and percentage of the total population living in the Southern Hemisphere

    ```python
    ###
    # A program that calculates and prints:
    # - the number of people and percentage of the total
    #   population living in the Northern Hemisphere
    # - the number of people and percentage of the total
    #   population living in the Southern Hemisphere
    #
    total = 8000000000
    north = 7200000000
    south = ...
    print("World population: ", total)
    print("Northern Hemisphere: ", north)
    print("Northern Hemisphere in %: ", north/total*100)
    ...
    ...
    ```

1. The following program calculates and prints the average grade of a student, but it contains several errors. Fix the program so that it works correctly.

    ```python
    ###
    # A program that calculates and prints
    # the average grade of a student
    #
    math = 5
    art = 4
    music = 5
    history = '3'
    average = mat + Art - muzic + history / 4
    print("Average grade is', averege)
    ```

## 4. Output Formatting

1. One of the basic functionalities of a computer program is printing results on the computer screen. To print the results in a readable form, string (text) formatting available in programming languages is often used. In Python, it is called f-strings.

    <https://www.pythontutorial.net/python-basics/python-f-strings/>
    
    <https://docs.python.org/3/tutorial/inputoutput.html> 

    Below is a program for printing any text along with the value of a variable using f-strings:

    ```python
    ###
    # Printing student's personal data
    #
    name = "Adam"
    print(f"My name is {name}.")
    ```

    Modify the program to print the student's age and height in addition to the name, as below.

    ```
    My name is Adam.
    I am ... years old, and my height is ... cm.
    In 6 years I will be ... years old.  
    ```

1. Write a program that calculates and prints the income of a family per person. To print the results in a readable form, use f-strings.

    ```python
    ###
    # Write a program that calculates and prints
    # the income of a family per person. To print the results
    # in a readable form, use f-strings.
    #
    father_income = 5450
    mother_income = 4920
    family_members = 5
    total_income = ...
    income_per_person = ...
    print(f'Total family income is ..., and income per person is ...')
    ```

1. The variables a and b contain two numbers. Write a program that prints the following expression containing the values of these variables and the value of the expression.

    ```python
    a = 3
    b = 5
    print(f'{a}+{b}=...')
    print(f'{a}-{b}...')
    print(f'{a}*...')
    print(f'{a}/...')
    ```


## 5. Data Input

1. In every programming language there is a function to take input from the user. The function allows the program to pause and wait for the user to type something on the keyboard. Whatever the user types is captured as a string.

    Complete the following program code:

    ```python
    # A program that reads your first and last name from the keyboard.
    # Store this data in two separate variables.
    # Then, print your full name i.e. first and last name separated by a single space.
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    full_name = ... + ' ' + ...
    print(f'Your first name is {first_name} and your last name is ...')
    print(f'And your full name is ...')
    ```

1. Take into account that whatever the user types on the keyboard is captured as a string. If you need a number for some arithmetic calculations, you have to convert the string of digits from the keyboard to a number using the int() function for integer numbers and float() function for real numbers. 

    Complete the following program code. Then, check the program for the following data:

    a = 4 --> volume = 64, surface area = 96\
    a = 7 --> volume = 343, surface area = 294


    ```python
    ###
    # A program to calculate the volume and surface area of ​​a cube.
    # 
    cube_side_string = input('Enter cube side: ')
    cube_side = int(cube_side_string)
    cube_volume = ...
    cube_surface_area = ...
    print(f'The volume of a cube with side {cube_side} is ...')
    print(f'The surface area of a cube with side ... is ...')
    ```

1. Write a program that calculates the volume and surface area of ​​a cuboid with sides a, b, and c. Then, check the program for the following data:

    a = 3, b = 4, c = 5 --> volume = 94, surface area = 60\
    a = 8, b = 1, c = 2 --> volume = 16, surface area = 52

    ```python
    ###
    # A program that calculates the volume
    # and surface area of ​​a cuboid with sides a, b, and c.
    # Read the dimensions of the cuboid from the keyboard.
    #
    a = input('a=')
    ...
    ...
    ...
    ```

1. 23% VAT was paid from an amount. Write a program that reads an amount from the keyboard. Then, it calculates and prints both the amount and its VAT. Apply formatting with two decimal places. Sample result:

    ```
    Amount  : 15.84
    VAT 23% :  3.64
    ```

1. The price of the product on the price tag is given before and after the discount is applied. Write a program that allows you to enter the product price and discount. Print the product price, discount, discounted product price, and the difference between the product price before and after the discount. Print all prices with two decimal places. Sample result:

    ```
    Enter price: 24.72
    Enter discount %: 15
    Price with discount: 21.01
    Reduction: 3.71
    ```

## 6. String Operations

1. The string type is a basic data type used to store sequences of characters such as letters, numbers, symbols, and special characters. It is one of the most commonly used data types that represents text and is extremely flexible. You can find out how many characters are in a string using the len() function.

    Complete the program below to calculate the number of characters in your name and surname.

    ```python
    ###
    # A program that calculates the number of characters
    # of your name, surname and full name
    #
    name = 'Anna'   # replace Anna with your name
    surname = 'May' # replace May with your surname
    characters_in_name = len(name)
    print(f'Your name has {characters_in_name} characters')
    print(f'Your surname has ... {len(...)} ...')
    print(f'Your full name has ...') # with a space between name and surname
    ```

1. Characters in a string are numbered (indexed) starting from 0. This means that the first character in the string has index 0, the second character has index 1, the third character has index 2, and so on. This rule is used in many programming languages.

    Modify the following program to print the initials of your name and surname, contained in the variables name and surname.

    ```python
    ###
    # A program that prints your initials
    #
    name = 'George'
    surname = ...
    print(name[0])
    ```

1. Write a program that prints the abbreviation of the university name (i.e. KUE)

    ```python
    ###
    # A program that prints a university abbreviation
    #   
    university = "Krakow University of Economics"
    ...
    ...
    ```

1. In Python, to read a range of characters from the string, a slicing method can be used.

    <https://www.w3schools.com/python/python_strings_slicing.asp>

    The employee file contains the employee's data in a descriptive form:

    ```
    "Mr. John May, born on 1998-02-16"
    ```

    Print the employee's name, surname, initials and date of birth on separate lines. Complete the following program code.

    ```python
    ###
    # A program for printing detailed information.
    #
    employee = "Mr. John May, born on 1998-02-16"
    print(f'Name: {employee[4:8]}')
    print(f'Surname: {...}')
    print(f'Born: {...}')
    print(f'Initials: {...}')
    ```

1. To improve readability, telephone numbers are often presented with a dash or space separating some digits. Write a program that prints a 9-digit telephone number entered from the keyboard as three groups of 3 digits each, separated by a dash character. Sample result:

    ```
    Enter phone number: 543097329
    Phone number: 543-097-329
    ```

    Complete the following program code.

    ```python
    ###
    # a program that prints a 9-digit telephone number
    # entered from the keyboard as three groups of 3 digits each,
    # separated by a dash character.
    #
    phone = input('Enter phone number: ')
    ...
    ...
    ```

1. In computer science, every written (graphic) character of human language (letters, digits, symbols, etc.) is encoded by assigning it a number. This allows characters to be stored, transmitted, and transformed using digital computers. To convert a character to its numerical representation, use the Python ord() function. 

    Write a program to print numerical representations of the following characters:

    a, b, z, A, B, Z, 1, =, +, €

    ```python
    ###
    # A program to print numerical representations of characters.
    #
    print(f'a {ord('a')}')
    print(f'b {ord('b')}')
    ...
    ...
    ```


1. Write a program that prints a numerical representation of each letter of your name. Sample result:

    ```python
    ###
    # A program that prints a numerical representation of each letter of your name.
    #
    name = 'John' # replace John with your name
    print(f'The letter {name[0]} has a code {ord(name[0])}')
    print(f'The letter {name[1]} has a code {ord(name[1])}')
    ...
    ...
    ```

1. Write a program that calculates how many letters are between two given letters. Then, using the program, calculate how many letters are between the letters:

    * A and D (2 letters)
    * B and M (10 letters)
    * K and K (0 letters)

    ```python
    ###
    # A program that calculates
    # how many letters are between two given letters
    #
    first = input('Enter first letter: ')
    last = input(...)
    first_letter_code = ord(first)
    ...
    number_of_letters = ...
    print(f'Between {first} and {last} is ... letters')
    ```

1. You can also check what character corresponds to the given code value. Use the available chr() function.

    Write a program that allows you to check what word is hidden in the following character codes:

    67, 111, 111, 108, 33

    ```python
    ###
    # Character code conversion
    #
    print(chr(67),chr(111),...)
    ```

1. Every programming language has a number of ready-to-use functions that you can use to manipulate strings. The most commonly used ones in Python can be found at:

    <https://www.w3schools.com/python/python_ref_string.asp>


    ```python
    ###
    # String manipulation
    #

    movie = "The Lord of the Rings: The Return of the King"

    # print number of characters
    print('Number of characters: ', len(movie))

    # print title in capital letters
    ...

    # print title in small letters
    ...

    # print how many times the vowel "e" appears in the title
    ...

    # print where in the text is the word "Lord"
    ...

    # print where in the text is the word "dragon"
    ...
    ```


## 7. Binary Operations

1. People up to and including 26 years of age are exempt from paying taxes in Poland. Write a program that, based on the person's age entered from the keyboard, prints True if the person is exempt from paying taxes and prints False otherwise. Then, check if the program works correctly for the following data (age in years):

    38, 27, 26, 22, 18

    ```python
    ###
    # People up to and including 26 years of age are exempt
    # from paying taxes in Poland. Write a program that,
    # based on the person's age entered from the keyboard,
    # prints True if the person is exempt from paying taxes
    # and prints False otherwise.
    #
    age = int(input('Enter age: '))
    no_tax = age < ...
    print(f'Exemption from paying taxes: {no_tax}')
    ```

1. The password is valid if it is at least 8 characters long. Write a program that checks whether the password length read from the keyboard is correct. Then, check if the program works correctly for the following passwords:

    university, peter123, (passwords ok)
    seven, anna333 (passwords to short)

    ```python
    ###
    # A program that checks whether the password length
    # read from the keyboard is correct.
    #
    password = input('Enter password: ')
    password_ok = len(password) >= ...
    print(f'Password length is valid: {password_ok}')
    ```

1. Write a program that checks whether the number entered from the keyboard is even. Print True when the number is even and False when the number is odd. A number is even if the remainder when divided by 2 is 0. Then, check if the program works correctly for the following numbers:

    24, 8, 31, 5

    ```python
    ###
    # A program that checks whether the number entered
    # from the keyboard is even.
    # A number is even if the remainder when divided by 2 is 0.
    # What operator do you need to use to calculate
    # the remainder of division?
    #

    number = int(input('Enter number: '))
    even = ...
    print(f'Number is even: {even}')
    ```

1. A tree may be cut down if its diameter is at least 50 cm. Write a program that, based on the circumference of the tree entered from the keyboard, calculates and prints the value True if the tree can be cut down, or print the value False otherwise. Sample result:

    ```
    Enter tree circumference in cm: 120 
    Tree can be cut down: False
    ```

    Then, check if the program works correctly. There are several trees in the garden with the given circumferences in cm. Which trees can be cut down?

    Tree 1: 160 
    Tree 2: 90
    Tree 3: 230
    Tree 4: 120

1. Vehicle registration numbers in Krakow start with the letters KR or KK. Write a program that checks whether the vehicle registration number entered from the keyboard means a vehicle from Krakow. Print True whether a car is from Krakow or False otherwise. Sample result:

    ```python
    ###
    # Vehicle registration numbers in Krakow start
    # with the letters KR or KK. Write a program that checks
    # whether the vehicle registration number entered
    # from the keyboard means a vehicle from Krakow.
    # Print True whether a car is from Krakow or False otherwise.
    #
    car_number = input('Enter car registration number')
    is_krakow = car_number[0:2] == "KR" or ...
    print('Car is from Krakow: {is_krakow}')
    ```

1. The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. Write a program that checks whether the vehicle speed entered from the keyboard is correct. Sample result:

    ```
    Enter vehicle speed: 158
    Speed is valid: False
    ```

1. Each programming language provides a set of functions that you can use in your programs. One of them is a function randint(a,b) that returns a integer random number in the range <a,b>. The function is available in a module called random, which you need to import into your program.

    <https://docs.python.org/3/library/random.html>

    Analyze the program below. Then, run the program five times and see what numbers are generated.

    ```python
    import random
    random_number = random.randint(5,10)
    print(random_number)
    ```


1. Write a program that prints results of three dice rolls and the sum of dice rolled. Apply a random number generator.

    ```python
    ###
    # A program that prints results of three dice rolls
    # and the sum of dice rolled.
    #
    import random
    dice_roll_1 = random.randint(...)
    dice_roll_2 = ...
    ...
    total = dice_roll_1 + ...
    print(...)
    ```

1. In many games, the numbers one and six on dice have special meaning. Write a program that prints the number of dice rolled and the value True if the number rolled is 1 or 6. Sample result:

    ```
    Dice rolled: 4
    Special number (1 or 6): False
    ```

1. Write a program that enables a user to challenge a computer. The computer throws dice. Then, the user then tries to guess the number from dice by entering a number from 1 to 6 from the keyboard. If the user has guessed the number from the dice, the computer prints True. Otherwise, the computer prints False.

    ```python
    ###
    # A program that enables a user to challenge a computer.
    # The computer throws dice. Then, the user then tries to guess
    # the number from dice by entering a number from 1 to 6
    # from the keyboard. If the user has guessed the number
    # from the dice, the computer prints True. Otherwise,
    # the computer prints False.
    #
    import random
    # COMPUTER TURN
    computer = random.randint(...)
    # YOUR TURN
    you = input(...)
    ...
    print(f'You won: {...}')
    ```

## 8. Practice Makes Perfect

1. Read the chapter in your class textbook that covers the topics in this section.

1. An algorithm is a step-by-step procedure or a set of rules designed to solve a problem. In computer science and mathematics, algorithms are critical because they provide a clear sequence of instructions that can be implemented to achieve a desired outcome.

    <https://www.programiz.com/dsa/algorithm>

    The following program code lists the steps to perform to calculate the area and circumference of a circle. Complete the program. Then, check the program for the following data:

    r = 1 --> circumference = 6.28, area = 3.14\
    r = 3 --> circumference = 18.84, area = 28.26
    
    ```python
    ###
    # Calculation of circle area and circumference 
    #

    # determine radius and PI values
    # calculate area 
    # calculate circumference 
    # print results
    ```

1. Write a program, a temperature converter, that reads temperature in degrees Celsius from the keyboard. Then, the program calculates and prints the temperature in Kelvin and Fahrenheit.

    ```python
    ###
    # A program that reads temperature in degrees Celsius from the keyboard.
    # Use comments to briefly describe the program's algorithm.
    #
    
    # ...
    # ...
    # ...
    ```



1. Write a program, a unit converter, that prints your height both in cm and in feet and inches. Use ue the division operator without remainder and the operator calculating the remainder of the division.

    ```python
    ###
    # A program that prints your height both in cm and in feet and inches.
    #
    cm = 170
    feet = ...
    inches = ...
    # calculate the number of feet

    print(f'I am {cm}cm tall, i.e. ... feet and ... inches')
    ```


1. A SWIFT code (also known as BIC - Bank Identifier Code) is a unique identification code used to identify a specific bank or financial institution globally. It is primarily used for international wire transfers and communication between banks.

    SWIFT code is typically 8 or 11 characters long and is composed of the following elements:

    * Bank Code (4 characters)
    * Country Code (2 characters)
    * Location Code (2 characters)
    * Branch Code (3 characters - optional)

    Write a program that reads a SWIFT code from the keyboard and prints the bank code and the country code. Then, use the program to print information for the following SWIFT codes:  
    BPKOPLPW, CHASUS33, DEUTDEFF.

    ```python
    ###
    # A program that reads a SWIFT code from the keyboard
    # and prints the bank code and country code.
    #
    swift = input('...: ')
    print(f'Bank Code: {...}')
    print('Country Code: ...')
    ``` 

1. A transport company needs a program to calculate the cost of transporting goods. The program calculates the cost of transporting goods based on the given distance in km, fuel price per 1 liter, and fuel consumption in liters per 100 km. Write such program.

    ```python
    ###
    # The program calculates the cost of transporting goods
    # based on the given distance in km, fuel price per 1 liter,
    # and fuel consumption in liters per 100 km.
    #
    distance = int(input('Enter distance in km: '))
    fuel_price = float(input('Enter fuel price per liter: '))
    fuel_consumption = float(input ...
    total_fuel_consumption = ...
    total_cost = ...
    print(...)
    print(...)
    ```

1. The binary numeral system is a positional numeral system that requires only two digits to write numbers: 0 and 1. The hexadecimal numeral system is a positional numeral system that uses sixteen distinct symbols, most often the symbols "0" to "9" to represent values 0 to 9, and "A" to "F" (or alternatively "a" to "f") to represent values from ten to fifteen. Both are widely used in mathematics, computer science and digital electronics. Write a program that reads an integer number from the keyboard and prints that value as a binary and hexadecimal number. To convert a decimal number to binary or hexadecimal value, use the available Python functions. Sample result:

    ```
    Enter number: 125
    Binary number: 0b1111101
    Hexadecimal number: 0x7d
    ```
