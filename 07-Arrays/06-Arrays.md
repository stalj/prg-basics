<!--
(c) Janusz Stal
Krakow University of Economics
Department of Informatics
stalj@uek.krakow.pl
-->

# ARRAYS

## 1. Lists

1. Watch the video on using lists:

   <https://youtu.be/ohCDWZgNIU0?feature=shared> 

1. Familiarise yourself with creating and manipulating Lists:

   <https://www.w3schools.com/python/python_lists.asp> 

1. Watch the video on using tuples:

   <https://youtu.be/NI26dqhs2Rk?feature=shared> 

1. Watch the video on using two dimensional (2D) lists in Python:

   <https://youtu.be/z49F119uv6g> 

1. Search the Internet to find out what an array is. Describe the properties of an array. Explain how an array differs from a list.

**Notice that in subsequent tasks, a list will be used in place of an array for basic applications.**

1. To visualize data, install the ‘Matplotlib’ library on your personal computer.
1. Familiarise yourself with methods of visualizing data:

   <https://www.w3schools.com/python/matplotlib_intro.asp> 

   Then, using ‘matplotlib’, draw a line in a diagram from position (1, 3) to position (8, 10):

   import matplotlib.pyplot as plt
   xpoints = [1, 8]
   ypoints = [3, 10]
   plt.plot(xpoints, ypoints)
   …

   ![Obraz zawierający linia, Wykres, diagram, tekst

Opis wygenerowany automatycznie](Aspose.Words.79ee0a06-2a21-4dc6-b8e6-a4728f8ad415.001.png)

## One dimensional arrays

1. An array contains values: 2, 3, 7, 5, 4. Write a program that displays:
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
   # 
   #
   arr = [2, 3, 7, 5, 4]

   print(arr)
   print('Number of elements', len(arr))
   print('First value', arr[...])
   print('Second value', arr[...])
   ...
   ...
   ```

   > Tip: to read the last value of an array: array[len(array)-1] or array[-1]

1. An array contains values: 1, 2, 3, 4, 5. Write a program that modifies the array values. Display the array after each change.

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

1. Write a program that displays the name of month for a given month number (1 to 12). Define a month(n) function that returns the name of month for the number n. Store month names in an array. Then, using defined function, display month names for the following month numbers: 1, 9, 12.

   ```python
   def month(n):
      month_name = ["January","February",…]
      return month_name[…]
   ```

   Sample result:

   ```
   Enter month number: 10
   Month name: October
   ```

1. An array contains integer numbers: [34,7,19,4,21,8]. Create a program that calculates and displays the number of even values in the array. Use the ‘for’ loop statement.

   ```python
   arr = [34,7,19,4,21,8]
   even = 0
   for a in arr:
      if ...:
         even = even + 1
   print(...)
   ```

1. In a certain company, 25 employees commute by car, 19 employees commute by public transport, 32 people commute by bike, and 7 people commute on foot. Write a program that displays this data in a bar chart. Remember to add a title for the chart and a description of the chart axes. Sample result:

   See a similar task from the BEFORE CLASS section.

## Two dimensional arrays

1. An array contains values: [[2,5,4],[9,0,3]]. Create a program that displays:
   1. the array
   1. size of the array (number of rows and columns)
   1. value 5 from the array
   1. value 3 from the array
   1. second row of the array as below:

      9 0 3

   Sample result:

   ```python
   [[2,5,4],[9,0,3]]
   2 3
   5
   3
   9 0 3
   ```

1. An array contains values: [[1,3,5],[8,7,2]]. Write a program that calculates and displays:

   1. Sum of the first element in the first row and the last element in the last row
   1. Sum of the elements in the middle column
   1. Sum of the elements in the last row

   Sample result:

   ```python
   3
   10
   17
   ```

1. An array contains values: [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]. Create a program that calculates the sum of all odd numbers.

   ```python
   arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
   sum_odd = 0
   for row in arr:
      for element in row:
         if ...:
            sum_odd = …
   print(...)
   ```

1. An array contains values: [[0,0,0],[0,0,0],[0,0,0]]. Create a program that replaces the values of the main diagonal with 1. Use a loop statement. Display the modified array. Sample result:

   ```python
   1 0 0
   0 1 0
   0 0 1
   ```

1. An array contains values: [[True,False],[True,True],[False,False]]. Create a program that changes values of an array to the opposite. Use a loop statement. Sample result:

   ```python
   Before: [[True,False],[True,True],[False,False]]
   After:  [[False,True],[False,False],[True,True]]
   ```


## Practice Makes Perfect

1. Try to create the following arrays. Then, display the created array content.

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

1. An array contains integer numbers: 34,7,19,4,21,8. Create a program that calculates and displays the number of even values in the array. Use the ‘while’ loop statement.

1. An array contains natural numbers: 15, 8, 31, 47, 2, 19. Create a program that displays the contents of the array in reverse order. Use any loop statement. Sample result:

   ```python
   existed array: 15 8 31 47 2 19 
   reverse array: 19 2 47 31 8 15
   ```

1. Create a program that computes the second power of each array element. Sample result:

   ```python
   Array: 8 2 5 1 9
   2nd power: 64 4 25 1 81
   ```

1. An array contains numbers: -15, 8, -31, 47, -2, 19. Create a program that finds and displays the maximum and minimum number. Do not use available functions.

1. An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and displays the array and the arithmetic mean of array values. Use the “for” loop statement.

1. An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and displays the array and the arithmetic mean of array values. Use the “while” loop statement.

1. An array contains a list of Polish names:

   ```
   Genowefa, Onufry, Celestyna, Alojzy, Pankracy
   ```

   Create a program that displays the longest name (consisting of the largest number of characters). Sample result:

   ```
   Names: Genowefa Onufry Celestyna Alojzy Pankracy
   Longest name: Celestyna
   ```

1. An array contains integer numbers: 2, 6, 4, 9, 7. Create a program that displays the array values graphically as below. Define a function star(n) that returns the given number of asterisks as a string. Use a defined function in the program.

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

   Display both arrays and the result of comparison. Sample result:

   ```python
   Array1: water book sky
   Array2: water book sky
   Comparison: arrays are the same
   ```

1. Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. Create a program that displays the numbers from the first array that do not appear in the second array.

1. Create a program that sorts elements of an array containing integer numbers. Apply the Bubble Sort sorting algorithm. Define a function bubblesort(array) that returns the sorted array. Try to sort and display any three arrays.

1. Create a program that displays all unique elements in an array. Sample result:

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

1. Write a program that creates a tuple containing single word ‘computation’. Save a tuple in a variable. Then, display the type of the variable.

1. Write a program that displays the tuple (10,20,30,40,50) in reverse order. Sample result:

   ```python
   Tuple: 10,20,30,40,50
   Reverse order: 50,40,30,20,10
   ```

1. Write a program that for the tuple ("Seven", [10, 20, 30], (5, 15, 25)) displays values:
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

   calculates and displays results. Sample result:

   ```
   Numbers: 7,3,8,5,2
   Second largest number: 7 
   Median: 5
   Smallest and largest number: 2,8
   Numbers as a string: 7-3-8-5-2
   ```

1. Write a program that, for the given array of real numbers, displays the number of elements that are greater than the given value entered from the keyboard.

1. Write a program to separate even and odd numbers of a given array of integers. Put all even numbers first, and then odd numbers.

   Sample result:

   ```

   ```

1. Write a program that checks whether the first array is a subset of the second one (whether all elements of the first array appear in the second array).

1. Define a function rand_elem(array) that returns a randomly selected array element. Using the function, display a few randomly selected array elements.

1. A variable contains text:

   An apple a day keeps the doctor away

   Create a module MyText, containing:

   1. A function that returns the number of words in the text
   1. A function that returns an ordered array of words, from longest to shortest
   1. A function that returns an alphabetically ordered array of words

   Then, write a program, call the functions and display results. Sample result:

   ```
   Text: An apple a day keeps the doctor away
   Number of words: 8
   Words from the longest: doctor,apple,…
   Words ordered alphabetically: a,An,apple,away,…
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

   # display chart
   ...
   ...

