# Algorithms & Programming






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
