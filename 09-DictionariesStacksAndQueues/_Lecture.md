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

# Dictionaries, Sets, Stacks and Queues

**Course:** Fundamentals of Programming

---

# After this block, students should understand

- how to store data as **key-value pairs**,
- how to use **sets** to work with unique values,
- how **stacks** and **queues** organize data flow,
- how dictionaries are used in practical data processing,
- how JSON represents structured data in text files.

---

# Why More Data Structures?

Lists are useful when data is naturally ordered by position.

```python
scores = [18, 12, 20, 15]
print(scores[0])
```

But many problems are easier when data has names, labels, or special access rules.

```python
student = {'name': 'John', 'age': 22}
print(student['name'])
```

> A data structure should match the way we want to use the data.

---

# Dictionary

A **dictionary** stores data as **key-value pairs**.

```python
student = {
    'name': 'John',
    'age': 22,
    'major': 'Computer Science'
}
```

Each element has two parts:

- **key**: the identifier,
- **value**: the data assigned to the key.

---

# Dictionary as a Mapping

A dictionary answers the question:

> What value is assigned to this key?

```text
'name'  -> 'John'
'age'   -> 22
'major' -> 'Computer Science'
```

```python
print(student['name'])
print(student['age'])
```

The key works like a label attached to the value.

---

# List vs Dictionary

| Structure | Access by | Best for |
|---|---|---|
| List | position | ordered sequences |
| Dictionary | key | named data |

```python
student_list = ['John', 22, 'Computer Science']
student_dict = {'name': 'John', 'age': 22, 'major': 'Computer Science'}
```

> Dictionaries are usually easier to read when data fields have names.

---

# Basic Dictionary Operations

```python
student = {
    'name': 'John',
    'age': 22,
    'major': 'Computer Science'
}

print(student['name'])       # read value
student['grade'] = 'A'       # add value
student['age'] = 23          # modify value
del student['major']         # remove value
```

> A dictionary is **mutable**, so it can be changed after creation.

---

# Dictionary Values Can Have Different Types

```python
person = {
    'name': 'Marek',
    'surname': 'Banach',
    'age': 25,
    'hobby': ['swimming', 'excursions'],
    'married': True,
    'phone': {'mobile': '777888999'}
}
```

A dictionary value can be: a number, text, a Boolean value, a list, another dictionary.

---

# Iterating Over a Dictionary

```python
mobile = {
    'OS': 'Android',
    'brand': 'Samsung',
    'memory': 128,
    'dual_sim': True
}

for key, value in mobile.items():
    print(f'{key}: {value}')
```

`.items()` gives both the key and the value.

---

# Checking if a Key Exists

Before reading a value, we often check whether the key exists.

```python
person = {'name': 'Alice', 'age': 30}

if 'name' in person:
    print(person['name'])
else:
    print('No name found')
```

This helps avoid errors when working with incomplete data.

---

# Dictionaries in Real Problems

Dictionaries are useful when we count, summarize, or look up data.

```python
inventory = {
    'Laptop': 15,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60
}
```

Example tasks:

- print all products and quantities,
- calculate total stock,
- update a quantity,

---

# Counting With a Dictionary

A dictionary can store counters.

```python
paragraph = 'cat dog mouse cat rat cat mouse'
counts = {}

for word in paragraph.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
```

> The word is the key. The number of occurrences is the value.

---

# Array of Dictionaries

Sometimes one object is not enough. We need a collection of records.

```python
countries = [
    {'name': 'Poland', 'population': 38000000},
    {'name': 'Germany', 'population': 83200000},
    {'name': 'France', 'population': 67800000}
]
```

Each dictionary represents one record.

The list stores many records together.

---

# Processing Records

```python
for country in countries:
    print(country['name'], country['population'])
```

This pattern is common in programs that process:

- employees,
- products,
- cities,
- reservations,
- orders,
- survey results.

---

# Set

A **set** is an unordered collection of unique values.

```python
emails = [
    'john@example.com',
    'jane@example.com',
    'john@example.com'
]

unique_emails = set(emails)
print(unique_emails)
```

> A set automatically removes duplicates.

---

# Set Operations

| Operation | Meaning |
|---|---|
| `A & B` | intersection: elements in both sets |
| `A \| B` | union: elements from both sets |
| `A - B` | difference: elements in A but not in B |
| `A ^ B` | symmetric difference |
| `A.issubset(B)` | checks whether A is inside B |

> Sets are useful when membership and uniqueness matter more than order.

---

# Intersection: Finding Common Elements

```python
emails_received = {
    'john@example.com',
    'spam1@example.com',
    'spam2@example.com'
}

spam_list = {'spam1@example.com', 'spam2@example.com'}

spam_emails = emails_received & spam_list
print(spam_emails)
```

Intersection answers:

> Which elements appear in both sets?

---

# Union: Combining Without Duplicates

```python
contacts_a = {'john@example.com', 'alice@example.com'}
contacts_b = {'alice@example.com', 'sara@example.com'}

merged_contacts = contacts_a | contacts_b
print(merged_contacts)
```

> Union is useful when we merge data from different sources.

> Duplicates are removed automatically.

---

# Difference: Missing Elements

```python
all_students = {'Alice', 'John', 'Sara', 'Bob'}
attended_students = {'Alice', 'Bob'}

absent_students = all_students - attended_students
print(absent_students)
```

