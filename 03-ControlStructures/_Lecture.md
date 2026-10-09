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

# Control Structures

**Course:** Fundamentals of Programming

---

# After this block, students should understand

- how programs make decisions using **if**, **else**, and **elif**,
- how to build conditions with comparison and logical operators,
- how to repeat instructions using **for** and **while** loops,
- how to use loops with strings, ranges, counters, and accumulators,
- how to design simple algorithms with decisions and repetition.

---

# Why Control Structures Matter

A program is not only a sequence of instructions.

It often needs to:

- choose between alternative actions,
- repeat an operation many times,
- stop when a condition is satisfied,
- react differently to different input data.

> Control structures decide the order in which instructions are executed.

---

# Three Basic Forms of Control

Most beginner programs combine three ideas.

| Control form | Meaning | Python example |
|---|---|---|
| Sequence | run instructions one after another | normal program lines |
| Selection | choose what to do | `if`, `else`, `elif` |
| Iteration | repeat instructions | `for`, `while` |

> Control structures turn simple calculations into real algorithms.

---

# Decision Statement

A decision statement lets the program execute code only when a condition is true.

```python
if condition:
    # code executed when condition is True
```

Example:

```python
speed_limit = 140
car_speed = int(input('Enter car speed: '))

if car_speed > speed_limit:
    print('Warning: speed limit exceeded!')
```

---

# A Condition Is a Question

A condition is an expression that gives a Boolean value.

```python
car_speed > speed_limit
account_balance >= total_payment
tasks_ok >= total_tasks / 2
number % 2 == 0
```

The answer is always:

```python
True
False
```

> The program uses this answer to decide what to do next.

---

# Indentation Defines the Block

In Python, indentation is part of the syntax.

```python
if car_speed > speed_limit:
    print('Too fast')
    print('Slow down')

print('End of speed check')
```

Only the indented lines belong to the `if` block.

> Wrong indentation changes the meaning of the program or causes an error.

---

# If and Else

`else` defines what should happen when the condition is false.

```python
account_balance = 500
total_payment = int(input('Payment amount: '))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')
```

> Use `else` when there are two possible paths.

---

# Boolean Flags

Sometimes we store the result of a condition in a variable.

```python
total_tasks = 20
tasks_ok = int(input('Correct tasks: '))

test_passed = tasks_ok >= total_tasks * 0.5

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
```

> A Boolean variable is often called a flag.

---

# Even or Odd

The remainder operator `%` is useful in conditions.

```python
number = int(input('Enter number: '))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
```

> A number is even when division by 2 leaves remainder 0.

---

# Multiple Conditions with Elif

`elif` means “else if”. It checks another condition only when previous conditions were false.

```python
if condition1:
    # first case
elif condition2:
    # second case
elif condition3:
    # third case
else:
    # all other cases
```

> Use `elif` when one value can belong to several categories.

---

# Example: Clothing Size

```python
size = input('Enter size symbol: ')

if size == 'S':
    print('Small size')
elif size == 'M':
    print('Medium size')
elif size == 'L':
    print('Large size')
elif size == 'XL':
    print('Extra large size')
else:
    print('Incorrect symbol')
```

> Only one branch is executed.

---

# Order of Elif Conditions Matters

Conditions are tested from top to bottom.

```python
temperature = 33

if temperature > 35:
    print('Extremely hot')
elif temperature > 30:
    print('Hot')
elif temperature >= 15:
    print('Warm')
elif temperature >= 0:
    print('Cold')
else:
    print('Warning, frost')
```

> Put the most specific or highest-priority conditions first.

---

# Logical Operators

Logical operators combine conditions.

| Operator | Meaning | Example |
|---|---|---|
| `and` | all conditions must be true | `age >= 18 and age <= 64` |
| `or` | at least one condition must be true | `age < 18 or age >= 65` |
| `not` | reverses the logical value | `not password_ok` |

---

# Example: Login and Password

Both login and password must be correct.

```python
login = 'joe'
password = 'abcd'

entered_login = input('Login: ')
entered_password = input('Password: ')

if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    print('Incorrect login or password')
```

---

# Example: Discount Eligibility

A discount is available to children under 18 or people 65 or older.

```python
age = int(input('Enter your age: '))

if age < 18 or age >= 65:
    print('Discount available')
else:
    print('No discount')
```

> The word “or” in the task usually becomes the operator `or` in code.

---

# Ranges and Boundaries

Many conditions check whether a value is inside an allowed range.

```python
speed = int(input('Enter vehicle speed: '))

speed_valid = speed >= 40 and speed <= 140

if speed_valid:
    print('Speed is valid')
else:
    print('Warning: invalid speed')
```

