# 🐍 Python Modules & Packages

> **Goal:** Learn how to use Python's built-in modules, create your own modules, organize code into packages, and understand `__name__`, `__main__`, `dir()` and `__init__.py`.

---

# 📚 Lecture 1 — Python Modules

## 1. What is a Module?

A **module** is simply a Python file (`.py`) containing variables, functions, classes, or other code that can be reused in another Python program.

### Example

**calculator.py**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**main.py**

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
```

### Why use modules?

* ♻️ Code reusability
* 🧹 Keeps code organized
* 🔧 Easier maintenance
* 📦 Avoids writing the same code repeatedly

---

# 2. Types of Modules

Python modules can mainly be:

### 1. Built-in Modules

Already provided by Python.

Examples:

```python
import math
import random
import datetime
import time
import uuid
```

### 2. User-defined Modules

Modules created by the programmer.

```text
calculator.py
student.py
employee.py
```

### 3. Third-party Modules

Installed separately using `pip`.

Examples:

```python
import numpy
import pandas
```

---

# 3. Importing a Module

### Basic Import

```python
import math

print(math.sqrt(25))
```

### Import Specific Function

```python
from math import sqrt
  
print(sqrt(25))
```

### Import Multiple Functions

```python
from math import sqrt, factorial

print(sqrt(16))
print(factorial(5))
```

### Import Everything

```python
from math import *
```

⚠️ **Not recommended** because it can cause naming conflicts.

---

# 4. Renaming / Aliasing a Module

Use `as` to give a module another name.

```python
import math as m

print(m.sqrt(25))
```

This is commonly used with libraries:

```python
import numpy as np
import pandas as pd
```

---

# 5. Important Built-in Modules

## `math`

Used for mathematical operations.

```python
import math

print(math.sqrt(25))
print(math.pow(2, 3))
print(math.factorial(5))
print(math.pi)
```

### Common functions

| Function      | Purpose        |
| ------------- | -------------- |
| `sqrt()`      | Square root    |
| `pow()`       | Power          |
| `factorial()` | Factorial      |
| `ceil()`      | Round upward   |
| `floor()`     | Round downward |
| `pi`          | Value of π     |

---

## `random`

Used to generate random values.

```python
import random

print(random.randint(1, 10))
print(random.random())
```

### Common functions

```python
random.randint(1, 100)
random.choice([10, 20, 30])
random.random()
```

### Example

```python
names = ["Amit", "Rahul", "Priya"]

print(random.choice(names))
```

---

## `datetime`

Used to work with dates and times.

```python
from datetime import datetime

now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)
```

### Create a specific date

```python
from datetime import datetime

date = datetime(2026, 8, 21)

print(date)
```

---

## `time`

Used for working with time-related operations.

```python
import time

print("Hello")

time.sleep(2)

print("World")
```

`time.sleep()` pauses program execution.

---

# 🧪 Lecture 1 Lab Work

### Task 1

Create a module named `calculator.py` containing:

* `add()`
* `subtract()`
* `multiply()`
* `divide()`

Import it into `main.py`.

### Task 2

Create a program that generates a random number between **1 and 100**.

### Task 3

Display:

* Current date
* Current time
* Current year
* Current month
* Current day

### Task 4

Create a countdown using `time.sleep()`.  

---

# 💪 Self Exercises — Lecture 1

1. What is a module?
2. Difference between built-in and user-defined modules.
3. Difference between `import math` and `from math import sqrt`.
4. What does `as` do?
5. Generate a random number between 1 and 50.
6. Select a random student from a list.
7. Find factorial of 6 using `math`.
8. Display today's date.
9. Pause a program for 5 seconds.
10. Create and import your own module.

---

# 📚 Lecture 2 — Packages & Advanced Modules

# 6. `uuid` Module

The `uuid` module generates **universally unique identifiers**.

```python
import uuid

id = uuid.uuid4()

print(id)
```

Example output:

```text
550e8400-e29b-41d4-a716-446655440000
```

Useful when creating:

* User IDs
* Order IDs
* File IDs
* Database identifiers

---

# 7. Higher-Order Functions

A **higher-order function** is a function that:

* accepts another function as an argument, or
* returns a function.

Python provides useful built-in higher-order functions:

```text
sorted()
map()
filter()
reduce()
```

---

## `sorted()`

Sorts an iterable and returns a **new list**.

```python
numbers = [5, 2, 8, 1, 3]

result = sorted(numbers)

print(result)
```

Output:

```text
[1, 2, 3, 5, 8]
```

### Descending order

```python
sorted(numbers, reverse=True)
```

---

## `map()`

Applies a function to every element.

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8]
```

### Remember

```text
map → transform every element
```

---

## `filter()`

