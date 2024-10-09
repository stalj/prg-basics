<!--
(c) Janusz Stal
Krakow University of Economics
Department of Informatics
stalj@uek.krakow.pl
-->

# CONTROL STRUCTURES

## 1. Decision Statement

1. Watch the videos on using **if-then-else** conditional statements:

    <https://youtu.be/FvMPfrgGeKs?feature=shared>

    > In your free time you can also watch other videos available on the Internet, such as:  
        <https://youtu.be/Zp5MuPOtsSY?feature=shared>  
        <https://youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er->

1. Decision statements in Python are used to make decisions based on logical conditions. The main decision-making structure is the if statement, which allows a block of code to be executed if a given condition is true.

    Familiarise yourself with the basic **if** statement syntax:

    ```python
    if condition:
        # code to execute if the condition is true
    else:
        # code to execute if the condition is false
        # (note that else is optional)
    ```

1. The speed limit on a motorway in Poland is 140 km/h. The following program
    checks whether a car exceeded the speed limit. If so, a warning
    is printed. Complete the program.

    ```python
    ###
    # Checking whether a car exceeded the speed limit
    #
    speed_limit = 140
    car_speed = int( input('Enter car speed (km/h): ') )
    
    if car_speed ...:
        print(f'Your speed is {...}km/h')
        print('Warning: speed limit exceeded!!')
    ```

1. A payment terminal in a store allows card payments. The customer has money in his bank account. The total value of purchases is given. The terminal prints a message whether the payment can be made or whether there are no funds in the customer's bank account. Write a program that acts as a payment terminal. Then, use the program and pay for the purchases below.

    140, 499, 500, 501, 720 (for the last two amounts, there are no funds)

    ```python
    ###
    # Credit card payment 
    #
    account_balance = 500
    total_payment = input ...
    
    if total_payment ... account_balance:
        print('Payment completed')
    else:
        print('No funds')
    ```

1. A test is passed when the number of correctly completed tasks is at
    least 50%. Write a program that checks whether the test is passed. Then use the program to check if you passed the test for the following number of properly performed tasks:

    20, 11, 10, 9, 0 

    ```python
    ###
    # Checking whether the test is passed
    # Test is passed when the number of correctly completed
    # tasks is at least 50%
    #
    total_tasks = 20
    tasks_ok = ...
    test_passed = False
    
    if tasks_ok ... total_tasks ... :
        test_passed = True
    
    if test_passed:
        print('Congratulations! You passed the test.')
    else:
        print('Unfortunately, you failed the test.')
    ```

1. Write a program that checks whether the number entered from the
    keyboard is even or odd.

    ```python
    ###
    # Checking whether the number
    # entered from the keyboard is even or odd 
    #
    number = int(input('Enter number: '))
    
    if number % 2 ...:
        print(f'{...} is even')
    else:
        print(f'{...} is odd')
    ```

1. The employee's basic salary is PLN 5000. The employee may receive a bonus of several percent of the basic salary. Write a program that calculates the employee's salary, taking into account the possibility of receiving a bonus. Then calculate the employee's total salary for the following cases:

    * The employee does not receive a bonus
    * The employee receives a bonus of 30%

    ```python
    ###
    # Program that calculates the employee's salary,
    # taking into account the possibility of receiving a bonus.
    #
    basic_salary = 5000
    total_salary = 0
    is_bonus = True # does the employee receive a bonus
    bonus = 0.15 # 15%
    
    if ...:
        total_salary = ...
    else:
        ...
    
    print('Basic salary: {...}')
    print('Bonus included? {...}')
    print('Total salary: {...}')
    ```


## 2. Multiple Conditions

1. In Python, **elif** (short for "else if") is used in conditional statements to check additional conditions if the previous **if** or **elif** was false. It allows you to execute different blocks of code depending on which condition is true. Using **elif** helps avoid nesting multiple **if** statements, making the code more readable and manageable.

    Notice the basic syntax of the **elif** statement:

    ```python
    if condition1:
        # code to execute if condition1 is true
    elif condition2:
        # code to execute if condition1 is false and condition2 is true
    elif condition3:
        # code to execute if condition2 is false and condition3 is true
    else:
        # code to execute if all the above conditions are false
    ```

    * The elif statement is only executed if the previous **if** (or **elif**) condition is false.
    * You can use as many **elif** statements as needed.
    * Optionally, you can have an **else** statement at the end, which will execute if none of the conditions are true.

