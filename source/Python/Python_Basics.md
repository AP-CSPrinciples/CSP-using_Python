# Python Basics
```Revised June 2026```

Python is an open-source, high-level programming language that is widely considered one of the best first languages to learn. It supports multiple programming paradigms — including **procedural**, **functional**, and **object-oriented programming (OOP)** — and is backed by an enormous standard library and community. As of 2024, it is one of the most in-demand languages in the job market, used in web development, data science, artificial intelligence, IoT, and cybersecurity.

This course is designed to prepare you for:
- 🎯 **AP Computer Science Principles (AP CSP)** — College Board performance task and exam
- 🏅 **PCEP™ – Certified Entry-Level Python Programmer** (Exam PCEP-30-02, OpenEDG Python Institute)

> **How to use this document:** Topics are organized to build skills progressively. PCEP exam objectives are labeled `🔖 PCEP` and AP CSP standards are labeled `📋 AP CSP`. Activities and projects are marked with `###`.

---

## 📅 Python Pacing Guide

`Aug 17 – Dec 18, 2026`

| Week | Dates | Content Focus | Notebook Spread | Activities / Projects | PT / CPT In-Class Time | Weekly Min |
|:---:|:---:|:---|:---:|:---|:---:|:---:|
| 1 | Aug 17–21 | How Python Works; Style; Debugging; Variables & Data Types | Spreads 1 & 2 | — | — | 216 |
| 2 | Aug 24–28 | Variables (cont.); Operators; Numeral Systems | Spread 3 | Movie Ticket Eligibility Checker | — | 216 |
| 3 | Aug 31–Sep 4 | Print Statements & Input/Output | Spread 4 | Hello, World! Variations | — | 216 |
| 4 | Sep 7–11 | Conditional Statements | Spread 5 | Grade Calculator | — | 216 |
| 5 | Sep 14–18 | Loops | Spread 6 | Nested Loop Pattern Design Studio | — | 216 |
| 6 | Sep 21–25 | Strings | Spread 7 | Receipt Formatter | — | 216 |
| 7 | Sep 28–Oct 2 | Lists | Spread 8 | — | — | 216 |
| 8 | Oct 5–9 | Tuples & Dictionaries; **Practice PT 1 Introduced** | Spread 9 | Student Contact Book | 40 min (Fri) *Practice* | 216 |
| 9 | Oct 12–16 | Functions; Practice PT 1 in-class work | Spread 10 | Math Operations Calculator; Recursion Practice — Three Levels | 176 min (2×88) *Practice* | 216 |
| 10 | Oct 19–23 | Functions (cont.); Modules and Packages; Practice PT 1 in-class work | — | **Project:** Random Trivia Quiz Generator | 176 min (2×88) *Practice* | 216 |
| 11 | Oct 26–30 | Exception Handling; **Practice PT 1 Due (Fri)** | Spread 11 | Safe Calculator | 88 min (1×88) *Practice* | 216 |
| 12 | Nov 2–6 | Data Structures Deep Dive; **Practice PT 2 Introduced** | Spread 12 | — | 176 min (2×88) *Practice* | 216 |
| 13 | Nov 9–13 | OOP | Spread 13 | OOP Zoo (3 options) | 128 min (88+40) *Practice* | 216 |
| 14 | Nov 16–20 | **PCEP Exam Prep; Certification Review** (Mon/Wed); **Practice PT 2 Due (Fri)** | — | — | 40 min (Fri) *Practice* | 216 |
| 15 | Nov 23–27 | **THANKSGIVING — No School** | — | — | — | — |
| 16 | Nov 30–Dec 4 | AP CSP CPT — Brainstorming Workshop | Spread 15 | CPT Brainstorming: students develop an **original** program idea | 216 min **Official CPT** | 216 |
| 17 | Dec 7–11 | AP CSP CPT — Writing Code, Recording Video, Developing PPR Responses | — | Official CPT Program (original idea, in progress) | 216 min **Official CPT** | 216 |
| 18 | Dec 14–18 | AP CSP CPT — Final Coding/Submission; **CPT Due (Fri, Dec 18)**; End-of-Course Reflection | Spread 16 | Official CPT Program (original idea, due) | 216 min **Official CPT** | 216 |

> **Practice PT 1 & 2** are formative — students write a full program to an actual College Board–style CPT prompt so they've rehearsed the task before the real one, but this time is **not counted** toward the AP CPT's official minimum. Practice PT 1 total ≈ 480 min (Weeks 8–11). Practice PT 2 total ≈ 344 min (Weeks 12–14).
>
> **Per AP College Board CPT requirements, the official CPT must be an original student idea.** Students may **not** submit Practice PT 1, Practice PT 2, or any other program they've already completed as their CPT — the program developed during Weeks 16–18 must be new. The Final Project Options (A/B/C) in the curriculum may still be offered as optional starting frameworks/scaffolds, but each student's actual CPT submission — the idea, the implementation, and the individual creative work behind it — must be their own original work developed within the official CPT window.
>
> **Official AP CSP CPT (the actual, submitted Create Performance Task) happens entirely in December**: Week 16 = brainstorming/planning an original idea, Week 17 = coding + video + PPR written responses, Week 18 = final coding, submission (due Fri, Dec 18), and course wrap-up — all three are full 5-day weeks.
> **Total Official CPT Time: 216 + 216 + 216 = 648 min (≈10.8 hrs) — clears the 9-hour College Board minimum with room to spare, entirely within December, even after setting aside time on the last day for End-of-Course Reflection.**


---


# Python Style Guidelines

<details><summary>📐 Click to expand PEP 8 Guidelines</summary>

