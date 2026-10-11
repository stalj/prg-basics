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

# Functions

**Course:** Fundamentals of Programming

---

# After this block, students should understand

- what a **function** is and why functions are useful,
- how to use **built-in functions** and functions from modules,
- how to define their own functions with `def`,
- how parameters, arguments, and return values work,
- how to divide a program into modules,
- how to test functions and organize larger programs.

---

# Why Do We Need Functions?

A function is a named block of code that performs one clear task.

Functions help us:

- avoid repeating the same code,
- divide a larger problem into smaller parts,
- make programs easier to read,
- test one part of a program independently,
- reuse solutions in many places.

> A function turns a repeated idea into a reusable tool.

---

# Function: The Basic Idea

A function usually follows this pattern:

```text
input data -> function -> result
```

Example:

```text
side lengths -> triangle_area() -> area
```

In Python, we already use functions from the first lesson.

```python
print('Hello World')
len('computer science')
type(50)
```

---

# Calling a Function

To execute a function, we **call** it.

```python
print('Hello World')
```

Function call elements:

- function name: `print`,
- parentheses: `(...)`,
- arguments: values passed to the function.

```python
max(7, 5, 6, 3, 8, 2)
```

> A function call asks Python to run a prepared piece of code.

---

# Built-in Functions

Python provides many functions that are ready to use.

| Function | Purpose | Example |
|---|---|---|
| `print()` | display information | `print('Hi')` |
| `input()` | read text from keyboard | `input('Name: ')` |
| `len()` | count elements | `len('book')` |
| `type()` | check type | `type(3.14)` |
| `max()` | largest value | `max(4, 8, 1)` |
| `min()` | smallest value | `min(4, 8, 1)` |

---

# Built-in Functions: Examples

```python
max_number = max(7, 5, 6, 3, 8, 2)
min_number = min(4, 7, 2, 3, 9, 8)
text_length = len('computer science')

print(max_number)
print(min_number)
print(text_length)
```

Other useful examples:

```python
int('20303')
bin(304)
hex(304)
ord('€')
abs(-17)
```

---

# Built-in Functions Are Also Abstractions

When we write:

```python
len('computer science')
```

we do not need to know how Python counts the characters internally.

We only need to know:

- what the function does,
- what input it expects,
- what result it returns.

> Abstraction means using a tool without knowing every internal detail.

---

# Functions From Modules

Not every function is available immediately.

Some functions are stored in modules.

```python
import math

square_root = math.sqrt(7)
print(square_root)
```

> A module is a file or library that contains ready-to-use code.

---

# Why Modules Matter

Modules help organize code by topic.

| Module | Example function | Use |
|---|---|---|
| `math` | `sqrt()` | mathematical calculations |
| `math` | `sin()` | trigonometry |
| `random` | `randint()` | random numbers |

> A module is a toolbox. Importing it gives the program access to its tools.

---

# Using the Math Module

```python
import math

square_root = math.sqrt(7)
logarithm = math.log(5)
angle = math.radians(90)
sine = math.sin(angle)

print(square_root)
print(logarithm)
print(sine)
```

Important idea:

```python
math.sqrt(7)
```

> means: use the function `sqrt()` from the module `math`.

---

# Using the Random Module

Randomness allows us to simulate events.

```python
import random

roll = random.randint(1, 6)
print('Dice roll:', roll)
```

This function needs two arguments:

```python
random.randint(start, end)
```

> It returns an integer from the selected range, including both limits.

---

# Defining Our Own Function

A function is defined with the `def` keyword.

```python
def function_name(parameters):
    # function body
    return result
```

Function components:

- `def` starts the definition,
- the name identifies the function,
- parameters define input data,
- the body contains the algorithm,
- `return` sends the result back.

---

# First Custom Function

```python
def add(a, b):
    result = a + b
    return result

sum_value = add(5, 3)
print(sum_value)
```

What happens?