1. Clothing sizes are often labeled with letter symbols. Write a program that prompts the user to enter a clothing size and then prints a verbal description of the clothing size, as below.

    * S: Small size
    * M: Medium size
    * L: Large size
    * XL: Extra large size
    * Incorrect symbol (if entered symbol dirrerent than S, M, L, XL)

    Then check the correctness of the program for each of the size symbols.

    ```python
    ###
    # A program for checking clothing sizes
    # S: Small size, M: Medium size, L: Large size
    # XL: Extra large size or Incorrect symbol (if entered symbol
    # dirrerent than S, M, L, XL)
    #
    size = input('Enter size symbol: ')

    if size == 'S':
        print('S: Small size')
    elif size == 'M':
        print(...)
    ...
    else:
    ...
    ```

1. The car has three driving modes: Auto (A), Manual (M) and Eco (E). In each of these three modes, the average fuel consumption in liters per 100 km is 7, 9 and 6 respectively. Write a program that calculates total fuel consumption for a given distance in km and a given driving mode. Then, calculate the total fuel consumption for the following data:

    * distance 200 km, driving mode M (the result should be 18 liters) 
    * distance 400 km, driving mode A (the result should be 28 liters) 
    * distance 350 km, driving mode E (the result should be 21 liters) 

    ```python
    ###
    # The car has three driving modes: Auto (A), Manual (M) and Eco (E).
    # In each of these three modes, the average fuel consumption in liters
    # per 100 km is 7, 9 and 6 respectively. Write a program that calculates
    # total fuel consumption for a given distance in km and a given
    # driving mode.
    #
    driving_mode = input('Enter driving mode (A/M/E):')
    distance = int(input('Enter distance in km'))

    if driving_mode == 'A':
        fuel_consumption = 7 # liters per 100km
    elif driving_mode == 'M':
        ...        
    ...

    total_consumption = ...
    print('Total fuel consumption over a distance of ... km in driving mode ... is ... liters')
    ```

1. Write a program that acts as a simple calculator. The program asks the user to enter a symbol of mathematical operation (+, -, *, /) and two numbers. Then, the program performs the appropriate mathematical operation on the given numbers and returns the result. Using the program, calculate:

    * 2 + 3
    * 2 * 4
    * 3 - 5
    * 5 * 6

    ```python
    ###
    # Simple calculator
    # Asks the user to enter a symbol of mathematical operation (+, -, *, /)
    # and two numbers. The program should perform the appropriate
    # mathematical operation on the given numbers and return the result.   
    # 
    number1 = input ...
    number2 = input ...
    operator = input ...

    if operator == ...:
        result = ...
    elif ...
    ...
    ...

    # print result
    print(f'{number1} {operator} {number2} = {result}')
    ```

1. Write a program that calculates and prints the quarter of the year for a given month number (1..12). Then check the program's results for the months:

    12, 10, 9, 1

    ```python
    ###
    # Calculates and prints the quarter of the year for a given
    # month number (1..12)
    #
    month = int(input('Enter month number (1..12): '))

    if month >= 10:
        quarter = 4
    elif ...:
        ...

    print('Month {...} is in quarter {...}')
    ```

1. Write a program that checks what number was entered from the keyboard and prints one of the messages below. Then run the program and check the following numbers:

    7, 1 ,0 ,-1 , -4

    * Number ... is positive
    * Number ... is negative
    * Number is 0

## 3. Logical Operators

1. You can combine conditions using logical operators like **and**, **or**, and **not**:

    * **and**: All conditions must be true.
    * **or**: At least one condition must be true.
    * **not**: Inverts the logical value of the condition.

1. Write a program that checks whether the entered login and password are correct.

    ```python
    ###
    # Checking login and password
    #
    login = 'joe'
    password = 'abcd'
    entered_login = input('Login: ')
    entered_password = input('Password: ')
    if login == entered_login and ... :
        print('You are logged in')
    else
        print('Incorrect login or password!!')
    ```

1. The discount is available to children under 18, or people 65 or older. Write a program that checks whether a person of a given age is eligible for the discount. Then use the program to check if people of the age listed below are eligible for a discount.

    72 (discount), 65 (discount), 64, 18, 17 (discount)

    ```python
    ###
    # Checking if discount is available
    # The discount is available to children under 18,
    # or people 65 or older.
    #
    age = int(input('Enter your age: '))

    if age < 18 or ... :
        print(...)
    else:
        print(...)
    ```

