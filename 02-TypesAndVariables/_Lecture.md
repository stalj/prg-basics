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

# Types and Variables

**Course:** Fundamentals of Programming  

---

# After this block, students should understand

- the difference between **interactive mode** and **script mode**,
- how programs store data in **variables**,
- what **data types** and **operators** are,
- how to read input, format output, and work with text,
- how to build simple logical expressions.

---

# Programming: The Basic Idea

## A program is a precise description of computation

Input data → processing → result

Example:

```text
height, weight → BMI calculation → user information
```
`BMI = weight / (height/100 * height/100)` # height in cm

> Programming means writing this procedure in a language that a computer can execute.

---

# Interactive Mode

Interactive mode lets you type single instructions and immediately see the result.

```python
>>> 7 + 4
11
>>> 2 ** 3
8
>>> 7 > 5
True
```

Best for:

- quick expression testing,
- experimenting with the language,
- checking small pieces of code.

---

# Script Mode

In script mode, we save a program in a file, for example `bmi.py`, and then run the whole file.

```bash
py bmi.py
```

```python
height = input('Enter your height in cm: ')
weight = input('Enter your weight in kg: ')
height = int(height)
weight = int(weight)
bmi = weight / (height/100)**2
print('Your BMI is', round(bmi, 2))
```

---

# When to Use Each Mode?

| Situation | Interactive mode | Script mode |
|---|---:|---:|
| Quick calculation | ✓ |  |
| Testing a function or operator | ✓ |  |
| Multi-line program |  | ✓ |
| Reusable program |  | ✓ |
| Syntax practice | ✓ | ✓ |

---

# Programming Environment

An IDE, such as Visual Studio Code, combines several tools in one place:

- code editor,
- terminal,
- program execution,
- syntax hints,
- project file organization.

```python
import random
print("Dice rolling simulator")
for i in range(5):
    dice_roll = random.randint(1, 6)
    print(dice_roll, end=" ")
```

---

# Expressions and Values

An **expression** is a piece of code that produces a value after evaluation.

```python
3 * 2 + 1      # 7
5 + 10 * 5     # 55
True != False  # True
```

> A value can be a number, text, or a logical value.

---

# Operators

An operator tells the computer what operation to perform on data.

| Operator | Meaning | Example |
|---|---|---|
| `+` | addition / string concatenation | `2 + 3`, `'A' + 'B'` |
| `*` | multiplication | `4 * 5` |
| `**` | exponentiation | `2 ** 3` |
| `/` | division | `7 / 2` |
| `//` | integer division | `7 // 2` |
| `%` | remainder after division | `7 % 2` |

---

# Order of Operations

Python follows an order similar to mathematics.

1. Parentheses: `( )`
2. Exponentiation: `**`
3. Multiplication, division, remainder: `* / // %`
4. Addition and subtraction: `+ -`
5. Comparisons: `>`, `<`, `==`, `!=`

```python
4 + 4 / 2 ** 2
4 + 4 / 4
4 + 1.0
```

---

# Data Type

A data type defines **what kind of value** we store and what can be done with it.

| Type | Meaning | Example |
|---|---|---|
| `int` | integer number | `50` |
| `float` | real number | `149.17` |
| `bool` | true/false | `True` |
| `str` | string/text | `'Krakow University of Economics'` |

```python
type(50)       # int
type(2 > 5)    # bool
```

---

# Type Affects Operator Behavior

The same operator can behave differently for different types.

```python
2 + 3          # 5
'2' + '3'      # '23'
```

```python
4 * 7          # 28
4.0 * 7        # 28.0
```

> Conclusion: the computer performs operations formally, according to data types.

---

# Variable


## A variable is a named value

Name → value → type


```python
company = "ABC Data"
employees = 25
remote_work = True
income_per_person = 4500000 / employees
```

> A variable lets us store a result and use it later.

---

# Good Variable Names

A good name explains **what a value represents**.

```python
# weak
x = 70
v = x / 3.6

# better
speed_kmh = 70
speed_ms = speed_kmh / 3.6
```

> **Practical rule**: a name should help us read the program like a description of the solution.

---

# Assignment

The `=` sign in programming does not ask “are these equal?”; it means **assignment**.

```python
x = 7
x = x + 1
print(x)  # 8
```

Read it as:

> calculate the value on the right-hand side and store it under the name on the left-hand side.

---

# Swapping Variable Values

Problem: `x = 7`, `y = 34`. After swapping, we need `x = 34`, `y = 7`.

```python
x = 7
y = 34
z = x
x = y
y = z
```

> The auxiliary variable `z` acts as a temporary storage place.

---

# Modules and Functions

We do not need to write everything ourselves. The language provides ready-made functions, and modules extend its capabilities.

```python
import math

a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
```

```python
import random

dice_roll = random.randint(1, 6)
```

---

# Program Output

A program communicates results with `print()`.

```python
number1 = 71
number2 = 14
result = number1 + number2
print('The result of summation:', result)
```

> In educational programs, it is useful to print not only the result, but also its meaning.

---

# F-strings

An f-string makes it easy to insert variable values into text.

