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

# Functional Programming

**Course:** Fundamentals of Programming

---

# After this block, students should understand

- what **functional programming** means,
- how to use **lambda functions**,
- what **first-class** and **higher-order functions** are,
- how to transform data with **map()**,
- how to select data with **filter()**,
- how to reduce many values into one result with **reduce()**.

---

# Programming Paradigms

A programming paradigm is a way of thinking about program structure.

Python supports several paradigms:

- procedural programming,
- object-oriented programming,
- functional programming.

> Functional programming is not a replacement for everything else. It is another useful tool for solving some types of problems clearly.

---

# Functional Programming: The Basic Idea

Functional programming treats computation as the evaluation of functions.

```text
input data -> function -> result
```

Example:

```python
def square(x):
    return x * x

result = square(5)
```

> The emphasis is on transforming values, not on changing program state step by step.

---

# Imperative vs Functional Style

## Imperative style

```python
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
    squares.append(n * n)
```

## Functional style

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda n: n * n, numbers))
```

Both versions solve the same problem.

---

# Key Ideas of Functional Programming

| Concept | Meaning |
|---|---|
| Pure function | result depends only on arguments |
| Immutability | avoid changing existing data |
| First-class function | a function can be stored and passed around |
| Higher-order function | a function takes or returns another function |
| Recursion | repetition through function calls |

---

# Pure Functions

A pure function always returns the same result for the same input.

```python
def add_tax(price):
    return price * 1.23
```

This function is predictable:

```python
add_tax(100)  # 123.0
add_tax(100)  # 123.0
```

> Pure functions are easier to test, debug, and reuse.

---

# Side Effects

A side effect is a change outside the function result.

Examples of side effects:

- printing on the screen,
- reading from the keyboard,
- writing to a file,
- modifying a global variable,
- changing a list passed as an argument.

```python
def show_price(price):
    print(price)  # side effect
```

---

# Immutability

In functional programming, we prefer creating new values instead of modifying existing ones.

```python
numbers = [1, 2, 3]
new_numbers = numbers + [4]
```

The original list remains unchanged:

```python
numbers      # [1, 2, 3]
new_numbers  # [1, 2, 3, 4]
```

> This makes data flow easier to understand.

---

# First-Class Functions

In Python, functions are values.

You can assign a function to a variable:

```python
def double(x):
    return x * 2

operation = double
print(operation(5))  # 10
```

You can also pass a function as an argument to another function.

---

# Lambda Functions

A lambda function is a short anonymous function.

```python
lambda arguments: expression
```

Example:

```python
mean = lambda x, y: (x + y) / 2

result = mean(10, 20)
print(result)  # 15.0
```

> Lambda functions are useful when a small function is needed only once.

---

# Regular Function vs Lambda Function

## Regular function

```python
def ms_to_kmh(ms):
    return ms * 3.6
```

## Lambda function

```python
ms_to_kmh = lambda ms: ms * 3.6
```

Usage is the same:

```python
print(ms_to_kmh(10))  # 36.0
```

---

# When to Use Lambda Functions?

Use a lambda function when:

- the operation is short,
- the function is used locally,
- the function is passed as an argument,
- the name of the function is not very important.

Avoid lambda functions when the logic becomes complex.

```python
is_even = lambda number: number % 2 == 0
```

---

# Higher-Order Functions

A higher-order function is a function that:

- receives another function as an argument, or
- returns another function as a result.

Example:

```python
def apply(operation, value):
    return operation(value)

result = apply(lambda x: x * 2, 7)
print(result)  # 14
```

---

# Returning a Function

A function can create and return another function.

```python
def min_pts(limit):
    def check(pts):
        return pts >= limit
    return check

assess_test = min_pts(50)
print(assess_test(52))  # True
print(assess_test(39))  # False
```

> The returned function remembers the value of `limit`.

---

# Sorting with a Key Function

The `sorted()` function can use another function as a sorting rule.

```python
names = ['James', 'Emily', 'William', 'Olivia', 'Benjamin']

sorted_names = sorted(names, key=lambda name: len(name))
```

Result:

```python
['James', 'Emily', 'Olivia', 'William', 'Benjamin']
```

---

# Data Processing Pipeline

Functional programming often uses a pipeline of transformations.

```text
source data -> map -> filter -> reduce -> result
```

Typical questions:

- How should each value be transformed?
- Which values should be kept?
- How should all values be combined into one result?

---

# map(): Transform Each Element

`map()` applies a function to every element of a collection.

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))

print(squares)  # [1, 4, 9, 16]
```

> Use `map()` when the output list should have one result for each input element.

---

# Example: Currency Conversion

