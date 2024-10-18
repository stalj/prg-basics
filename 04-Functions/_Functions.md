<!--
(c) Janusz Stal
Krakow University of Economics
Department of Informatics
stalj@uek.krakow.pl
-->

# FUNCTIONS

## 1. Introduction

1. Functions are reusable blocks of code that perform a specific task. They allow you to break down complex problems into smaller, more manageable parts, and help in avoiding code repetition by enabling reuse of the same block of code with different inputs.

    Every function has a name. To execute the code inside a function, you "call" the function by using its name followed by parentheses, including any arguments required by the function. 

    For example, if you want to print information on the screen, you use the `print()` function, using its name and, in parentheses, the function's arguments, if any are required.

    ```python
    print('Hello World')
    ```

## 2. Built-in Functions

1. There are a number of built-in functions, ready to use, e.g. `len()`, `print()`, `input()` or `type()`. 

    <https://docs.python.org/3/library/functions.html>

    Using built-in Python functions, write a program that calculates and prints:

    * the largest number: 7,5,6,3,8,2
    * the smallest number: 4,7,2,3,9,8
    * length of the phrase: \"computer science\"
    * letter read from the keyboard
    * number representing the string \"20303\"
    * binary string representing decimal number 304
    * hexadecimal string representing decimal number 304
    * integer representing the Unicode code of the € sign
    * absolute value of -17

    ```python
    ###
    # Program for testing built-in functions
    #
    max_number = max(7,5,6,3,8,2)
    print('Max number of 7,5,6,3,8,2 is', max_number)

    min_number = min(4,7,2,3,9,8)
    print('Min number of 4,7,2,3,9,8 is', min_number)

    str_length = len("computer science")
    print('The number of characters in "computer science" is', str_length)

    ...
    ...
    ```

## 3. Using Modules

1. In addition to the built-in functions, you can use numerous functions available in ready-to-use modules. One example is the `math` module.

    <https://docs.python.org/3/library/math.html>

    Using functions and constants available in the `math` module, write a program that calculates and prints:

    * square root of 7
    * natural logarithm of 5
    * sine of 90 degrees

    ```python
    ###
    # To use the functions available in an external module,
    # you must include that module in your program.
    import math

    square_root = math.sqrt(7)
    print('A square root of 7 is', square_root)
    
    ...
    ...
    ```

1. Write a program that generates and prints a random number between 1 and 6, similar to rolling a dice. Use one of the functions from the `random` module to generate a random integer within a given range.

    <https://www.w3schools.com/python/ref_random_randint.asp>

    ```python
    ###
    # Generates and prints a random number between 1 and 6,
    # similar to rolling a dice
    #
    import random

    ...
    ...
    ```

## 4. Defining a Function

1. Watch the videos on defining a function:

    <https://youtu.be/89cGQjB5R4M?feature=shared>

1. A function is defined using the def keyword, followed by the function name, parentheses, and a colon. Inside the parentheses, you can specify parameters that the function can accept. The function's code block is indented.

    ```python
    def function_name(parameters):
        # Code block (function body)
        return result  # Optional: Returns a value
    ```

    Components of a Function:

    * `def`: Keyword used to define a function.
    * `function_name`: The name of the function. It should be descriptive of the task the function performs.
    * `parameters`: Optional inputs that the function accepts. They are defined inside the parentheses.
    * `Function Body`: Code block that contains the logic of the function. This code is executed whenever the function is called.
    * `return`: Optional statement that specifies the value to be returned by the function.

    Take a look at the function below that allows you to sum two numbers. The add function takes two parameters, `a` and `b`, and returns their sum. The returned value is stored in the variable `sum_value` and then printed.

    ```python
    def add(a, b):
        result = a + b
        return result

    sum_value = add(5, 3)
    print(sum_value)  # Output: 8
    ```