1. A user enters two integer numbers from the keyboard. Write a program
    that checks whether at least one of them is not negative.

    ```python
    ###
    # Checks whether at least one number entered
    # from the keyboard is not negative
    # 
    x = int(input('Enter first number: '))
    y = ...
    
    if not x < ... or ... :
        print(f'At least one of the numbers {} and {} is not negative')
    ```

1. Write a program that calculates and prints the number of days in a given month (1..12). Assume that February always has 28 days.

    ```python
    ###
    # Calculates the number of days in a month
    #
    month = int(input('Enter month number (1..12)'))
    
    if month==1 or month==3 or ... :
        days = 31 ## months with 31 days
    elif ... :
        days = ... ## months with 30 days
    ...
    ## February 28 days 
    
    print('Month ... has ... days')
    ```

1. Write a program that checks if the given day number of the month is correct. Then, run the program for the following data:

    * month 3, day 17
    * month 9, day 31
    * month 2, day 30

    ```python
    ###
    # Checks if the given day number of the month is correct
    #
    month = int(input('Enter month number (1..12): '))
    day = int(input('Enter the day number of the month: '))
    day_ok = False
    
    if month==1 or month==3 or ...:
        if day >=1 and day <= 31:
            day_ok = True
    elif month== ...:
        if day >=1 and day <= ...:
            ...
    ...
    
    message = f'Day {...} for the month {...}'
    if day_ok:
        print('{message} is correct')
    else
        print(...)
    ```

## 4. Iteration Over a Sequence

1. Watch the video on using the **for** statement:

    <https://youtu.be/KWgYha0clzw?feature=shared>

1. The **for** loop is used to iterate over a sequence and execute a block of code for each item in the sequence.

    Here is the basic syntax of the **for** statement:

    ```python
    for item in sequence:
        # code block to execute
    ```

    Look at the following example, which takes every character from a string and prints it on the screen. Then run the program.

    ```python
    city = 'Krakow'
    for char in city:
        print(char)
    ```

    You can use range() to loop over numbers:

    ```python
    for i in range(5):
        print(i)
    ```

1. The following program prints the sentence "Practice makes perfect!" four times. Modify the program to print the text six times. Then run the program.

    ```python
    for i in range(4):
        print('Practice makes perfect!')
    ```

1. Write a program that prints the name of university where you are studying with an extra space between characters (add a space between each character).

    ```python
    ###
    # Prints the name of university where you are studying
    # with an extra space between characters (add a space between
    # each character)
    #
    university = 'Krakow University of Economics'
    university_expanded = ''

    for char in university:
        univerity_expanded = ...university_expanded + ... + ...

    print(...)
    print(...)
    ```

    Sample result:

    ```
    Krakow University of Economics
    K r a k o w   U n i v e r s i t y   o f   E c o n o m i c s
    ```

