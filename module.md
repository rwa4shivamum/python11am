# 🐍 Python Modules & Packages

> **Topics Covered**
>
> * Creating & Importing Modules
> * Renaming Modules using `as`
> * `__name__` and `__main__`
> * Creating & Using Packages
> * `dir()`
> * Practice Exercises

---

# 1. What is a Module?

A **module** is simply a Python file (`.py`) that contains reusable code such as:

* Variables
* Functions
* Classes
* Statements

### Example

Suppose we create a file:

```text
calculator.py
```

Inside it:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Here, `calculator.py` is a **module**.
//DRY( don't repeat yourself ) Principle 
We can use these functions in another Python file instead of writing them again.

---

# 2. Why Do We Use Modules?

Imagine writing one huge Python file:

```text
project.py
```

containing:

```text
1000+ lines
suggestion write only 200 lines in single file
```

It becomes difficult to:

* Maintain
* Debug
* Reuse code
* Understand the project

Instead, we can divide our code:

```text
project/
│
├── calculator.py
├── student.py
├── employee.py
└── main.py
```

This makes the project **organized and reusable**.

### Main advantages

| Advantage       | Meaning                                            |
| --------------- | -------------------------------------------------- |
| Reusability     | Use the same code multiple times                   |
| Organization    | Divide large programs into smaller files           |
| Maintainability | Easier to modify code                              |
| Readability     | Code becomes easier to understand                  |
| Collaboration   | Different developers can work on different modules |

---

# 3. Creating a Module

### Step 1: Create a Python file

Create:

```text
calculator.py
```

### Step 2: Add code

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

Now we have created our own module.

---

# 4. Importing a Module

Create another file:

```text
main.py
```

Import the module:

```python
import calculator
```

Now we can access its functions.

```python
print(calculator.add(10, 20))
print(calculator.multiply(5, 4))
```

### Output

```text
30
20
```

### Syntax

```python
import module_name
```

Access members using:

```python
module_name.member_name
```

---

# 5. Import Specific Functions

Instead of importing the complete module:

```python
import calculator
```

we can import specific functions.

```python
from calculator import add
```

Now we can directly use:

```python
print(add(10, 20))
```

No need to write:

```python
calculator.add()
```

### Multiple functions

```python
from calculator import add, multiply
```

---

# 6. Import Everything using `*`

We can import everything from a module:

```python
from calculator import *
```

Now:

```python
print(add(10, 20))
print(multiply(5, 4))
```

### ⚠️ Why should we generally avoid this?

Because it can make it unclear where a function or variable came from.

For example:

```python
from calculator import *
from maths import *
```

If both modules contain:

```python
add()
```

it becomes difficult to know which `add()` is being used.

### Better approach

Prefer:

```python
import calculator
```

or:

```python
from calculator import add
```

---

# 7. Renaming a Module using `as`

Sometimes module names are long.

Example:

```python
import calculator
```

We can give it another name:

```python
import calculator as calc
```

Now:

```python
print(calc.add(10, 20))
```

Instead of:

```python
calculator.add(10, 20)
```

### Syntax

```python
import module_name as alias
```

### Example

```python
import numpy as np
```

Here:

```text
numpy → actual module
np    → alias
```

We then write:

```python
np.array([10, 20, 30])
```

---

# 8. Renaming Imported Functions

We can also rename a specific function.

```python
from calculator import add as addition
```

Now:

```python
print(addition(10, 20))
```

Here:

```text
add       → original function
addition  → alias
```

---

# 9. What is `__name__`?

Every Python module has a special built-in variable:

```python
__name__
```

Its value depends on **how the Python file is being executed**.

### If the file is executed directly

```python
python calculator.py
```

then:

```python
__name__ == "__main__"
```

### If the file is imported

Suppose:

```python
import calculator
```

Then inside `calculator.py`:

```python
__name__
```

will contain:

```text
calculator
```

---

# 10. Understanding `__name__` with Example

Create:

### `calculator.py`

```python
print(__name__)
```

Now run:

```text
calculator.py
```

Output:

```text
__main__
```

Because we directly executed the file.

---

Now create:

### `main.py`

```python
import calculator
```

Run:

```text
main.py
```

Output:

```text
calculator
```

Because `calculator.py` was imported.

---