1. Define a function `triangle_area` that calculates and returns the area of ​​a triangle with sides `a`, `b`, and `c`. Use Heron's formula:

    <https://en.wikipedia.org/wiki/Heron%27s_formula>

    Write a program that calculates the area of ​​a triangle based on the lengths of the triangle's sides read from the keyboard. Use the defined function. Then calculate the area of ​​the triangle for the following dimensions of sides `a`, `b`, and `c`:

    * 3, 4, 5 (result is 6)
    * 5, 12, 13 (result is 30)
    * 7, 24, 25 (result is 84)

    ```python
    ###
    # Calculates the area of a triangle based on the lengths
    # of the triangle's sides
    #
    def triangle_area(a,b,c):
        ...
        return ...

    print('The area of ​​a triangle with sides ... is ...')
    print('The area of ​​a triangle with sides ... is ...')
    print('The area of ​​a triangle with sides ... is ...')
    ```

1. Define a function that calculates and returns the sum of the digits in a number. Then write a program that reads a number from the keyboard and prints the sum of its digits.

    **Steps of the algorithm to sum digits in a number:**
    
    1. Take an integer input from the user. The number can be positive, negative, or zero.
    1. Handle Negative Numbers: Convert the number to its absolute value using the `abs()` function. This step ensures the algorithm correctly processes negative numbers by ignoring the negative sign.
    1. Convert to String: Convert the number to a string using `str()`. This allows iteration over each digit in the number.
    1. Iterate Over Digits:
        * Loop through each character (digit) in the string representation of the number.
        * Convert each character back to an integer.
    1. Sum Digits: Add each integer value to a running total.
    1. Output the Result: Return the sum of the digits

    ```python
    ###
    # Calculates the sum of the digits in a number
    #
    def sum_digits(number):
        ...
        ...
        return ...
    
    any_number = int(input('Enter integer number: '))
    result = sum_digits(...)
    print('The sum of the digits in the number ... is ...')
    ```

1. Define a function that calculates the final grade for a test based on the number of points obtained, according to the rules:

    * Less than 10 points, final grade: Fail
    * At least 10 points, final grade: Satisfactory
    * At least 14 points, final grade: Good
    * At least 18 points, final grade: Excellent

    ```python
    ###
    # Calculates the final grade for a test based
    # on the number of points obtained
    #
    def pts_to_grade(points):
        grade = ''
        if points >= 18:
            grade = 'Excellent'
        ...
        ...
        return grade

    test_result = 15
    final_grade = pts_to_grade(test_result)
    print('You scored ... points on the test. Your final grade is ...')
    ```


1. Define a function that returns the full name of a day of the week based on its number.

    ```python
    ###
    # Function that returns the full name of a day of the week
    # based on its number
    #
    def day_name(day_number):
        result = ''
        if day_number == 1:
            result = 'Monday'
        elif day_number == 2:
            ...
        ...
        ...
        return result

    # Function usage
    print('The name of day 5 in the week is', day_name(5))
    print('The name of day 3 in the week is', day_name(3))
    print('The name of day 7 in the week is', day_name(7))
    ```

1. The ICAO (International Civil Aviation Organization) phonetic alphabet is used internationally for spelling out letters in radio communication. The icao.py program contains a function that returns the corresponding word for a given letter. Complete the program to spell out a name entered from the keyboard.

1. Define a function `time_string(hours, minutes, time_format)` that, given the number of hours (0..23) and the number of minutes (0..59), returns a string specifying the time in the given format ('24' for 24-hour time and '12' for 12-hour time).

    Then write a program that tests whether the function works correctly.

    * time_string(15, 38, '24') returns '15:38'
    * time_string(8, 3, '24') returns '08:03'
    * time_string(0, 5 '24') returns '00:05'
    * time_string(11, 15, '12') returns '11:15am'
    * time_string(0, 7, '12') returns '12:07am'
    * time_string(7, 30, '12') returns '7:30am'
    * time_string(12, 46, '12') returns '12:46pm'
    * time_string(13, 10, '12') returns '1:10pm'
    * time_string(19, 02, '12') returns '7:02pm'

    Hint: Use `f-strings` formatting. Search the Internet for 'Format numbers using f-strings'.

## 5. Dividing Program Code into Modules

1. Familiarise yourself with dividing a program code into modules:

    <https://www.w3schools.com/python/python_modules.asp>

    <https://docs.python.org/3/tutorial/modules.html>