[**PEP 8 Guidelines**](https://peps.python.org/pep-0008/) is the official style guide for Python code. Following these standards is required on all assignments and is tested on the PCEP exam.

`🔖 PCEP 1.2` — Python's logic and structure; indentation; PEP-8 recommendations
`🔖 PCEP 1.3` — Naming conventions; implementing PEP-8

**All *Projects* Must Include a Header Block:**

```python
#       Assignment:  Program [number]:  [Assignment Title]
#
#       Author:  [Your Name]
#       Partner:  [Partner's Name]
#
#       Course Name:  [Course Name]
#       Instructor:  [Instructor Name]
#       Due Date:  [Due Date and Time]
#
#       Description:  [Describe the program's goal, IN DETAIL.]
#
#       Language:  Python 3.x
#       Ex. Packages:  [List any external packages used]
#
#       Deficiencies:  [Known problems, or state there are none.]
```

---

**1. Use Descriptive Variable and Function Names**
- **Guideline**: Use `snake_case` names that clearly describe their purpose.
- **Example**:
  ```python
  # Good
  total_cost = price * quantity

  # Bad
  x = p * q
  ```

**2. Use Consistent Indentation (4 Spaces)**
- **Guideline**: Use four spaces per indentation level; do not use tabs.
- **Example**:
  ```python
  def calculate_area(radius):
      return 3.14 * radius ** 2
  ```

**3. Limit Line Length to 79 Characters**
- Improves readability on all devices and screen sizes.

**4. Use Blank Lines to Separate Code Sections**
- Two blank lines between top-level functions/classes; one blank line between class methods.

**5. Use Docstrings to Document Functions and Classes**
- **Example**:
  ```python
  def calculate_area(radius):
      """Calculate the area of a circle given its radius."""
      return 3.14 * radius ** 2
  ```

**6. Use Spaces Around Operators**
  ```python
  result = (a + b) * (c - d)   # Good
  result=(a+b)*(c-d)           # Bad
  ```

**7. Avoid Excessive Nesting** — break complex logic into smaller functions.

**8. Use List Comprehensions for Simple Operations**
  ```python
  squares = [x ** 2 for x in range(10)]  # Good
  ```

**9. Handle Exceptions Properly** — use specific exception types, never bare `except`.

**10. Use Meaningful Constants Instead of Magic Numbers**
  ```python
  TAX_RATE = 0.15
  total_cost = price * (1 + TAX_RATE)
  ```

**11. Avoid Global Variables** — use function parameters or class attributes.

**12. Use `is` for Comparison to `None`**
  ```python
  if value is None:    # Good
  if value == None:    # Bad
  ```

**13. Organize Imports Properly** — standard library → third-party → local modules.

**14. Use Type Annotations (Python 3.5+)**
  ```python
  def calculate_total(cost: float, tax_rate: float) -> float:
      return cost * (1 + tax_rate)
  ```

</details>

---

# Debugging Strategies

`📋 AP CSP: CRD-2.J` — Identify and correct errors in algorithms and programs.

**Types of Errors**

| Error Type | Description | Example |
|---|---|---|
| **Syntax Error** | Code violates Python grammar rules | Missing `:` after `if` |
| **Runtime Error** | Code crashes while running | Dividing by zero |
| **Logic Error** | Code runs but gives wrong output | Using `+` instead of `*` |

**Debugging Strategies**

1. **Read the Error Message Carefully** — find the exact line number, identify the error type.
2. **Trace the Program Step-by-Step** — walk through code line by line; track variable values.
3. **Use Print Statements** — insert `print("Value of score:", score)` to expose variable state.
4. **Test with Simple Inputs** — start with values where you know the expected output.
5. **Isolate the Problem** — comment out sections; test smaller pieces individually.
6. **Check Variables and Data Types** — confirm types with `type()`.
7. **Review Logic and Conditions** — check `if`, loop conditions, and operator use carefully.
8. **Rubber Duck Debugging** — explain the code out loud step-by-step; mistakes often surface.
9. **Use Incremental Development** — write and test small pieces before adding features.
10. **Take a Break and Revisit** — fresh eyes catch simple mistakes.
11. **Ask for Help with Evidence** — be ready to explain: *what it should do, what it does, what you tried*.

### Student Debugging Checklist

Before asking for help, confirm:

☐ Read the error message carefully

☐ Checked the exact line number and nearby code

☐ Added print/debug statements to trace variables

☐ Tested with simple, predictable inputs

☐ Traced variable values step-by-step

☐ Explained the code out loud (Rubber Duck Method)

---

# Section 1 — Computer Programming and Python Fundamentals
`🔖 PCEP Section 1 — 18% of exam (7 items)`
`📋 AP CSP: CRD-2.A, CRD-2.B`

## How Python Works

`🔖 PCEP 1.1` — Understand fundamental terms and definitions

Python is an **interpreted** language. Instead of being compiled into machine code before running, a Python **interpreter** reads and executes your source code line-by-line at runtime.

| Concept | Definition |
|---|---|
| **Source code** | The human-readable Python instructions you write |
| **Interpreter** | The program that reads and runs your Python code |
| **Compiler** | Translates entire source code to machine code before running (e.g., C, Java) |
| **Lexis** | The vocabulary of the language — valid words/tokens Python recognizes |
| **Syntax** | The grammar rules for how code must be structured |
| **Semantics** | The meaning of correctly written code |

> <mark>A **SyntaxError** means Python cannot understand your code structure. A **logic error** means Python understands it but does something you didn't intend.</mark>

## Python Keywords and Structure

`🔖 PCEP 1.2` — Understand Python's logic and structure

**Keywords** are reserved words that Python uses for specific purposes. You cannot use them as variable names.

```
False    None     True     and      as       assert
async    await    break    class    continue def
del      elif     else     except   finally  for
from     global   if       import   in       is
lambda   nonlocal not      or       pass     raise
return   try      while    with     yield
```

<mark>**Indentation** is not optional in Python — it defines code blocks. Incorrect indentation causes a `IndentationError`.</mark>

```python
# Correct indentation
if True:
    print("Indented correctly")   # 4 spaces

# Wrong
if True:
print("This will crash")          # IndentationError
```

**Comments** are notes for humans; Python ignores them:

```python
# This is a single-line comment
```

A **docstring** is a special string placed as the very first line inside a function, class, or module to document what it does. Unlike a `#` comment, Python actually stores a docstring as part of the object — it can be viewed later with `help()` or `.__doc__`.

```python
def area_of_rectangle(length, width):
    """Calculate and return the area of a rectangle."""
    return length * width

print(area_of_rectangle.__doc__)   # Calculate and return the area of a rectangle.
```

| | `#` comment | `"""docstring"""` |
|---|---|---|
| Purpose | Note for a human reading the code | Documentation for someone *using* the function |
| Location | Anywhere | Must be the first line inside a function/class/module |
| Stored by Python? | No — ignored by the interpreter | Yes — accessible via `.__doc__` or `help()` |

> <mark>**Rule of thumb:** a comment explains a line to a fellow programmer; a docstring is the instruction manual for someone who will never open the function's source code.</mark>

## Variables and Data Types

`🔖 PCEP 1.3` — Introduce literals and variables; numeral systems
`📋 AP CSP: DAT-1.A` — Explain how data can be represented using bits.

A **variable** is a named location in memory that stores a value. <mark>Python uses **dynamic typing** — the data type is inferred from the assigned value, not declared in advance.</mark>

```python
age = 25            # int
name = "Alice"      # str
price = 9.99        # float
is_student = True   # bool
result = None       # NoneType
```

**Core Data Types**

| Type | Keyword | Example | PCEP Focus |
|---|---|---|---|
| Integer | `int` | `age = 25` | ✅ |
| Float | `float` | `price = 9.99` | ✅ |
| String | `str` | `name = "Alice"` | ✅ |
| Boolean | `bool` | `is_valid = True` | ✅ |
| None | `NoneType` | `result = None` | ✅ |
| List | `list` | `colors = ["red", "blue"]` | ✅ |
| Tuple | `tuple` | `coords = (10, 20)` | ✅ |
| Dictionary | `dict` | `person = {"name": "Alice"}` | ✅ |

**Numeral Systems** — `🔖 PCEP 1.3`

Python supports writing integer literals in multiple bases:

```python
decimal     = 255        # base 10
binary      = 0b11111111 # base 2  → 255
octal       = 0o377      # base 8  → 255
hexadecimal = 0xFF       # base 16 → 255

print(binary, octal, hexadecimal)  # All print: 255 255 255
```

**Scientific Notation**

Python lets you write very large or very small numbers using `e` notation, where `e` means "times 10 to the power of." This is the same idea as scientific notation in math class (`1.5 × 10⁶`), just written on one line without exponents or superscripts.

- `1.5e6` means `1.5 × 10^6` → move the decimal point 6 places **right** → `1,500,000.0`
- `2.5e-4` means `2.5 × 10^-4` → move the decimal point 4 places **left** → `0.00025`

```python
big_num  = 1.5e6    # 1,500,000.0
tiny_num = 2.5e-4   # 0.00025
```

> <mark>Both `big_num` and `tiny_num` are stored as `float` type — `e` notation is just a *display/input shortcut*, not a separate data type.</mark>

**Type Casting** — converting between data types:

```python
x = int("42")        # str → int
y = float(7)         # int → float
z = str(3.14)        # float → str
b = bool(0)          # int → bool (0 = False, anything else = True)
```

> <mark>**Floating-point accuracy**: `0.1 + 0.2` does **not** equal exactly `0.3` in Python due to how floats are stored in binary. This is a known limitation tested on the PCEP exam.</mark>

```python
print(0.1 + 0.2)        # 0.30000000000000004
print(round(0.1 + 0.2, 2))  # 0.3
```

## Operators

`🔖 PCEP 1.4` — Choose operators and data types adequate to the problem
`📋 AP CSP: AAP-2.F` — Use mathematical operations in algorithms.

**Arithmetic Operators**

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `**` | Exponentiation | `2 ** 3` | `8` |
| `*` | Multiplication | `4 * 3` | `12` |
| `/` | Division (always float) | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Modulo (remainder) | `7 % 3` | `1` |
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |

**String Operators**

```python
"Hello" + " World"   # Concatenation → "Hello World"
"Ha" * 3             # Repetition → "HaHaHa"
```

**Assignment and Shortcut Operators**

```python
x = 10
x += 5   # x = x + 5 → 15
x -= 3   # x = x - 3 → 12
x *= 2   # x = x * 2 → 24
x //= 4  # x = x // 4 → 6
x **= 2  # x = x ** 2 → 36
```

**Operator Precedence (Highest → Lowest)**

| Level | Category | Operators |
|:---:|:---:|:---:|
| 7 *(high)* | Exponent | `**` |
| 6 | Multiplication | `*, /, //, %` |
| 5 | Addition | `+, -` |
| 4 | Relational | `==, !=, <=, >=, >, <` |
| 3 | Logical | `not` |
| 2 | Logical | `and` |
| 1 *(low)* | Logical | `or` |

> <mark>Parentheses `()` always override precedence — use them to make code intentions clear.</mark>

**Relational Operators** — return `True` or `False`

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater or equal | `x >= 5` |
| `<=` | Less or equal | `x <= 5` |

**`==` vs. `is`** — `🔖 PCEP 1.4` `📋 AP CSP: AAP-2.F`

`==` and `is` are **not interchangeable**, even though both can return `True`/`False` in a comparison.

| Operator | Checks | Question it answers |
|---|---|---|
| `==` | **Equality** of value | "Do these contain the same data?" |
| `is` | **Identity** of object | "Are these the exact same object in memory?" |

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)   # True  — same values
print(a is b)   # False — two different list objects
print(a is c)   # True  — c points to the same object as a
```

> <mark>**PCEP Exam Trap:** Use `is` / `is not` only for identity checks — most importantly `x is None` (the Python standard, preferred over `x == None`). Use `==` for comparing values (numbers, strings, list contents, etc.). Small integers and short strings may sometimes evaluate `is` as `True` due to CPython's internal caching — this is an implementation detail, not something to rely on in your own code.</mark>

**Boolean / Logical Operators**

```python
True and False   # False — both must be True
True or False    # True  — at least one must be True
not True         # False — reverses the boolean
```

<details><summary>Compound Boolean Expressions (expand)</summary>

```python
age = 20
has_license = True

