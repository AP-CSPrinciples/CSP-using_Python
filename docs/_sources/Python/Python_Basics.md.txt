# Python Basics

Python is an open-source programming language that is one of the easiest programs that a person can learn for their first programming language.  Python is a versatile programming language that can be used in many areas such as data analysis, science, web development, AI, and IoT.  As of 2024, it is one of the most in demand programming languages in the market place.  Python is a high-level programming language that offers simplicity, readability, and versatility.  Python supports multiple programming paradigms and has an extensive library that simplifies coding tasks. Python has a robust community and documentation support that enables beginners to excel quickly in this language.   

We will be looking at syntax and structures of Python. We will use an Integrated Development Environment to develop our code in this course.  


## Python Style Guidelines

Here are some key Python style guidelines, along with examples and rationales, to help you write clean, readable, and maintainable code:

-------------------------------------------------------------------------

**1. PEP 8 Guidelines**
   - **PEP 8** is the official style guide for Python code and covers naming conventions, code layout, and indentation.

-------------------------------------------------------------------------

**2. Use Descriptive Variable and Function Names**
   - **Guideline**: Use descriptive names that make the purpose of the variable or function clear.
   - **Example**:
     ```python
     # Good
     total_cost = price * quantity
     
     # Bad
     x = p * q
     ```
   - **Rationale**: Code is more readable when variable names clearly indicate their purpose, making it easier to understand and maintain.

-------------------------------------------------------------------------

**3. Use Consistent Indentation (4 Spaces)**
   - **Guideline**: Use four spaces per indentation level; do not use tabs.
   - **Example**:
     ```python
     def calculate_area(radius):
         return 3.14 * radius ** 2
     ```
   - **Rationale**: Consistent indentation is essential for readability and prevents syntax errors.

-------------------------------------------------------------------------

**4. Limit Line Length to 79 Characters**
   - **Guideline**: Limit all lines to a maximum of 79 characters.
   - **Example**:
     ```python
     # Good
     def display_message(message):
         print(f"Message: {message}")
         
     # Bad (line too long)
     def display_message(message): print(f"Message: {message}")
     ```
   - **Rationale**: This improves readability and ensures the code displays well on all devices, including smaller screens.

-------------------------------------------------------------------------

**5. Use Blank Lines to Separate Code Sections**
   - **Guideline**: Use two blank lines to separate top-level functions and class definitions, and one blank line to separate methods within a class.
   - **Example**:
     ```python
     class Animal:
         
         def speak(self):
             pass

     class Dog(Animal):
         
         def bark(self):
             print("Woof!")
     ```
   - **Rationale**: Blank lines help visually separate sections of code, improving readability.

-------------------------------------------------------------------------

**6. Use Docstrings to Document Functions, Classes, and Modules**
   - **Guideline**: Use triple-quoted strings (`"""`) for all public modules, functions, classes, and methods.
   - **Example**:
     ```python
     def calculate_area(radius):
         """Calculate the area of a circle given its radius."""
         return 3.14 * radius ** 2
     ```
   - **Rationale**: Docstrings provide useful explanations of code functionality, which helps future readers and collaborators.

-------------------------------------------------------------------------

**7. Use Spaces Around Operators**
   - **Guideline**: Use spaces around operators and after commas, but not directly inside parentheses.
   - **Example**:
     ```python
     # Good
     result = (a + b) * (c - d)

     # Bad
     result=(a+b)*(c-d)
     ```
   - **Rationale**: Spacing around operators makes expressions easier to read.

-------------------------------------------------------------------------

**8. Avoid Excessive Nesting**
   - **Guideline**: Break down complex logic with multiple levels of nesting into smaller functions.
   - **Example**:
     ```python
     # Good
     def process_data(data):
         if not data:
             return None
         cleaned_data = clean(data)
         return analyze(cleaned_data)

     # Bad
     def process_data(data):
         if data:
             cleaned_data = clean(data)
             if cleaned_data:
                 return analyze(cleaned_data)
     ```
   - **Rationale**: Deeply nested code is harder to read and debug. Breaking code into smaller functions improves readability and reusability.

-------------------------------------------------------------------------

**9. Use List Comprehensions for Simple Operations**
   - **Guideline**: Use list comprehensions for simple operations but avoid them for complex nested operations.
   - **Example**:
     ```python
     # Good
     squares = [x ** 2 for x in range(10)]

     # Bad
     squares = []
     for x in range(10):
         squares.append(x ** 2)
     ```
   - **Rationale**: List comprehensions are concise and often faster than equivalent for-loops for simple operations.

-------------------------------------------------------------------------

**10. Handle Exceptions Properly**
   - **Guideline**: Use specific exceptions rather than catching all exceptions with `except` alone.
   - **Example**:
     ```python
     # Good
     try:
         result = 10 / divisor
     except ZeroDivisionError:
         print("Cannot divide by zero.")
         
     # Bad
     try:
         result = 10 / divisor
     except:
         print("An error occurred.")
     ```
   - **Rationale**: Catching specific exceptions allows you to handle errors appropriately, making debugging easier.

-------------------------------------------------------------------------

**11. Use Meaningful Constants Instead of Magic Numbers**
   - **Guideline**: Define constants with descriptive names for “magic numbers” (unexplained numerical values).
   - **Example**:
     ```python
     # Good
     TAX_RATE = 0.15
     total_cost = price * (1 + TAX_RATE)

     # Bad
     total_cost = price * 1.15
     ```
   - **Rationale**: Constants with meaningful names improve readability and make the code easier to modify and maintain.

-------------------------------------------------------------------------

