# Algorithms & Programming

## Functions/ Methods/ Procedures

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


## Objects/ Classes

Here is a program that demonstrates the use of objects and classes to represent dogs. It includes constructors with no arguments, one argument, and two arguments.

```python
class Dog:
    def __init__(self, name=None, breed=None):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

    def display_info(self):
        if self.name and self.breed:
            return f"This is {self.name}, a {self.breed} dog."
        elif self.name:
            return f"This is {self.name}."
        elif self.breed:
            return f"This is a {self.breed} dog."
        else:
            return "This is a dog."


# Creating an instance of Dog with no arguments
dog1 = Dog()
print(dog1.display_info())  # Output: This is a dog.

# Creating an instance of Dog with one argument
dog2 = Dog("Buddy")
print(dog2.display_info())  # Output: This is Buddy.

# Creating an instance of Dog with two arguments
dog3 = Dog("Max", "Labrador")
print(dog3.display_info())  # Output: This is Max, a Labrador dog.

# Accessing methods of the Dog class
print(dog3.bark())  # Output: Woof!
```

Explanation:

- We define a class `Dog` with a constructor `__init__` which initializes the attributes `name` and `breed`. The constructor can take 0, 1, or 2 arguments.
- The `bark` method returns a string representing the sound a dog makes.
- The `display_info` method displays information about the dog based on its attributes.
- We create instances of the `Dog` class with different combinations of arguments to demonstrate the constructors with no arguments, one argument, and two arguments.
- Finally, we access methods of the `Dog` class using the created instances.



## Methods

In Python, **methods** are functions that belong to objects and are used to operate on those objects. They are similar to functions but have a special relationship with the object they belong to, known as the **instance**.

Let's break down the key concepts:

### 1. **Method vs. Function**
   - A **function** is a block of code that performs a specific task and can exist independently of any object. For example, `print()` and `len()` are functions.
   - A **method**, on the other hand, is a function that is associated with an object. It is called on an object and can access the object’s internal data. For instance, `str.upper()` is a method called on a string object to return an uppercase version of that string.

### 2. **Instance Methods**
   - Most methods are called **instance methods** because they operate on an instance of a class (an object created from a class).
   - When an instance method is defined, the first parameter is usually `self`, which represents the instance of the class on which the method is called. This `self` parameter allows the method to access other attributes and methods of the same object.
   
   ```python
   class Dog:
       def __init__(self, name):
           self.name = name
       
       def bark(self):   # Instance method
           print(f"{self.name} says Woof!")
   
   my_dog = Dog("Buddy")
   my_dog.bark()  # Output: "Buddy says Woof!"
   ```
   In this example, `bark()` is an instance method that uses `self` to access the `name` attribute of the `my_dog` instance.

### 3. **Class Methods**
   - **Class methods** are methods that operate on the class itself rather than on individual instances. They are marked with the `@classmethod` decorator.
   - Instead of `self`, they take `cls` as their first parameter, which refers to the class itself, not an instance.
   
   ```python
   class Dog:
       species = "Canis familiaris"
       
       @classmethod
       def get_species(cls):
           return cls.species
   
   print(Dog.get_species())  # Output: "Canis familiaris"
   ```
   Here, `get_species()` is a class method that accesses the `species` attribute defined on the class itself.

### 4. **Static Methods**
   - **Static methods** are methods that don’t operate on an instance or class. They behave like normal functions but reside within a class for organizational purposes.
   - Static methods are marked with the `@staticmethod` decorator and don’t require `self` or `cls` parameters.
   
   ```python
   class MathHelper:
       @staticmethod
       def add(a, b):
           return a + b
   
   print(MathHelper.add(5, 7))  # Output: 12
   ```
   `add()` is a static method and does not rely on any data from an instance or the class. It simply performs a task.

