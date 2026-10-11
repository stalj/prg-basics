---
marp: true
theme: default
paginate: true
size: 16:9
---

<!--
_class: lead invert
_paginate: false
-->

# Arrays

**Course:** Fundamentals of Programming

---

# After this block, students should understand

- how to store many values under one name,
- how to access and modify elements by index,
- how to process lists with loops,
- how to analyze collections of data,
- how to work with two-dimensional arrays,
- how simple sorting algorithms work.

---

# Why Do We Need Arrays?

A variable stores one value.

```python
temperature = 7
```

But many problems require storing many related values.

```python
temperatures = [3, 7, 1, -2, 6, -4]
```

> An array-like structure lets us treat many values as one collection.

---

# Lists as Arrays in Python

Python commonly uses lists for basic array-like tasks.

```python
numbers = [2, 3, 7, 5, 4]
```

A list is:

- ordered,
- indexed,
- changeable,
- able to store many values.

> In this block, we use Python lists as practical arrays.

---

# Lists and Arrays

| Feature | Python list | Classical array |
|---|---|---|
| Data type | Can be mixed | Usually one type |
| Size | Flexible | Often fixed |
| Use | General data | Structured data |
| Numerical speed | Good for basics | Better with special libraries |

> For beginners, a list is the most convenient way to learn array thinking.

---

# Creating a List

A list is created with square brackets.

```python
arr = [2, 3, 7, 5, 4]
```

The list has:

- a name: `arr`,
- elements: `2`, `3`, `7`, `5`, `4`,
- positions called indexes.

---

# Indexing

Indexes start from zero.

```text
values:   2   3   7   5   4
indexes:  0   1   2   3   4
```

```python
arr = [2, 3, 7, 5, 4]
print(arr[0])  # 2
print(arr[1])  # 3
print(arr[4])  # 4
```

> The first element has index `0`, not `1`.

---

# Length of a List

The `len()` function returns the number of elements.

```python
arr = [2, 3, 7, 5, 4]
number_of_elements = len(arr)
print(number_of_elements)  # 5
```

The last valid index is:

```python
len(arr) - 1
```

---

# First, Last, and Middle Elements

```python
arr = [2, 3, 7, 5, 4]

first = arr[0]
last = arr[len(arr) - 1]
middle = arr[len(arr) // 2]
```

For this list:

```text
first = 2
last = 4
middle = 7
```

---

# Negative Indexes

Python also allows negative indexes.

```python
arr = [2, 3, 7, 5, 4]

print(arr[-1])  # 4
print(arr[-2])  # 5
```

Negative indexes count from the end.

```text
values:    2   3   7   5   4
indexes:  -5  -4  -3  -2  -1
```

---

# Modifying List Elements

Lists are changeable.

```python
arr = [1, 2, 3, 4, 5]

arr[0] = arr[0] - 1
arr[len(arr) - 1] = arr[len(arr) - 1] + 4
arr[2] = arr[2] * 2

print(arr)
```

Result:

```text
[0, 2, 6, 4, 9]
```

---

# Processing a List with a for Loop

A `for` loop can process every element.

```python
shopping_list = [
    'milk', 'bread', 'eggs', 'butter', 'cheese'
]

for item in shopping_list:
    print(item)
```

> Use this form when you need values, not indexes.

---

# Processing a List with Indexes

Sometimes we need the position of each element.

```python
games = ['Minecraft', 'Fortnite', 'The Witcher 3']

i = 0
while i < len(games):
    print(i + 1, games[i])
    i += 1
```

> Use indexes when the position matters.

---

# Searching in a List

Example: print registration numbers from Krakow.

```python
plates = ['KR5233F', 'PO6987E', 'KK12255', 'WA7930T']

for plate in plates:
    if plate[0:2] == 'KR' or plate[0:2] == 'KK':
        print(plate)
```

The list stores data.

The condition selects only the data we need.

---

# Counting Values

Example: test answers stored as logical values.

```python
test_results = [False, True, False, True, True]

correct = 0
for answer in test_results:
    if answer:
        correct += 1

incorrect = len(test_results) - correct
percentage = correct / len(test_results) * 100
```

> Counting is one of the most common list operations.

---

# Aggregating Values

Aggregation means calculating one result from many values.

```python
temperatures = [3, 7, 1, -2, 6, -4]

total = 0
for temp in temperatures:
    total += temp

average = total / len(temperatures)
```

> Common aggregations: sum, average, minimum, maximum,  count.

---

# Built-in Functions for Lists

Python gives us useful functions.

```python
temperatures = [3, 7, 1, -2, 6, -4]

number = len(temperatures)
minimum = min(temperatures)
maximum = max(temperatures)
total = sum(temperatures)
```