> Always check boundary values such as 40, 140, 39, and 141.

---

# Nested Decisions

A decision can contain another decision.

```python
month = int(input('Month: '))
day = int(input('Day: '))

day_ok = False

if month == 2:
    if day >= 1 and day <= 28:
        day_ok = True
```

> Nested decisions are useful, but too much nesting can make code hard to read.

---

# Iteration

Iteration means repeating a block of code.

Programs use loops when they need to:

- process many values,
- repeat a calculation,
- search for something,
- ask again until input is correct,
- simulate repeated events.

> Python has two basic loop types: `for` and `while`.

---

# For Loop

A `for` loop iterates over a sequence.

```python
for item in sequence:
    # repeated code block
```

Example:

```python
city = 'Krakow'

for char in city:
    print(char)
```

> The loop variable receives one element of the sequence at a time.

---

# Looping Over a Range of Numbers

`range()` generates a sequence of numbers.

```python
for i in range(5):
    print(i)
```

Result:

```text
0
1
2
3
4
```

Important: `range(5)` starts from 0 and stops before 5.

---

# Range with Start and Stop

```python
for i in range(1, 6):
    print(i)
```

Result:

```text
1
2
3
4
5
```

The second argument is not included.

> `range(1, 6)` means values from 1 up to 5.

---

# Repeating an Instruction

```python
for i in range(6):
    print('Practice makes perfect!')
```

This prints the same sentence six times.

The variable `i` is useful when we need the number of the current repetition.

```python
for i in range(1, 7):
    print(f'Repetition {i}')
```

---

# Building Text in a Loop

A loop can gradually build a result.

```python
university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + ' '

print(university_expanded)
```

> This pattern is common in text processing.

---

# Accumulator Pattern

An accumulator stores a value that grows step by step.

```python
total = 0

for i in range(1, 6):
    total = total + i

print(f'Sum is {total}')
```

Shorter form:

```python
total += i
```

---

# Combining Loop and Decision

A loop can contain an `if` statement.

```python
total = 0

for i in range(1, 11):
    if i % 2 == 0:
        total += i

print(total)
```

This calculates the sum of even numbers from 1 to 10.

---

# Continue

`continue` skips the rest of the current loop iteration.

```python
total = 0

for i in range(1, 11):
    if i % 2 != 0:
        continue
    total += i

print(total)
```

> Use `continue` when some values should be ignored.

---

# While Loop

A `while` loop repeats code as long as a condition is true.

```python
while condition:
    # repeated code block
```

Example:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

> A `while` loop is useful when we do not know the number of repetitions in advance.

---

# Asking Until Input Is Correct

```python
name = ''

while name == '':
    name = input('Enter your name: ')

print(f'Hello {name}')
```

The loop continues while the user gives an empty answer.

> This is a typical validation pattern.

---

# Break

`break` immediately exits the loop.

```python
total_sum = 0

while True:
    number = int(input('Enter number, 0 to stop: '))

    if number == 0:
        break

    total_sum += number

print(total_sum)
```

> `while True` creates an intentional infinite loop controlled by `break`.

---

# For or While?

| Situation | Better choice |
|---|---|
| Repeat exactly 10 times | `for` |
| Process every character in text | `for` |
| Process numbers from 1 to N | `for` |
| Repeat until user enters correct input | `while` |
| Repeat until a random event happens | `while` |
| Menu that runs until Exit is selected | `while` |

---

# Nested Loops

A loop can contain another loop.

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row, col)
```

Nested loops are useful for:

- tables,
- grids,
- patterns,
- repeated operations inside repeated operations.

---

# Designing Programs with Control Structures

A good beginner algorithm often follows this pattern:

```text
1. Read input data
2. Convert input to proper types
3. Check conditions
4. Repeat calculations if needed
5. Store intermediate results
6. Print clear output
```

> First describe the algorithm, then write the code.

---

# Common Beginner Mistakes

| Mistake | Example | How to think about it? |
|---|---|---|
| Missing colon | `if x > 0` | control statements end with `:` |
| Wrong indentation | code outside the block | indentation defines meaning |
| Assignment instead of comparison | `x = 5` | use `==` in conditions |
| Infinite loop | condition never changes | update the loop variable |
| Wrong range end | `range(1, 10)` | stop value is excluded |

---

# Summary

This block introduced control structures:

- `if`, `else`, and `elif` for decisions,
- comparison and logical operators for conditions,
- `for` loops for sequence-based repetition,
- `while` loops for condition-based repetition,
- `break` and `continue` for loop control,
- nested loops and practical algorithm design.
