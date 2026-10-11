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

# Classes and Objects

**Course:** Fundamentals of Programming

---

# After this block, students should understand

- what **object-oriented programming** is,
- the difference between a **class** and an **object**,
- how attributes describe object state,
- how methods describe object behavior,
- how constructors initialize new objects,
- how objects can cooperate with modules and other objects.

---

# Why Do We Need Classes?

Until now, programs were built mainly from:

- variables,
- functions,
- lists and dictionaries,
- files and control structures.

These tools are enough for many tasks, but larger programs need a better way to organize related data and operations.

> Classes let us keep data and behavior together.

---

# Object-Oriented Programming

Object-oriented programming is a way of designing programs around **objects**.

An object represents something that has:

- **state**: what the object knows,
- **behavior**: what the object can do.

Examples:

- a car,
- a bank account,
- a student,
- a TV set,
- an e-book.

---

# Object as a Model of Reality

A program does not contain a real car or a real bank account.

It contains a simplified **model** of it.

```text
Real-world thing -> selected features -> object in a program
```

Example:

```text
Car -> brand, model, year -> accelerate(), display_info()
```

> A useful object includes only the information and actions needed for the task.

---

# Class and Object

A **class** is a pattern or blueprint.

An **object** is a concrete instance created from that class.

```text
Class:  Car
Object: Toyota Corolla 2021
Object: Ford Focus 2018
Object: Fiat 500 2020
```

> One class can be used to create many different objects.

---

# Class Definition

In Python, a class is defined with the `class` keyword.

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, year: {self.year}")
```

This class describes what every `Car` object should contain and what it can do.

---

# Attributes

Attributes are variables stored inside an object.

They describe the object's state.

```python
self.brand = brand
self.model = model
self.year = year
```

For a car object, attributes may describe:

- brand,
- model,
- production year,
- current speed,
- fuel level.

---

# Methods

Methods are functions defined inside a class.

They describe object behavior.

```python
def display_info(self):
    print(f"Car: {self.brand} {self.model}, year: {self.year}")
```

Methods usually:

- read object attributes,
- modify object attributes,
- calculate results based on object data,
- print or return information about the object.

---

# Constructor

The constructor initializes a new object.

In Python, the constructor is the special method `__init__()`.

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
```

When a new object is created, Python calls `__init__()` automatically.

---

# The Role of `self`

`self` means: **this particular object**.

```python
self.brand = brand
```

This line means:

> store the value from the parameter `brand` as the `brand` attribute of this object.

Each object has its own values.

```python
car1.brand
car2.brand
```

---

# Creating an Object

An object is created by calling the class name like a function.

```python
my_car = Car("Toyota", "Corolla", 2021)
```

Then we can call its methods.

```python
my_car.display_info()
```

The object name works like a variable that stores a reference to the created object.

---

# Many Objects from One Class

```python
car1 = Car("Toyota", "Corolla", 2021)
car2 = Car("Ford", "Focus", 2018)
car3 = Car("Fiat", "500", 2020)

car1.display_info()
car2.display_info()
car3.display_info()
```

All objects use the same class definition.

Each object stores its own attribute values.

---

# Example: Square Class

A square has one important attribute: side length.

It can calculate its area and perimeter.

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side
```

---

# Using the Square Class

```python
square1 = Square(4)
square2 = Square(6)

print("Square with side 4")
print("Area:", square1.area())
print("Perimeter:", square1.perimeter())

print("Square with side 6")
print("Area:", square2.area())
print("Perimeter:", square2.perimeter())
```

> The object knows its own side length, so methods do not need it as an extra argument.

---

# Object State Can Change

Objects are useful because their state can change during program execution.

```python
class TV:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
```

The same object can represent the TV before and after switching it on.

---

# TV Object: State and Behavior

State:

- is the TV on?
- what channel is selected?
- what volume level is set?
- what channels are available?

Behavior:

- turn on,
- turn off,
- change channel,
- increase volume,
- decrease volume,
- show status.

---

# Example: TV Status

```python
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1

    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")
```

The method prints different information depending on the current object state.

---

# Adding Controlled Behavior

A method can protect the object from incorrect values.

```python
class TV:
    def __init__(self):
        self.channel_no = 1

    def set_channel(self, new_channel_no):
        if new_channel_no >= 1:
            self.channel_no = new_channel_no