# 11. `if __name__ == "__main__"`

This is one of the **most important concepts** in Python modules.

We can write:

```python
if __name__ == "__main__":
    print("Program started")
```

This code runs **only when the file is executed directly**.

---

## Example

### `calculator.py`

```python
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(10, 20))
```

### Case 1 — Direct execution

```text
python calculator.py
```

Output:

```text
30
```

### Case 2 — Importing

```python
import calculator
```

The `add()` function becomes available, but:

```python
print(add(10, 20))
```

inside the `if` block does **not** execute.

---

# 12. Why Do We Use `__main__`?

Imagine:

```text
calculator.py
```

contains:

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

Now another file imports it:

```python
import calculator
```

The moment we import it, this runs:

```python
print(add(10, 20))
```

That's often undesirable.

Instead:

```python
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(10, 20))
```

Now the testing/demo code runs only when `calculator.py` is executed directly.

### ⭐ Simple rule for students

> `__main__` means: **"This file is being run directly."**

---

# 13. Creating a Package

A **package** is a way of organizing multiple related modules into a directory.

Example:

```text
project/
│
├── main.py
│
└── calculator/
    ├── __init__.py
    ├── arithmetic.py
    └── scientific.py
```

Here:

```text
calculator
```

is a package.

And:

```text
arithmetic.py
scientific.py
```

are modules inside that package.

---

# 14. Creating a Simple Package

Create this structure:

```text
project/
│
├── main.py
│
└── maths/
    ├── __init__.py
    ├── addition.py
    └── multiplication.py
```

### `addition.py`

```python
def add(a, b):
    return a + b
```

### `multiplication.py`

```python
def multiply(a, b):
    return a * b
```

---

# 15. Using a Package

Inside `main.py`:

```python
from maths import addition
from maths import multiplication

print(addition.add(10, 20))
print(multiplication.multiply(5, 4))
```

Output:

```text
30
20
```

---

# 16. Importing Directly from a Package

We can also write:

```python
from maths.addition import add
```

Then:

```python
print(add(10, 20))
```

### General syntax

```python
from package.module import member
```

Example:

```python
from maths.addition import add
```

Breakdown:

```text
maths       → package
addition    → module
add         → function
```

---

# 17. What is `__init__.py`?

`__init__.py` is a special Python file associated with a package.

Example:

```text
maths/
│
├── __init__.py
├── addition.py
└── multiplication.py
```

It can be used to:

* Initialize package-related code
* Expose selected functionality
* Control what gets imported from the package
* Store package-level variables/functions

### Important modern Python point

In **modern Python**, a directory can sometimes work as a package **without** `__init__.py` because of **namespace packages**.

However, for teaching beginners and for many traditional package structures, keeping:

```text
__init__.py
```

is still a clear and common approach.

---

# 18. Using `__init__.py`

Suppose:

### `maths/__init__.py`

```python
print("Maths package loaded")
```

When the package is imported:

```python
import maths
```

the initialization code can execute.

---

# 19. `dir()` Function

`dir()` is a built-in Python function used to see the **names available inside an object/module**.

### Basic example

```python
import math

print(dir(math))
```

It displays names such as:

```text
sqrt
pow
factorial
sin
cos
pi
...
```

---

# 20. `dir()` with a String

```python
name = "Python"

print(dir(name))
```

You will see methods such as:

```text
upper
lower
split
replace
find
startswith
endswith
...
```

So we can use `dir()` to explore what an object provides.

---

# 21. `dir()` with a List

```python
numbers = [10, 20, 30]

print(dir(numbers))
```

It will show methods such as:

```text
append
extend
insert
remove
pop
sort
reverse
...
```

### Very useful for students

Instead of memorizing every method, students can use:

```python
dir(object)
```

to explore available attributes and methods.

---

# 22. `dir()` Without an Argument

We can also write:

```python
print(dir())
```

This shows names available in the **current scope**.

Example:

```python
name = "Shivam"
age = 25

print(dir())
```

The result will contain names such as:

```text
name
age
```

along with other automatically available names.

---

# 23. Module vs Package

| Module                               | Package                                |
| ------------------------------------ | -------------------------------------- |
| Usually a `.py` file                 | Usually a directory containing modules |
| Contains functions/classes/variables | Organizes related modules              |
| Example: `calculator.py`             | Example: `maths/`                      |
| Smaller unit                         | Higher-level organization              |