1. Write a program that draws the function y = sin(x) for an angle value in the range 0-360 degrees.

1. A two-dimensional array of size 2 by 4 contains integer numbers. Create a program that displays array values in rows and columns.

1. A two-dimensional array contains the following numbers:

   ```
   7 3 7 9 0
   2 9 0 1 5
   3 8 6 4 7
   8 7 1 1 5
   ```

   Create a program that calculates the sum of values in the last column.

1. A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0. Create a program and the function. Then create a two-dimensional array with dimensions of 3 by 5. Display the created array.

1. An array contains values:

   ```
   [[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
   ```
   
   Create a program that modifies the array values to create a multiplication table as below. Use loop statements. Display the array.

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

1. A two-dimensional array of the size 3 by 5 contains integer numbers. Create a program that swaps the first and the last row. Display array values in rows and columns before and after changes.

1. A two-dimensional array of the size 3 by 5 contains integer numbers. Create a program that swaps the first and the last column. Display array values in rows and columns before and after changes.

1. In mathematics, a matrix is a rectangular array or table of numbers, symbols, or expressions, arranged in rows and columns, e.g.:

   ```
   -7  12 38
   41 -19 11
   ```

   Create a function identity_matrix(n) that returns an identity matrix(2D array) of size n.
   
   <https://en.wikipedia.org/wiki/Identity_matrix>
   
   Then, create a function that displays a 2D array in rows and columns. Finally, create a program that displays three identity matrices with dimensions of 3, 5 and 8. Sample result:

   ```
   1 0 0 0 0
   0 1 0 0 0
   0 0 1 0 0
   0 0 0 1 0
   0 0 0 0 1
   ```

1. Create a function transpose_matrix(m) that returns transposed matrix m:

   <https://en.wikipedia.org/wiki/Transpose> 

   Then, create a program that displays transposed matrices, in rows and columns, for the following matrices.
   1. 1 2 3\
      4 5 6\
      7 8 9
   1. 1 2 3 4 5\
      6 7 8 9 0
   1. 5 6 7 8
1. Create a function that convert two-dimensional (2D) array into 1D. Then create a program that displays 1D array for the following 2D arrays.

   1. 2 3\
      1 5 
   1. 5 0 3 7 5\
      9 0 9 1 2
   1. 2 1\
      3 5\
      7 4\
      2 6