**12. Avoid Global Variables**
   - **Guideline**: Avoid using global variables; instead, use function parameters or class attributes.
   - **Example**:
     ```python
     # Good
     def calculate_total(cost, tax_rate):
         return cost * (1 + tax_rate)

     # Bad
     TAX_RATE = 0.15
     def calculate_total(cost):
         return cost * (1 + TAX_RATE)
     ```
   - **Rationale**: Global variables can lead to hard-to-track bugs and make code harder to reuse and maintain.

-------------------------------------------------------------------------

**13. Use `is` for Comparison to `None`**
   - **Guideline**: Use `is` or `is not` when comparing to `None`.
   - **Example**:
     ```python
     # Good
     if value is None:
         print("No value")

     # Bad
     if value == None:
         print("No value")
     ```
   - **Rationale**: `is` is more efficient and explicitly intended for this type of comparison, improving clarity and performance.

-------------------------------------------------------------------------

**14. Organize Imports Properly**
   - **Guideline**: Group imports into three sections in this order: standard library imports, related third-party imports, and local application-specific imports. Separate each group with a blank line.
   - **Example**:
     ```python
     # Good
     import os
     import sys
     
     import numpy as np
     import pandas as pd
     
     from my_app.utilities import helper_function
     ```
   - **Rationale**: This structure improves readability and avoids clutter.

-------------------------------------------------------------------------

**15. Use Type Annotations (Python 3.5+)**
   - **Guideline**: Use type annotations to specify expected data types for function arguments and return values.
   - **Example**:
     ```python
     def calculate_total(cost: float, tax_rate: float) -> float:
         return cost * (1 + tax_rate)
     ```
   - **Rationale**: Type annotations make it clear what types are expected, which can help prevent bugs and improve readability. 

------------------------------------------------------------------------- 

Following these guidelines helps ensure code that is easy to read, maintain, and understand across teams.


## Print Statements

In Python, there are several ways to format and print strings. Each method offers a different approach to injecting variables or formatting output. Here are some popular variations:

1. **Basic `print` statement**  
2. **Using `print` with variables**  
3. **Using concatenation (`+` operator)**  
4. **Using `format()` method**  
5. **Using f-strings (formatted string literals)**  
6. **Using special characters for formatting**

Here’s a Python program illustrating each of these methods:

```python
# 1. Basic print statement
print("Hello, World!")

# 2. Using print with variables
name = "Alice"
age = 25
print("Name:", name)
print("Age:", age)

# 3. Using concatenation (with `+` operator)
city = "New York"
country = "USA"
print("Location: " + city + ", " + country)

# 4. Using format() method
greeting = "Hello"
print("Message: {}! My name is {} and I am {} years old.".format(greeting, name, age))

# 5. Using f-strings (formatted string literals)
# Introduced in Python 3.6, this is one of the most concise and popular methods for formatting.
print(f"{greeting}! My name is {name} and I am {age} years old.")

# 6. Using special characters for formatting (e.g., newline `\n`, tab `\t`)
print("Hello\nWorld!")  # newline
print("Hello\tWorld!")  # tab
print("Name:\t", name)   # tab
print("Age:\t", age)     # tab
```

**Explanation of Each Method**

1. **Basic `print` statement**: Just prints the text directly.
  
2. **Using `print` with variables**: Allows direct printing of variables by separating values with commas. This adds a space automatically.

3. **Using concatenation**: The `+` operator combines strings. However, this method works only if all parts are strings, so numbers must be converted (using `str()`).

4. **Using `format()` method**: This method replaces `{}` placeholders in the string with values provided to `format()`. It’s flexible for various formatting needs.

5. **Using f-strings**: These formatted string literals are enclosed with an `f` prefix. Variables can be embedded directly within `{}` braces, making it compact and readable.

6. **Using special characters**: Special characters like `\n` (newline) and `\t` (tab) can be used to format output, particularly for line breaks and indentation.

These different print methods offer flexibility in formatting and display for different contexts.


## Variables and Data Types

In Python, **variables** are used to store data, which can be used and manipulated throughout a program. **Data types** specify the kind of value a variable holds, determining what operations can be performed on it. Python automatically assigns a data type based on the value assigned to a variable.

**Python Variables**
A **variable** is essentially a name given to a memory location where data is stored. In Python, you don’t need to declare the data type of a variable; you just assign a value to it, and Python infers the type.

**Syntax**:
```python
variable_name = value
```

**Example**:
```python
age = 25            # age is an integer
name = "Alice"      # name is a string
price = 9.99        # price is a floating-point number
is_student = True   # is_student is a boolean
```

**Python Data Types**
Here are the basic data types in Python, along with examples for each.

1. **Integer (`int`)**
   - Whole numbers, positive or negative, without a decimal point.
   - **Example**:
     ```python
     age = 25
     count = -10
     print(type(age))  # Output: <class 'int'>
     ```

2. **Floating-point number (`float`)**
   - Numbers with a decimal point, used for more precise calculations.
   - **Example**:
     ```python
     price = 19.99
     temperature = -5.5
     print(type(price))  # Output: <class 'float'>
     ```

3. **String (`str`)**
   - A sequence of characters, enclosed in single or double quotes.
   - **Example**:
     ```python
     name = "Alice"
     greeting = 'Hello, World!'
     print(type(name))  # Output: <class 'str'>
     ```

4. **Boolean (`bool`)**
   - Represents one of two values: `True` or `False`.
   - **Example**:
     ```python
     is_open = True
     is_available = False
     print(type(is_open))  # Output: <class 'bool'>
     ```

5. **List (`list`)**
   - An ordered collection of items, which can be of different data types. Lists are mutable, meaning items can be changed.
   - **Example**:
     ```python
     fruits = ["apple", "banana", "cherry"]
     numbers = [1, 2, 3, 4, 5]
     mixed_list = [1, "Hello", 3.5, True]
     print(type(fruits))  # Output: <class 'list'>
     ```