> Built-in functions make programs shorter, but loops help us understand the algorithm.

---

# Parallel Lists

Sometimes related data is stored in separate lists.

```python
categories = ['Food', 'Transport', 'Rent', 'Entertainment']
expenses = [500, 150, 1000, 200]
```

The same index connects the values.

```text
Food            500
Transport       150
Rent           1000
Entertainment   200
```

---

# Processing Parallel Lists

```python
categories = ['Food', 'Transport', 'Rent', 'Entertainment']
expenses = [500, 150, 1000, 200]

max_index = 0
for i in range(len(expenses)):
    if expenses[i] > expenses[max_index]:
        max_index = i

print(categories[max_index], expenses[max_index])
```

> The index connects the category with its value.

---

# Sorting Data

Sorting means arranging elements in a defined order.

```python
numbers = [7.2, 6.8, 7.5, 7.0]
sorted_numbers = sorted(numbers)
```

Result:

```text
[6.8, 7.0, 7.2, 7.5]
```

> Sorting helps with: analysis, reporting, searching, presentation.

---

# Built-in Sorting

In real programs, we often use built-in sorting.

```python
distances = [120, 150, 180, 90, 200]
print(sorted(distances))
```

Descending order:

```python
temperatures = [16, 17, 15, 14, 18]
print(sorted(temperatures, reverse=True))
```

> Learn the algorithm first, then use built-in tools when appropriate.

---

# Two-Dimensional Arrays

A two-dimensional array stores data in rows and columns.

```python
board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]
```

This structure can represent:

- game boards,
- tables,
- weekly plans,
- seats in a cinema.

---

# Accessing 2D Elements

Use two indexes:

```python
board[row][column]
```

Example:

```python
board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

print(board[0][0])  # X
print(board[1][2])  # O
```

> The first index selects the row. The second selects the element in that row.

---

# Printing a 2D Array

A nested loop processes rows and elements.

```python
for row in board:
    for cell in row:
        print(cell, end=' ')
    print()
```

Output:

```text
X O X
  X O
O   X
```

---

# Monthly Expenses as a 2D Array

```python
monthly_expenses = [
    [200, 50, 100],
    [180, 60, 110],
    [220, 55, 105],
    [210, 65, 95]
]
```

Rows can represent weeks.

Columns can represent categories.

```text
Food, Transport, Utilities
```

---

# Summing Rows

A row sum gives the total for one week.

```python
for week in monthly_expenses:
    week_total = 0
    for value in week:
        week_total += value
    print(week_total)
```

> Row processing is useful when each row is one object or time period.

---

# Summing Columns

A column sum gives the total for one category.

```python
food_total = 0
for week in monthly_expenses:
    food_total += week[0]

transport_total = 0
for week in monthly_expenses:
    transport_total += week[1]
```

> Column processing is useful when the same position has the same meaning in every row.

---

# Functions Working with Arrays

Functions make array processing reusable.

```python
def seats_available(seats):
    available = 0
    for row in seats:
        for seat in row:
            if seat == 'A':
                available += 1
    return available
```

The same function works for any seating plan with the same symbols.

---

# Matrix Diagonal

A square matrix has the same number of rows and columns.

```python
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
```

The main diagonal contains elements where row index equals column index.

```text
[0][0], [1][1], [2][2]
```

---

# Creating an Identity Matrix

```python
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(matrix)):
    matrix[i][i] = 1
```

Result:

```text
1 0 0
0 1 0
0 0 1
```

---

# Tuples

A tuple is an ordered collection that cannot be changed after creation.

```python
values = (10, 20, 30, 40, 50)
```

Lists are mutable.

Tuples are immutable.

Use tuples when the collection should stay constant.

---

# List Comprehensions

A list comprehension creates a list from a rule.

```python
arr = [i for i in range(1, 10)]
```

```python
squares = [i * i for i in range(1, 6)]
```

```python
zeros = [0 for i in range(15)]
```

> It is a compact way to generate data.

---

# Typical Beginner Mistakes

| Mistake | Example | How to think about it |
|---|---|---|
| Wrong first index | `arr[1]` as first item | first index is `0` |
| Index too large | `arr[len(arr)]` | last index is `len(arr) - 1` |
| Forgetting nested loops | printing 2D data | one loop for rows, one for cells |
| Mixing row and column | `matrix[col][row]` | usually `matrix[row][col]` |
| Modifying while iterating | changing structure unexpectedly | plan changes carefully |

---

# Summary

This block introduced arrays as collections of data:

- one-dimensional lists,
- indexes and element modification,
- loops for processing data,
- searching, counting, summing, and sorting,
- two-dimensional arrays,
- tuples and generated lists.

> Arrays help us move from single values to structured data processing.
