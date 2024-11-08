# Python Basics

Python is an open-source programming language that is one of the easiest programs that a person can learn for their first programming language.  Python is a versatile programming language that can be used in many areas such as data analysis, science, web development, AI, and IoT.  As of 2024, it is one of the most in demand programming languages in the market place.  Python is a high-level programming language that offers simplicity, readability, and versatility.  Python supports multiple programming paradigms and has an extensive library that simplifies coding tasks. Python has a robust community and documentation support that enables beginners to excel quickly in this language.   

We will be looking at syntax and structures of Python. We will use an Integrated Development Environment to develop our code in this course.  


## Python Style Guidelines


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

### Explanation of Each Method

1. **Basic `print` statement**: Just prints the text directly.
  
2. **Using `print` with variables**: Allows direct printing of variables by separating values with commas. This adds a space automatically.

3. **Using concatenation**: The `+` operator combines strings. However, this method works only if all parts are strings, so numbers must be converted (using `str()`).

4. **Using `format()` method**: This method replaces `{}` placeholders in the string with values provided to `format()`. It’s flexible for various formatting needs.

5. **Using f-strings**: These formatted string literals are enclosed with an `f` prefix. Variables can be embedded directly within `{}` braces, making it compact and readable.

6. **Using special characters**: Special characters like `\n` (newline) and `\t` (tab) can be used to format output, particularly for line breaks and indentation.

These different print methods offer flexibility in formatting and display for different contexts.


## Variables and Data Types

In Python, **variables** are used to store data, which can be used and manipulated throughout a program. **Data types** specify the kind of value a variable holds, determining what operations can be performed on it. Python automatically assigns a data type based on the value assigned to a variable.

### Python Variables
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

### Python Data Types
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

### Example Program Demonstrating Python Data Types

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

Arithmetic operators take precedence over logical operators. Python will always evaluate the arithmetic operators first (** is highest, then multiplication/division, then addition/subtraction). Next comes the relational operators. Finally, the logical operators are done last. This means that the expression x*5 >= 10 and y-6 <= 20 will be evaluated so as to first perform the arithmetic and then check the relationships. The and will be done last. Many programmers might place parentheses around the two relational expressions, (x*5 >= 10) and (y-6 <= 20). It is not necessary to do so, but causes no harm and may make it easier for people to read and understand the code.
The following table summarizes the operator precedence from highest to lowest. A complete table for the entire language can be found in the Python Documentation.  http://docs.python.org/py3k/reference/expressions.html#expression-lists

| Level	| Category	| Operators |
| :--: | :--: | :--: |
| 7 *(high)*	| exponent	| ** |
| 6	| multiplication |	*,/,//,% |
| 5	| addition	| +,- |
| 4	| relational	| ==,!=,<=,>=,>,< |
| 3	| logical	| not |
| 2	| logical	| and |
| 1 *(low)*	|logical |	or |


## Modules and Packages



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

```
_______________________________________________
string1 = |  P  |  O  |  T  |  A  |  T  |  O  |

index #   0     1     2     3     4     5     6
_______________________________________________
```



## File Handling


## Object-Oriented Programming


## Exception Handling


## Lambda Functions


## Data Structures