```python
name = "Adam"
age = 19
height = 180

print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height} cm.")
print(f"In 6 years I will be {age + 6} years old.")
```

> This is the clearest way to format simple messages.

---

# Number Formatting

Often we want to limit the number of decimal places.

```python
amount = 15.84
vat = amount * 0.23

print(f"Amount  : {amount:.2f}")
print(f"VAT 23% : {vat:.2f}")
```

> `:.2f` means: display a floating-point number with two decimal places.

---

# Input Data

`input()` pauses the program and reads text typed by the user.

```python
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your full name is {full_name}')
```

> Important: `input()` always returns a value of type `str`.

---

# Type Conversion

When the user enters a number, the program still receives text.

```python
cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)
volume = cube_side ** 3
```

Common conversions:

- `int(...)` — integer number,
- `float(...)` — real number,
- `str(...)` — string/text.

---

# Typical Structure of a Calculation Program


**Read data** → **Convert types** → **Calculate** → **Format result** → **Display**


```python
price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))
new_price = price * (1 - discount / 100)
reduction = price - new_price
print(f'Price with discount: {new_price:.2f}')
print(f'Reduction: {reduction:.2f}')
```

---

# Strings as Sequences of Characters

A `str` is an ordered sequence of characters.

```python
name = 'Anna'
len(name)      # 4
name[0]        # 'A'
name[1]        # 'n'
```

Indexing starts from zero.

```text
A  n  n  a
0  1  2  3
```

---

# Slicing Text

Slicing lets us take a fragment of a string.

```python
employee = "Mr. John May, born on 1998-02-16"

employee[4:8]      # 'John'
employee[9:12]     # 'May'
employee[-10:]     # '1998-02-16'
```

> The notation `text[a:b]` means: from index `a` to index `b - 1`.

---

# Practical String Operations

```python
movie = "The Lord of the Rings: The Return of the King"

len(movie)
movie.upper()
movie.lower()
movie.count('e')
movie.find('Lord')
```

> These operations are the basis for processing textual data: names, codes, numbers, abbreviations, and identifiers.

---

# Characters and Codes

A computer stores characters as numbers.

```python
ord('A')   # 65
ord('B')   # 66
chr(67)    # 'C'
```

Example use:

```python
first = 'A'
last = 'D'
letters_between = ord(last) - ord(first) - 1
```

---

# Logical Values

The `bool` type has only two values:

```python
True
False
```

They most often appear as the result of a comparison:

```python
age = 22
no_tax = age <= 26
```

A logical value answers the question: **is the condition satisfied?**

---

# Comparison Operators

| Operator | Meaning | Example |
|---|---|---|
| `==` | equal to | `x == 5` |
| `!=` | not equal to | `x != 5` |
| `>` | greater than | `x > 5` |
| `<` | less than | `x < 5` |
| `>=` | greater than or equal to | `x >= 5` |
| `<=` | less than or equal to | `x <= 5` |

> Note: `=` assigns, while `==` compares.

---

# Logical Operators

Logical operators combine conditions.

```python
speed = 120
speed_ok = speed >= 40 and speed <= 140
```

```python
car_number = 'KR12345'
is_krakow = car_number[0:2] == 'KR' or car_number[0:2] == 'KK'
```

```python
not speed_ok
```

---

# Remainder and Even Numbers

The `%` operator returns the remainder after division.

```python
7 % 2   # 1
8 % 2   # 0
```

A number is even when the remainder after division by 2 is 0.

```python
number = int(input('Enter number: '))
even = number % 2 == 0
print(f'Number is even: {even}')
```

---

# Randomness in a Program

Randomness allows us to simulate events, for example rolling a dice.

```python
import random

dice_roll = random.randint(1, 6)
print(dice_roll)
```

We can combine random values with logical conditions:

```python
special = dice_roll == 1 or dice_roll == 6
```

---

# Algorithm


## An algorithm is an ordered way to solve a problem


Example: area and circumference of a circle.

```text
1. Set radius r
2. Set the value of pi
3. Calculate area: pi * r ** 2
4. Calculate circumference: 2 * pi * r
5. Display the results
```

---

# From Task to Program


### Task

Calculate transport cost using distance, fuel price, and fuel consumption.


### Program

```python
distance = int(input('Distance: '))
fuel_price = float(input('Fuel price: '))
consumption = float(input('L/100 km: '))
fuel = distance * consumption / 100
cost = fuel * fuel_price
print(f'Cost: {cost:.2f}')
```


---

# Common Beginner Mistakes

| Mistake | Example | How to think about it? |
|---|---|---|
| Missing conversion | `input() + 5` | `input()` gives text |
| Typo in a name | `averege` | names must match exactly |
| Confusing `=` and `==` | `x = 5` | assignment vs comparison |
| Wrong order of operations | `a+b/2` | use parentheses |
| Unclosed string | `'Average` | quotation marks must come in pairs |

---

# Summary

This block introduced programming foundations:

- a program as an algorithm written in a programming language,
- values, types, variables, and operators,
- program input and output,
- strings as data,
- logical conditions as preparation for control structures.

> The natural next step: conditional statements and loops.