### Easy way to remember

```text
Module  → File
Package → Folder of modules
```

---

# 24. Complete Example

Let's build a small project.

```text
student_project/
│
├── main.py
│
└── student/
    ├── __init__.py
    ├── details.py
    └── marks.py
```

### `details.py`

```python
def get_name():
    return "Rahul"
```

### `marks.py`

```python
def get_marks():
    return 85
```

### `main.py`

```python
from student.details import get_name
from student.marks import get_marks

print("Name:", get_name())
print("Marks:", get_marks())
```

Output:

```text
Name: Rahul
Marks: 85
```

This example combines:

* Modules
* Packages
* Importing
* Functions
* Package structure

---

# 25. Important Syntax Cheat Sheet

### Import module

```python
import module
```

### Import multiple modules

```python
import module1, module2
```

### Import specific member

```python
from module import function
```

### Import multiple members

```python
from module import function1, function2
```

### Rename module

```python
import module as m
```

### Rename function

```python
from module import function as f
```

### Package import

```python
from package import module
```

### Import from module inside package

```python
from package.module import function
```

### Check direct execution

```python
if __name__ == "__main__":
    ...
```

### Explore members

```python
dir(object)
```

---

# 26. Common Mistakes Students Make

### ❌ Mistake 1 — Forgetting module name

```python
import calculator

add(10, 20)
```

If `add` wasn't imported directly, this is incorrect.

### ✅ Correct

```python
calculator.add(10, 20)
```

---

### ❌ Mistake 2 — Confusing `__name__`

Students often think:

```python
__name__
```

is always:

```text
__main__
```

### Correct understanding

```text
Direct execution → __main__

Imported module → module's name
```

---

### ❌ Mistake 3 — Using `from module import *`

Although valid:

```python
from calculator import *
```

it can make code harder to understand.

Prefer explicit imports.

---

### ❌ Mistake 4 — Confusing module and package

```text
calculator.py → Module

calculator/   → Package
```

---

# 27. 🎯 Practice Exercises

## Beginner

### Q1

Create a module called:

```text
calculator.py
```

Create functions:

```text
add()
subtract()
multiply()
divide()
```

Import and use them from `main.py`.

---

### Q2

Create:

```text
student.py
```

with:

```python
name
age
course
```

Import the module and print the values.

---

### Q3

Import the `math` module and use:

```python
sqrt()
pow()
factorial()
```

---

## Intermediate

### Q4

Create:

```text
calculator.py
```

and use:

```python
import calculator as calc
```

Call its functions using the alias.

---

### Q5

Create a module containing:

```python
def greet():
    print("Hello Student")
```

Add:

```python
if __name__ == "__main__":
    greet()
```

Test it by:

1. Running the file directly
2. Importing it from another file

Observe the difference.

---

### Q6

Create this package:

```text
college/
├── __init__.py
├── student.py
└── teacher.py
```

Create functions in both modules and use them from `main.py`.

---

## 🔥 Challenge

Create:

```text
banking/
│
├── __init__.py
├── account.py
├── deposit.py
└── withdraw.py
│
└── main.py
```

Implement:

```text
create account
deposit money
withdraw money
display balance
```

Use modules and packages to organize the project.

---

# 🧠 Final Concept Map

```text
Python Code Organization
│
├── Module
│   └── Python file (.py)
│
├── Import
│   ├── import module
│   ├── from module import ...
│   └── import module as alias
│
├── __name__
│   ├── Direct execution → "__main__"
│   └── Import → module name
│
├── Package
│   └── Folder containing related modules
│       └── __init__.py
│
└── dir()
    └── Explore available names/members
```

## ⭐ One-minute revision

> **Module = Python file containing reusable code.**

> **Package = Collection/organization of related modules.**

> **`import` = Bring a module into another Python program.**

> **`as` = Give an alias/short name.**

> **`__name__` = Tells how the module is being used.**

> **`__main__` = The file is being executed directly.**

> **`__init__.py` = Package initialization/configuration file.**

> **`dir()` = Explore names/attributes available in an object or module.**



#from className Import 

from file_name import ClassName

# Usage
my_object = ClassName()