1. The Caesar cipher (also known as Caesar's code or Caesar shift) is one of the simplest and oldest encryption techniques. It is named after Julius Caesar, who reportedly used it to communicate secretly with his generals. The cipher is a type of substitution cipher, where each letter in the plaintext is shifted a certain number of places down the alphabet. 

    Write a program that encrypts text using Caesar Code, shifting each letter in the alphabet right one position.

    ```python
    ###
    # Encrypts text using Caesar Code, shifting each letter
    # in the alphabet right one position
    #
    plain_text = 'The early bird catches the worm'
    encrypted_text = ''

    for char in plain_text:
        # read the character's code (use ord())
        ...
        # add one to the character's code
        ...
        # replace new character code with its
        # corresponding character (use chr())
        ...
        # add encrypted character to encrypted text
        ...

    print(plain_text...)
    print(encrypted_text...)
    ```

1. The following program calculates the sum of integer numbers in the range \<1,5\>. Make the following changes to the program:

    * sum the numbers from 5 to 10
    * use the **+=** operator in the expression **sum=sum+i**

    ```python
    ###
    # Calculates the sum of integer numbers in the range <1,5>
    #
    sum = 0

    for i in range(1,6):
        sum = sum + i
    
    print(f'Sum is {sum}')
    ```

1. Write a program that calculates the sum of even numbers in the range \<1,10\>.

    ```python
    ###
    # Calculates the sum of even numbers in the range <1,10>
    #
    sum = 0
    
    for i n range(...):
        if not i%2...:
            continue
        sum += ...
    
    print('Sum of even numbers in the range <1,10> is ...')
    ```

1. Write a program that calculates values for the following fractions: 1/2, 1/3, ..., 1/10. Sample result:

    1/1 = 1.0\
    1/2 = 0.5\
    1/3 = 0.3333333333333333\
    ...\
    1/10 = 0.1

    ```python
    ###
    # Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
    #
    for i in range(...):
        print('1/{...} = {...}')
    ```

## 5. Conditional Iteration

1. Watch the video on using the **while** statement:

    <https://youtu.be/APWy6Pc83gE?feature=shared>


1. The ***while** loop executes a block of code as long as a specified condition is True.

    Here is the basic syntax of the **while** statement:

    ```python
    while condition:
        # code block to execute
    ```

    Look at the following example. Then try to run the program.

    ```python
    count = 0
    while count < 5:
        print(count)
        count += 1
    ```

1. 
    ```python
    ###
    # Prints a greeting
    #
    name = ''

    while name == '':
        name = input('Enter your name: ')

    print(f'Hello {name}')
    ```

1. The program below is a simple number guessing game. Analyze the program code. Then complete the program. 

    ```python
    ###
    # A simple number guessing game
    #
    import random

    # Randomly chosen number to be guessed from 1 to 100
    number_to_guess = random.randint(1, 100)
    user_guess = 0

    print("Guess the number between 1 and 100!")

    while user_guess != number_to_guess:
        user_guess = int(input("Enter your guess: "))

        if user_guess < ...:
            print("Too low! Try again.")
        elif ...:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
    ```

1. The following program sums numbers input by the user until they enter 0. Modify the program so that it also calculates the arithmetic mean of the numbers.

    ```python
    ###
    # Sums numbers entered by user
    #
    total_sum = 0

    while True:
        number = int(input("Enter a number (0 to stop): "))
        
        if number == 0:
            break  # Exit the loop when 0 is entered
        total_sum += number

    print(f"The total sum of the numbers is: {total_sum}")
    ```

1. The following program calculates the sum of even numbers from 1 to a given number N using a for loop. Modify the program. Replace the 'for' statement with a 'while' statement.

    ```python
    ###
    # Calculates the sum of even numbers from 1 to a given number N
    #
    N = 10
    sum_even = 0

    # Calculate the sum of even numbers
    for i in range(1, N + 1):
        if i % 2 == 0:
            sum_even += i

    print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
    ```



1. The timer.py program takes a number from the user and counts down to zero. Modify the program so that the last five seconds of the counter are printed in words, i.e. five, four, three, two, one.

1. The atm.py program simulates a simple ATM where the user can deposit, withdraw, or check the balance. Analyze the program code and then run the program. Next, add two more functions to the program:

    * Check PIN
    * Change PIN

    The PIN should consist of exactly 4 digits. To check if a string contains only digits, you can use the isdigit() method. This method returns True if all characters in the string are digits and False otherwise:

    <https://www.geeksforgeeks.org/python-string-isdigit-method/>



## 6. Practice Makes Perfect

1. Read the chapter in your class textbook that covers the topics in this section.

1. The vowels.py program counts vowels in the text. Modify the program. Replace the 'for' statement with a 'while' statement. 

1. A lamp in a room has three light bulbs. Switch one lights one bulb, and switch two lights the other two bulbs. Write a program that tells you how many bulbs are lit, depending on the state of switch one and switch two.

    ```python
    ###
    # House lighting with three bulbs and two switches
    # Checking how many bulbs are illuminating the house
    #
    light_switch1 = False # False - switch off, True - switch on
    light_switch2 = False
    bulbs_on = 0
    if light_switch1:
        bulbs_on += 1
    if light_switch2:
        ...
    print(...)
    ```

1. Password length has a significant impact on the level of data protection. Write a program that checks whether the new password provided is at least 12 characters long.

    ```python
    ###
    # Password validator
    # New password is at least 12 characters long
    #
    new_password = input('Enter new password: ')
    if len(...) < ...:
       print('Password too short (min. 12 chars)') 
    ```

1. The electronic thermometer prints the temperature in degrees Celsius and verbal information according to the following criteria:

    * It is extremely hot, for a temperature above 35 degrees,
    * It is hot, for a temperature above 30 degrees,
    * It is warm, for a temperature of at least 15 degrees,
    * It is cold, for a temperature of at least 0 degrees,
    * Warning, frost, for a temperature below 0 degrees.

    Write a program that simulates the operation of an electronic thermometer. Then check the correctness of the program for the following temperatures in degrees Celsius: 

    33, 30, 8, 0, -2

    ```python
    ###
    # Program that simulates the operation of an electronic thermometer.
    #
    temperature = 32
    if temperature > 35:
        print("It is extermely hot")
    elif temperature > 30:
        print ...
    elif ...
    ```

1. The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:

    * 1-2 hours: 5 PLN
    * 3-6 hours: 15 PLN
    * Over 6 hours: 20 PLN

    Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.

1. Write a program that asks the user for their age and then checks which age group they belong to:

    * Child: under 13
    * Teen: 13 to 19
    * Adult: 20 to 64
    * Senior: 65 or older

1. Write a program that checks that both people are adults. Read
    people's data from the keyboard.

    ```python
    ###
    # Checking if both people are adults
    #
    person1_name = input('Enter first person name: ')
    person1_age = int(input('Enter first person age: '))
    person2_name = ...
    person2_age = ...
    if person1_age >= 18 and person2 ...:
        print('Both {person1_name} and {...} are ...')
    else:
        print('Either {...} or {...} is not an adult')
    ```

1. Most female names in Polish end with the letter \"a\". Write a program that prints the name entered from the keyboard, provided it is a female name. Sample result:

    Enter name: Anna\
    Anna -- Polish female name

1. Write a program that calculates a dog\'s age in dog's years. For the first two years, a dog\'s life is equal to 10.5 human years. After that, each dog year is equal to 4 human years. Sample result:

    Enter the dog\'s age in human years: 15\
    The dog\'s age in dog's years is 73 years.

1. A computer program analyses the price of a product in an online store. If the product price decreases by at least 10%, the program prints a purchase recommendation:

    Buy the product!!\
    Product price reduced by 17%

    Create such program. The current and previous price of the product are included in variables. Sample result:

    Current product price: 140.00\
    Previous product price: 200.00\
    Buy the product!!\
    Product price reduced by 30%

1. In one of the online stores, a 25% discount is charged for each product purchased over two. Write a program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard. Sample result:

    Number of products purchased: 5\
    Product price: 40\
    Amount to pay: 170.00

1. The speed of vehicles on highways in Poland is at least 40 km/h and not more than 140 km/h. Write a program that prints a message when the specified car speed, read from the keyboard, has been exceeded. Sample result:

    Enter car speed: 38\
    Warning: invalid car speed!!

    Use the following variables in your program:

    car_speed\
    speed_limit_min\
    speed_limit_max

1. An influencer is a person who can influence other people\'s behaviour. An influencer communicates with other people using social networking sites. Write a program that checks whether a given person is a good influencer, that is, whether the person has at least two of the following accounts: Facebook, Twitter or Instagram. Use logical type variables: facebook, twitter, instagram, the value of which indicates whether the person has an account on the social networking site. Sample result:

    facebook = True\
    twitter = False\
    instagram = True\
    You are a good influencer!

1. EAN-13 (European Article Number) is a barcode for marking goods. The first 3 digits (590) usually indicate goods manufactured in Poland. Write a program that checks whether the EAN-13 number entered from the keyboard consists of exactly 13 characters (digits). Print a message if the number is correct. Additionally, only when the article number is correct, print a message when the product was manufactured in Poland. Sample result:

    Enter EAN-13 article number: 5901230094938\
    Article number is correct\
    Article manufactured in Poland

1. A washing machine allows you to wash a jacket, which takes 40 minutes, wash underwear, which takes 70 minutes, and wash shoes, which takes 20 minutes. In addition, it is possible to program an additional rinse (15 minutes) and an additional spin (9 minutes). The washing machine settings are saved in variables. Write a program that calculates and prints the total washing time. Sample result:

    washing_product = \"shoes\"\
    rinse = True\
    spin = False\
    Total washing time: 35 minutes

    ```python
    ###
    # Calculates and prints the total washing time.
    #
    # A washing machine allows you to wash a jacket, which takes
    # 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
    # which takes 20 minutes. In addition, it is possible to program
    # an additional rinse (15 minutes) and an additional spin (9 minutes).
    #
    total_washing_time = 0
    program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
    extra_rinse = input('Extra rinse? (y/n)')
    extra_spin = input('Extra spin? (y/n)')
    ...
    ...
    ```

1. Write a program that allows you to convert time in 24-hour format to 12-hour format. The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

    Enter time (24-hour format): 16:32\
    Time in 12-hour format: 4:32pm

1. Let x and y denote the coordinates of a point on the plane. Write a program that determines in which quadrant of the coordinate system the point P(x, y) is located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system. Sample result:

    x = 5\
    y = 2\
    Point P(5,2) is in the first quadrant of the coordinate system

1. Yes-no question are often used in surveys to gauge people\'s attitudes with regard to specific ideas or beliefs. Write a program that prints a survey consisting of three questions. Save the answers to logical type variables. Then view the survey result. Sample result:

    SURVEY
    Are you interested in computer science? (y/n): y\
    Do you like playing computer games? (y/n): n\
    Do you have an Instagram account? (y/n): y

    SURVEY RESULTS
    Interested in computer science: Yes\
    Playing computer games: No\
    Has an Instagram account: Yes

1. Write a program that converts a decimal number into a binary number. To convert a decimal number to binary, follow these steps:

    1. Read a decimal number from the keyboard.
    1. Divide the number by 2 and note the remainder.
    1. Divide the quotient obtained by 2 and note the remainder.
    1. Repeat the same process till we get 0 as the quotient.
    1. Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.

    Sample result:

    Enter decimal number: 12\
    12(10) = 1100(2)

1. There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

    Enter the amount in PLN: 18\
    The amount of PLN 18 in coins:\
    5 PLN coins: 3\
    2 PLN coins: 1\
    1 PLN coins: 1

1. Write a program that prints numbers from 1 to 30. If the number is divisible by 3 then the program prints the word \'THREE\'. Next, if the number is divisible by 5 then the program prints the word \'FIVE\'. Finally, if the number is divisible by both 3 and 5 then the program prints the word \'BINGO\'. Sample result:

    1 2 THREE 4 FIVE THREE 7 \...

1. Write a program that creates a multiplication table in the range 1 to 10 for any number entered by the user. Sample result:

    Enter number: 6\
    6 x 1 = 6\
    6 x 2 = 12\
    6 x 3 = 18\
    6 x 4 = 24\
    6 x 5 = 30\
    6 x 6 = 36\
    6 x 7 = 42\
    6 x 8 = 48\
    6 x 9 = 54\
    6 x 10 = 60

1. Write a program that creates the following pattern. Sample result:

    \*\
    \* \*\
    \* \* \*\
    \* \* \* \*\
    \* \* \* \* \*\
    \* \* \* \*\
    \* \* \*\
    \* \*\
    \*

1. Write a program that creates the following pattern. Sample result:

    1\
    22\
    333\
    4444\
    55555\
    666666\
    7777777\
    88888888\
    999999999

41. The payment card is secured with a four-digit PIN code (0805). Write a program that checks if the PIN code entered in the payment terminal is correct. The user has up to three possibilities for entering a PIN code. In case of three unsuccessful attempts, the card is blocked. Sample result:

    Enter the PIN code: 2398\
    Incorrect\...\
    Enter the PIN code: 0912\
    Incorrect\...\
    Enter the PIN code: 7860\
    Incorrect\...\
    Sorry, your payment card has been blocked.

1. A computer numeric keyboard has the arrangement of the keys as below. The included program code prints the computer keyboard. Analyse the program in terms of the printed results. Do you understand each program statement? Then make changes in your program code. Replace the 'for' with a 'while' statement.

    7 8 9\
    4 5 6\
    1 2 3

    ```python
    for i in range(6,-1,-3):
        for j in range(1,4):
            print(f'{i+j}',end=' ')
        print()
    ```

1. Write a program that prints the first twenty words of the Fibonacci sequence. The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two. Sample result:

    <https://en.wikipedia.org/wiki/Fibonacci_number>

    0 1 1 2 3 5 8 13 21 34 ...

1. A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number. Write a program that finds N leading prime numbers. Read the value of N from the keyboard. Using loop statements check that the number N is divisible only by 1 and by N.

    Prime numbers: 2 3 5 7 11 ...

1. Write a program that prints a lottery coupon (numbers from 1
    to 49) in the format as below.

    1 8 15 22 29 36 43\
    2 9 16 23 30 37 44\
    3 10 17 24 31 38 45\
    4 11 18 25 32 39 46\
    5 12 19 26 33 40 47\
    6 13 20 27 34 41 48\
    7 14 21 28 35 42 49

1. Write a program that prints 20 integer random numbers in the range of 5 to 10.