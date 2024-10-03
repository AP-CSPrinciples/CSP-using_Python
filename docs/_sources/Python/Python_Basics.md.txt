# Python Basics

Python is an open-source programming language that is one of the easiest programs that a person can learn for their first programming language.  Python is a versatile programming language that can be used in many areas such as data analysis, science, web development, AI, and IoT.  As of 2024, it is one of the most in demand programming languages in the market place.  Python is a high-level programming language that offers simplicity, readability, and versatility.  Python supports multiple programming paradigms and has an extensive library that simplifies coding tasks. Python has a robust community and documentation support that enables beginners to excel quickly in this language.   

We will be looking at syntax and structures of Python. We will use an Integrated Development Environment to develop our code in this course.  


## Python Style Guidelines


## Print Statements


## Variables and Data Types


### Order of Operation

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



## Python Turtle Methods


## File Handling


## Object-Oriented Programming


## Exception Handling


## Lambda Functions


## Pygame
Pygame is a free and open-source Python library used for creating 2D video games. It provides modules to handle graphics, sound, user input, and more.

### Why Pygame instead of Turtle?

Pygame is commonly used to create AP CSP performance tasks. Pygame allows you to add features like images, sound, and animations, making your project more interactive and polished. By using Pygame, your project will have better graphics and functionality, allowing you to showcase your creativity to your potential.

## Pygame Installation
Official Pygame Installation Guide:
[https://www.pygame.org/wiki/GettingStarted]

- If theres any trouble, there are many youtube tutorials on Pygame Installation.
- If theres still trouble, consider asking ChatGPT or Mr.Virak for help. 

## Pygame Basics

### Before you Start

This command must be called whenever you want to put something on the screen.

```python

window.blit(bg, (0,0))

#window is the main Pygame Window 
#bg is an object to be rendered
# (0,0) are the (x,y) coordinates

```

 However, in order to actually render the object on the screen:

```python

pygame.display.update()

```
**Tip**: This command should always be present in the end of the Pygame Main Loop

## Pygame Window

Pygame has the ability to create a window. This window will contain all the visual graphics of your game.

```python

height = 500
length = 500

window = pygame.display.set_mode((length, height))
pygame.display.set_caption("Example Game")

```

This Code will create a window 500 pixel by 500 pixel black screen with the title of "Example Game".

#### Pygame Window Customization

You may also set the background to a certain image or color. 

```python

bg = pygame.transform.smoothscale(pygame.image.load("bg.jpeg"), (length, height))

#pygame.transform.smoothscale() will scale any image to any size
#pygame.image.load("bg.jpeg") will load the bg.jpeg
#(length, height) will the the target size of the image

```
**Tip**: Pygame can load many image types. However, jpeg and png work the best.

**Debugging**: Make sure that the image you're trying to load is in the same folder as the code. 
**Debugging**: Don't forget to blit the object!

Pygame uses a large while True loop in order to keep the game running. Below is an example of such loop:

```python
# PyGame Main Loop

keepGameRunning = True

while keepGameRunning:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          state.keepGameRunning = False

      pygame.display.update()
```
pygame has many prebuilt events, (such as button pressing) and this loop, in order to not be an infinite loop, checks if the user has clicked on the red X on the top left of the Pygame Window.

## Data Structures