### 5. **Special Methods (Magic Methods)**
   - Special methods, also known as **magic methods** or **dunder methods** (short for "double underscore"), allow instances of classes to interact with built-in Python operations in unique ways.
   - These methods have names starting and ending with double underscores (e.g., `__init__`, `__str__`, `__len__`).
   
   ```python
   class Book:
       def __init__(self, title, author):
           self.title = title
           self.author = author
       
       def __str__(self):
           return f"{self.title} by {self.author}"
   
   my_book = Book("1984", "George Orwell")
   print(my_book)  # Output: "1984 by George Orwell"
   ```
   The `__str__()` method is a magic method that defines how an object should be represented as a string.

### 6. **Method Chaining**
   - **Method chaining** allows you to call multiple methods on the same object in a single statement. To enable this, each method must return the object itself.
   
   ```python
   class TextEditor:
       def __init__(self, text=""):
           self.text = text
       
       def add_text(self, text):
           self.text += text
           return self
       
       def make_uppercase(self):
           self.text = self.text.upper()
           return self
   
   editor = TextEditor().add_text("Hello ").add_text("World!").make_uppercase()
   print(editor.text)  # Output: "HELLO WORLD!"
   ```
   Here, `add_text` and `make_uppercase` return `self`, so you can chain the methods together.

### Key Points to Remember
- **Instance Methods**: Operate on individual objects and use `self`.
- **Class Methods**: Operate on the class itself and use `cls`.
- **Static Methods**: Do not operate on instances or the class; they're independent but grouped within the class.
- **Special Methods**: Have specific purposes within Python's syntax (e.g., `__init__` for initialization, `__str__` for string representation).

Methods make object-oriented programming in Python powerful, allowing objects to encapsulate both data and functionality.




## Pythod Turtle Graphic Methods

Here's a comprehensive list of Python's Turtle Graphics module methods, divided into categories for easier reference. These methods are often used to control the turtle's movements, set its appearance, draw shapes, and control the window. This list includes methods available up to Python 3.10.

### 1. **Turtle Motion and Positioning**

| Method | Description |
|--------|-------------|
| `forward(distance)` or `fd(distance)` | Move the turtle forward by the specified distance. |
| `backward(distance)` or `bk(distance)` or `back(distance)` | Move the turtle backward by the specified distance. |
| `right(angle)` or `rt(angle)` | Turn the turtle clockwise by the specified angle. |
| `left(angle)` or `lt(angle)` | Turn the turtle counterclockwise by the specified angle. |
| `goto(x, y)` or `setpos(x, y)` or `setposition(x, y)` | Move the turtle to the specified coordinates. |
| `setx(x)` | Set the turtle’s x-coordinate. |
| `sety(y)` | Set the turtle’s y-coordinate. |
| `setheading(angle)` or `seth(angle)` | Set the turtle’s heading to the specified angle. |
| `home()` | Move the turtle to the origin (0, 0) and set its heading to 0 degrees. |
| `circle(radius, extent=None, steps=None)` | Draw a circle with the specified radius. Optional extent to draw only part of the circle, and steps for polygon approximation. |
| `dot(size=None, color=None)` | Draw a dot with the specified size and color. |
| `stamp()` | Stamp a copy of the turtle shape onto the canvas and return its stamp ID. |
| `clearstamp(stampid)` | Delete a specific stamp by its ID. |
| `clearstamps(n=None)` | Delete all stamps or the last `n` stamps if `n` is provided. |
| `undo()` | Undo the last turtle action. |
| `speed(speed)` | Set the turtle’s speed. `0` means no animation, `1` is slow, `10` is fast. |

### 2. **Turtle State and Status**

| Method | Description |
|--------|-------------|
| `position()` or `pos()` | Return the current position as a tuple `(x, y)`. |
| `towards(x, y)` | Return the angle towards the specified point. |
| `xcor()` | Return the turtle’s x-coordinate. |
| `ycor()` | Return the turtle’s y-coordinate. |
| `heading()` | Return the turtle’s current heading angle. |
| `distance(x, y)` | Return the distance from the turtle’s position to the specified point. |
| `isdown()` | Return `True` if the pen is down, `False` otherwise. |
| `isvisible()` | Return `True` if the turtle is visible, `False` otherwise. |

### 3. **Turtle Pen Control**