1. The `converters.py` file defines two functions for converting length units (cm-->m and m-->cm). The test_converters.py file uses these functions to convert values.

    Define the following functions in the `converters.py` file that allow you to:

    * convert centimeters to inches
    * convert feet and inches to centimeters

    Then complete the main program to test the added functions.

1. As you remember, the `input()` function allows you to read only a string from the keyboard. In the module `keyboard.py`, define your own functions that allow reading other types of data from the keyboard:

    * `input_string()` that returns a string entered from the keyboard
    * `input_integer()` that returns an integer number entered from the keyboard
    * `input_real()` that returns a real number entered from the keyboard
    * `input_boolean()` that returns a boolean value depending on the pressed y/n key
    
    ```python
    ###
    # Functions to read any data type from the keyboard
    #
    def input_string(message):
        ... = input(message)
        return ...

    def input_integer(message):
        ... = input(message)
        return ...

    def input_real(message):
        ... = input(message)
        return ...

    def input_boolean(message):
        ... = input(message)
        return ...
    ```

    Then, write a program that allows you to enter and print employee data. Due to personal data protection, you can determine whether information about the employee's salary will be printed.

    > Hint: when importing a module, note that:
    > * the name of the module to be imported is given without the file name extension (only the name itself)
    > * the program first searches for the module in the same folder where the program is located

    ```python
    ###
    # Allows to enter and print employee data. Due to personal
    # data protection, you can determine whether information about
    # the employee's salary will be printed
    #
    import keyboard # your own defined module

    # Reads employee's data from keyboard
    first_name = input_string('Enter name: ')
    last_name = ...
    age = ...
    salary = ...
    is_salary_hidden = input_boolean('Hide salary? (y/n)')

    # Prints employee's record
    print('DATA RECORD')
    print('===========')
    print('Name:', ...)
    print(...)
    print(...)
    if ...:
        print('Salary')
    ```

1. The following program draws a square with a specified side length using the turtle module.

    ```python
    import turtle

    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Side length
    side_length = 100

    # Draw a square
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()
    ```

    Save the program in the file `draw_figures.py`. Then, run the program. Next, change the program so that the square is drawn using the `draw_square(length)` function with the only parameter being the length of the square's side. Place the defined function in a separate module `figures.py`. Finally, run the program again.

    ```python
    ###
    # Draw a square
    #
    def draw_square(length)
        ...
        ...
    ```

1. In the `figures.py` module, add the following function definitions:

    * `draw_trangle(length)` to draw an isosceles triangle
    * `draw_rectangle(lenght_a, lenght_b)` to draw a rectangle with sides a and b

    Then, write a program which draws each of the figures (square, triangle, rectangle) twice, in different locations. To draw a figure in a different place, use the information below.

    * `pen.penup()`: Lifts the pen so that the turtle can move without drawing.
    * `pen.goto(-100, 100)`: Moves the turtle to the coordinates (-100, 100). You can change these values to move the turtle to any location on the screen.
    * `pen.pendown()`: Puts the pen down to start drawing again.

    By using `penup()` and `pendown()`, you can control when the turtle draws on the screen and move it freely to any location.

    ```python
    ###
    # Draws each of the figures (square, triangle, rectangle) twice,
    # in different locations
    #
    import ...
    import turtle

    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)   
    
    ## Draw figures
    ...
    ...
    ...
    
    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()
    ```

## 7. Practice Makes Perfect

1. Read the chapter in your class textbook that covers the topics in this section.

1. In Python, the `__name__ == "__main__"` construct is commonly used to control the execution of code when a Python file is run directly versus when it is imported as a module in another file.

    The `if __name__ == "__main__":` block ensures that certain parts of the code are only executed when the file is run directly, and not when it is imported. Look at the following example:

    ```python
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    if __name__ == "__main__":
        # This block will only execute when the script is run directly
        x = 10
        y = 5
        print(f"Add: {add(x, y)}")
        print(f"Subtract: {subtract(x, y)}")
    ```

    Try using this construction in your future tasks where you define functions. To test the function, place the function call statements in an `if __name__ == "__main__":` block, as in the example above.

    If you want your programs to look really professional, you can also define a main() function. It is considered good practice to define a main() function in larger or more complex programs to improve code organization and readability. It's really very simple. See the example below:

    ```python
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def main():
        # This block will only execute when the script is run directly
        x = 10
        y = 5
        print(f"Add: {add(x, y)}")
        print(f"Subtract: {subtract(x, y)}")

    if __name__ == "__main__":
        main()
    ```

