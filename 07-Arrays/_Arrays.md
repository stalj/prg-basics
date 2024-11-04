<!--
(c) Janusz Stal
Krakow University of Economics
Department of Informatics
stalj@uek.krakow.pl
-->

# ARRAYS

## 1. One dimensional arrays

1. Watch the video on using lists:

   <https://youtu.be/ohCDWZgNIU0?feature=shared> 

1. Familiarise yourself with creating and manipulating Lists:

   <https://www.w3schools.com/python/python_lists.asp> 

1. Many programming languages ​​provide both arrays and lists to store and manage collections of data. Despite their many similarities, they have key differences in terms of functionality, flexibility, and performance.

   The main differences between an array and a list are presented in the table below. 

   | FEATURE           | LISTS                         | ARRAYS                         |
   |-------------------|-------------------------------|-------------------------------|
   | Data Types        | Mixed                        | Single, fixed data type       |
   | Flexibility       | Highly flexible              | Less flexible                |
   | Performance       | Slower for numerical ops     | Faster for numerical ops      |
   | Memory Efficiency | Less efficient               | More efficient               |
   | Built-in Support  | Yes                          | Needs `array` or `numpy`     |

   > **Notice that in subsequent tasks, a list will be used in place of an array for basic applications.**

1. An array contains values: 2, 3, 7, 5, 4. Write a program that prints:
   1. the array
   1. number of elements
   1. first value
   1. second value
   1. last value
   1. last but one value (do not use negative index values)
   1. sum of the first and last value
   1. middle value
   1. all array values separated by a single space (use a loop statement)

   ```python
   ###
   # Prints some array elements
   #
   arr = [2, 3, 7, 5, 4]

   print(arr)
   print('Number of elements', len(arr))
   print('First value', arr[...])
   print('Second value', arr[...])
   ...
   ...
   ```

   > Tip: to read the last value of an array use array[len(array)-1] or array[-1]

1. An array contains values: 1, 2, 3, 4, 5. Write a program that modifies the array values. Print the array after each change.

   1. subtract one from the first element of the array
   1. increase the last array element by 4
   1. multiple the middle array element by 2

   Sample result:

   ```python
   Array: [1,2,3,4,5]
   Array: [0,2,3,4,5]
   Array: [0,2,3,4,9]
   Array: [0,2,6,4,9]
   ```

1. Write a program that prints the name of the day of the week for a given day number. Then, using the defined function, print the name of the day of the week for the following day numbers: 1, 4, 7.

   ```python
   ###
   # Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
   #
   def weekday(n):
         weekdays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
      return weekdays[...]

   ...
   ...   
   ```

1. Write a program that prints a shopping list, each product on a separate line.

   ```python
   ###
   # Prints shopping list
   #
   shopping_list = [
      "milk", "bread", "eggs", "butter", "cheese",
      "tomatoes", "potatoes", "carrots", "onions", "garlic"
   ]
   for item in shopping_list:
      print(...)
   ```

1. Write a program that prints a popular computer games, each game name on a separate line. Use the while statement. Additionally, number the list (print the next number before each list item) and sort the list alphabetically (use one of a Python built-in functions for sorting)

   ```python
   computer_games = [
      "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
      "League of Legends", "Valorant", "Grand Theft Auto V", 
      "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
   ]
   ```

1. The list contains vehicle registration numbers in Poland. Cars from Krakow have numbers starting with the letters 'KR' or 'KK'. Write a program that prints car registration numbers from Krakow. Number the list printed.

   ```python
   ###
   # Prints vehicle registration numbers from Krakow
   #
   polish_license_plates = [
      'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
      'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
      'KK54985', 'LU4864U'
   ]
   counter = 1
   for car_number in polish_license_plates:
      if car_number ...:
         print(counter, ...)
         counter += 1
   ```

1. The array contains the student's test results. A value of True indicates that the student answered the question correctly, while a value of False indicates an incorrect answer. Write a program that prints information about the test results:

   * Number of questions:
   * Number of correct answers:
   * Number of incorrect answers:
   * Percentage of correct answers:

   ```python
   ###
   # Prints test statistics
   #
   test_results = [
      False, True, False, True, True,
      True, True, False, True, True,
      False, True, True, True, False
   ]

   # calculates the number of test questions
   question number = len(...)

   # calculates the number of correct answers
   correct_answers = 0
   for answer in test_results:
      if ...:
         correct_answer = ...
   
   # calculates the number of incorrect answers
   ...

   # calculates the percentage of correct answers
   ...

   print('TEST STATISTICS')
   print('===============')
   print('Number of questions:', ...)
   print('Number of correct answers:', ...)
   ...
   ...
   ```