6. **Tuple (`tuple`)**
   - Similar to a list, but immutable, meaning items cannot be changed once set.
   - **Example**:
     ```python
     coordinates = (10, 20)
     dimensions = (1920, 1080)
     print(type(coordinates))  # Output: <class 'tuple'>
     ```

7. **Dictionary (`dict`)**
   - A collection of key-value pairs, where each key is unique. Dictionaries are mutable.
   - **Example**:
     ```python
     student = {
         "name": "Alice",
         "age": 20,
         "is_student": True
     }
     print(type(student))  # Output: <class 'dict'>
     ```

8. **Set (`set`)**
   - An unordered collection of unique items. Sets are mutable but don’t allow duplicate elements.
   - **Example**:
     ```python
     colors = {"red", "green", "blue"}
     numbers_set = {1, 2, 3, 4, 5}
     print(type(colors))  # Output: <class 'set'>
     ```

9. **None Type (`NoneType`)**
   - Represents the absence of a value or a null value.
   - **Example**:
     ```python
     result = None
     print(type(result))  # Output: <class 'NoneType'>
     ```

**Example Program Demonstrating Python Data Types**

```python
# Integer
age = 30
print("Age:", age, "| Data type:", type(age))

# Float
height = 5.9
print("Height:", height, "| Data type:", type(height))

# String
name = "John"
print("Name:", name, "| Data type:", type(name))

# Boolean
is_active = True
print("Is Active:", is_active, "| Data type:", type(is_active))

# List
colors = ["red", "blue", "green"]
print("Colors:", colors, "| Data type:", type(colors))

# Tuple
dimensions = (1920, 1080)
print("Dimensions:", dimensions, "| Data type:", type(dimensions))

# Dictionary
person = {"name": "Alice", "age": 25}
print("Person:", person, "| Data type:", type(person))

# Set
unique_numbers = {1, 2, 3, 4, 5}
print("Unique Numbers:", unique_numbers, "| Data type:", type(unique_numbers))

# NoneType
result = None
print("Result:", result, "| Data type:", type(result))
```

Each variable in this example demonstrates a different data type. Using the `type()` function, we can easily check the data type of each variable.



## Order of Operation

In Python, expressions are evaluated based on a well-defined **order of operations**, also known as **operator precedence**. This hierarchy determines the sequence in which operations (arithmetic, logical, relational, etc.) are performed. Here, we will cover:

1. **Arithmetic Operators** (PEMDAS rules)
2. **Relational Operators**
3. **Logical Operators**


------------------------------------------------------------

**Operator Precedence in Python**

Python’s precedence rules are designed to make expressions behave intuitively. Here’s the order of precedence, from highest to lowest:

1. **Parentheses** (`()`)
2. **Exponentiation** (`**`)
3. **Arithmetic Operators**: Multiplication (`*`), Division (`/` and `//`), and Modulus (`%`)  
4. **Arithmetic Operators**: Addition (`+`) and Subtraction (`-`)
5. **Relational Operators**: `<`, `<=`, `>`, `>=`, `==`, `!=`
6. **Logical Operators**: `not`, `and`, `or`

Understanding this precedence order and the **left-to-right** evaluation rule allows for correctly interpreting complex expressions in Python. Following these rules helps ensure that Python evaluates each part of an expression as intended, providing accurate and predictable results.

The following table summarizes the **operator precedence** from *highest to lowest*. A complete table for the entire language can be found in the Python Documentation.  http://docs.python.org/py3k/reference/expressions.html#expression-lists

| Level	| Category	| Operators |
| :--: | :--: | :--: |
| 7 *(high)*	| exponent	| ** |
| 6	| multiplication |	*,/,//,% |
| 5	| addition	| +,- |
| 4	| relational	| ==,!=,<=,>=,>,< |
| 3	| logical	| not |
| 2	| logical	| and |
| 1 *(low)*	|logical |	or |

------------------------------------------------------------

**1. Arithmetic Operators and PEMDAS**

The arithmetic operators follow **PEMDAS**:
- **Parentheses**: Highest precedence, used to group expressions.
- **Exponents**: Calculated next, evaluated from right to left.
- **Multiplication, Division, and Modulus**: Evaluated left to right.
- **Addition and Subtraction**: Evaluated left to right.

**Example**:
```python
result = 5 + 2 * (3 ** 2 - 4) / 2
print(result)  # Output: 8.0
```

**Step-by-Step Evaluation**
1. **Parentheses** (`3 ** 2 - 4`)
   - `3 ** 2` is calculated first, giving `9`.
   - Then, `9 - 4` gives `5`.
   - Expression becomes `5 + 2 * 5 / 2`.

2. **Multiplication and Division** (`*` and `/` left to right):
   - `2 * 5` is `10`, so the expression is `5 + 10 / 2`.
   - `10 / 2` results in `5.0` (division returns a float).
   - Now we have `5 + 5.0`.

3. **Addition**:
   - `5 + 5.0` results in `10.0`.

**Final result**: `10.0`.

------------------------------------------------------------

**NOTE: Why Division Returns a Float**

In Python 3, the `/` operator always returns a float, even if both operands are integers. This is to provide accurate results without unexpected truncation. For integer-only results, Python offers the `//` operator (floor division).

**Example**:
```python
result = 7 / 2  # Output: 3.5 (float)
result = 7 // 2  # Output: 3 (integer)
```

The `/` operator preserves fractional results, which is especially helpful in complex calculations, while `//` discards the decimal part.

------------------------------------------------------------

**2. Relational (Comparison) Operators**

