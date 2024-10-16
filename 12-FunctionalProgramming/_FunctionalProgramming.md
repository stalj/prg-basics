# FUNCTIONAL PROGRAMMING

1. Functional programming (FP) is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. It emphasizes the use of pure functions, immutability, and higher-order functions. Functional programming is declarative rather than imperative, meaning that it focuses on what to do rather than how to do it.

   In Functional Programming, functions are treated as first-class citizens, meaning they can be assigned to variables, passed as arguments, and returned from other functions. This makes it easy to create modular, reusable, and composable code.

   **Key Concepts of Functional Programming:**

   * **Pure Functions**: A pure function is a function where the output is determined only by its input values and has no side effects (doesn’t modify any external state or variables). Given the same input, a pure function will always return the same output.

   * **Immutability**: Data is considered immutable, meaning it cannot be changed after it is created. Instead of modifying data, new data structures are created.

   * **Higher-Order Functions**: A higher-order function is a function that either takes one or more functions as arguments, returns a function, or both. This allows functions to be composed, reused, and passed around like any other data.

   * **First-Class Functions**: Functions are first-class citizens, meaning they can be treated like variables. They can be passed as arguments, returned from other functions, and stored in data structures.

   * **Recursion**: Instead of using loops, functional programming often relies on recursion for iteration. Recursion allows a function to call itself until a base condition is met.

1. Python is not a purely functional programming language; it is a multi-paradigm language, meaning it supports functional, object-oriented, and procedural programming. However, Python provides several features that allow for functional programming techniques, such as:

   * First-class functions.
   * Higher-order functions like map(), filter(), and reduce().
   * Lambda functions (anonymous functions).

   Watch the video to learn how to use functions (map, filter, reduce) to support functional programming in Python.

   <https://youtu.be/hUes6y2b--0?feature=shared>

## 1. Anonymous (Lambda) Function

1. Define a function that calculates the arithmetic mean of two numbers. Then, write a program that takes two integer numbers from the keyboard and calculates their arithmetic mean.

   ```python
   ###
   # Calculates arithmetic mean of two integer numbers
   #
   def mean(x,y):
      ...
      return ...
   
   # takes two numbers from keyboard
   n1 = input(...)
   n2 = ...

   # calculates arightmtic mean and print result
   result = mean(n1,n2)
   print(f'The arithmetic mean of the numbers ... and ... is ...')
   ```

1. Define an anonymous (lambda) function that calculates the arithmetic mean of two numbers. Details on how to define an anonymous function can be found at:

   <https://www.w3schools.com/python/python_lambda.asp>

   Then, write a program that takes two integer numbers from the keyboard and calculates their arithmetic mean.

   ```python
   # takes two numbers from keyboard
   n1 = input(...)
   n2 = ...

   # define an anonymous function
   mean = lambda x,y: (x+y)/2


   # calculates arightmtic mean and print result
   result = mean(n1,n2)
   print(f"The arithmetic mean of ...............")
   ```

1. Write a program that converts speed in meters per second to speed in kilometers per hour. Define a function `ms_to_kmh(ms)` that returns the calculated speed in km/h. Sample result:

   ```
   10 m/s = 36 km/h
   35 m/s = 126 km/h
   ```

1. Write a program that converts speed in meters per second to speed in kilometers per hour. Define and use an anonymous function `ms_to_kmh(ms)`. Sample result:

   ```
   10 m/s = 36 km/h
   35 m/s = 126 km/h
   ```

1. Write a program that calculates the average speed of a vehicle. Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. Define a function `avg_speed(distance,hours,minutes)` that returns the calculated average speed. Sample result:

   ```
   Enter distance in km: 70
   Enter number of travel hours: 1
   Enter number of travel minutes: 23
   Average speed: 50.6 km/h 
   ```

1. Write a program that calculates the average speed of a vehicle. Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. Define and use an anonymous function `avg_speed(distance,hours,minutes)` to calculate the result. Sample result:

   ```
   Enter distance in km: 70
   Enter number of travel hours: 1
   Enter number of travel minutes: 23
   Average speed: 50.6 km/h 
   ```

1. Define an anonymous function is_even(number) that checks whether a number is even. Then test it by writing a program.

1. Define an anonymous function initials(name,surname) that returns the first letters of the name and surname.

## 2. Higher-Order Function

1. The educational course ends with a test checking the participants' knowledge. To pass the course, the participant must obtain a minimum number of points. The program below contains a higher order function min_pts, that returns other function. Read the program code. Then run the program.

   ```python
   def min_pts(limit):
      def check(pts):
         if pts >= limit:
            return True
         return False
      return check

   print("=== MIN 50 PTS TO PASS ===")
   assess_test = min_pts(50)
   print(f"52 pts -> {assess_test(52)}")
   print(f"39 pts -> {assess_test(39)}")

   print("=== MIN 60 PTS TO PASS ===")
   assess_test = min_pts(60)
   print(f"52 pts -> {assess_test(52)}")
   print(f"39 pts -> {assess_test(39)}")
   ```