1. The weather station measures temperature once a day. The measurement results for each day in March are stored in an array. Write a program that analyzes the temperature based on the observations from March and prints the following report:

   ```
   TEMPERATURE REPORT
   Month: March
   Number of measurements:
   Average temperature in the month:
   Minimum temperature:
   Maximum temperature:
   Number of days with negative temperature:
   ```

   ```python
   ###
   # The weather station report
   #
   temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
   ]

   # number of mesaurements
   mesaurements = len(...)

   # calculates average temperature
   temp_total = 0
   for temp in temperatures:
      temp_total = ...
   avg_temp = temp_total ...

   # calculates min and max temperatures
   min_temp = min(...)
   max_temp = ...

   # calculates number of days with negative temp
   negative_temp = 0
   i = 0
   while i < ...:
      if temperatures[...] < ...:
         negative_temp ...
      i = ...

   # prints out month report
   ...
   ...
   ...
   ```

1. Monthly expenses and their corresponding expense categories are included in the arrays below. Write a program that calculates which expense category was the most expensive.

   ```python
   categories = ["Food", "Transport", "Rent","Entertainment"]
   expenses = [500, 150, 1000, 200]
   ```

1. The store has 10 types of goods in stock. The prices of the goods and the number of pieces of goods are given below. Write a program that calculates the value of all the goods available in the store.

   ```python
   # Prices of 10 products in the computer store (in currency units)
   product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

   # Number of units available for each product
   product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]
   ```

1. Very often, there is a need to organize the data contained in the array. Organized data allows for faster retrieval, analysis, and presentation of information. There are many sorting algorithms that organize data in the array. One of the simplest is bubble sort, which organizes data in ascending or descending order.

   Watch the video on bubble sort algorithm:

   <https://youtu.be/hahrx5WUeNI?feature=shared>

   Bubble Sort is one of the simplest sorting algorithms. It works by repeatedly stepping through the list or array, comparing adjacent elements, and swapping them if they are in the wrong order. This process is repeated until no more swaps are needed, which means the list is sorted.

   Here is the bubble sort algorithm expressed in pseudocode, a universal notation that is independent of the programming language:

   ```python
   procedure bubbleSort(arr):
      n = length(arr)
      for i = 0 to n-1:
         for j = 0 to n-i-2:
            if arr[j] > arr[j+1]:
                  swap arr[j] and arr[j+1]
      return arr
   ```

1. Define a function that sorts an array of numbers using the bubble sort algorithm. Use the information in the pseudocode provided earlier. Then, write a program that sorts the following collections of data:

   ```python
   car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
   bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
   ```

   ```python
   ###
   # Bubble sort
   #
   def bubble_sort(arr):

      for i in n:
         for ...:
            if ...:

      return arr

   car_fuel_consumption = ...
   print(car_fuel_consumption)
   sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
   print(sorted_car_fuel_consumption)

   bank_transactions = ...
   ...
   ...
   ...
   ```

1. Programming languages ​​often provide built-in functions for sorting collections of data. Data can be sorted in ascending or descending order. Look at the list of built-in functions below and find the one that allows you to sort collections of data.

   <https://docs.python.org/3/library/functions.html>

   Then write a program that uses the built-in function to sort the data below:

   ```python
   # Sort the data from lowest to highest value
   distances_traveled = [120, 150, 180, 90, 200, 175, 160]
   # Sort the data in descending order, from highest to lowest value
   daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
   # Sort the data in ascending order
   file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
      "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
   ```

## 2. Two dimensional arrays

1. Watch the video on using two dimensional (2D) lists in Python:

   <https://youtu.be/z49F119uv6g> 

1. Tic-Tac-Toe is a simple yet fun game for two players. You play on a grid of nine squares arranged in three rows and three columns.

   The array below shows a Tic-Tac-Toe board. Write a program that prints a board on the screen.

   ```python
   # 3x3 Tic-Tac-Toe board
   tic_tac_toe_board = [
      ['X', 'O', 'X'],
      [' ', 'X', 'O'],
      ['O', ' ', 'X']
   ]

   for row in tic_tac_toe_board:
      for ... in ...:
         print(..., end=" ")
      print()
   ```

   > Hint: end=" " means that the cursor is not moved to the next line; a space is printed instead 