# AND: both must be True
is_eligible = age >= 18 and has_license   # True

# OR: at least one must be True
can_enter = age >= 18 or has_vip_pass     # True

# NOT: reverses the boolean
is_minor = not (age >= 18)               # False

# Complex example
gets_discount = (age > 25 or is_eligible) and not has_discount_coupon
```

</details>

### Activity: Movie Ticket Eligibility Checker

Write a program that determines whether a person can buy a discounted movie ticket, using **only compound boolean expressions** (`and`, `or`, `not`) — no `if/elif` chains yet.

**Requirements:**

1. Ask the user for their age and whether they have a student ID (`yes`/`no`).
2. A ticket is discounted if the person is **under 13, OR over 65, OR (between 13–25 AND has a student ID)**.
3. Store the result of that full condition in a single boolean variable, e.g. `gets_discount = ...`, then print `"Discount applies!"` or `"Full price."` based on its value.
4. Add a second check: the theater is closed to anyone under 6 with **no adult present** — ask a follow-up question and use `not` to write the condition for "an adult is NOT present."
5. Print a trace of your boolean logic as a comment above each condition, explaining what it evaluates in plain English (this mirrors how you'll need to explain conditions in your AP CSP written responses).

*PCEP: 1.4 | AP CSP: AAP-2.F*

---

**Why Bitwise Operators Matter**

Bitwise operators work directly on the **binary representation** of numbers — the individual `0`s and `1`s — rather than on the number's value as a whole. Most everyday Python code never needs them, but they matter for a few reasons worth knowing:

- **They're on the PCEP exam** — you're expected to trace what `&`, `|`, `^`, `~`, `<<`, and `>>` do to binary values.
- **They connect back to how computers actually store data** — ties directly to the binary/decimal/hex conversions you just learned.
- **They show up in real systems programming**: setting individual permission flags (read/write/execute), working with network protocols, compressing data, and low-level graphics/hardware code all lean on bitwise operations because they're extremely fast and memory-efficient.
- **Shifts are a fast way to multiply/divide by powers of 2**: `a << 1` doubles a number, `a >> 1` halves it (integer division) — a trick you'll sometimes see in performance-sensitive code.

You won't use these daily as a beginner, but recognizing them — and knowing they operate on bits, not on the number's "everyday" value — will keep you from being caught off guard by `&` (bitwise AND) when you meant `and` (logical AND), which is a common bug even experienced programmers make.

**Bitwise Operators** — `🔖 PCEP 1.4`

```python
a = 0b1010   # 10
b = 0b1100   # 12

print(a & b)   # AND  → 8   (0b1000)
print(a | b)   # OR   → 14  (0b1110)
print(a ^ b)   # XOR  → 6   (0b0110)
print(~a)      # NOT  → -11
print(a << 1)  # Left shift → 20
print(a >> 1)  # Right shift → 5
```

## Print Statements and Input/Output

`🔖 PCEP 1.5` — Perform Input/Output console operations
`📋 AP CSP: CRD-2.B` — Implement algorithms in a programming language.

```python
# 1. Basic print
print("Hello, World!")

# 2. f-strings (most readable — preferred method)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# 3. format() method
print("My name is {} and I am {} years old.".format(name, age))

# 4. Concatenation (must convert non-strings)
print("Name: " + name + ", Age: " + str(age))

# 5. sep= and end= keyword parameters
print("A", "B", "C", sep="-")   # A-B-C
print("Hello", end="! ")
print("World")                  # Hello! World
```

**User Input**

```python
name = input("Enter your name: ")          # always returns a string
age  = int(input("Enter your age: "))      # convert to int
price = float(input("Enter price: "))      # convert to float
```

> <mark>**PCEP Exam Tip:** `input()` always returns a `str`. You must use `int()` or `float()` to convert it for math operations.</mark>

### Activity: Hello, World! Variations

Write a program that asks the user for their name, age, and favorite color. Print a formatted sentence using each of the three print methods (f-string, `format()`, concatenation). Include a header block.

*AP CSP: CRD-2.B | PCEP: 1.5*

---

# Section 2 — Control Flow: Conditional Blocks and Loops
`🔖 PCEP Section 2 — 29% of exam (8 items)`
`📋 AP CSP: AAP-2.E` — Develop algorithms using sequencing, selection, and iteration.

## Conditional Statements

**Control flow** determines which code runs, when, and how often. Conditionals let the program **make decisions**.

```python
# if
if condition:
    # runs if True

# if-else
if condition:
    # runs if True
else:
    # runs if False

# if-elif-else
if condition1:
    # ...
elif condition2:
    # ...
else:
    # fallback
