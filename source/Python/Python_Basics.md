# Python Basics

We will be looking at syntax and structures of Python. We will use an Integrated Development Environment to develop our code in this course.  

## Print Statements


## Comments


## Variables


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


## Python Loops

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

## Lists

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