1. Each month of a calendar year can be expressed by its name or by a number that indicates the position of the month in year. In a separate module, define a function month(n) that returns a month name based on the month number (values from 1 to 12). Then, write a program to print the name of the month 7. Import the module with the created function. Sample result:

    ```
    Enter month number: 9
    The name of month 9 is September
    ```

1. Write a program that calculates how many times the given letter appears in any text. Then create a program and check how many times the letter 'e' appears in the text below. In a separate module, define a function for making calculations. Sample result:

    ```
    You never get a second chance to make a first impression
    The number of letter 'e': 7
    ```

1. In a separate module, define a function that checks if the number is within the range `<x, y>`. The function returns a boolean value. Then, create a program and use the function you defined. Sample result:

    ```
    A number: 7
    Number 7 in the range <2,15>: yes
    ```

1. The credit card number consists of 16 digits. In a separate module, define a function `hide(card_number)` that masks the card number. The function returns a character string in which only the first two and the last four digits of the card number are visible. The remaining digits of the card number are replaced with an asterisk. Then, create a program that masks some credit card digits. Import the module with the created function. Finally, print the credit card number. Sample result:

    ```
    f("5290312400019022") returns "52**********9022"
    ```

1. The binary numerical system uses two symbols to represent a number: 0 and 1. Define a function `f(binary_number)` that returns True if the given string of digits is a valid binary number, or False otherwise. Sample result:

    ```
    f("101101") returns True
    f("1311a10100") returns False
    ```

1. The vending machine accepts 1, 2 and 5 PLN coins. Define a function `f(amount_to_pay)` that returns the minimum number of coins that can be used to pay for the purchased product. Sample result:

    ```
    f(23) returns 6
    f(8) returns 3
    f(2) returns 1
    f(0) returns 0
    ```

1. Create a function `f(number, even)` that computes the sum of the digits of a number. When the value of the even parameter is True, the function returns the sum of the even digits. When the value of the even parameter is False, the function returns the sum of the odd digits. Sample result:

    ```
    f(3124,True) returns 6
    f(3124,False) returns 4
    f(20576,False) returns 12
    f(20576,True) returns 8
    f(13115,True) returns 0
    ```

1. Define the function `f(x,y)` that returns the number of negative even numbers in the range `<x,y>`. Sample result:

    ```
    f(-7,8) returns 3
    f(-1,11) returns 0
    ```

1. Define the function `f(n1,n2,n3)`, which returns `True` if at least one of the numbers `n1,n2,n3` is negative or False otherwise. Sample result:

    ```
    f(11,6,-4) returns True
    f(5,4,14) returns False
    ```

1. Define a function f(n) that returns a string of `n` asterisks, separated by a slash sign. Sample result:

    ```
    f(4) returns "*/*/*/*"
    f(1) returns "*"
    ```

1. Define the function `f(n)`, which returns numbers from 1 to n as a string. Sample result:

    ```
    f(11) returns "1234567891011"
    f(4) returns "1234"
    ```

1. Two numbers and an operator are given. Define a function `f(number1,number2,operator)` that returns the result of an arithmetic operation. The available operators are `+,-,*,%,**`. Sample result:

    ```
    f(2,3, "+") returns 5
    f(2,3, "%") returns 2
    f(2,3, "**") returns 8
    f(2,3, "*") returns 6
    f(2,3, "-") returns -1
    ```

1. A device in a door registers people entering and leaving a room.The + sign means a person entering a room and the -- sign a person leaving a room. Define the function `f(detector)` that returns `True` if at least 3 people were in the room at the same time, or False otherwise. Sample result:

    ```
    f("+-+++-+---") returns True
    f("+-+-+-+-") returns False
    f("+-++-+--") returns False
    f("+-++-++-+---") returns True
    ```