```

**Example: Grade Calculator**

```python
score = int(input("Enter your score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

**Nested Conditionals**

```python
if score >= 70:
    if score >= 90:
        print("A or A+")
    else:
        print("Pass")
else:
    print("Fail")
```

> 💡 Prefer `elif` over deep nesting when possible — it keeps code readable.

### Activity: Grade Calculator

Write a grade calculator that accepts a numerical score and outputs:
- The letter grade (A–F)
- Whether the student passed or failed
- A motivational message for scores below 70

Use `if-elif-else` and at least one nested conditional.

*AP CSP: AAP-2.E | PCEP: 2.1*

---

## Loops

`🔖 PCEP 2.2` — Perform different types of iterations
`📋 AP CSP: AAP-2.E` — Iteration; `AAP-2.K` — For loops

**`for` Loop** — iterates over a sequence

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6, 2):  # 1, 3, 5
    print(i)
```

**`while` Loop** — repeats while a condition is `True`

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Loop Control Keywords**

| Keyword | Purpose | Example |
|---|---|---|
| `break` | Exit loop immediately | `if x == 3: break` |
| `continue` | Skip to next iteration | `if x % 2 == 0: continue` |
| `pass` | Placeholder — does nothing | `if x == 2: pass` |
| `else` | Runs if loop ends without `break` | `for..else:` |

**`while-else` and `for-else`** — `🔖 PCEP 2.2`

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")   # This runs
```

**Nested Loops**

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()
```

### Activity: Nested Loop Pattern Design Studio

A single loop can only move in one direction. The moment a shape has **both rows and columns** — a triangle, a diamond, a hollow box — you need a loop *inside* a loop. The outer loop picks the row; the inner loop decides what happens across that row.

**Warm-up — reading a pattern like a programmer.** Before writing code, answer these for the pattern below:
1. How many rows are there?
2. Row by row, what changes? (number of characters, starting character, spacing)
3. Is there a pattern to the pattern? (e.g., "row `i` prints `i` stars")
4. Is it **solid** (every position filled) or **hollow** (only a border filled)?

```
*
* *
* * *
* * * *
* * * * *
```

**Guided example — hollow rectangle:**

```python
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if i == 1 or i == rows or j == 1 or j == cols:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

**Discussion:** What single condition controls whether the shape is solid or hollow? *(The `if`/`else` inside the inner loop — remove it and the shape becomes solid.)*

**The Studio Project — Design Your Own**

Design and code **4 original patterns**. "Original" means not shown in class, not copied from a classmate. For each pattern, choose one option from each category below (no repeating the exact same combination twice):

| Category | Options |
|---|---|
| **Fill type** | Solid / Hollow |
| **Content** | ASCII character (your choice) / Sequential numbers / Repeating digit tied to row number |
| **Orientation** | Grows then stays / Grows then shrinks (diamond/hourglass) / Right-aligned / Shifts diagonally (parallelogram) |
| **Input** | At least one of your 4 patterns must accept user input for size |

**Suggested difficulty progression:**
- Tier 1 — Solid, fixed growth (e.g., a solid right triangle)
- Tier 2 — Hollow (border-only conditional logic)
- Tier 3 — Numeric (a value that changes per row)
- Tier 4 — Your choice / mirrored or diagonal shape

**Required process (before coding):** sketch each pattern on grid paper, answer the four warm-up questions for your own design, and write pseudocode for the outer loop, inner loop, and the row-vs-column relationship — *then* code it.

**Deliverable:** 4 working programs, each with its grid-paper sketch, pseudocode, final code, and one paragraph explaining what the outer loop controls vs. what the inner loop controls.

**Rubric (8 pts per pattern, 32 pts total):**

| Criteria | Points |
|---|---|
| Sketch and pseudocode completed *before* code, and match the final output | 2 |
| Pattern runs without errors and matches the intended design | 2 |
| Nested loop logic is correct (not hard-coded repeated `print()` statements) | 2 |
| At least one pattern correctly uses user input to control size | 1 |
| Written explanation correctly identifies the role of outer vs. inner loop | 1 |

*AP CSP: AAP-2.E | PCEP: 2.2*

---

# Section 3 — Data Collections: Lists, Tuples, Dictionaries, and Strings
`🔖 PCEP Section 3 — 25% of exam (7 items)`
`📋 AP CSP: AAP-4.A` — Use data abstractions to manage complexity.

## Strings

`🔖 PCEP 3.4` — Operate with strings
`📋 AP CSP: DAT-1.A`

Strings are **ordered, immutable** sequences of characters.

```python
greeting = "Hello, World!"
print(greeting[0])       # H      (indexing)
print(greeting[-1])      # !      (negative index)
print(greeting[0:5])     # Hello  (slicing)
print(greeting[::-1])    # !dlroW ,olleH (reverse)
print(len(greeting))     # 13
```

**String Indexing Reference**

```
string =   |  P  |  O  |  T  |  A  |  T  |  O  |
pos_index:    0     1     2     3     4     5
neg_index:   -6    -5    -4    -3    -2    -1
```

**Escape Characters**

```python
print("She said \"Hello\"")  # She said "Hello"
print("Line 1\nLine 2")      # newline
print("Col1\tCol2")          # tab
print("Backslash: \\")       # \
```

**Multi-line Strings**

```python
poem = """
Roses are red,
Violets are blue.
"""
```

**Beginner String Methods**

| Method | Description | Example |
|---|---|---|
| `.lower()` | Lowercase | `"HELLO".lower()` → `"hello"` |
| `.upper()` | Uppercase | `"hello".upper()` → `"HELLO"` |
| `.strip()` | Remove whitespace | `"  hi  ".strip()` → `"hi"` |
| `.replace(old, new)` | Replace text | `"cat".replace("c","b")` → `"bat"` |
| `.split(sep)` | Split into list | `"a b c".split()` → `["a","b","c"]` |
| `len()` | Length | `len("hello")` → `5` |
| `.find(sub)` | Index of substring | `"apple".find("p")` → `1` |
| `.count(sub)` | Count occurrences | `"banana".count("a")` → `3` |
| `.startswith(text)` | Starts with? | `"hello".startswith("he")` → `True` |
| `.endswith(text)` | Ends with? | `"file.txt".endswith(".txt")` → `True` |
| `.isalpha()` | All letters? | `"abc".isalpha()` → `True` |
| `.isdigit()` | All digits? | `"123".isdigit()` → `True` |

---

### Activity: Receipt Formatter

Write a program that formats a store receipt using string methods and escape characters.

**Requirements:**

1. Ask the user for a store name, an item name, and a price.
2. Use `.upper()` to print the store name in all caps as a header.
3. Use `.title()` to properly capitalize the item name (e.g., `"blue notebook"` → `"Blue Notebook"`).
4. Use `\t` to align the item name and price in two columns, and `\n` to add blank lines between sections.
5. Use `\"` to print a quoted "Thank you for shopping with us!" message at the bottom.
6. Ask the user to re-enter the item name with extra spaces on purpose (e.g., `"  notebook   "`), then use `.strip()` to clean it before printing — show the *before and after* to prove the method worked.
7. Use `.replace()` to apply a discount label — replace `"Price:"` with `"Sale Price:"` in your printed line if the price is above $20.
8. Bonus: use `.startswith()` or `.endswith()` to check if the item name starts with a vowel, and print a fun fact if it does.

**Sample interaction:**
```
Enter store name: target
Enter item name:   blue notebook   
Enter price: 24.99

TARGET
Blue Notebook	Sale Price: $24.99

"Thank you for shopping with us!"
```

*PCEP: 3.4 | AP CSP: DAT-1.A*

---

## Lists

`🔖 PCEP 3.1` — Collect and process data using lists
`📋 AP CSP: AAP-4.A` — Lists for data abstraction

A **list** is an **ordered, mutable** sequence. It is the most versatile data collection in Python.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
print(fruits[-1])      # cherry
print(fruits[1:3])     # ['banana', 'cherry']
```

**Common List Methods**

```python
fruits.append("orange")        # Add to end
fruits.insert(1, "blueberry")  # Insert at index
fruits.remove("banana")        # Remove by value
popped = fruits.pop()          # Remove & return last item
fruits.sort()                  # Sort in place
fruits.reverse()               # Reverse in place
print(fruits.index("apple"))   # Find index
print(fruits.count("apple"))   # Count occurrences
fruits2 = fruits.copy()        # Clone the list
fruits.clear()                 # Remove all items
```

**Iterating Through Lists**

```python
for item in fruits:
    print(item)

for i, item in enumerate(fruits):
    print(f"{i}: {item}")
```

**`in` and `not in` Operators**

```python
print("apple" in fruits)       # True
print("grape" not in fruits)   # True
```

**List Comprehensions**

A **list comprehension** is a compact way to build a new list by looping over an existing sequence — it packs a `for` loop (and optionally an `if` condition) into a single line. It always follows the same shape:

```
new_list = [expression for item in sequence if condition]
```

- **`expression`** — what to do with each item before adding it to the new list
- **`for item in sequence`** — the loop, exactly like a normal `for` loop
- **`if condition`** *(optional)* — only include the item if this is `True`

The traditional loop version and the comprehension version produce the *exact same result* — the comprehension is just shorter:

```python
# Traditional loop
squares = []
for x in range(10):
    squares.append(x ** 2)

# Equivalent list comprehension
squares = [x ** 2 for x in range(10)]
```

```python
squares     = [x ** 2 for x in range(10)]
evens       = [x for x in range(20) if x % 2 == 0]
upper_words = [word.upper() for word in ["hi", "bye"]]
```

> <mark>**When to use which:** list comprehensions are great for simple, one-line transformations. If your loop needs multiple steps, `print()` statements along the way, or complex logic, a traditional `for` loop is usually more readable — don't force a comprehension just because it's shorter. Readability counts, per PEP 8.</mark>

**Copying vs. Cloning**

```python
original = [1, 2, 3]
alias    = original        # NOT a copy — both point to same list
clone    = original.copy() # Independent copy
clone2   = original[:]     # Also a copy (slicing)
```

**2D Lists (Matrices)**

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(grid[1][2])   # 6  (row 1, col 2)

# Iterate a 2D list
for row in grid:
    for val in row:
        print(val, end=" ")
    print()
```

---

## Tuples

`🔖 PCEP 3.2` — Collect and process data using tuples

A **tuple** is an **ordered, immutable** sequence — values cannot be changed after creation.

```python
coords     = (40.7128, -74.0060)    # GPS: New York City
rgb        = (255, 128, 0)
single     = (42,)                  # Note the comma for single-element tuple

print(coords[0])    # 40.7128
print(len(rgb))     # 3
```

**Tuples vs. Lists**

| Feature | List | Tuple |
|---|---|---|
| Ordered | ✅ | ✅ |
| Indexed | ✅ | ✅ |
| Mutable | ✅ | ❌ |
| Duplicates | ✅ | ✅ |
| Use when | Data changes | Data is fixed |

**Lists inside Tuples and Tuples inside Lists**

```python
mixed = ([1, 2, 3], [4, 5, 6])   # tuple of lists
nested = [(1, "a"), (2, "b")]     # list of tuples
```

---

## Dictionaries

`🔖 PCEP 3.3` — Collect and process data using dictionaries
`📋 AP CSP: AAP-3.B` — Use abstractions to organize data.

A **dictionary** stores **key-value pairs**. Keys must be unique and immutable. Dictionaries are **ordered** (Python 3.7+) and **mutable**.

```python
student = {
    "name": "Alice",
    "age": 16,
    "grade": "A"
}

print(student["name"])       # Alice
student["age"] = 17          # Update value
student["school"] = "CAMS"   # Add new key
del student["grade"]         # Remove key
```

**Checking for Keys**

```python
if "name" in student:
    print("Key exists!")
```

**Dictionary Methods**

```python
student.keys()     # dict_keys(['name', 'age', ...])
student.values()   # dict_values(['Alice', 17, ...])
student.items()    # dict_items([('name','Alice'), ...])
```

**Iterating**

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

**List of Dictionaries (real-world pattern)**

```python
students = [
    {"name": "Alice", "age": 14},
    {"name": "Bob",   "age": 15},
    {"name": "Charlie", "age": 14}
]

for s in students:
    print(s["name"])

# Count students age 14
count = sum(1 for s in students if s["age"] == 14)
```

### Activity: Student Contact Book

Build a program that stores a contact book as a **list of dictionaries**. Each contact has a name, phone number, and email. The user can:
1. Add a new contact
2. Search by name
3. Delete a contact
4. Display all contacts

Use a `while` loop for the menu and a `for` loop to search/display.

*AP CSP: AAP-3.B, AAP-2.E | PCEP: 3.3*

---

# Section 4 — Functions and Exceptions
`🔖 PCEP Section 4 — 28% of exam (8 items)`
`📋 AP CSP: AAP-3.B` — Use procedures/functions to manage complexity.

## Functions, Methods, and Procedures

`🔖 PCEP 4.1` — Decompose the code using functions
`📋 AP CSP: AAP-3.B` — Abstractions; `CRD-2.G` — Call procedures.

| Term | Python Form | Returns Value? | Used For |
|---|---|---|---|
| **Function** | `def` with `return` | ✅ Yes | Computing and returning a result |
| **Procedure** | `def` without `return` | ❌ No | Side effects (printing, updating) |
| **Method** | Function inside a class | ✅/❌ | Behaviors belonging to an object |

```python
# Function — returns a value
def add(a, b):
    return a + b

result = add(3, 5)   # result = 8

# Procedure — no return value
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # Hello, Alice!
```

**Parameters vs. Arguments**

```python
# 'a' and 'b' are PARAMETERS (in definition)
def multiply(a, b):
    return a * b

# 5 and 3 are ARGUMENTS (passed at call)
multiply(5, 3)
```

### Activity: Math Operations Calculator

Write a Python program called `math_operations.py` that performs addition, subtraction, multiplication, division, and modulo on two numbers entered by the user — using a separate function for each operation.

**Requirements:**

1. Write five functions: `get_sum(num1, num2)`, `get_difference(num1, num2)`, `get_product(num1, num2)`, `get_quotient(num1, num2)`, and `get_modulo(num1, num2)`. Each function should perform one calculation and `return` the result (no `print()` inside the functions).
2. In `main()`, prompt the user for two numbers using `input()`, and convert them to the correct type (`int` for whole numbers).
3. Call each function, store the result in a variable, and print all five results using f-strings, formatted like:
   ```
   Sum = 15
   Difference = 5
   Product = 50
   Quotient = 2.00
   Remainder = 0
   ```
4. `get_quotient()` should always return a `float` — use `float()` or a division with `/` (not `//`) to avoid integer division.
5. Include a full program header block (Assignment, Author, Description, etc.) at the top, following the course style guide.

**Stretch challenge:** What happens if the user enters `0` as the second number for division or modulo? Add a `try/except` block (or an `if` check) so the program doesn't crash — print a friendly error message instead.

> **Teaching note:** This activity mirrors a classic C-language exercise (functions returning `int`/`float`, separate function per operation) — a good one to point out explicitly if any students are also in a C/C++ or Java course, since the *logic* is identical even though the syntax (no semicolons, no type declarations, no `#include`) is different.

*PCEP: 1.4, 1.5, 4.1 | AP CSP: AAP-2.F, AAP-3.B*

**Default Parameter Values** — `🔖 PCEP 4.2`

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Good morning")  # Good morning, Bob!
```

**Positional, Keyword, and Mixed Arguments**

```python
def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe("Alice", 16, "HB")             # Positional
describe(age=16, name="Alice", city="HB")  # Keyword
describe("Alice", city="HB", age=16)    # Mixed
```

**The `return` Keyword and `None`**

```python
def square(n):
    return n ** 2

result = square(4)   # result = 16

def do_nothing():
    pass

print(do_nothing())  # None — functions without return give None
```

**Variable Scope and `global`** — `🔖 PCEP 4.2`

```python
counter = 0             # global variable

def increment():
    global counter      # must declare to modify global
    counter += 1

increment()
print(counter)          # 1
```

> <mark>**Name Hiding (Shadowing):** A local variable with the same name as a global hides (shadows) the global inside the function. This is a common PCEP exam trap.</mark>

```python
x = 10

def show():
    x = 99   # local x shadows global x
    print(x)

show()       # 99
print(x)     # 10 — global unchanged
```

**Recursion** — `🔖 PCEP 4.1`

A **recursive function** calls itself. Every recursion needs a **base case** to stop.

```python
def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))     # 120
```

Call stack visualization:
```
factorial(5)
  factorial(4)
    factorial(3)
      factorial(2)
        factorial(1)
          factorial(0)  ← base case: returns 1