| Method | Description |
|--------|-------------|
| `pendown()` or `pd()` or `down()` | Lower the pen to draw when the turtle moves. |
| `penup()` or `pu()` or `up()` | Raise the pen to prevent drawing when the turtle moves. |
| `pensize(width)` or `width(width)` | Set the width of the pen. |
| `pen(pen=None, **pendict)` | Return or set the pen’s attributes (color, width, etc.). |
| `pen(pencolor, fillcolor)` | Set both pen color and fill color. |
| `pencolor(color)` | Set the pen color. |
| `fillcolor(color)` | Set the fill color. |
| `begin_fill()` | Start filling a shape. |
| `end_fill()` | Fill the shape drawn after `begin_fill()` is called. |
| `color(pencolor, fillcolor)` | Set both the pen and fill color. |
| `reset()` | Reset the turtle’s state, clearing the drawing and resetting attributes. |
| `clear()` | Clear the drawing without changing the turtle’s position. |
| `write(arg, move=False, align='left', font=('Arial', 8, 'normal'))` | Write text at the turtle's current position. |

### 4. **Turtle Appearance**

| Method | Description |
|--------|-------------|
| `shape(name)` | Set the turtle’s shape (`'arrow'`, `'turtle'`, `'circle'`, `'square'`, `'triangle'`, `'classic'`). |
| `shapesize(stretch_wid=None, stretch_len=None, outline=None)` or `turtlesize(...)` | Stretch the turtle’s shape. |
| `shearfactor(factor)` | Set or get the shear factor for the turtle's shape. |
| `tilt(angle)` | Tilt the turtle shape by the specified angle. |
| `tiltangle(angle=None)` | Set or get the tilt angle of the turtle shape. |
| `get_shapepoly()` | Return the current shape as a polygon. |
| `showturtle()` or `st()` | Make the turtle visible. |
| `hideturtle()` or `ht()` | Make the turtle invisible. |
| `resizemode(rmode)` | Set the resize mode (`'auto'`, `'user'`, `'noresize'`). |

### 5. **Screen Control and Events**

| Method | Description |
|--------|-------------|
| `Screen()` | Return the Screen object used for window control. |
| `bye()` | Close the Turtle Graphics window. |
| `bgcolor(color)` | Set or get the background color. |
| `bgpic(picname)` | Set or get the background image. |
| `title(title)` | Set the title of the window. |
| `clearscreen()` | Clear the screen. |
| `onclick(fun, btn=1, add=None)` | Bind a function to a mouse click. |
| `onkey(fun, key)` | Bind a function to a key press. |
| `listen()` | Set focus on the screen to capture key presses. |
| `mainloop()` | Start the main event loop. |
| `tracer(n=None, delay=None)` | Set the screen update delay to control animation speed. |
| `update()` | Force an update of the screen. |

### 6. **Miscellaneous**

| Method | Description |
|--------|-------------|
| `begin_poly()` | Start recording the vertices of a polygon. |
| `end_poly()` | Stop recording and store the polygon shape. |
| `get_poly()` | Return the recorded polygon. |
| `delay(delay=None)` | Set the delay value for screen updates. |
| `window_width()` | Return the width of the turtle window. |
| `window_height()` | Return the height of the turtle window. |
| `getcanvas()` | Return the Canvas object of the turtle window. |
| `getscreen()` | Return the TurtleScreen object. |

### Additional Notes

- **`Screen()` Object Methods**: The `Screen` object returned by `turtle.Screen()` has many methods for window and event control, such as `bgcolor`, `title`, `onkey`, `onscreenclick`, and `listen`.
- **Aliases**: Many methods have shorthand aliases (e.g., `fd` for `forward`, `bk` for `backward`).
  
This list provides a solid foundation for creating various Turtle Graphics applications in Python.


## Compound Boolean Expressions

Certainly! Here are some examples of compound Boolean expressions along with explanations for each:

### 1. Using **AND** (`&&` or `and` in Python)
   ```python
   age = 25
   has_license = True
   is_eligible = age >= 18 and has_license
   ```
   **Explanation**: Here, `is_eligible` will be `True` only if both conditions are `True`. In this case, `age >= 18` and `has_license` both need to be `True` for `is_eligible` to be `True`. If `age` is less than 18 or `has_license` is `False`, `is_eligible` will be `False`.

### 2. Using **OR** (`||` or `or` in Python)
   ```python
   temperature = 35
   raining = False
   go_for_walk = temperature >= 20 or raining
   ```
   **Explanation**: The variable `go_for_walk` will be `True` if either `temperature >= 20` or `raining` is `True`. With `OR`, only one of the conditions needs to be `True` for the overall expression to evaluate as `True`.

### 3. Combining **AND** and **OR**
   ```python
   is_weekend = True
   has_free_time = False
   is_tired = False
   can_go_hiking = is_weekend and (has_free_time or not is_tired)
   ```
   **Explanation**: In this case, `can_go_hiking` is `True` if it is the weekend (`is_weekend` is `True`) **and** either there is free time (`has_free_time`) **or** the person is not tired (`not is_tired`). This example shows how parentheses can group parts of a compound Boolean expression to control evaluation order.

### 4. Using **NOT** (`!` or `not` in Python)
   ```python
   is_student = False
   has_discount = not is_student
   ```
   **Explanation**: The expression `not is_student` reverses the Boolean value of `is_student`. If `is_student` is `False`, `has_discount` will be `True`. The **NOT** operator is useful for negating a condition.

### 5. Complex Condition with **Multiple AND/OR/NOT**
   ```python
   age = 30
   is_member = True
   has_discount_coupon = False
   gets_discount = (age > 25 or is_member) and not has_discount_coupon
   ```
   **Explanation**: This expression checks if someone can get a discount. They qualify if they are older than 25 or are a member, but they should not have a discount coupon already. The expression `(age > 25 or is_member)` will evaluate first, and then `not has_discount_coupon` will apply, which must be `True` for `gets_discount` to be `True`.

### 6. Nested Compound Boolean Expression
   ```python
   score = 80
   attendance = 90
   has_passed = (score >= 70 and attendance >= 80) or (score >= 60 and attendance >= 90)
   ```
   **Explanation**: Here, `has_passed` will be `True` if either of these conditions is met:
   - The score is at least 70 and attendance is at least 80.
   - The score is at least 60 and attendance is at least 90.
   
   This kind of expression is useful when there are multiple pathways to meet a requirement.


## Dictionary


Here's a Python program that demonstrates how to create, use, add, remove, and modify items in a dictionary. It also explains the differences and similarities between dictionaries and sets.

```python
# Python program demonstrating dictionary operations

# Creating a dictionary with 15 items
student_scores = {
    "Alice": 85,
    "Bob": 78,
    "Catherine": 92,
    "David": 88,
    "Eva": 90,
    "Frank": 76,
    "Grace": 89,
    "Hank": 93,
    "Ivy": 82,
    "John": 79,
    "Kara": 95,
    "Liam": 91,
    "Mona": 87,
    "Nathan": 84,
    "Olivia": 94
}

print("Initial Dictionary:", student_scores)

# Accessing values in a dictionary
# Accessing the score of 'Alice'
print("Alice's score:", student_scores["Alice"])

# Adding an item to the dictionary
student_scores["Paul"] = 88
print("\nAfter Adding Paul's score:", student_scores)

# Modifying an item in the dictionary
student_scores["Alice"] = 90
print("\nAfter Modifying Alice's score:", student_scores)

# Removing an item from the dictionary
del student_scores["Frank"]
print("\nAfter Removing Frank's score:", student_scores)

# Checking if a key exists in the dictionary
if "Eva" in student_scores:
    print("\nEva's score exists in the dictionary.")

# Looping through dictionary items
print("\nListing all students and their scores:")
for student, score in student_scores.items():
    print(f"{student}: {score}")

# Dictionary methods
# Getting a list of keys
keys = list(student_scores.keys())
print("\nAll Student Names:", keys)

# Getting a list of values
values = list(student_scores.values())
print("All Scores:", values)

# Using the get() method with a default value
score = student_scores.get("Zara", "Score not found")
print("\nScore for Zara (not in dictionary):", score)

# Clearing the dictionary
student_scores.clear()
print("\nDictionary after clearing all items:", student_scores)

# Differences and Similarities Between Dictionary and Set

# Dictionary - Stores key-value pairs
# Set - Stores unique values, no key-value pairs

# Example of a set
unique_scores = {85, 78, 92, 88, 90, 76, 89, 93, 82, 79, 95, 91, 87, 84, 94}

print("\nExample Set of Unique Scores:", unique_scores)

# Similarity: Both dictionaries and sets are mutable
# Difference: A set only stores unique values, whereas a dictionary has key-value pairs

# Attempting to add duplicate items in a set (will have no effect)
unique_scores.add(85)  # Already in the set
print("\nAfter Attempting to Add Duplicate in Set:", unique_scores)

# Summary of Differences:
# 1. Dictionaries have key-value pairs; sets contain only unique values.
# 2. Dictionaries allow lookup by key; sets do not have keys.
# 3. Sets automatically ignore duplicates; dictionaries handle duplicates by updating the value for a given key.
```