1. In Python, the `sorted()` function is used to return a new sorted list from the elements of any iterable, such as a list, tuple, or dictionary. It doesn’t modify the original iterable but instead returns a new sorted list.

   One of the `sorted()` function optional argument can be a function that serves as a key for the sort comparison. For example, you can pass a function that extracts a specific field from the items.

   Find a syntax for the `sorted()` function online. Then use the function to sort a list of names by their length (number of letters). Define an anonymous function, which you use as an argument to the sorted() function. Sample result:

   ```
   Unsorted list:
   names = [
      'James',
      'Emily',
      'William',
      'Olivia',
      'Benjamin',
      'Sophia',
      'Henry']
   ```

   ```
   Sorted list:
   James
   Emily
   Henry
   Olivia
   Sophia
   William
   Benjamin
   ```


## 3. Data Mapping

1. The report below shows the last five credit card payments in Euro:

   ```
   15.90
   38.47
   4.07
   132.70
   9.15
   ```

   Write a program that calculates and displays transaction amounts in Polish zlotys (1 EUR = 4.5 PLN). Use anonymous and `map()` functions. Sample result:

   ```
   71.55
   173.11
   18.31
   597.15
   41.17
   ```

   ```python
   transactions_in_eur = [15.90,38.47,4.07,132.70,9.15]
   transactions_in_pln = list(map(lambda x:x*4.5, transactions_in_eur))
   # print pln list ...
   ```

1. For the following text:

   ```
   I completely agree with you
   ```

   write a program that calculates and displays the number of letters in each word. Use the `map()` and an anonymous functions to calculate the number of letters.
   
   > Tip: to split text into words, use the `split()` function.
   
   Sample result:

   ```
   Text: I completely agree with you
   No. of letters in words: [1,10,5,4,3]
   ```

   ```python
   sentence = '...'
   result = list(map(lambda ... , sentence. ...))
   print(result)
   ```

1. The data below contains a list of products available in stock and their unit price.

   ```python
   stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
   ```

   Write a program that calculates the total value of products in stock. Use the map(), sum() and an anonymous function. Sample result:

   ```python
   Products in stock: [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
   Total value: 423.35
   ```

## 4. Data Filtering

1. The following people are employed in one of the company's departments:

   ```
   SMITH Lucy
   JONES Janet
   LEE Jerry
   JACKSON Peter
   JOHNSON Rick
   LEWIS Terry
   CLARKE Robin
   ```

   Save the list of employees in a string array. Then, write a program that displays people whose surnames start with the letter 'J'. Use anonymous and `filter()` functions. Sample result:

   ```
   JONES Janet
   JACKSON Peter
   JOHNSON Rick
   ```

   ```python
   employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
                  "JACKSON Peter","JOHNSON Rick",
                  "LEWIS Terry","CLARKE Robin"]
   emp_J = list(filter(lambda e:...=="J", employees))
   # print a list …
   ``` 
   ...

1. A speed camera located in a city measures the speed of passing vehicles. The maximum permitted speed of vehicles is 50 km/h. In the last minute, the speed camera recorded the following values:

   ```
   48,47,54,50,42,68,39,46
   ```

   Write a program that displays speed values higher than the allowed speed. Use anonymous and `filter()` functions. Sample result:

   ```
   Recorded values: 48,47,54,50,42,68,39,46
   Speed too high: 54,68
   ```

1. The final grades obtained by students in the "Economic Geography" course are included in the array:

   ```
   [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
   ```

   Write a program that calculates the arithmetic mean of the grades, excluding negative grades (2.0). Use the `filter()` along with an anonymous function. Sample result:

   ```
   Arithmetic mean for grades <> 2.0 is 3.85
   ```

## 5. Data Reducing

1. The `reduce()` function in Python, which is available in the functools module, is used to apply a function cumulatively to the elements of an iterable, reducing it to a single value. Syntax:

   ```python
   from functools import reduce

   reduce(function, iterable[, initializer])
   ```

   Where:

   * function: A function that takes two arguments and performs an operation on them.
   * iterable: The iterable (like a list, tuple, etc.) whose elements are reduced.
   * initializer (optional): An initial value to start the reduction process.

   How reduce() works:

   * Takes a function that accepts two arguments.
   * Applies the function to the first two elements of the iterable.
   * Uses the result of the function to combine with the next element.
   * Repeats this process until all elements have been processed.
   * Returns a single, reduced value as the final result.

   The following program calculates the sum of numbers. Notice the use of the `reduce()` function. Then modify the program: replace the regular function `add(x,y)` with an anonymous function.


   ```python
   from functools import reduce

   # Function to add two numbers
   def add(x, y):
      return x + y

   numbers = [1, 2, 3, 4, 5]

   # Using reduce to sum the numbers
   result = reduce(add, numbers)
   print(result)  # Output: 15
   ```

1. Write a program that calculates the sum of even numbers. Use `filter()`, `reduce()` and anonymous functions.

   > Tip. First, use filtering to extract even numbers. Then use `reduce()` to calculate the sum of those numbers.

   ```python
   numbers = [2,4,6,3,7,5]
   ```

## 6. Practice Makes Perfect