1. The data below represents monthly expenses divided into categories and weeks. Write a program that calculates and prints:

   * total expenses for each category
   * total expenses for each week
   * total expenses for a month

   ```python
   # Weekly expenses for different categories
   # [Food, Transport, Utilities]
   monthly_expenses = [
      [200, 50, 100],  # Week 1
      [180, 60, 110],  # Week 2
      [220, 55, 105],  # Week 3
      [210, 65, 95]    # Week 4
   ]

   # Calculates expenses
   # Use loop statements
   ...
   ...
   ...

   # Print expenses
   print('MONTHLY EXPENSES')
   print('----------------')
   print('Food:',...)
   print('Transport:',...)
   print('Utilities:',...)
   print('Week 1:',...)
   print('Week 2:',...)
   print('Week 3:',...)
   print('Week 4:',...)
   print('---------------')
   print('TOTAL:',...)
   ```

1. The data below contains weekly meal plan. Write a program that prints the weekly meal plan along with the day name as in the example below.

   ```
   WEEKLY MEAL PLAN
   (Breakfast, Lunch, Dinner)
   ==========================
   Monday: Oatmeal, Grilled Checken Salad, Spaghetti
   Tuesday: ...
   Wednesday: ...
   ...
   ...
   ...
   ...
   ```


   ```python
   # Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
   meal_plan = [
      ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
      ["Pancakes", "Sandwich", "Steak"],
      ["Smoothie", "Chicken Wrap", "Salmon"],
      ["Eggs", "Pasta", "Soup"],
      ["Toast", "Burrito", "Pizza"],
      ["Cereal", "Salad", "Fish Tacos"],
      ["Bagel", "Rice and Beans", "Stir-fry"]
   ]

   # Returns a week day name
   def weekday(n):
      weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
      return weekdays[n-1]

   # Returns a string with day meal names
   # separated by comma
   def day_meal_plan(meal_plan, day_number):
      ...
      return ...

   # Prints weekly meal plan
   ...
   ...
   ...
   ```

1. The data below represents a cinema's seating arrangement. Write a program that:

   * calculates how many seats are available
   * calculates how many seats are booked
   * informs what the status of a seat is in a given row and given place (available or booked)

   ```python
   # 5x5 cinema seating
   # A = Available, B = Booked
   cinema_seats = [
      ['A', 'A', 'B', 'A', 'A'],
      ['A', 'B', 'B', 'A', 'A'],
      ['A', 'A', 'A', 'A', 'B'],
      ['B', 'A', 'A', 'A', 'A'],
      ['A', 'B', 'A', 'A', 'A']
   ]

   def seats_total(seats):
      ...
      return ...

   def seats_available(seats):
      ...
      ...
      return ...

   def seats_booked(seats):
      ...
      ...
      return ...

   def seat_status(seats, row, place):
      ...
      ...
      return ...

   print('CINEMA INFORMATION TABLE')
   print('Total seats:',...)
   print('Seats available:',...)
   print('Seats booked:', ...)
   print('Seat in row 1, place 1:', ...)
   print('Seat in row 5, place 5:', ...)
   print('Seat in row 3, place 5:', ...)
   ```



1. The following array represents a square matrix and contains values:

   ```python
   [
      [0,0,0],
      [0,0,0],
      [0,0,0]
   ]
   ```

   Create a program that replaces the values of the main diagonal with 1. Use a loop statement. Print the modified array. Sample result:

   ```
   1 0 0
   0 1 0
   0 0 1
   ```

## 3. Practice Makes Perfect

1. Read the chapter in your class textbook that covers the topics in this section.

1. Try to create the following arrays. Then, print the created array content.

   ```python
   arr1 = [3,7,1,0,4]
   arr2 = [[2,3],[7,1],[0,4]]
   arr3 = [7 for i in range(5)]
   arr4 = [i for i in range(1,10)]
   arr5 = [i*2 for i in range(1,10)]
   arr6 = [random.randint(1,20) for i in range(10)]
   arr7 = [[] for i in range(5)]
   arr8 = [[1 for i in range(2)] for j in range(4)]
   arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
   an array with values: 4,0,3
   15-element array filled with zeros
   an array with integer values in the range of <1,30>
   20-element array filled with 0 or 1 randomly
   two dimensional array with five rows and two columns filled with False
   ```
 > **Hint: Don't forget to import the random module before using random.randint**

1. An array contains integer numbers: 34,7,19,4,21,8. Create a program that calculates and prints the number of even values in the array. Use the ‘while’ loop statement.