Relational operators compare values and have **lower precedence** than arithmetic operators but **higher precedence** than logical operators. These include:
- `==` (equal to)
- `!=` (not equal to)
- `<`, `<=`, `>`, `>=` (less than, greater than, and their variants)

**Example**:
```python
result = 5 + 3 > 2 * 3
print(result)  # Output: True
```

**Step-by-Step Evaluation**
1. **Arithmetic Operators**:
   - `5 + 3` results in `8`.
   - `2 * 3` results in `6`.
   
2. **Relational Operator**:
   - The comparison `8 > 6` is evaluated, resulting in `True`.

**Final result**: `True`.

------------------------------------------------------------

**3. Logical Operators**

Logical operators (`not`, `and`, `or`) combine boolean expressions. They have the lowest precedence, so they are evaluated after arithmetic and relational operators.

**Order of Precedence for Logical Operators**:
1. **not**: Highest among logical operators.
2. **and**: Middle precedence.
3. **or**: Lowest precedence.

**Example**:
```python
result = 3 > 2 and 5 == 5 or not (4 + 1 < 6)
print(result)  # Output: True
```

**Step-by-Step Evaluation**
1. **Parentheses** (`4 + 1 < 6`):
   - `4 + 1` results in `5`.
   - The comparison `5 < 6` results in `True`.
   - `not (True)` then results in `False`.

2. **Relational Operators**:
   - `3 > 2` evaluates to `True`.
   - `5 == 5` evaluates to `True`.

3. **Logical Operators**:
   - `True and True` is `True`.
   - Finally, `True or False` evaluates to `True`.

**Final result**: `True`.

------------------------------------------------------------

**Combined Example with All Operators**

Let’s consider an example combining arithmetic, relational, and logical operators.

```python
result = (2 + 3 * 2) >= 7 and 4 / 2 < 3 or not (5 == 4)
print(result)  # Output: True
```

**Step-by-Step Evaluation**

1. **Parentheses** (`2 + 3 * 2` and `5 == 4`):
   - For `2 + 3 * 2`, `3 * 2` is evaluated first, giving `6`.
   - Then, `2 + 6` results in `8`.
   - So `(2 + 3 * 2)` becomes `8`.
   - `(5 == 4)` results in `False`.

2. **Arithmetic and Relational Operators**:
   - The comparison `(2 + 3 * 2) >= 7` evaluates as `8 >= 7`, which is `True`.
   - `4 / 2` results in `2.0`, so `2.0 < 3` evaluates as `True`.

3. **Logical Operators**:
   - `True and True` results in `True`.
   - `not (False)` results in `True`.
   - Finally, `True or True` results in `True`.

**Final result**: `True`.

------------------------------------------------------------

**Summary of Python’s Operator Precedence**

Here’s a quick summary of operator precedence from highest to lowest:

1. **Parentheses** `()`
2. **Exponents** `**`
3. **Arithmetic Operators** `*`, `/`, `//`, `%`
4. **Arithmetic Operators** `+`, `-`
5. **Relational Operators** `<`, `<=`, `>`, `>=`, `==`, `!=`
6. **Logical `not`**
7. **Logical `and`**
8. **Logical `or`**

------------------------------------------------------------



## Modules and Packages


In Python, **modules** and **packages** are essential organizational tools that help in managing, organizing, and reusing code. They make code more modular and allow developers to structure their projects efficiently.

### Modules in Python

A **module** in Python is simply a file with a `.py` extension that contains Python code—variables, functions, classes, or runnable code. Each module serves as a standalone file that you can import and use in other Python programs. Modules allow for logical organization, reduce redundancy, and make code easier to maintain and debug.

**Why Modules are Used**:
- **Code Reusability**: Once written, a module can be reused in different programs.
- **Organization**: Modules keep related code together, making it more manageable and readable.
- **Namespace Management**: Using modules prevents naming conflicts, as each module has its own namespace.

**Creating and Using a Module**

Let's create a module named `math_utils.py`:

```python
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

To use this module, save it in your project directory and import it into your main script:

```python
# main.py
import math_utils

result = math_utils.add(5, 3)
print(result)  # Output: 8
```

Or, you could import only specific functions from the module:

```python
from math_utils import add

result = add(5, 3)
print(result)  # Output: 8
```

### Packages in Python

A **package** is a collection of related modules organized in a directory hierarchy. Packages allow for structuring your project logically, especially as it grows larger with multiple modules. A package is essentially a directory that contains multiple modules and an `__init__.py` file, which signifies to Python that the directory should be treated as a package.

**Why Packages are Used**:
- **Organization of Large Codebases**: Packages help in grouping related modules, which makes larger projects more manageable.
- **Namespace Management**: Packages can have sub-packages, which help in avoiding naming conflicts and managing large amounts of code.
- **Ease of Distribution**: Packages can be distributed and installed using package managers like `pip`, making it easier to share and use code libraries.

**Creating and Using a Package**

Suppose we have a package directory structure as follows:

```
my_package/
    __init__.py
    arithmetic.py
    geometry.py
```

- `__init__.py`: This can be an empty file or contain initialization code for the package.
- `arithmetic.py` and `geometry.py`: These are modules inside the `my_package` package.

Let's define functions in `arithmetic.py` and `geometry.py`:

```python
# arithmetic.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

```python
# geometry.py
def area_circle(radius):
    import math
    return math.pi * (radius ** 2)

def area_square(side):
    return side * side
```

To use this package in your script, you can import it like this:

```python
# main.py
from my_package import arithmetic, geometry

# Using functions from the package
print(arithmetic.add(10, 5))  # Output: 15
print(geometry.area_circle(3))  # Output: 28.27 (approx)
```

---

**Common Python Modules and Packages**