Difference answers:

> What is present here but not there?

---

# Subset: Required Permissions

```python
required_permissions = {'read', 'write', 'execute'}
user_permissions = {'read', 'write'}

has_permissions = required_permissions.issubset(user_permissions)
print(has_permissions)
```

A subset check answers:

> Does the user have everything that is required?

---

# Stack

A **stack** follows the **Last In, First Out** rule.

```text
push 2
push 3
push 7
pop  -> 7
pop  -> 3
```

The last element added is the first element removed.

> Think of a stack as a pile of plates.

---

# Stack Operations

| Operation | Meaning |
|---|---|
| push | add an element on top |
| pop | remove the top element |
| peek | check the top element |
| empty | check whether stack has no elements |

In Python, a list can be used as a simple stack.

```python
stack = []
stack.append(2)
stack.append(3)
value = stack.pop()
```

---

# Stack Example: Browser Back Button

A browser stores visited pages on a stack.

```text
visit home
visit products
visit contact
back -> products
back -> home
```

The most recently visited page is the first one returned to.

This is exactly the Last In, First Out rule.

---

# Stack Example: Checking Brackets

A stack helps check whether brackets are properly matched.

```python
expression = '[(2+3)*4+5]'
```

Algorithm idea:

1. Read characters one by one.
2. Push opening brackets onto the stack.
3. When closing bracket appears, pop from the stack.
4. Check whether the pair matches.

---

# Bracket Matching Pattern

```python
pairs = {')': '(', ']': '[', '}': '{'}
stack = []

for char in expression:
    if char in '([{':
        stack.append(char)
    elif char in ')]}':
        if not stack or stack.pop() != pairs[char]:
            print('Brackets are not correct')
```

> A stack remembers what still needs to be closed.

---

# Stack Example: Decimal to Binary

To convert a decimal number to binary:

1. Divide the number by 2.
2. Push the remainder onto the stack.
3. Continue until the number becomes 0.
4. Pop all remainders from the stack.

```text
18 / 2 = 9 remainder 0
9 / 2 = 4 remainder 1
4 / 2 = 2 remainder 0
2 / 2 = 1 remainder 0
1 / 2 = 0 remainder 1
```

Result: `10010`

---

# Queue

A **queue** follows the **First In, First Out** rule.

```text
enqueue A
enqueue B
enqueue C
dequeue -> A
dequeue -> B
```

The first element added is the first element removed.

> Think of a queue as people waiting in line.

---

# Queue Operations

| Operation | Meaning |
|---|---|
| enqueue | add an element to the end |
| dequeue | remove an element from the front |
| front | check the first element |
| empty | check whether queue has no elements |

In Python, queues can be created using the `queue` module.

```python
import queue

q = queue.Queue()
q.put('document.pdf')
file_name = q.get()
```

---

# Queue Example: Print Jobs

A printer should process files in the order in which they were added.

```text
1. Add file to print
2. Print next file
0. Quit
```

When a file is added, it goes to the end of the queue.

When a file is printed, it is taken from the front of the queue.

---

# Stack vs Queue

| Structure | Rule | Typical example |
|---|---|---|
| Stack | Last In, First Out | browser Back button |
| Queue | First In, First Out | printer queue |

```text
Stack: last added, first removed
Queue: first added, first removed
```

> Choosing the right structure makes the algorithm simpler.

---

# JSON

JSON stores structured data as text.

```json
{
  "name": "John",
  "age": 25,
  "student": true
}
```

> JSON is based on: key-value pairs, arrays, strings, numbers, Boolean values.

---

# JSON and Python Dictionaries

JSON data often maps naturally to Python dictionaries.

```python
import json

with open('computer.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for key, value in data.items():
    print(key, ':', value)
```

> `json.load()` reads JSON data from a file into Python data structures.

---

# Array of Dictionaries in JSON

A JSON file may contain a list of objects.

```json
[
  {"city": "Krakow", "population": 800000},
  {"city": "Warsaw", "population": 1800000}
]
```

In Python, this becomes a list of dictionaries.

```python
for city in data:
    print(city['city'])
```

---

# Writing JSON Files

```python
import json

product = {
    'name': 'Keyboard',
    'price': 99.99,
    'paid': True
}

with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)
```

> `json.dump()` writes Python data to a JSON file.

---

# Choosing a Data Structure

| Problem | Useful structure |
|---|---|
| Store student fields | dictionary |
| Remove duplicate emails | set |
| Check matching brackets | stack |
| Manage print jobs | queue |
| Save structured data | JSON |

> The same data can often be represented in many ways, but some representations make the solution much clearer.

---

# Common Beginner Mistakes

| Mistake | Example | How to think about it? |
|---|---|---|
| Missing key | `person['salary']` | check if key exists |
| Confusing list and dictionary access | `person[0]` | dictionaries use keys |
| Expecting set order | printing a set | sets are unordered |
| Popping empty stack | `stack.pop()` | check before removing |
| Wrong queue rule | newest first | queue means first first |

---

# Summary

This block introduced data structures for more complex programs:

- dictionaries store named data,
- sets store unique elements,
- stacks support Last In, First Out processing,
- queues support First In, First Out processing,
- JSON stores structured data in text files.

> Data structures are not only containers. They express how a program thinks about data.