### Explanation

1. **Creating the Dictionary**: The `student_scores` dictionary has 15 items, where each student's name is the key, and their score is the value.

2. **Accessing Values**: We can access values using a key. For instance, `student_scores["Alice"]` retrieves Alice's score.

3. **Adding an Item**: You can add a new key-value pair by assigning a value to a new key, as shown with `"Paul": 88`.

4. **Modifying an Item**: Modify the value for an existing key, as shown with `"Alice": 90`.

5. **Removing an Item**: Use the `del` statement to remove a key-value pair, as shown with `del student_scores["Frank"]`.

6. **Checking if a Key Exists**: The `in` keyword checks if a key is in the dictionary.

7. **Looping Through Items**: Use `.items()` to loop through keys and values.

8. **Dictionary Methods**: 
   - `.keys()` to get all keys.
   - `.values()` to get all values.
   - `.get()` for safe value retrieval with a default fallback.

9. **Clearing the Dictionary**: `.clear()` removes all items from the dictionary.

### Dictionary vs. Set

- **Dictionary**: Stores key-value pairs, allows retrieval by key, and handles duplicates by overwriting values for duplicate keys.
- **Set**: Stores only unique values, ignores duplicates, and doesn’t use key-value pairs.

This code provides a complete introduction to dictionaries with additional details on how dictionaries differ from sets.


Sure! Below is a Python 3 program that demonstrates the use of objects, classes, and constructors, along with explanations for each part.

### Program: A Simple Bank Account System

```python
class BankAccount:
    """A class representing a bank account."""
    
    def __init__(self, account_holder, balance=0):
        """
        Constructor to initialize the account holder's name and balance.
        
        Args:
            account_holder (str): The name of the account holder.
            balance (float): The initial balance of the account (default is 0).
        """
        self.account_holder = account_holder  # Instance variable for account holder's name
        self.balance = balance  # Instance variable for account balance

    def deposit(self, amount):
        """
        Deposit money into the bank account.
        
        Args:
            amount (float): The amount to be deposited.
        """
        if amount > 0:
            self.balance += amount  # Increase balance by the deposit amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """
        Withdraw money from the bank account.
        
        Args:
            amount (float): The amount to be withdrawn.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount  # Decrease balance by the withdrawal amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount!")

    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance

    def display_account_info(self):
        """Display the account holder's information and current balance."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

# Main program
if __name__ == "__main__":
    # Create an instance of BankAccount
    account1 = BankAccount("Alice Smith", 1000)

    # Display account information
    account1.display_account_info()

    # Perform some transactions
    account1.deposit(500)
    account1.withdraw(200)
    account1.withdraw(1500)  # This should fail
    account1.display_account_info()
```

### Explanation

1. **Class**:
   - `class BankAccount:` defines a class named `BankAccount`. A class is a blueprint for creating objects, encapsulating data and methods that operate on that data.