```

### Activity: Recursion Practice — Three Levels

Recursion clicks once you can identify two things in *any* recursive problem: the **base case** (when to stop) and the **recursive case** (how the problem gets smaller each call). Practice with three functions, in order:

**Level 1 — Countdown.** Write `countdown(n)` that prints every number from `n` down to `1`, then prints `"Liftoff!"` — using recursion, not a loop. Identify: what is the base case? What gets smaller with each call?

**Level 2 — Sum of a list.** Write `list_sum(numbers)` that returns the sum of all numbers in a list using recursion (hint: the base case is an empty list, which sums to `0`; the recursive case is `numbers[0] + list_sum(numbers[1:])`).

**Level 3 — Power function.** Write `power(base, exponent)` that calculates `base ** exponent` using recursion instead of the `**` operator. (Base case: `exponent == 0` returns `1`.)

**For each function, before coding, write on paper:**
1. What is the base case, and what does it return?
2. What is the recursive case, and how does it move the problem toward the base case?
3. Trace through one full call by hand (like the `factorial(5)` call stack above) and predict the output.

**Stretch challenge:** Add a `print()` inside each function showing the current call's argument and indenting one extra level per recursive call — this visually recreates the call stack diagram above, using your own code.

*PCEP: 4.1*

---

## Modules and Packages

`📋 AP CSP: AAP-2.G` — Use abstraction to manage complexity.

A **module** is a `.py` file containing reusable code. A **package** is a directory of related modules.

```python
import math
import random
import datetime