Python has a rich standard library with many commonly used modules and packages that are built into Python. Some of these are:

1. **`math` Module**: Provides mathematical functions.
   - Example:
     ```python
     import math
     print(math.sqrt(16))  # Output: 4.0
     ```

2. **`datetime` Module**: Handles date and time manipulations.
   - Example:
     ```python
     import datetime
     print(datetime.datetime.now())  # Output: Current date and time
     ```

3. **`random` Module**: Used for generating random numbers.
   - Example:
     ```python
     import random
     print(random.randint(1, 10))  # Output: Random integer between 1 and 10
     ```

4. **`os` Module**: Provides functions to interact with the operating system.
   - Example:
     ```python
     import os
     print(os.getcwd())  # Output: Current working directory
     ```

5. **`sys` Module**: Provides access to system-specific parameters and functions.
   - Example:
     ```python
     import sys
     print(sys.version)  # Output: Python version
     ```

6. **`re` Module**: Used for working with regular expressions.
   - Example:
     ```python
     import re
     pattern = r"\bword\b"
     text = "Find the word in this sentence."
     match = re.search(pattern, text)
     print(match.group())  # Output: 'word'
     ```

7. **`json` Module**: Used for parsing JSON data.
   - Example:
     ```python
     import json
     data = '{"name": "John", "age": 30}'
     parsed_data = json.loads(data)
     print(parsed_data['name'])  # Output: John
     ```

8. **`collections` Module**: Provides specialized container data types, like `Counter`, `defaultdict`, and `namedtuple`.
   - Example:
     ```python
     from collections import Counter
     data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
     print(Counter(data))  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})
     ```

9. **`numpy` Package** (external): Used for numerical computations, especially for array operations.
   - Example:
     ```python
     import numpy as np
     array = np.array([1, 2, 3])
     print(np.mean(array))  # Output: 2.0
     ```

10. **`pandas` Package** (external): Used for data analysis and manipulation.
    - Example:
      ```python
      import pandas as pd
      data = {'Name': ['John', 'Jane'], 'Age': [28, 24]}
      df = pd.DataFrame(data)
      print(df)
      ```

**Summary**

- **Modules** are single files with Python code, useful for organizing and reusing functions, classes, or variables.
- **Packages** are directories containing multiple related modules and an `__init__.py` file, which make large projects more manageable and prevent naming conflicts.

Using modules and packages keeps Python code modular, readable, and reusable, making it easier to structure and manage projects.
## Control Flow and Conditional Statements


## Loops

```python
# CODE 1
for x in range (1, 6):
  for y in range (1, 6):
    print("*", end="")
  print()

# CODE 2
for x in range (1, 6):
  for y in range (1, 6):
    print(x, end="")
  print()

# CODE 4
for x in 'ABCDE':
  for y in 'ABCDE':
    print(x, end="")
  print()

# CODE 6
for x in range (5, 0, -1):
  for y in range (5, 0, -1):
    print(x, end="")
  print()

# CODE 7
for x in range (5, 0, -1):
  for y in range(5, 0, -1):
    print(y, end="")
  print()

# CODE 8
for x in range (69, 64, -1):
  for y in range(1, 6):
    print(chr(x), end="")
  print()
  
# CODE 10
for x in range (1, 6):
  for y in range (1, x+1):
    print("x", end="")
  print()

# CODE 12
for x in range (1, 6):
  for y in range (1, x+1):
    print(y, end="")
  print()

# CODE 13
for x in range (65, 70):
  for y in range (65, x+1):
    print(chr(x), end="")
  print()

# CODE 14
for x in range (65, 70):
  for y in range (65, x+1):
    print(chr(y), end="")
  print()

# CODE 15
for x in range (1, 6):
  for y in range (6, x, -1):
    print("*", end="")
  print()

# CODE 16
for x in range (1, 6):
  for y in range (6, x, -1):
    print(x, end="")
  print()

# CODE 17
for x in range (6, 1, -1):
  for y in range (1, x):
    print(y, end="")
  print()

# CODE 21
for x in range (1, 6):
  for y in range (5, x-1, -1):
    print(y, end="")
  print()

# CODE 22
for x in range (5, 0, -1):
  for y in range (0, x):
    print(chr(x+64), end="")
  print()

# CODE 24
for x in range (1, 6):
  for y in range (5, x, -1):
    print("", end="")
  for z in range (0, x):
    print("*", end="")
  print()

# CODE 25
for x in range (1, 6):
  for y in range (5, x, -1):
    print(" ", end="")
  for z in range (0, x):
    print(x, end="")
  print()

```

```python
# Create a square

size = int(input("Enter the size of the square: "))

for i in range(size):
  for j in range(size):
    if i == 0 or i == size-1 or j == 0 or j == size-1:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print("\r")

```


Sample Output

```python
Enter the size of the square: 10

* * * * * * * * * * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
* * * * * * * * * * 
```

-------------------------------------------------------------------------------------------------


## Functions/ Methods/ Parameters
In computer programming, the terms **function**, **method**, and **procedure** have distinct meanings, though they are often used interchangeably in casual conversation. Here’s a breakdown of each:

### Function
- **Definition**: A function is a block of code that takes inputs (arguments), performs a specific task, and returns a value. Functions are designed to compute a value and can be used across different parts of a program.
- **Example**: In Python, a simple function might look like this:
  ```python
  def add(a, b):
      return a + b
  ```

### Method
- **Definition**: A method is similar to a function but is associated with an object or a class in object-oriented programming (OOP). Methods operate on data contained within the object and can modify the object's state.
- **Example**: In Java, a method in a class might look like this:
  ```java
  public class Calculator {
      public int add(int a, int b) {
          return a + b;
      }
  }
  ```