1. Familiarise yourself with the basic concepts of functional programming:

   <https://www.geeksforgeeks.org/functional-programming-in-python/>

1. Read the text related to functional programming in Python:

   <https://www.codecademy.com/article/functional-programming-in-python>

1. Watch the video to learn about higher order functions:

   <https://youtu.be/xZtTIm3fpfA?feature=shared>

1. An array contains numbers from 1 to 20. Write a program that calculates and displays their third power. Use the `map()` and an anonymous function.

1. An array contains numbers from 1 to 20. Write a program that displays only numbers divisible by 2 and 3 without remainder. Use the `filter()` and an anonymous function.

1. The array below contains employee data: 

   ```python
   [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
      ("Jackson","Peter"),("Johnson","Rick"),
      ("Lewis","Terry"),("Clarke","Robin")]
   ```

   Write a program that determines and displays a list of employees whose last names are given in capital letters followed by first names, separated by commas. Sample result:

   ```
   SMITH, Lucy
   JONES, Janet
   …
   …
   ```

1. In ski jumping competitions, each competitor is assessed by five judges. Each judge can award a score from 0 to 20 points. The highest and lowest scores are discarded. The remaining three scores are added up to form the final score obtained by the competitor. The ratings of four players are presented below.

   ```
   [(17,15,16,17,15),
    (16,18,19,17,19),
    (19,15,15,19,18),
    (18,17,19,15,16)]
   ```

   Calculate and display the total points obtained by competitors.
   
   > Tip: use the Python built-in functions: `map()`, `sum()`, `min()`, `max()`.
   
   Sample result:

   ```
   [48, 54, 52, 51]
   ```

1. The educational course finished with a test checking the participants' knowledge. Here are the results obtained by the students:

   ```
   [37,51,44,23,78,92,39,84,83,51]
   ```

   Write a program that calculates and displays student scores that are equal to or greater than the following minimum number of points to pass the course:

   1. 70
   1. 40
   1. 30

   Use the `filter()` function and the following higher order function:

   ```python
   def min_pts(limit):
      return lambda pts: pts>=limit
   ```

   Sample result:

   ```
   Min 70 pts: [78, 92, 84, 83]
   Min 40 pts: [51, 44, 78, 92, 84, 83, 51]
   Min 30 pts: [37, 51, 44, 78, 92, 39, 84, 83, 51]
   ```

1. Measuring stations recorded the following temperatures in degrees Celsius:

   ```
   {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
   ```

   Write a program that displays the names of towns where positive temperatures were recorded. Use anonymous and `filter()` functions. Sample result:

   ```
   Cities with positive temperatures: Krakow Sopot Opole
   ```

1. Measuring stations recorded the following temperatures in degrees Celsius:

   ```
   {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
   ```

   Write a program that creates a bar chart showing temperatures recorded in cities. Add a title for the chart and descriptions for the x and y axes.
   
   > Tip: use the `map()` function to create two arrays of data for the chart.

1. Students obtained the following test results (in points, from 0 to 100):

   ```python
   test_results = [
      {"name":"Peter","result":27},
      {"name":"Anna","result":63},
      {"name":"Robert","result":92},
      {"name":"Paul","result":46},
      {"name":"Barbara","result":52}]
   ```

   Write a program that displays students whose scores are between 50 and 70 points. Use an anonymous function and `filter()` function.

1. At one of the Olympic Games, the medal classification is as follows:

   ```
   {"country":"Denmark","gold":2,"silver":4,"bronze":6}
   {"country":"Finland","gold":5,"silver":0,"bronze":4}
   {"country":"USA","gold":12,"silver":5,"bronze":11}
   {"country":"Peru","gold":0,"silver":1,"bronze":7}
   ```

   Write a program that displays the data of countries that have won at least 10 medals. Use anonymous and ```filter()``` functions. Sample result:

   ```
   COUNTRIES WITH AT LEAST 10 MEDALS
   Denmark: 2,4,6
   USA: 12,5,11
   ```

1. At one of the Olympic Games, the medal classification is as follows:

   ```
   {"country":"Denmark","gold":2,"silver":4,"bronze":6}
   {"country":"Finland","gold":5,"silver":0,"bronze":4}
   {"country":"USA","gold":12,"silver":5,"bronze":11}
   {"country":"Peru","gold":0,"silver":1,"bronze":7}
   ```

   Write a program that creates a bar chart showing the total number of medals won by each country. Add a title for the chart and descriptions for the x and y axes.
   
   > Tip: Use the `map()` function to create arrays of data for your chart.

1. In a beverage factory, a machine fills 500ml bottles. The computer checks whether the bottle has been filled correctly. For a 500ml bottle, the allowable tolerance is 2%. In the last ten bottles checked, the filling was:

   ```
   508,500,512,499,492,511,503,476,501,509
   ```

   Write a program that calculates the percentage of incorrectly filled bottles. Use the `filter()` along with a higher order function. Sample result:

   ```
   Bottle capacity:    500ml
   Filling tolerance:  2%
   Filled bottles:     508,500,512,499,492,511,503,476,501,509
   Incorrectly filled: 30%
   ```