print(math.sqrt(16))          # 4.0
print(random.randint(1, 10))  # random int 1–10
print(datetime.date.today())   # today's date
```

**Import Styles**

```python
import math                   # access as math.sqrt()
from math import sqrt         # access as sqrt()
from math import sqrt, pi     # import multiple
import numpy as np            # alias
```

**Common Standard Library Modules**

| Module | Purpose | Example |
|---|---|---|
| `math` | Math functions | `math.sqrt()`, `math.pi` |
| `random` | Random numbers | `random.randint()`, `random.choice()` |
| `datetime` | Date/time | `datetime.date.today()` |
| `os` | Operating system | `os.getcwd()` |
| `json` | JSON data | `json.loads()`, `json.dumps()` |
| `tkinter` | GUI windows | `tk.Tk()`, `tk.Button()` |

---

### Project: Random Trivia Quiz Generator

Build a trivia quiz program that pulls together **modules, functions, lists, dictionaries, and string formatting** — everything you've learned so far — into one working project.

**Requirements:**

1. Use the `random` module to randomly select and shuffle quiz questions each time the program runs.
2. Use the `datetime` module to timestamp the start and end of the quiz, and calculate/print how long the student took using `datetime.datetime.now()`.
3. Store at least 8 trivia questions as a list of dictionaries, each with keys like `"question"`, `"choices"`, and `"answer"`.
4. Write a function `ask_question(question_dict)` that displays a question and its choices, collects the user's answer, and returns `True`/`False` for correct/incorrect.
5. Write a function `run_quiz(questions)` that loops through all questions, tracks the score, and calls `ask_question()` for each one.
6. At the end, print the score as both a raw count (`"7/8 correct"`) and a percentage, formatted to 1 decimal place using an f-string.
7. Import at least one module using each of the three import styles covered above (`import x`, `from x import y`, `import x as y`).
8. Include a full program header block.

**Rubric (25 points total)**

| Criteria | Points |
|---|---|
| `random` module correctly used to shuffle/select questions | 4 |
| `datetime` module correctly used to time the quiz | 4 |
| Questions stored as a list of dictionaries with consistent keys | 4 |
| `ask_question()` function correctly returns `True`/`False` | 4 |
| `run_quiz()` function correctly tracks and returns the score | 4 |
| Score printed as both count and percentage (f-string formatting) | 2 |
| All three import styles used correctly somewhere in the program | 2 |
| Program header block, PEP 8 style, and no crashes on normal input | 1 |

**Stretch challenge:** Add a fourth import — `json` — to save the student's score to a `scores.json` file after each run, and load/display their best score at the start of the next run.

*AP CSP: AAP-2.G, CRD-2.B*

---

## Exception Handling

`🔖 PCEP 4.3` — Python Built-In Exceptions Hierarchy
`🔖 PCEP 4.4` — Basics of Python Exception Handling
`📋 AP CSP: CRD-2.J` — Test and debug programs.

**What Is an Exception?**

An **exception** is a runtime error that interrupts normal program flow. Without handling, it crashes the program. <mark>With `try-except`, you can catch and respond to errors gracefully.</mark>

**Basic Syntax**

```python
try:
    # code that may raise an exception
except SomeException as e:
    # runs if the exception occurs
else:
    # runs if NO exception occurred
finally:
    # ALWAYS runs — cleanup code
```

**Example: Safe Division**

```python
try:
    result = 10 / int(input("Enter a divisor: "))
except ValueError:
    print("That wasn't a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Operation attempted.")
```

**Exception Hierarchy** — `🔖 PCEP 4.3`

```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    └── FileNotFoundError
```

> <mark>**PCEP Exam Tip:** Order `except` blocks from **most specific to most general**. Python checks them in order and runs the first match.</mark>

```python
try:
    x = int("abc")
except ValueError:          # caught here — most specific
    print("Value error")
except Exception:           # broader fallback
    print("Some error")
```

**Common Exceptions**

| Exception | When it occurs |
|---|---|
| `ZeroDivisionError` | Dividing by zero |
| `ValueError` | Wrong value type, e.g., `int("abc")` |
| `TypeError` | Wrong data type in operation |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | File doesn't exist |
| `NameError` | Variable not defined |

**Propagating Exceptions** — `🔖 PCEP 4.4`

```python
def divide(a, b):
    return a / b           # may raise ZeroDivisionError

try:
    result = divide(10, 0) # exception propagates up to here
except ZeroDivisionError:
    print("Caught in caller!")
```

**File Handling with Exceptions**

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading file.")
```


### Activity: Safe Calculator

Build a calculator program that:
1. Accepts two numbers and an operator (`+`, `-`, `*`, `/`)
2. Handles `ZeroDivisionError` and `ValueError`
3. Loops until the user types `quit`
4. Uses a function for each operation
5. Uses `try-except-else-finally`

*AP CSP: CRD-2.J | PCEP: 4.3, 4.4*

---

# Data Structures Deep Dive

`📋 AP CSP: AAP-3.A, AAP-3.B, AAP-3.C`

Python's built-in data structures serve different organizational needs:

| Structure | Ordered | Mutable | Indexed | Duplicates | Use When |
|---|---|---|---|---|---|
| **List** | ✅ | ✅ | ✅ | ✅ | General-purpose ordered collection |
| **Tuple** | ✅ | ❌ | ✅ | ✅ | Fixed data (coords, config) |
| **Set** | ❌ | ✅ | ❌ | ❌ | Unique values, set operations |
| **Dictionary** | ✅ | ✅ | By key | ❌ (keys) | Key-value lookup |

**Sets**

```python
user_ids = {101, 102, 103, 101}   # duplicates removed
print(user_ids)                   # {101, 102, 103}

a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)   # Union:        {1, 2, 3, 4}
print(a & b)   # Intersection: {2, 3}
print(a - b)   # Difference:   {1}
```

**Stacks (LIFO) using Lists**

A **stack** follows **LIFO** — **Last In, First Out**. Think of a stack of plates: you add a new plate to the top, and you also take from the top. The most recently added item is always the first one removed. Python's `undo` button behavior, browser back-buttons, and function call stacks (like the recursion diagram above!) all work this way.

```python
stack = []
stack.append("action1")   # push — add to the top
stack.append("action2")
last = stack.pop()         # pop → "action2" (last one in, first one out)
```

