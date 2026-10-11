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

# File Handling

**Course:** Fundamentals of Programming

---

# After this block, students should understand

- what files are and why programs use them,
- how to read text data from files,
- how to write and append data to files,
- how to process line-based and tabular data,
- how regular expressions help find patterns in text,
- how to handle file-related errors safely.

---

# Why Do Programs Use Files?

A file lets a program store data permanently.

Without files, data exists only while the program is running.

```text
program runs → data is created → program ends → data disappears
```

With files:

```text
program runs → data is saved → data can be used again later
```

> File handling connects a program with real data stored on disk.

---

# What Is a File?

A file is a named place on disk where data is stored.

Common file types:

| File type | Example | Typical content |
|---|---|---|
| Text file | `countries.txt` | readable text |
| CSV file | `employees.csv` | table-like data |
| Python file | `program.py` | source code |
| Binary file | `image.png` | data not directly readable as text |

---

# Text Files

A text file stores characters.

Example: `countries.txt`

```text
Poland, Warsaw, 38265000
Germany, Berlin, 83240000
France, Paris, 67850000
Japan, Tokyo, 125800000
Canada, Ottawa, 38250000
```

Each line is a separate piece of information.

---

# The Basic File Workflow

Most file programs follow the same idea:

**Open file** → **Read or write data** → **Close file**

In Python, the recommended style is to use `with`:

```python
with open('example.txt', 'r') as file:
    content = file.read()
```

> The file is closed automatically when the `with` block ends.

---

# File Opening Modes

The second argument of `open()` tells Python what we want to do.

| Mode | Meaning | Typical use |
|---|---|---|
| `'r'` | read | read an existing file |
| `'w'` | write | create or overwrite a file |
| `'a'` | append | add data at the end |

```python
open('data.txt', 'r')
open('data.txt', 'w')
open('data.txt', 'a')
```

---

# Reading the Whole File

`read()` reads the entire file content as one string.

```python
with open('countries.txt', 'r') as file:
    content = file.read()

print(content)
```

Use this when:

- the file is small,
- you need the whole text at once,
- you want to search in the complete document.

---

# Reading Line by Line

A file can also be processed one line at a time.

```python
with open('countries.txt', 'r') as file:
    for line in file:
        print(line, end='')
```

This is useful when:

- the file contains records,
- each line has separate meaning,
- the file can be large.

---

# Why `end=''` Is Sometimes Needed

Lines read from a file usually already contain an end-of-line character.

```python
print(line)
```

prints:

```text
Poland, Warsaw, 38265000

Germany, Berlin, 83240000
```

To avoid extra empty lines:

```python
print(line, end='')
```

---

# Reading Lines into a List

`splitlines()` divides a string into separate lines.

```python
with open('countries.txt', 'r') as file:
    content = file.read()

lines = content.splitlines()

for line in lines:
    print(line)
```

> A list of lines can be sorted, counted, filtered, or analyzed.

---

# Numbering Lines

A counter variable can be used to number printed records.

```python
with open('countries.txt', 'r') as file:
    counter = 1
    for line in file:
        print(f'{counter}. {line}', end='')
        counter += 1
```

This is a typical pattern:

```text
initialize counter → process item → increase counter
```

---

# Sorting File Content

When file lines are stored in a list, they can be sorted.

```python
with open('countries.txt', 'r') as file:
    content = file.read()

countries = content.splitlines()
sorted_countries = sorted(countries)

for country in sorted_countries:
    print(country)
```

> Sorting changes presentation, not necessarily the original file.

---

# Files and the Current Folder

When we write:

```python
open('countries.txt')
```

Python looks for the file in the current working folder.

A common beginner problem:

```text
FileNotFoundError: No such file or directory
```

Possible reason:

> The program runs from a different folder than the file location.

---

# Processing Numeric Data from Files

File content is text. Numbers must be converted before calculations.

Example: `car_park.txt`

```text
23
18
31
25
29
```

```python
total = 0

with open('car_park.txt', 'r') as file:
    for line in file:
        total += int(line)

print('Total cars parked:', total)
```

---

# Counting Words in a File

A text can be split into words.

```python
word_count = 0

with open('pets.txt', 'r') as file:
    for line in file:
        words = line.split()
        word_count += len(words)

print('Number of words:', word_count)
```

Important idea:

> A line is a string; `split()` turns it into a list of words.

---

# Filtering Lines

Sometimes we need only selected lines.

Example: print employees whose job title is `Software Engineer`.

```python
job_title = 'Software Engineer'

with open('it_company.csv', 'r') as file:
    counter = 1
    for line in file:
        if job_title in line:
            print(counter, line, end='')
            counter += 1
```

> Filtering means checking a condition for every record.

---

# Writing to a File

To save data, open the file in write mode.

```python
movie_title = 'Inception'
director = 'Christopher Nolan'
lead_actor = 'Leonardo DiCaprio'

with open('movie_details.txt', 'w') as file:
    file.write(f'Movie Title: {movie_title}\n')
    file.write(f'Director: {director}\n')
    file.write(f'Lead Actor: {lead_actor}\n')
```

> Mode `'w'` creates a new file or overwrites an existing one.

---

# The Newline Character

`write()` does not automatically move to the next line.

```python
file.write('First line')
file.write('Second line')
```

Result:

```text
First lineSecond line
```

Correct version:

```python
file.write('First line\n')
file.write('Second line\n')
```

---

# Writing a List to a File