### Procedure
- **Definition**: A procedure is a block of code that performs a task but does not necessarily return a value. Procedures are often used for executing a sequence of statements and might be called for their side effects rather than for a result.
- **Example**: In Pascal, a procedure might look like this:
  ```pascal
  procedure DisplayMessage;
  begin
      writeln('Hello, World!');
  end;
  ```

### Summary of Differences
- **Return Value**:
  - **Function**: Returns a value.
  - **Method**: Can return a value (if designed to do so) and is associated with an object.
  - **Procedure**: Typically does not return a value.

- **Context**:
  - **Function**: Used in various programming paradigms (procedural, functional).
  - **Method**: Specific to object-oriented programming.
  - **Procedure**: Often used in procedural programming languages.

Understanding these distinctions can help in writing clearer, more organized code and communicating effectively with other developers.


## Lists and List Manipulation

For this class, we will not be using tuples, but you should be familiar with how they are used and the difference of a list.

|      | Indexing | Ordered | Mutable | Duplicate |
|------------|---------------|----------------|------------------------------------|----------------|
| List | <ul><li>[X] Yes</li><li>[ ] No</li></ul> | <ul><li>[X] Yes</li><li>[ ] No</li></ul> | <ul><li>[X] Yes</li><li>[ ] No</li></ul> | <ul><li>[X] Yes</li><li>[ ] No</li></ul> |
| Tuple | <ul><li>[X] Yes</li><li>[ ] No</li></ul> | <ul><li>[X] Yes</li><li>[ ] No</li></ul> | <ul><li>[ ] Yes</li><li>[X] No</li></ul> | <ul><li>[X] Yes</li><li>[ ] No</li></ul> |
| Set |  <ul><li>[ ] Yes</li><li>[X] No</li></ul> | <ul><li>[ ] Yes</li><li>[X] No</li></ul> | <ul><li>[ ] Yes</li><li>[X] No</li></ul> | <ul><li>[ ] Yes</li><li>[X] No</li></ul> |
| Dictionary |  <ul><li>[ ] Yes</li><li>[X] No</li></ul> | <ul><li>[X] Yes</li><li>[ ] No</li></ul> | <ul><li>[X] Yes</li><li>[ ] No</li></ul> | <ul><li>[ ] Yes</li><li>[X] No</li></ul> |


In Python, lists are **indexed** collections, meaning each item in a list has a specific position. Python uses **zero-based indexing**, which means the first element is accessed with index `0`, the second with `1`, and so on. Python also supports **negative indexing**, where `-1` refers to the last item, `-2` to the second-to-last, and so forth.

**Example of indexing POTATO**

```
_______________________________________________
string1 = |  P  |  O  |  T  |  A  |  T  |  O  |

index #   0     1     2     3     4     5     6
_______________________________________________
```


**Accessing List Elements with Indexing**

Given a list:

```python
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
```

- `my_list[0]` gives `"apple"`, the first item.
- `my_list[1]` gives `"banana"`, the second item.
- `my_list[4]` gives `"elderberry"`, the fifth item.

If you try to access an index outside the range, Python will raise an `IndexError`:

```python
print(my_list[5])  # Raises IndexError: list index out of range
```

**Negative Indexing**

Python also allows negative indices to start counting from the end of the list:

- `my_list[-1]` gives `"elderberry"`, the last item.
- `my_list[-2]` gives `"date"`, the second-to-last item.
- `my_list[-5]` gives `"apple"`, the first item (same as `my_list[0]`).

**Slicing a List**

Python also allows you to retrieve a **subset of elements** from a list using slicing. The syntax is `list[start:end:step]`, where:
- **`start`** is the index where the slice begins (inclusive).
- **`end`** is where the slice ends (exclusive).
- **`step`** determines the number of steps between each item in the slice (optional).

**Example of Slicing**

```python
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Slicing from the start to the end of the list
print(my_list[1:4])  # Output: ['banana', 'cherry', 'date']

# Slicing with a step of 2
print(my_list[0:5:2])  # Output: ['apple', 'cherry', 'elderberry']

# Slicing with negative indices
print(my_list[-4:-1])  # Output: ['banana', 'cherry', 'date']
```

**Omitting Start, End, or Step**

You can omit any part of the slice syntax:
- **Omitting `start`** defaults it to the beginning of the list.
- **Omitting `end`** goes to the end of the list.
- **Omitting `step`** defaults it to `1`.

**Examples of Omitting Parts of the Slice**

```python
# All elements from the start
print(my_list[:3])  # Output: ['apple', 'banana', 'cherry']

# All elements from a specific index to the end
print(my_list[2:])  # Output: ['cherry', 'date', 'elderberry']

# Entire list with a step of 2
print(my_list[::2])  # Output: ['apple', 'cherry', 'elderberry']
```

**Using Negative Step**

A negative `step` reverses the order, allowing you to iterate backward through the list.

**Example with Negative Step**

```python
# Reverse the entire list
print(my_list[::-1])  # Output: ['elderberry', 'date', 'cherry', 'banana', 'apple']

# Every second item from the end to the beginning
print(my_list[::-2])  # Output: ['elderberry', 'cherry', 'apple']
```

In summary, Python’s list indexing is versatile, supporting positive and negative indices, as well as slicing with optional start, end, and step parameters. This flexibility allows for efficient access and manipulation of list elements.


### Specifically Lists


In this program, we use the most common methods that is able to manipulate a list:  `append`, `insert`, `remove`, `pop`, `sort`, `reverse`, `count`, `index`, `extend`, and `clear`.