**Queues (FIFO) using deque**

A **queue** follows **FIFO** — **First In, First Out**. Think of a line at a store checkout: the first person in line is the first person served. New items are added to the back and removed from the front.

```python
from collections import deque
queue = deque()
queue.append("first")      # add to the back
queue.append("second")
first = queue.popleft()    # remove from the front → "first" (first one in, first one out)
```

> <mark>**Memory trick:** LIFO = last in, first out (a **stack** of trays). FIFO = first in, first out (a **line** at the store). Both use `.append()` to add, but stacks remove with `.pop()` (from the end) while queues remove with `.popleft()` (from the front).</mark>

---

# Object-Oriented Programming (OOP)

`📋 AP CSP: AAP-3.B` — Abstractions; `CRD-2.B` — Implement in a language.

> **Why OOP?** Real programs model real-world things — students, cars, bank accounts, game characters. OOP lets us **group data and behavior** together in reusable, organized units called **classes**.

## Core OOP Concepts

**Key Vocabulary**

| Term | Definition |
|---|---|
| **Class** | A blueprint/template for creating objects |
| **Object** | An instance (specific example) of a class |
| **Attribute** | A variable that belongs to a class or object |
| **Method** | A function that belongs to a class |
| **Constructor** | `__init__` — initializes a new object's attributes |
| **`self`** | Refers to the current instance of the class |
| **Encapsulation** | Bundling data and methods together |
| **Inheritance** | A child class acquires attributes/methods from a parent |
| **Polymorphism** | Different classes can share the same method name |

## Building a Class

```python
class Car:
    """Blueprint for a car object."""

    def __init__(self, make, model, year):
        """Constructor — runs automatically when object is created."""
        self.make  = make    # instance attribute
        self.model = model   # instance attribute
        self.year  = year    # instance attribute

    def start_engine(self):
        """Instance method — uses self to access attributes."""
        print(f"The {self.year} {self.make} {self.model}'s engine is running.")

    def stop_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is off.")

    def __str__(self):
        """Magic method — controls how object prints."""
        return f"{self.year} {self.make} {self.model}"
```

**Creating and Using Objects**

```python
car1 = Car("Toyota", "Corolla", 2022)   # create object
car2 = Car("Honda",  "Civic",   2020)

car1.start_engine()     # The 2022 Toyota Corolla's engine is running.
print(car2)             # 2020 Honda Civic  (uses __str__)

# Access attributes directly
print(car1.make)        # Toyota
car1.year = 2023        # Modify an attribute
```

## Types of Methods

```python
class Dog:
    species = "Canis familiaris"   # CLASS attribute (shared by all instances)

    def __init__(self, name, breed=None):
        self.name  = name          # INSTANCE attribute (unique per object)
        self.breed = breed

    def bark(self):                # INSTANCE method
        print(f"{self.name} says Woof!")

    @classmethod
    def get_species(cls):          # CLASS method — operates on the class
        return cls.species

    @staticmethod
    def is_domestic():             # STATIC method — no instance or class needed
        return True
```

## Inheritance

<mark>**Inheritance** allows a **child class** to reuse and extend the behavior of a **parent class**.</mark>

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):                       # Dog inherits from Animal
    def speak(self):                     # Override the parent method
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

animals = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]
for animal in animals:
    print(animal.speak())                # Polymorphism in action