1. An array contains natural numbers: 15, 8, 31, 47, 2, 19. Create a program that prints the contents of the array in reverse order. Use any loop statement. Sample result:

   ```python
   existed array: 15 8 31 47 2 19 
   reverse array: 19 2 47 31 8 15
   ```

1. Create a program that computes the second power of each array element. Sample result:

   ```python
   Array: 8 2 5 1 9
   2nd power: 64 4 25 1 81
   ```

1. An array contains numbers: -15, 8, -31, 47, -2, 19. Create a program that finds and prints the maximum and minimum number. Do not use available functions.

1. An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and prints the array and the arithmetic mean of array values. Use the “for” loop statement.

1. An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and prints the array and the arithmetic mean of array values. Use the “while” loop statement.

1. An array contains a list of Polish names:

   ```
   Genowefa, Onufry, Celestyna, Alojzy, Pankracy
   ```

   Create a program that prints the longest name (consisting of the largest number of characters). Sample result:

   ```
   Names: Genowefa Onufry Celestyna Alojzy Pankracy
   Longest name: Celestyna
   ```

1. An array contains integer numbers: 2, 6, 4, 9, 7. Create a program that prints the array values graphically as below. Define a function star(n) that returns the given number of asterisks as a string. Use a defined function in the program.

   ```python
   2: **
   6: ******
   4: ****
   9: *********
   7: *******
   ```

1. Define a function compare(array1, array2) that returns True if both arrays are the same or False otherwise.  Two arrays are the same if they have the same number of elements and values of elements in cells of arrays with the same index are equal. Then create a program and try to compare the following arrays: 

   ```python
   1. ["water","book","sky"]   ["water","book","sky"]
   1. [True,False]   [True,False,True]
   1. [5,3,1]   [5,3,1]
   1. [3,2,1]   [3,2]
   ```

   Print both arrays and the result of comparison. Sample result:

   ```python
   Array1: water book sky
   Array2: water book sky
   Comparison: arrays are the same
   ```

1. Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. Create a program that prints the numbers from the first array that do not appear in the second array.

1. Create a program that sorts elements of an array containing integer numbers. Apply the Bubble Sort sorting algorithm. Define a function bubblesort(array) that returns the sorted array. Try to sort and print any three arrays.

1. Create a program that prints all unique elements in an array. Sample result:

   ```python
   Array: 2 3 2 5 8 1 9 8
   Unique elements: 3 5 1 9
   ```

1. Define a function occurs(number, array) that returns True if a given number is present in an array. Then create a program that checks whether the number entered from the keyboard is present in the array [15, 38, 7, 23, 14]. Sample result:

   ```python   
   Number: 23
   Array: 15 38 7 23 14
   Result: number 23 appears in the array
   ```

1. A tuple in Python is an immutable, ordered collection of elements. Tuples are similar to lists, but unlike lists, once a tuple is created, its elements cannot be modified, added, or removed.

   Write a program that creates a tuple containing a single word ‘computation’. Save a tuple in a variable. Then, print the type of the variable.

1. Write a program that prints the tuple (10,20,30,40,50) in reverse order. Sample result:

   ```python
   Tuple: 10,20,30,40,50
   Reverse order: 50,40,30,20,10
   ```

1. Write a program that for the tuple ("Seven", [10, 20, 30], (5, 15, 25)) prints values:
   1. “Seven”
   1. 30

1. Write a program that counts the number of occurrences of any value from a tuple. Sample result:

   ```python
   Tuple: 50,20,40,50,30,50
   Value: 50
   Number of occurrences: 3
   ```

1. Create a module MyArrays containing functions to operate on an array of numbers:

   1. A function that returns the second largest element in an array
   1. A function that returns the difference between the largest and smallest values in an array
   1. A function that returns the median of numbers in an array. 
   
   Do not use built-in functions. The median is the middle value in the ordered sequence of numbers:

      <https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png> 

   1. A function that returns a two-element array containing the smallest and largest values in an array
   
   1. A function that returns array elements as a string, separated by the minus sign

   Then, write a program that for the sequence of numbers:

   ```python
   7,3,8,5,2
   ```

   calculates and prints results. Sample result:

   ```
   Numbers: 7,3,8,5,2
   Second largest number: 7 
   Median: 5
   Smallest and largest number: 2,8
   Numbers as a string: 7-3-8-5-2
   ```

1. Write a program that, for the given array of real numbers, prints the number of elements that are greater than the given value entered from the keyboard.