2. **Constructor**:
   - The `__init__` method is a special method called the constructor. It is invoked when an object of the class is created. In this example, it initializes the account holder's name and balance:
     - `account_holder`: A string representing the name of the account holder.
     - `balance`: A float representing the initial balance of the account (default is 0).

3. **Instance Variables**:
   - `self.account_holder` and `self.balance` are instance variables that store the account holder's name and balance for each instance of the `BankAccount` class.

4. **Methods**:
   - `deposit(amount)`: This method adds a specified amount to the account balance, ensuring the amount is positive.
   - `withdraw(amount)`: This method subtracts a specified amount from the balance, ensuring the withdrawal does not exceed the current balance.
   - `get_balance()`: Returns the current balance of the account.
   - `display_account_info()`: Displays the account holder's information and current balance.

5. **Objects**:
   - `account1 = BankAccount("Alice Smith", 1000)`: This line creates an instance (object) of the `BankAccount` class with "Alice Smith" as the account holder and an initial balance of $1000.

6. **Main Program**:
   - The main program creates an account, displays account information, performs deposits and withdrawals, and handles invalid transactions gracefully.

### Running the Program
You can copy and paste this code into a Python environment. It will create a bank account for "Alice Smith," allowing you to see how deposits and withdrawals affect the balance.


## Nested Conditionals using Functions with parameters

Sure! Below is a Python 3 program that demonstrates nested conditionals using functions with arguments. The program will classify a given number based on its value and check if it’s even or odd, using nested conditionals within functions.

### Program: Number Classification

```python
def classify_number(num):
    """Classify the number as positive, negative, or zero."""
    if num > 0:
        classification = "positive"
    elif num < 0:
        classification = "negative"
    else:
        classification = "zero"
    
    return classification

def is_even_or_odd(num):
    """Determine if the number is even or odd."""
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def analyze_number(num):
    """Analyze the number and print its classification and parity."""
    classification = classify_number(num)
    
    if classification == "positive":
        print(f"{num} is {classification} and {is_even_or_odd(num)}.")
    elif classification == "negative":
        print(f"{num} is {classification} and {is_even_or_odd(num)}.")
    else:  # classification == "zero"
        print(f"{num} is {classification}.")

# Main program
if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))
        analyze_number(user_input)
    except ValueError:
        print("Please enter a valid integer.")
```

### Explanation

1. **Functions**:
   - `classify_number(num)`: Classifies the number as positive, negative, or zero.
   - `is_even_or_odd(num)`: Determines if the number is even or odd.
   - `analyze_number(num)`: Calls the classification and parity functions, and prints the results.

2. **Nested Conditionals**:
   - Inside `analyze_number`, we use nested conditionals to determine how to print the result based on the classification of the number.

3. **Main Program**:
   - Prompts the user for input, converts it to an integer, and analyzes the number. It also handles invalid input gracefully.

### Running the Program
To run the program, just copy and paste the code into a Python environment, and it will prompt you to enter a number for analysis.


## Conditions with nested iteration and loops

Certainly! In Python, conditional statements can take various forms, often used with loops, nested iterations, and more. 
Below are examples of different variations of using conditional statements along with input, nested iterations, and 
nested-nested iterations.

### Basic Conditional Statements

```python
# Basic conditional example
x = int(input("Enter a number: "))

if x > 0:
    print("The number is positive.")
elif x < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

### Conditional Statements with Loops

#### Simple Loop with Conditional

```python
# Using a loop with conditional
numbers = [1, -1, 0, 3, -5]

for num in numbers:
    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    else:
        print(f"{num} is zero.")
```

#### Nested Loop with Conditional

```python
# Nested iteration with conditional
matrix = [
    [1, 2, -1],
    [-2, 3, 0],
    [0, -3, 4]
]

for row in matrix:
    for value in row:
        if value > 0:
            print(f"{value} is positive.")
        elif value < 0:
            print(f"{value} is negative.")
        else:
            print(f"{value} is zero.")