```

## Magic / Dunder Methods

```python
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder  = holder
        self.balance = balance

    def __str__(self):
        return f"Account({self.holder}, ${self.balance:.2f})"

    def __len__(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

# Usage
account = BankAccount("Alice Smith", 1000)
print(account)             # Account(Alice Smith, $1000.00)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)     # Insufficient funds
```

### Activity: OOP Zoo

Design a `Zoo` simulation using OOP:

1. Create a base class `Animal` with attributes `name`, `species`, `age`, and a method `describe()`.
2. Create at least three subclasses (e.g., `Mammal`, `Bird`, `Reptile`) that each override a `speak()` method.
3. Create a `Zoo` class that holds a list of `Animal` objects and can:
   - `add_animal(animal)`
   - `show_all()` — print all animals
   - `find_by_species(species)` — return a list of matching animals
4. Create at least 5 animal objects, add them to the zoo, and demonstrate all methods.

Include `__str__` and proper docstrings.

**Option 2 — Library Management System**

Design a simplified library check-out system using OOP:

1. Create a base class `Item` with attributes `title`, `id_number`, `checked_out` (default `False`), and a method `describe()`.
2. Create at least two subclasses (e.g., `Book`, `Magazine`) that each override `describe()` to include a subclass-specific detail (author for `Book`, issue number for `Magazine`).
3. Create a `Library` class that holds a list of `Item` objects and can:
   - `add_item(item)`
   - `check_out(id_number)` — marks an item unavailable, or prints a message if already checked out
   - `return_item(id_number)` — marks an item available again
   - `list_available()` — prints all items currently not checked out
4. Create at least 5 items, add them to the library, and demonstrate checking items in and out.

**Option 3 — RPG Character Builder**

Design a role-playing game character system using OOP:

1. Create a base class `Character` with attributes `name`, `health`, `level`, and a method `attack()` that returns a damage value.
2. Create at least three subclasses (e.g., `Warrior`, `Mage`, `Healer`) that each override `attack()` with different behavior (e.g., `Mage` deals more damage but has less health; `Healer`'s `attack()` restores health to an ally instead).
3. Create a `Party` class that holds a list of `Character` objects and can:
   - `add_member(character)`
   - `show_party()` — print all members and their stats
   - `total_party_health()` — return the combined health of all members
4. Create at least 4 characters across different subclasses, add them to a party, and simulate a round of attacks.

**Rubric for All Three Options (10 points)**

| Criteria | Points |
|---|---|
| Base class correctly defined with required attributes and at least one method | 2 |
| At least the required number of subclasses created, each correctly inheriting from the base class | 2 |
| Each subclass overrides the specified method with genuinely different behavior (not just a copy/paste) | 2 |
| Container class (`Zoo`/`Library`/`Party`) correctly manages a list of objects with all required methods | 2 |
| Program includes `__str__` and docstrings, follows PEP 8, and runs without errors on the demonstration code | 2 |

*AP CSP: AAP-3.B, CRD-2.B | Demonstrates: Abstraction, Inheritance, Polymorphism*

---

# AP CSP Performance Task Preparation

`📋 AP CSP: CRD-2` — Program Design and Development

> The **AP CSP Create Performance Task (CPT)** is 30% of your AP score. You write a program and submit written responses explaining it. This section helps you align your project to College Board requirements.

## CPT Requirements at a Glance

| Requirement | Description |
|---|---|
| **Program Purpose** | Clearly state what problem your program solves |
| **Algorithm** | Must include sequencing, selection, AND iteration |
| **Abstraction** | Must use a list (or other collection) and a procedure/function |
| **Procedure with parameter** | A function that takes input and affects behavior |
| **Output** | Must produce visible output based on input |

## CPT Checklist — Does Your Program Have?

☐ A clear **purpose** that solves a meaningful problem

☐ **Input** from the user or a data source

☐ **Output** that responds to the input

☐ An **algorithm** using:
  - ☐ Sequencing (steps in order)
  - ☐ Selection (`if-elif-else`)
  - ☐ Iteration (`for` or `while` loop)

☐ A **list** (or collection) that stores and processes data

☐ At least one **student-defined function** that:
  - ☐ Has a **parameter** that affects behavior
  - ☐ Is **called** at least once in the program

☐ Your function implements an **algorithm** (not just `print`)

☐ A **second call** to the function with different arguments

## CPT Written Response Tips

**Prompt 3a — Program Function and Purpose:**
- Describe what your program does and the **problem it solves**
- Describe what input your program accepts
- Describe the output your program produces

**Prompt 3b — Data Abstraction:**
- Show your code that **stores data in a list** (or other collection)
- Explain **what data is in the list** and how it represents information
- Explain what would be harder **without** using a list

**Prompt 3c — Managing Complexity:**
- Show your **function/procedure** with a parameter
- Explain what the parameter does and how it affects output
- Explain how the function **manages complexity**

**Prompt 3d — Procedural Abstraction:**
- Identify the algorithm embedded in your function
- Describe the algorithm step-by-step in plain English

### Activity: CPT Brainstorming Workshop

With a partner, evaluate 3 program ideas against the CPT checklist. For each idea, identify:
1. The input source
2. The list and what it stores
3. The function and its parameter
4. The algorithm (sequencing, selection, iteration)

Select the strongest idea and create a one-page project proposal.

*AP CSP: CRD-2.A, CRD-2.B*

---

# Final Project Options

## Option A — Text-Based Adventure Game (Beginner–Intermediate)

Build a multi-room text adventure with:
- Classes for `Player`, `Room`, and `Item`
- A `list` of rooms and items
- A `while` loop game engine
- User-input navigation using `if-elif`
- At least one function with a parameter
- Exception handling for invalid input
- A scoring system

**AP CSP Alignment:** CRD-2.B, AAP-2.E, AAP-3.B, AAP-4.A

---

## Option B — Student Data Tracker (Intermediate)

Build a command-line tracker that:
- Stores student records as a list of dictionaries
- Supports add, delete, search, and update operations
- Calculates class average, highest/lowest scores
- Uses OOP (a `Student` class with methods)
- Handles all exceptions gracefully
- Optionally reads/writes to a `.json` file

**AP CSP Alignment:** CRD-2.B, AAP-3.A, AAP-3.B, AAP-3.C, AAP-4.A

---

## Option C — Mini Minesweeper (Advanced)

Build a simplified Minesweeper game using Python and Tkinter with OOP design.

**Project Objectives**

1. A 6×6 grid stored as a **2D list**
2. Random mine placement
3. Count adjacent mines per cell
4. Allow player left-clicks and right-click flagging
5. Score tracking for safe clicks
6. Move history stored in a **list**
7. Game over on mine click
8. Flood-fill reveal using **recursion**
9. Win/loss detection
10. "Try Again" button to reset

**AP CSP Alignment:** AAP-2.E, AAP-4.A, CRD-2.B, CRD-2.J

*AP CSP Learning Goals:*
- `AAP-2.E` — Algorithms with sequencing, selection, iteration
- `AAP-4.A` — Data abstractions (lists/2D lists) to manage complexity
- `CRD-2.B` — Implementing algorithms in a programming language
- `CRD-2.J` — Testing and debugging

**Starter Code Skeleton:**

```python
import tkinter as tk
import random

class Minesweeper:

    def __init__(self, root):
        self.root  = root
        self.root.title("<<YOUR NAME>> Minesweeper")
        self.size  = 6
        self.mines = 6

        # TODO: Create instance variables for:
        # self.score, self.high_score, self.moves (list), self.flags (set)

        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack()
        self.create_board()

    def create_board(self):
        self.buttons = []
        for r in range(self.size):
            row = []
            for c in range(self.size):
                btn = tk.Button(self.grid_frame, width=3, height=1)
                btn.grid(row=r, column=c)
                btn.bind("<Button-1>", lambda e, r=r, c=c: self.click(r, c))
                btn.bind("<Button-3>", lambda e, r=r, c=c: self.flag(r, c))
                row.append(btn)
            self.buttons.append(row)
        self.place_mines()

    def place_mines(self):
        self.mine_locations = set()
        # TODO: Randomly place self.mines mines in mine_locations

    def count_mines(self, r, c):
        count = 0
        # TODO: Check 8 surrounding cells; count mines
        return count

    def click(self, r, c):
        # TODO: Prevent clicking flagged or already-revealed cells
        # TODO: If mine → game_over(); else reveal number
        # TODO: If count == 0 → reveal_empty(r, c)
        # TODO: Update score and moves list
        pass

    def reveal_empty(self, r, c):
        # TODO: Recursive flood-fill to reveal adjacent empty cells
        pass

    def flag(self, r, c):
        # TODO: Toggle flag on/off; limit flags to self.mines count
        pass

    def game_over(self):
        # TODO: Reveal all mines; disable all buttons
        pass

root = tk.Tk()
game = Minesweeper(root)
root.mainloop()
```

**Extensions (Choose Any):**
- Flagging system with right-click 🚩
- High score tracking
- Timer scoring
- Difficulty levels: Easy (6×6), Medium (8×8), Hard (10×10)
- Win screen
- Save/load high score to file

**Grading Rubric (10 Points)**

| Criteria | Points |
|---|---|
| Mine placement algorithm works correctly | 1 |
| Nearby mine counting algorithm works | 2 |
| Flagging system implemented and limited | 2 |
| Empty region reveal (recursion) | 2 |
| Lists/sets used for tracking game data | 1 |
| Program runs correctly; tested and debugged | 1 |
| Reflection (text file) | 1 |
| **Total** | **10** |

**Reflection (1 page):** Explain your mine-counting algorithm, how recursion works in the reveal function, and how lists are used for data abstraction.

---

# Certification Alignment Reference

## PCEP-30-02 Exam Topic Map

| PCEP Objective | Topics | Covered In |
|---|---|---|
| **1.1** | Interpreter, compiler, lexis, syntax, semantics | Section 1 — How Python Works |
| **1.2** | Keywords, indentation, comments | Section 1 — Python Structure |
| **1.3** | Literals, variables, numeral systems, PEP-8 | Section 1 — Variables & Data Types |
| **1.4** | Operators, precedence, Boolean, bitwise, type casting | Section 1 — Operators |
| **1.5** | `print()`, `input()`, `sep=`, `end=`, `int()`, `float()` | Section 1 — I/O |
| **2.1** | `if`, `if-else`, `if-elif-else`, nested conditionals | Section 2 — Conditionals |
| **2.2** | `while`, `for`, `range()`, `break`, `continue`, `pass`, `else` | Section 2 — Loops |
| **3.1** | Lists, indexing, slicing, methods, comprehensions, 2D lists | Section 3 — Lists |
| **3.2** | Tuples, immutability, nesting | Section 3 — Tuples |
| **3.3** | Dictionaries, keys/values/items, iteration | Section 3 — Dictionaries |
| **3.4** | Strings, indexing, slicing, escaping, methods | Section 3 — Strings |
| **4.1** | Functions, `return`, `None`, recursion | Section 4 — Functions |
| **4.2** | Parameters, arguments, defaults, scope, `global`, shadowing | Section 4 — Functions |
| **4.3** | Exception hierarchy: `BaseException`, `Exception`, `ValueError`, etc. | Section 4 — Exceptions |
| **4.4** | `try-except`, ordering branches, propagation | Section 4 — Exceptions |

---

## AP CSP Standards Alignment

| AP CSP Standard | Description | Covered In |
|---|---|---|
| **CRD-2.A** | Program design and development | Throughout |
| **CRD-2.B** | Implement algorithms | Functions, OOP, Projects |
| **CRD-2.G** | Call procedures | Functions |
| **CRD-2.J** | Test and debug | Debugging, Exception Handling |
| **AAP-2.E** | Sequencing, selection, iteration | Control Flow |
| **AAP-2.F** | Mathematical operations | Operators |
| **AAP-2.G** | Abstraction to manage complexity | Functions, Modules, OOP |
| **AAP-2.K** | List iteration | Lists |
| **AAP-3.A** | Collect and represent data | Data Structures |
| **AAP-3.B** | Use abstractions to organize data | Dictionaries, OOP, Lists |
| **AAP-3.C** | Analyze data to draw conclusions | Data Structures |
| **AAP-4.A** | Data abstractions for complexity | Lists, 2D Lists, Classes |

---

*Document maintained for AP CSP and PCEP-30-02 certification alignment.*
*Revised June 2026*