Credit card payments in Euro:

```python
transactions_in_eur = [15.90, 38.47, 4.07, 132.70, 9.15]
```

Convert to PLN using `1 EUR = 4.5 PLN`:

```python
transactions_in_pln = list(
    map(lambda amount: round(amount * 4.5, 2), transactions_in_eur)
)

print(transactions_in_pln)
```

---

# Example: Word Lengths

For a text, calculate the length of each word.

```python
sentence = 'I completely agree with you'
words = sentence.split()

lengths = list(map(lambda word: len(word), words))

print(lengths)  # [1, 10, 5, 4, 3]
```

> `split()` changes text into a list of words.

---

# Example: Stock Value

Each tuple stores quantity and unit price.

```python
stock = [(20, 5.50), (15, 8.30), (37, 3.85), (4, 11.60)]

values = list(map(lambda item: item[0] * item[1], stock))
total = sum(values)

print(round(total, 2))
```

A tuple can be accessed by index:

```python
item[0]  # quantity
item[1]  # price
```

---

# filter(): Select Elements

`filter()` keeps only elements for which the function returns `True`.

```python
numbers = [2, 7, 4, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # [2, 4, 10]
```

> Use `filter()` when some elements should be removed from further processing.

---

# Example: Surnames Starting with J

```python
employees = [
    'SMITH Lucy', 'JONES Janet', 'LEE Jerry',
    'JACKSON Peter', 'JOHNSON Rick'
]

emp_j = list(filter(lambda e: e[0] == 'J', employees))

for employee in emp_j:
    print(employee)
```

Result:

```text
JONES Janet
JACKSON Peter
JOHNSON Rick
```

---

# Example: Speed Camera

The allowed speed is 50 km/h.

```python
speeds = [48, 47, 54, 50, 42, 68, 39, 46]

too_fast = list(filter(lambda speed: speed > 50, speeds))

print(too_fast)  # [54, 68]
```

The lambda function describes the condition:

```python
lambda speed: speed > 50
```

---

# Example: Excluding Negative Grades

In this course, grade `2.0` means a negative grade.

```python
grades = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0]

positive_grades = list(filter(lambda grade: grade != 2.0, grades))
average = sum(positive_grades) / len(positive_grades)

print(round(average, 2))
```

---

# reduce(): Combine Values

`reduce()` combines many values into one value.

It is available in the `functools` module.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)

print(result)  # 15
```

> Use `reduce()` when each step combines the current result with the next value.

---

# How reduce() Works

```python
numbers = [1, 2, 3, 4, 5]
reduce(lambda x, y: x + y, numbers)
```

Step by step:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
```

Final result:

```python
15
```

---

# Combining filter() and reduce()

Task: calculate the sum of even numbers.

```python
from functools import reduce

numbers = [2, 4, 6, 3, 7, 5]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
result = reduce(lambda x, y: x + y, even_numbers)

print(result)  # 12
```

> First select data, then combine it.

---

# map(), filter(), reduce(): Comparison

| Function | Main question | Result |
|---|---|---|
| `map()` | How to transform each element? | collection |
| `filter()` | Which elements should remain? | collection |
| `reduce()` | How to combine all elements? | single value |

Examples:

```python
map(lambda x: x * 2, numbers)
filter(lambda x: x > 0, numbers)
reduce(lambda x, y: x + y, numbers)
```

---

# Functional Style and Readability

Functional style can make programs concise.

```python
result = sum(map(lambda item: item[0] * item[1], stock))
```

But clarity is more important than short code.

A longer version may be easier for beginners:

```python
values = map(lambda item: item[0] * item[1], stock)
result = sum(values)
```

---

# Common Beginner Mistakes

| Mistake | Example | How to think about it? |
|---|---|---|
| Forgetting `list()` | `map(...)` | `map()` returns an iterable |
| Too complex lambda | long expression | define a regular function |
| Confusing map and filter | filtering with map | map transforms, filter selects |
| Missing import | `reduce(...)` | use `from functools import reduce` |
| Wrong data type | input as text | convert before calculation |

---

# From Task to Functional Program

## Task

For numbers from 1 to 20, calculate third powers only for numbers divisible by 2 and 3.

## Program

```python
numbers = range(1, 21)
selected = filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers)
powers = list(map(lambda x: x ** 3, selected))

print(powers)
```

---

# Summary

This block introduced functional programming techniques:

- pure functions and avoiding side effects,
- lambda functions,
- first-class and higher-order functions,
- transforming collections with `map()`,
- selecting data with `filter()`,
- combining values with `reduce()`.

> Functional programming helps express data transformations clearly and compactly.