1. Define the function `f(n)`, which returns the n-th value of the Fibonacci sequence. The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. Each subsequent value is the sum of the previous two. Sample result:

    ```
    f(5) returns 3
    f(9) returns 21
    ```

1. A palindrome is an expression that sounds the same when read backwards. Define a function `f(palindrome)` that returns True if the expression is a palindrome or False otherwise. Sample result:

    ```
    f("radar") returns True
    f("12-11-21") returns True
    f("book") returns False
    ```

1. A sentence is an ordered group of words separated by spaces. Define a function `f(sentence)` that returns a sentence with spaces removed. Sample result:

    ```
    f("integrated development environment") returns
    "integrateddevelopmentenvironment"
    f("A programming language is a system of notation for writing
    computer programs") returns
    "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"
    ```

1. Define a function `f(number)` that returns the sum of repeated digits in a number. Sample result:

    ```
    f(1027) returns 0
    f(230335) returns 9
    f(513553007) returns 21
    ```

1. Define the function `f(n)` that returns the n-th prime number. A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:

    ```
    f(1) returns 2
    f(5) returns 11
    ```

1. Define the function `f(number1,number2,number3)`, which returns the difference between the largest and smallest numbers. Sample result:

    ```
    f(7,4,9) returns 5
    f(2,12,8) returns 10
    ```

1. A text contains any number of words. Define a function `f(name)` that returns the acronym (first letters of all words). Sample result:

    ```
    f("Internet of Things") returns "IoT"
    f("For Your Information") returns "FYI"
    f("Python") returns "P"
    ```

1. A valid password should consist of at least six characters and each character appears only once in the password. Define a function `f(password)` that returns True if the password is correct or False otherwise. Sample result:

    ```
    f("ax15") returns False
    f("book123") returns False
    f("A2water3") returns True
    f("qwerty") returns True
    f("") returns False
    ```

1. An expression contains operators for adding and subtracting single-digit numbers. Define a function `f(expression)` that returns the value of the expression. Sample result:

    ```
    f("2+3") returns 5
    f("3+8+1") returns 12
    f("2+3-4+5-0") returns 6
    ```

1. Define the function `f(x,y)`, which returns the sum of numbers in the range `<x,y>` that are completely divisible by 2 and 3 and not divisible by 4. Sample result:

    ```
    f(1,20) returns 24
    f(10,30) returns 48
    ```

1. Define a function `f(text)` that returns the given text with all characters separated by a dash sign. Example:

    ```
    f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
    f("UE") returns "U-E"
    f("x") returns "x"
    f("") returns ""
    ```

1. Products are marked with a special code consisting of 3 digits and afourth control digit. The forth digit is determined by calculating the remainder of dividing the sum of the first three digits by 7. Define a function `f(product_code)` that returns `True` if the product code is correct or `False` otherwise. Sample result:

    ```
    f("1082") returns True
    f("2035") returns True
    f("1114") returns False
    f("7071") returns False
    ```

1. The sequence of digits contains the number of points rolled with a dice. Define a function `f(dice)` that returns a number specifying the number of dice rolled the most times in a row. Sample result:

    ```
    f("5233165554211") returns 5
    f("2133") returns 3
    ```

1. The following function calculates the factorial recursively. Try to analyse the function. Do you understand how it works? Then, write a program and use the function to calculate the factorial value for n = 5.

    ```python
    def factorial(n):
    
    # 0! = 1, 1! = 1
        if n==0 or n==1:
            return 1
    
    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)
    ```

1. Define a function `sum_natural(n)` that for the given natural number n calculates the sum of all natural numbers between 1 and n. Apply recursion. Then, create a program that calculates the sum of natural numbers in the range `<1,10>`.

1. Define a function `power(x, n)` that calculates x<sup>n</sup>. Apply recursion. Then, calculate 5<sup>3</sup>.

    > Tip: x<sup>n</sup> = x * x<sup>n-1</sup>