1. `5` is assigned to `a`.
2. `3` is assigned to `b`.
3. The function calculates `a + b`.
4. The result is returned.
5. The result is stored in `sum_value`.

---

# Parameters and Arguments

These two words are related, but not identical.

| Term | Meaning | Example |
|---|---|---|
| Parameter | variable in the function definition | `a`, `b` |
| Argument | actual value passed during a call | `5`, `3` |

```python
def add(a, b):      # a and b are parameters
    return a + b

add(5, 3)           # 5 and 3 are arguments
```

---

# Return Value

A function can calculate a value and return it to the program.

```python
def square(number):
    return number ** 2

result = square(6)
print(result)
```

Important:

```python
return number ** 2
```

> means: send this value back to the place where the function was called.

---

# Returning vs Printing

`return` and `print()` are not the same.

```python
def square(number):
    return number ** 2
```

This function gives a result that can be reused.

```python
area = square(5)
price = square(5) * 2
```

```python
def show_square(number):
    print(number ** 2)
```

This function only displays information.

---

# A Function Should Usually Do One Thing

Weak design:

```python
def process_data():
    # reads input
    # calculates result
    # prints result
    # saves data
```

Better design:

```python
def calculate_area(a, b):
    return a * b
```

> A good function has a clear name and one main responsibility.

---

# Example: Triangle Area

Task: define a function that calculates triangle area from three side lengths.

We can use Heron's formula:

```text
s = (a + b + c) / 2
area = sqrt(s * (s - a) * (s - b) * (s - c))
```

The function receives three numbers and returns one number.

```text
a, b, c -> triangle_area() -> area
```

---

# Triangle Area: Function

```python
import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
```

Example calls:

```python
print(triangle_area(3, 4, 5))
print(triangle_area(5, 12, 13))
print(triangle_area(7, 24, 25))
```

---

# Example: Sum of Digits

Problem: calculate the sum of digits in an integer number.

Algorithm:

1. Read an integer number.
2. Use `abs()` to ignore a possible minus sign.
3. Convert the number to text with `str()`.
4. Go through every digit.
5. Convert each digit back to integer.
6. Add digits to the total.

---

# Sum of Digits: Function

```python
def sum_digits(number):
    number = abs(number)
    text = str(number)
    total = 0

    for digit in text:
        total += int(digit)

    return total
```

Usage:

```python
any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of digits is {result}')
```

---

# Functions and Decisions

Functions can contain conditional statements.

```python
def pts_to_grade(points):
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'

    return grade
```

---

# Why Order of Conditions Matters

In this grading function, conditions must be checked from the highest threshold.

```python
if points >= 18:
    grade = 'Excellent'
elif points >= 14:
    grade = 'Good'
elif points >= 10:
    grade = 'Satisfactory'
else:
    grade = 'Fail'
```

If we start with `points >= 10`, then a result of 19 would already match the first condition.

---

# Functions and Selection Problems

A function can convert a code or number into a meaningful description.

```python
def day_name(day_number):
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number == 3:
        result = 'Wednesday'
    else:
        result = 'Unknown day'

    return result
```

---

# Function Naming

Good function names usually start with a verb or describe a result.

| Weak name | Better name |
|---|---|
| `f()` | `sum_digits()` |
| `calc()` | `triangle_area()` |
| `test()` | `is_valid_password()` |
| `data()` | `input_integer()` |

> A function name should tell the reader what the function is expected to do.

---

# Boolean Functions

Some functions answer a yes-or-no question.

They return `True` or `False`.

```python
def is_even(number):
    return number % 2 == 0
```

```python
def is_binary(text):
    for char in text:
        if char != '0' and char != '1':
            return False
    return True
```

> Names often start with `is_`, `has_`, or `can_`.

---

# Functions and Loops

Functions can contain loops when the task requires repetition.

```python
def count_letter(text, letter):
    counter = 0

    for char in text:
        if char == letter:
            counter += 1

    return counter
```

Example:

```python
count_letter('computer science', 'e')
```

---

# Functions Returning Text

A function can return a string.

```python
def hide(card_number):
    first = card_number[0:2]
    last = card_number[-4:]
    stars = '*' * 10
    return first + stars + last
```

Example:

```python
print(hide('5290312400019022'))
```

Result:

```text
52**********9022
```

---

# Dividing Code Into Modules

A larger program can be divided into files.

Example:

```text
converters.py       # functions for unit conversion
test_converters.py  # program that uses these functions
```

Benefits:

- related functions are stored together,
- the main program is shorter,
- functions can be reused in other programs.

---

# Creating a Simple Module

File: `converters.py`

```python
def cm_to_m(cm):
    return cm / 100

def m_to_cm(m):
    return m * 100
```

File: `test_converters.py`

```python
import converters

print(converters.cm_to_m(175))
print(converters.m_to_cm(1.75))
```

---

# Importing From Your Own Module

When importing a module:

- use the file name without `.py`,
- place the module in the same folder as the main program,
- call functions through the module name.

```python
import converters

meters = converters.cm_to_m(170)
```

Alternative form:

```python
from converters import cm_to_m

meters = cm_to_m(170)
```

---

# Input Helper Functions

We can write functions that read and convert data.

```python
def input_string(message):
    value = input(message)
    return value

def input_integer(message):
    value = input(message)
    return int(value)

def input_real(message):
    value = input(message)
    return float(value)

def input_boolean(message):
    value = input(message)
    return value == 'y'
```

---

# Using Input Helper Functions

```python
import keyboard

first_name = keyboard.input_string('Enter name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
hide_salary = keyboard.input_boolean('Hide salary? (y/n): ')

print('DATA RECORD')
print('Name:', first_name)
print('Age:', age)

if not hide_salary:
    print('Salary:', salary)
```

---

# Program Entry Point

A Python file can be run directly or imported as a module.

```python
def add(a, b):
    return a + b

if __name__ == '__main__':
    print(add(10, 5))
```

The block runs only when this file is executed directly.

It does not run automatically when the file is imported.

---

# The main Function

For larger programs, it is common to define `main()`.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    x = 10
    y = 5
    print(add(x, y))
    print(subtract(x, y))

if __name__ == '__main__':
    main()
```

---

# Recursion

A recursive function calls itself.

Example: factorial.

```text
5! = 5 * 4 * 3 * 2 * 1
```

Recursive idea:

```text
n! = n * (n - 1)!
```

Every recursive solution needs:

- a base case,
- a recursive step.

---

# Recursive Factorial

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)
```

Call example:

```python
print(factorial(5))
```

How to read it:

```text
factorial(5) = 5 * factorial(4)
```

The calculation stops when `n` becomes `1`.

---

# Recursion vs Iteration

Some problems can be solved with a loop or with recursion.

Loop version:

```python
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```

Recursive version:

```python
def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)
```

---

# Common Beginner Mistakes

| Mistake | Example | How to think about it? |
|---|---|---|
| Forgetting parentheses | `print` | a function call needs `()` |
| Forgetting `return` | result is not sent back | use `return` when a value is needed |
| Printing instead of returning | `print(result)` | printing is not reusable |
| Wrong indentation | body not inside function | function body must be indented |
| Name mismatch | `sumDigit()` vs `sum_digits()` | names must match exactly |


---

# From Task to Function

When designing a function, ask:

1. What should the function do?
2. What input data does it need?
3. What value should it return?
4. What is a good name for it?
5. How will I test it?

Example:

```text
Task: check if a password is valid
Input: password text
Output: True or False
Name: is_valid_password
```

---

# Summary

This block introduced functions as reusable program components.

Students should now understand:

- how to call built-in and module functions,
- how to define custom functions with `def`,
- how parameters, arguments, and return values work,
- why functions improve readability and reuse,
- how to divide code into modules,
- how to test functions and use a program entry point,
- the basic idea of recursion.