```python
seven_wonders = [
    'Great Wall of China',
    'Petra',
    'Christ the Redeemer',
    'Machu Picchu',
    'Chichen Itza',
    'Roman Colosseum',
    'Taj Mahal'
]

with open('seven_wonders.txt', 'w') as file:
    for item in sorted(seven_wonders):
        file.write(item + '\n')
```

---

# Copying a Text File

Copying a file can be expressed as:

**read original** → **write copy**

```python
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

with open(original_file, 'r') as file:
    content = file.read()

with open(target_file, 'w') as file:
    file.write(content)
```

---

# Saving Selected Data

Read from one file and write selected lines to another file.

```python
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'
job_title = 'Software Engineer'

with open(employees_file, 'r') as input_file:
    with open(position_file, 'w') as output_file:
        for line in input_file:
            if job_title in line:
                output_file.write(line)
```

---

# Appending to a File

Append mode adds data at the end of a file.

```python
def add_product(file_name, product_name):
    with open(file_name, 'a') as file:
        file.write(product_name + '\n')
```

Example use:

```python
shopping_list = 'shopping_list.txt'
product = input('Enter product name: ')
add_product(shopping_list, product)
```

> Mode `'a'` keeps existing file content.

---

# Interactive File Creation

A loop can collect many values and save them one by one.

```python
file_name = 'shopping_list.txt'
product = ''

while product != '0':
    product = input('Enter product name (0 stops): ')
    if product != '0':
        with open(file_name, 'a') as file:
            file.write(product + '\n')
```

> This combines: input, loop, condition, file writing.

---

# CSV Files

CSV means comma-separated values.

Example:

```text
John,Smith,john.smith@example.com,Software Engineer
Anna,Brown,anna.brown@example.com,Graphic Designer
```

A CSV file is still a text file, but its structure represents a table.

```text
row → record
comma → field separator
```

---

# Simple CSV Processing

For simple tasks, a line can be split into fields.

```python
with open('it_company.csv', 'r') as file:
    for line in file:
        fields = line.strip().split(',')
        first_name = fields[0]
        last_name = fields[1]
        email = fields[2]
        job_title = fields[3]
```

> This works for simple CSV files without commas inside fields.

---

# CSV Module

For more reliable CSV processing, Python provides the `csv` module.

```python
import csv

with open('it_company.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        first_name = row[0]
        last_name = row[1]
        email = row[2]
        job_title = row[3]
```

> Use a module when the data format has its own rules.

---

# Regular Expressions

A regular expression describes a text pattern.

Typical uses:

- find dates,
- find phone numbers,
- validate usernames,
- extract amounts of money,
- identify structured fragments in text.

```text
text → pattern matching → selected fragments
```

---

# The `re` Module

Python supports regular expressions through the `re` module.

```python
import re

text = 'Phone: 555-123-4567'
pattern = r'\d{3}-\d{3}-\d{4}'

matches = re.findall(pattern, text)
print(matches)
```

Result:

```text
['555-123-4567']
```

---

# Common Regex Building Blocks

| Pattern | Meaning | Example match |
|---|---|---|
| `\d` | digit | `7` |
| `\w` | word character | `A`, `x`, `5` |
| `.` | any character | `a`, `7`, `?` |
| `+` | one or more | `aaa` |
| `*` | zero or more | empty text, `aaa` |
| `{3}` | exactly three times | `555` |

---

# Why Encoding Matters

Some files contain special characters, for example:

```text
€, ą, ć, ł, ñ
```

To read such files correctly, specify encoding.

```python
with open('report.txt', 'r', encoding='utf-8') as file:
    content = file.read()
```

> UTF-8 is a common encoding that supports many international characters.

---

# Handling File Errors

File operations can fail.

Common reasons:

- file does not exist,
- wrong folder,
- no permission,
- unexpected data format.

Without error handling, the program may stop.

```text
try risky operation → handle error → continue program
```

---

# Try-Except

`try-except` lets a program react to errors.

```python
try:
    with open('missing_file.txt', 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print('The file does not exist.')
```

> Error handling does not remove the error, but it prevents uncontrolled program termination.

---

# Counting Lines, Words, and Characters

```python
file_name = input('File name: ')

try:
    with open(file_name, 'r') as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print('Number of lines:', len(lines))
    print('Number of words:', len(words))
    print('Number of characters:', characters)
except FileNotFoundError:
    print('File not found.')
```

---

# A General Pattern for File Analysis

Most file-analysis programs use a similar structure:

```text
1. Open the file
2. Read data
3. Split data into useful parts
4. Convert types if needed
5. Filter, count, sum, or search
6. Print or save the result
```

Example tasks:
- find employees by job title,
- calculate money spent,
- extract email fields.

---

# Good Practices

- Use `with open(...)` instead of manually closing files.
- Use meaningful file names and variable names.
- Convert text to numbers before calculations.
- Specify `encoding='utf-8'` when special characters may appear.
- Handle missing files with `try-except`.
- Use modules, such as `csv` or `re`, when they simplify the task.

---

# Common Beginner Mistakes

| Mistake | Example | How to think about it? |
|---|---|---|
| Wrong folder | `FileNotFoundError` | check current working directory |
| Forgetting newline | `write('text')` | add `\n` when needed |
| Missing conversion | `total += line` | file data is text |
| Overwriting file | mode `'w'` | use `'a'` to append |
| Too broad regex | `.*` | make the pattern specific |

---

# Summary

This block introduced file handling and text processing:

- reading text files,
- processing lines and lists,
- writing and appending data,
- filtering and copying files,
- working with CSV-like data,
- using regular expressions,
- handling file-related errors safely.

> The next step is to combine files with larger programs and structured data processing.