```python
# Initializing a list
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# 1. append() - Adds an element at the end of the list
fruits.append("orange")
print("After append:", fruits)

# 2. insert() - Adds an element at the specified position
fruits.insert(1, "blueberry")
print("After insert at index 1:", fruits)

# 3. remove() - Removes the first item with the specified value
fruits.remove("banana")
print("After remove 'banana':", fruits)

# 4. pop() - Removes the element at the specified position (default is the last element)
popped_item = fruits.pop()
print("After pop:", fruits)
print("Popped item:", popped_item)

# 5. index() - Returns the index of the first element with the specified value
index_of_cherry = fruits.index("cherry")
print("Index of 'cherry':", index_of_cherry)

# 6. count() - Returns the number of elements with the specified value
fruits.append("apple")
apple_count = fruits.count("apple")
print("Count of 'apple':", apple_count)

# 7. sort() - Sorts the list in ascending order
fruits.sort()
print("After sort:", fruits)

# 8. reverse() - Reverses the order of the list
fruits.reverse()
print("After reverse:", fruits)

# 9. extend() - Adds all elements of a list to another list
more_fruits = ["mango", "pineapple", "kiwi"]
fruits.extend(more_fruits)
print("After extend with more_fruits:", fruits)

# 10. clear() - Removes all elements from the list
fruits.clear()
print("After clear:", fruits)
```

### Explanation of the methods:

1. **`append()`**: Adds an item to the end of the list.
2. **`insert(index, item)`**: Inserts an item at the specified index.
3. **`remove(item)`**: Removes the first occurrence of an item from the list.
4. **`pop(index)`**: Removes and returns the item at the given index; default is the last item.
5. **`index(item)`**: Finds the index of the first occurrence of the specified item.
6. **`count(item)`**: Counts how many times an item appears in the list.
7. **`sort()`**: Sorts the list in ascending order (in-place).
8. **`reverse()`**: Reverses the list (in-place).
9. **`extend(list)`**: Extends the list by appending elements from another list.
10. **`clear()`**: Removes all elements from the list.


## File Handling


File handling in Python allows you to work with files on your computer: reading data from files, writing data to files, and appending data. Python provides built-in functions and modules to make this straightforward. Here's a guide to the basics of file handling in Python 3.x, with examples.

**1. Opening and Closing Files**

The `open()` function is used to open a file. It takes two main parameters:
- **Filename**: the name of the file you want to work with.
- **Mode**: how you want to open the file, such as for reading or writing.

Here are the common modes:
- **`'r'`** - Read (default mode). Opens a file for reading. Raises an error if the file doesn’t exist.
- **`'w'`** - Write. Opens a file for writing. Creates a new file if it doesn’t exist or truncates the file if it exists.
- **`'a'`** - Append. Opens a file for appending. Creates a new file if it doesn’t exist.
- **`'r+'`** - Read and write. Opens a file for both reading and writing.

It’s a good practice to close a file after you’re done working with it to free up system resources. You can do this with the `close()` method or by using a `with` statement (recommended), which automatically closes the file for you.

**Example of Opening and Closing a File**

```python
# Opening a file for reading
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()  # Closing the file
```

Using a `with` statement:

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# No need to close the file, it’s automatically handled
```

**2. Reading Files**

There are several methods to read from a file:
- **`read()`**: Reads the entire file as a string.
- **`readline()`**: Reads a single line at a time.
- **`readlines()`**: Reads all lines and returns them as a list of strings.

**Example of Reading a File**

Assuming `example.txt` contains:
```
Hello, World!
This is a text file.
```

```python
# Reading the entire file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Reading all lines as a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

**3. Writing to Files**

To write data to a file, you can use:
- **`write()`**: Writes a string to the file.
- **`writelines()`**: Writes a list of strings to the file.

**Example of Writing to a File**

```python
# Writing to a file (overwrites if the file already exists)
with open("example.txt", "w") as file:
    file.write("This is a new line.\n")
    file.write("Writing to the file.")

# Writing multiple lines at once
with open("example.txt", "w") as file:
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    file.writelines(lines)
```

**4. Appending to Files**

To add data to the end of an existing file, use the `'a'` mode.

**Example of Appending to a File**

```python
with open("example.txt", "a") as file:
    file.write("\nAppending this line to the file.")
```

**5. Working with Binary Files**

Binary files (like images or executable files) require using the `'b'` mode (e.g., `'rb'` for reading, `'wb'` for writing).

**Example of Working with Binary Files**

```python
# Reading a binary file (e.g., an image)
with open("image.jpg", "rb") as file:
    data = file.read()
    print(data)

# Writing to a binary file
with open("copy_image.jpg", "wb") as file:
    file.write(data)
```

**6. Using `seek()` and `tell()` for File Positioning**

- **`seek(offset, from_what)`**: Moves the file pointer to a specific position.
- **`tell()`**: Returns the current position of the file pointer.

**Example of Using `seek()` and `tell()`**

```python
with open("example.txt", "r") as file:
    print(file.read(5))    # Read first 5 characters
    print(file.tell())      # Output current file position
    file.seek(0)            # Go back to the beginning
    print(file.read(5))     # Read first 5 characters again
```

**Summary**

- Use `open()` with the appropriate mode for your needs.
- Use `with open()` to ensure files are properly closed.
- Use `read()`, `readline()`, or `readlines()` for reading files.
- Use `write()` or `writelines()` for writing to files.
- Use `seek()` and `tell()` to navigate through files. 

This covers the basics of file handling in Python!


## Object-Oriented Programming


## Exception Handling


Exception handling in Python allows you to manage errors that arise during program execution, helping the program to continue running or provide a more user-friendly message instead of crashing. Python uses `try`, `except`, `else`, and `finally` blocks for this purpose.

**Basic Syntax of Exception Handling**
The basic syntax for handling exceptions in Python looks like this:

```python
try:
    # Code that may raise an exception
except SomeException as e:
    # Code that runs if the specified exception occurs
else:
    # Code that runs if no exceptions occur
finally:
    # Code that always runs, regardless of whether an exception occurred
```

- **try**: Wraps code that may raise an exception.
- **except**: Catches and handles specific exceptions.
- **else**: Executes code if no exception occurred.
- **finally**: Executes code regardless of whether an exception occurred, often used for cleanup actions.

**Example 1: Basic Exception Handling**
Here’s a basic example of handling a `ZeroDivisionError`:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful:", result)
finally:
    print("End of operation.")
```

**Example 2: Handling Multiple Exceptions**
You can handle multiple exceptions by specifying them in separate `except` blocks or by combining them.

```python
try:
    user_input = int(input("Enter a number: "))
    result = 100 / user_input
except ValueError:
    print("Invalid input! Please enter an integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")
```

**Real-World Examples of Exception Handling**

**1. File Handling with Exceptions**
When working with files, it’s common to check if a file exists before attempting to read or write to it. Using exception handling here ensures that the program doesn’t crash if the file is missing.

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'data.txt' does not exist.")
except IOError:
    print("An error occurred while reading the file.")
```

**2. Database Connection Handling**
In applications that connect to a database, it’s essential to handle exceptions in case the connection fails due to network issues, wrong credentials, etc.

```python
import sqlite3

try:
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    print(data)
except sqlite3.DatabaseError as e:
    print("Database error:", e)
finally:
    if connection:
        connection.close()
```

**3. User Input Validation**
In scenarios where user input is required, validation and exception handling ensure that unexpected input doesn’t crash the program.

```python
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print("Invalid input:", e)
else:
    print(f"Your age is {age}")
```

**4. Network Request Handling**
When making network requests (e.g., API requests), it’s good practice to handle exceptions, especially for connectivity issues, timeouts, or HTTP errors.

```python
import requests

try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
    data = response.json()
    print(data)
except requests.ConnectionError:
    print("Failed to connect to the server.")
except requests.Timeout:
    print("The request timed out.")
except requests.HTTPError as e:
    print("HTTP error:", e)
except requests.RequestException as e:
    print("An error occurred:", e)
```

**Summary**
Exception handling helps manage different types of errors gracefully, enabling applications to run smoothly without abrupt failures. In real-world applications, exception handling is vital for improving reliability, especially in operations involving file access, user input, database connections, or network requests.

## Lambda Functions


In Python, a **lambda function** is a small, anonymous function that is defined using the `lambda` keyword. Unlike regular functions created with `def`, lambda functions are written in a single line and are often used for short, simple operations that are not reused elsewhere. 

### Basic Syntax of Lambda Functions
```python
lambda arguments: expression
```
- **arguments**: The input(s) to the function.
- **expression**: The operation or calculation that returns a result.

Lambda functions can take any number of arguments, but they are limited to a single expression. They are useful when you need a simple function for a short period and don’t want to formally define it with `def`.

**1. Basic Example of a Lambda Function**
A simple example of a lambda function that adds 10 to a given number:

```python
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15
```

**2. Lambda Function with Multiple Arguments**
Lambda functions can accept multiple arguments, which is useful for quick calculations.

```python
multiply = lambda x, y: x * y
print(multiply(4, 5))  # Output: 20
```

**3. Using Lambda Functions with `map()`**
`map()` applies a function to each item in an iterable (like a list). Lambda functions are frequently used with `map()` to simplify operations.

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

**4. Using Lambda Functions with `filter()`**
`filter()` applies a function to each item in an iterable and returns only those items for which the function returns `True`. Lambda functions are handy for creating quick filters.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]
```

**5. Using Lambda Functions with `sorted()`**
You can use lambda functions as the `key` argument in `sorted()` to define custom sorting logic.

```python
names = ["John", "Paul", "George", "Ringo"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  # Output: ['Paul', 'John', 'Ringo', 'George']
```

**6. Lambda Function in a Dictionary**
Lambda functions are sometimes used in dictionaries to create simple mathematical operations or other functions based on keys.

```python
calculator = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else 'Division by zero'
}

print(calculator['add'](10, 5))         # Output: 15
print(calculator['divide'](10, 2))      # Output: 5.0
print(calculator['divide'](10, 0))      # Output: Division by zero
```

**7. Using Lambda with Conditional Expressions**
Lambda functions can contain conditional expressions to add logic in a concise format.

```python
max_value = lambda x, y: x if x > y else y
print(max_value(10, 20))  # Output: 20
```

**8. Lambda in List Comprehension**
Lambdas can be used within list comprehensions for quick transformations.

```python
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [(lambda x: x * 2)(x) for x in numbers]
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]
```

**9. Using Lambda Functions in Higher-Order Functions**
Lambda functions are often used in higher-order functions (functions that take other functions as arguments). For instance, they can be used to apply custom logic in a function parameter.

```python
def apply_operation(func, x, y):
    return func(x, y)

result = apply_operation(lambda x, y: x * y, 10, 5)
print(result)  # Output: 50
```

**10. Lambda Functions for Data Manipulation in Pandas**
In data science, lambda functions are commonly used with libraries like `pandas` for quick data transformations.

```python
import pandas as pd

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22]
})

data['AgeGroup'] = data['Age'].apply(lambda x: 'Young' if x < 25 else 'Adult')
print(data)
```

**Summary**
Lambda functions in Python provide a concise way to define simple functions without the need for formal `def` syntax. They are useful in scenarios where small, throwaway functions are needed, like with `map()`, `filter()`, and data processing tasks. However, lambda functions are limited to single expressions, so they're best for straightforward operations rather than complex logic.
## Data Structures