```

### Nested-Nested Iterations with Conditionals

```python
# Nested-nested iteration with conditionals
nested_list = [
    [
        [1, -1],
        [2, 0]
    ],
    [
        [-2, 3],
        [0, 4]
    ]
]

for sublist in nested_list:
    for row in sublist:
        for value in row:
            if value > 0:
                print(f"{value} is positive.")
            elif value < 0:
                print(f"{value} is negative.")
            else:
                print(f"{value} is zero.")
```

### Conditional Statements with Input Inside Loops

```python
# Input inside a loop with conditionals
num_count = int(input("How many numbers do you want to check? "))
for _ in range(num_count):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
```

### Combining Conditionals with List Comprehensions

```python
# Using conditionals in a list comprehension
numbers = [1, 2, 3, -1, -2, 0]
classification = ["positive" if n > 0 else "negative" if n < 0 else "zero" for n in numbers]

print(classification)  # Output: ['positive', 'positive', 'positive', 'negative', 'negative', 'zero']
```

### Summary

- **Basic Conditional Statements**: Use `if`, `elif`, and `else` to handle multiple conditions.
- **Loops with Conditionals**: Iterate over collections and apply conditionals to each item.
- **Nested Iterations**: Implement loops within loops for multi-dimensional data.
- **Nested-Nested Iterations**: Further nest loops for deeper structures, applying conditionals accordingly.
- **Input Inside Loops**: Collect user input repeatedly and use conditionals to process each entry.
- **List Comprehensions**: Efficiently apply conditionals within a single line to transform data.

These examples illustrate how to leverage conditionals effectively in Python programming, especially when dealing 
with various data structures and iterations.


## Activity X.X

## Coding Exercise
You will create a rock, paper, scissors, lizard, Spock game to play against a computer using static methods. 
First, you'll ask the user to pick rock, paper, scissors lizard or Spock.
You will have the computer randomly choose one of the options. 
You will use the Randomizer class to help the computer make a choice.
Print the winner of each round and increment the wins, losses, and ties as you play the game.  
You may either choose a specific number of rounds to play or keep playing the game until the user enters quit.

#### Randomizer Class
- `public static int nextInt()`: returns a random integer from 1-10
- `public static int nextInt(int min, int max)`: returns a random integer from min-max
- HINT: Remember that we can get random integers using the formula `int randInteger = (int)(Math.random() * (range + 1) + startingNum)`.

#### RPS Class
- create static variables `userWins, compWins,` and `ties`
- create static method `getWinner(String user, String computer)` that determines whether the user or computer won the game, and return the correct winner! Should also update the win totals.
- create static getters

#### Main Class
- create a static method `getCompChoice()` that returns the computer's choice depending upon a random integer.
- ask user to make a choice. have computer get a choice. print the choices and results. repeat until user quits.

## Sample Output
```java
Enter the number of rounds that you would like to play: 
7
Enter your choice (rock, paper,  scissors, lizard or Spock):
rock
User: rock
Computer: scissors
User wins!
Record User-Comp-Tie: 1-0-0

Enter your choice (rock, paper,  scissors, lizard or Spock):
paper
User: paper
Computer: paper
Tie
Record User-Comp-Tie: 1-0-1

Enter your choice (rock, paper,  scissors, lizard or Spock):
scissors
User: scissors
Computer: scissors
Tie
Record User-Comp-Tie: 1-0-2

Enter your choice (rock, paper,  scissors, lizard or Spock):
paper
User: paper
Computer: rock
User wins!
Record User-Comp-Tie: 2-0-2

Enter your choice (rock, paper,  scissors, lizard or Spock):
rock
User: rock
Computer: paper
Computer wins!
Record User-Comp-Tie: 2-1-2

Enter your choice (rock, paper,  scissors, lizard or Spock):
rock
User: rock
Computer: paper
Computer wins!
Record User-Comp-Tie: 2-2-2

Enter your choice (rock, paper,  scissors, lizard or Spock):
rock
User: rock
Computer: paper
Computer wins!
Record User-Comp-Tie: 2-3-2

Computer wins, Thanks for playing!
```