1. Write a program to separate even and odd numbers of a given array of integers. Put all even numbers first, and then odd numbers.

   Sample result:

   ```python
   arr = [7,9,2,4,5,6]
   ...
   ...
   arr = [2,4,6,7,9,5]
   ```

1. Write a program that checks whether the first array is a subset of the second one (whether all elements of the first array appear in the second array).

1. Define a function rand_elem(array) that returns a randomly selected array element. Using the function, print a few randomly selected array elements.

1. A variable contains text:

   An apple a day keeps the doctor away

   Create a module MyText, containing:

   1. A function that returns the number of words in the text
   1. A function that returns an ordered array of words, from longest to shortest
   1. A function that returns an alphabetically ordered array of words

   Then, write a program, call the functions and print results. Sample result:

   ```
   Text: An apple a day keeps the doctor away
   Number of words: 8
   Words from the longest: doctor,apple,…
   Words ordered alphabetically: a,An,apple,away,…
   ```

1. Familiarise yourself with methods of visualizing data:

   <https://www.w3schools.com/python/matplotlib_intro.asp> 

   Then, using ‘matplotlib’, draw a line in a diagram from position (1, 3) to position (8, 10). 

   > Hint: to use 'matplotlib' in your programs, first you have to install the module by using the 'pip' command (python package manager).

   <https://pythonguides.com/how-to-install-matplotlib-python/>

   ```python
   import matplotlib.pyplot as plt
   xpoints = [1, 8]
   ypoints = [3, 10]
   plt.plot(xpoints, ypoints)
   plt.show()
   ```
   

1. Write a program that draws the graph of the function f(x)=x<sup>2</sup>-3. Sample result:

   ```python
   import matplotlib.pyplot as plt

   x = []
   y = []

   # create x values
   for n in range(-100,101):
      x = x + [n]

   # create y values
   for n in x:
      y = ...

   # print chart
   ...
   ...

1. Write a program that draws the function y = sin(x) for an angle value in the range 0-360 degrees.

1. A two-dimensional array of size 2 by 4 contains integer numbers. Create a program that prints array values in rows and columns.

1. A two-dimensional array contains the following numbers:

   ```
   7 3 7 9 0
   2 9 0 1 5
   3 8 6 4 7
   8 7 1 1 5
   ```

   Create a program that calculates the sum of values in the last column.

1. A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0. Create a program and the function. Then create a two-dimensional array with dimensions of 3 by 5. print the created array.

1. An array contains values:

   ```
   [[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
   ```
   
   Create a program that modifies the array values to create a multiplication table as below. Use loop statements. Print the array.

   ```
   1  2  3  4  5
   2  4  6  8 10
   3  6  9 12 15
   4  8 12 16 20
   5 10 15 20 25
   ```
   
1. An array contains integer numbers:

   ```
   [[-38, 19], [5,40],[-7,11],[29,16]]
   ```

   Create a program that finds the smallest and largest values in the array and in which row and column they are located. 

1. A two-dimensional array of the size 3 by 5 contains integer numbers. Create a program that swaps the first and the last row. Print array values in rows and columns before and after changes.

1. A two-dimensional array of the size 3 by 5 contains integer numbers. Create a program that swaps the first and the last column. Print array values in rows and columns before and after changes.

1. In mathematics, a matrix is a rectangular array or table of numbers, symbols, or expressions, arranged in rows and columns, e.g.:

   ```
   -7  12 38
   41 -19 11
   ```

   Create a function identity_matrix(n) that returns an identity matrix(2D array) of size n.
   
   <https://en.wikipedia.org/wiki/Identity_matrix>
   
   Then, create a function that prints a 2D array in rows and columns. Finally, create a program that prints three identity matrices with dimensions of 3, 5 and 8. Sample result:

   ```
   1 0 0 0 0
   0 1 0 0 0
   0 0 1 0 0
   0 0 0 1 0
   0 0 0 0 1
   ```

1. Create a function transpose_matrix(m) that returns transposed matrix m:

   <https://en.wikipedia.org/wiki/Transpose> 

   Then, create a program that prints transposed matrices, in rows and columns, for the following matrices.
   1. 1 2 3\
      4 5 6\
      7 8 9
   1. 1 2 3 4 5\
      6 7 8 9 0
   1. 5 6 7 8
1. Create a function that convert two-dimensional (2D) array into 1D. Then create a program that prints 1D array for the following 2D arrays.

   1. 2 3\
      1 5 
   1. 5 0 3 7 5\
      9 0 9 1 2
   1. 2 1\
      3 5\
      7 4\
      2 6