Filters elements based on a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6]
```

### Remember

```text
filter → select required elements
```

---

## `reduce()`

`reduce()` repeatedly combines elements into a single result.

Import it from `functools`.

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

Output:

```text
10
```

### Remember

```text
map    → transform
filter → select
reduce → combine
sorted → arrange
```

---

# 8. What is a Package?

A **package** is a directory containing multiple Python modules.

Example:

```text
project/
│
├── main.py
│
└── calculator/
    ├── __init__.py
    ├── basic.py
    └── advanced.py
```

Here:

```text
calculator → Package
basic.py   → Module
advanced.py → Module
```

---

# 9. Creating a Package

### Step 1 — Create folder

```text
calculator
```

### Step 2 — Create modules

```text
calculator/
│
├── __init__.py
├── basic.py
└── advanced.py
```

### `basic.py`

```python
def add(a, b):
    return a + b
```

### `main.py`

```python
from calculator.basic import add

print(add(10, 20))
```

---

# 10. What is `__init__.py`?

`__init__.py` is a special Python file used inside a package.

Example:

```text
calculator/
│
├── __init__.py
├── basic.py
└── advanced.py
```

It can be used to:

* Mark/define package structure
* Run package initialization code
* Expose selected functions/classes

For beginners, remember:

> **`__init__.py` belongs to a package and helps Python treat/initialize the directory as a package.**

Modern Python can also support **namespace packages without `__init__.py`**, but you should still teach students the conventional package structure using it.

---

# 11. `__name__` and `__main__`

Every Python module has a special variable:

```python
__name__
```

When a file is executed directly:

```python
python file.py
```

Python sets:

```python
__name__ = "__main__"
```

When the same file is imported:

```python
import file
```

then:

```python
__name__ = "file"
```

---

## Why use `if __name__ == "__main__"`?

Example:

**calculator.py**

```python
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(10, 20))
```

If we run:

```text
calculator.py
```

the test code executes.

But if we import:

```python
import calculator
```

the test code does **not** execute.

### Best Practice

Use:

```python
if __name__ == "__main__":
```

for code that should execute **only when the file is run directly**.

---

# 12. `dir()`

`dir()` shows the available attributes and methods of an object/module.

```python
import math

print(dir(math))
```

You can also use:

```python
numbers = [1, 2, 3]

print(dir(numbers))
```

Useful for **exploring an unfamiliar module or object**.

---

# 🧪 Lecture 2 Lab Work

### Task 1 — UUID

Generate a unique ID for every student:

```text
Student Name → UUID
```

---

### Task 2 — `map()`

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

Create a new list containing their squares.

Expected:

```text
[1, 4, 9, 16, 25]
```

---

### Task 3 — `filter()`

From:

```python
numbers = [10, 15, 20, 25, 30, 35]
```

extract only even numbers.

---

### Task 4 — `reduce()`

Calculate the product:

```text
1 × 2 × 3 × 4 × 5
```

---

### Task 5 — Package

Create:

```text
student/
│
├── __init__.py
├── details.py
└── marks.py
```

Create functions in both modules and import them into `main.py`.

---

### Task 6 — `__name__`

Create a module containing:

```python
def message():
    print("Hello Python")


if __name__ == "__main__":
    message()
```

Test it both by:

1. Running the file directly
2. Importing it into another file

---

# 💪 Self Exercises — Lecture 2

1. What is a package?
2. Module vs package.
3. What is `__init__.py`?
4. What is `__name__`?
5. What is the purpose of `if __name__ == "__main__"`?
6. What does `dir()` return?
7. Difference between `map()` and `filter()`.
8. What does `reduce()` do?
9. Generate 5 UUIDs.
10. Create a package containing 3 modules.

---

# 🎯 Quick Revision

| Concept       | Remember                              |
| ------------- | ------------------------------------- |
| Module        | `.py` file containing reusable code   |
| Package       | Collection of modules                 |
| `import`      | Import module                         |
| `as`          | Rename/alias                          |
| `math`        | Mathematical operations               |
| `random`      | Random values                         |
| `datetime`    | Date & time                           |
| `time`        | Time-related operations               |
| `uuid`        | Unique identifiers                    |
| `sorted()`    | Sort data                             |
| `map()`       | Transform data                        |
| `filter()`    | Select data                           |
| `reduce()`    | Combine data                          |
| `__init__.py` | Package initialization/structure      |
| `__name__`    | Identifies how a module is being used |
| `__main__`    | Indicates direct execution            |
| `dir()`       | Explore available attributes          |

---

# 🏆 Mini Project — 2 Days

## **Student Management Package**

Create:

```text
student_management/
│
├── main.py
│
└── student/
    ├── __init__.py
    ├── details.py
    ├── marks.py
    └── operations.py
```

### Requirements

Your project should:

* Add student details
* Generate a UUID for each student
* Store marks
* Calculate total/average
* Filter students based on marks
* Sort students by marks
* Use `map()`, `filter()`, `reduce()` and `sorted()`
* Use proper module imports
* Use `__name__ == "__main__"`

### 🎯 Learning Outcome

By the end of these **2 lectures**, students should be able to:

> **Create → import → organize → reuse Python code using modules and packages.**