```

Instead of changing attributes directly, we can define rules inside methods.

---

# Encapsulation: Practical Meaning

Encapsulation means keeping related data and operations in one place.

```text
TV object
- data: is_on, channel_no, volume
- methods: turn_on(), set_channel(), show_status()
```

This makes the program easier to understand because the logic connected with the TV is inside the TV class.

---

# String Representation of an Object

When we print an object, we usually want readable information.

Python uses the special method `__str__()` for this purpose.

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
```

---

# Printing an Object

```python
my_car = Car("Toyota", "Corolla", 2021)
print(my_car)
```

Output:

```text
2021 Toyota Corolla
```

Without `__str__()`, the output would be technical and not useful for the user.

---

# Example: Song Class

```python
class Song:
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return (
            f"Performer: {self.artist}\n"
            f"Title:     {self.title}\n"
            f"Album:     {self.album}\n"
            f"Year:      {self.year}"
        )
```

---

# Using the Song Class

```python
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

print(song1)
print()
print(song2)
```

The object decides how it should be displayed as text.

---

# Classes and Modules

A class definition can be placed in a separate file.

```text
tv.py       -> class TV
main.py     -> program that creates and uses a TV object
```

Example:

```python
from tv import TV

television = TV()
television.turn_on()
television.show_status()
```

This keeps the program organized.

---

# A Larger Object: E-book

An e-book can be modeled as an object.

Possible attributes:

- title,
- author,
- number of pages,
- current page,
- open or closed status.

Possible methods:

- open book,
- close book,
- go to next page,
- go to previous page,
- show status.

---

# Designing a Class

When designing a class, ask four questions:

1. What real or abstract thing do I model?
2. What data describes it?
3. What actions can it perform?
4. What rules should protect its state?

Example:

```text
Bank account
Data: account number, balance
Actions: deposit, withdraw, show balance
Rules: withdrawal cannot exceed balance
```

---

# Example: Bank Account

```python
class BankAccount:
    def __init__(self, number):
        self.number = number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds on the account")
```

---

# Object Methods Can Enforce Rules

The `withdraw()` method protects the account balance.

```python
account = BankAccount("12 3456 5555 9090 1111 0000 7722")
account.deposit(25.30)
account.withdraw(31.70)
account.withdraw(14)
```

Important idea:

> The user of the object asks it to perform an operation. The object decides how to do it correctly.

---

# Objects Can Store Collections

An object can contain a list or a dictionary.

```python
class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)
```

This is useful when an object manages many values.

Examples:

- contact list,
- list of posts,
- set of numbers,
- list of available TV channels.

---

# Example: Contact and Contact List

One class can describe a single contact.

Another class can manage many contacts.

```text
Contact
- name
- email
- telephone

ContactList
- contacts
- add_contact()
- display_contacts()
```

This mirrors the real structure of a smartphone address book.

---

# Object Cooperation

Objects can contain other objects.

```python
class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
```

Here, `ContactList` stores many `Contact` objects.

> Larger programs are often built from many cooperating objects.

---

# Common Beginner Mistakes

| Mistake | Example | How to think about it? |
|---|---|---|
| Missing `self` | `brand = brand` | object attributes need `self.` |
| Calling method on class | `Car.display_info()` | usually call it on an object |
| Forgetting parentheses | `car.display_info` | method call needs `()` |
| Changing state directly | `tv.channel_no = -5` | use methods with validation |
| Too much in one class | one class does everything | split responsibility |

---

# Procedural vs Object-Oriented Thinking

Procedural style asks:

> What steps should the program execute?

Object-oriented style asks:

> What objects take part in the problem, and what should each object know and do?

Both styles are useful.

Classes are especially helpful when a program manages many related pieces of data and behavior.

---

# Summary

This block introduced object-oriented programming foundations:

- classes as blueprints for objects,
- objects as instances with state and behavior,
- attributes, methods, constructors, and `self`,
- string representation with `__str__()`,
- modules containing class definitions,
- objects that model real-world entities.

> The next step is to practice designing classes from problem descriptions.
