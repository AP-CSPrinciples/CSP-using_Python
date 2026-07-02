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

**All Projects and Assignments Must Include a Header Block:**

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
# Python Basics 
```Revised March 2026```

Python is an open-source programming language that is one of the easiest programs that a person can learn for their first programming language.  Python is a versatile programming language that can be used in many areas such as data analysis, science, web development, AI, and IoT.  As of 2024, it is one of the most in demand programming languages in the market place.  Python is a high-level programming language that offers simplicity, readability, and versatility.  Python supports multiple programming paradigms and has an extensive library that simplifies coding tasks. Python has a robust community and documentation support that enables beginners to excel quickly in this language.   

We will be looking at syntax and structures of Python. We will use an Integrated Development Environment to develop our code in this course.  


## Python Style Guidelines

<details><summary>Click Here</summary>




[**PEP 8 Guidelines**](https://peps.python.org/pep-0008/) is the official style guide for Python code and covers naming conventions, code layout, and indentation.  These style guidelines, along with the examples and rationales, will help you write clean, readable, and maintainable code. 

**All Projects and assignments should have a header block for the teacher**

```python
#       Assignment:  Program [number]:  [Assignment Title]
#
#       Author:  [Your Name ]
#       Partner:  [Partner's Name ]
#
#       Course Name:  [Course Name]
#       Instructor:  John Smith
#       Due Date:  [Due Date and Time]
#
#       Description:  [Describe the program's goal, IN DETAIL.]
#
#       Language:  [ Python version 18]
#       Ex. Packages:  [List names and sources of all external packages
#                       required by this program.]
#
#       Deficiencies:  [If you know of any problems with the code, provide
#                      details here, otherwise clearly state that you know
#                      of no unsatisfied requirements and no logic errors.]
#
```


---

**1. Use Descriptive Variable and Function Names**
   - **Guideline**: Use descriptive names that make the purpose of the variable or function clear.
   - **Example**:
     ```python
     # Good
     total_cost = price * quantity
     
     # Bad
     x = p * q
     ```
   - **Rationale**: Code is more readable when variable names clearly indicate their purpose, making it easier to understand and maintain.

---

**2. Use Consistent Indentation (4 Spaces)**
   - **Guideline**: Use four spaces per indentation level; do not use tabs.
   - **Example**:
     ```python
     def calculate_area(radius):
         return 3.14 * radius ** 2
     ```
   - **Rationale**: Consistent indentation is essential for readability and prevents syntax errors.

---

**3. Limit Line Length to 79 Characters**
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

---

**4. Use Blank Lines to Separate Code Sections**
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

---

**5. Use Docstrings to Document Functions, Classes, and Modules**
   - **Guideline**: Use triple-quoted strings (`"""`) for all public modules, functions, classes, and methods.
   - **Example**:
     ```python
     def calculate_area(radius):
         """Calculate the area of a circle given its radius."""
         return 3.14 * radius ** 2
     ```
   - **Rationale**: Docstrings provide useful explanations of code functionality, which helps future readers and collaborators.

---

**6. Use Spaces Around Operators**
   - **Guideline**: Use spaces around operators and after commas, but not directly inside parentheses.
   - **Example**:
     ```python
     # Good
     result = (a + b) * (c - d)

     # Bad
     result=(a+b)*(c-d)
     ```
   - **Rationale**: Spacing around operators makes expressions easier to read.

---

**7. Avoid Excessive Nesting**
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

---

**8. Use List Comprehensions for Simple Operations**
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

---

**9. Handle Exceptions Properly**
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

---

**10. Use Meaningful Constants Instead of Magic Numbers**
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

---

**11. Avoid Global Variables**
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

---

**12. Use `is` for Comparison to `None`**
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

---

**13. Organize Imports Properly**
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

---

**14. Use Type Annotations (Python 3.5+)**
   - **Guideline**: Use type annotations to specify expected data types for function arguments and return values.
   - **Example**:
     ```python
     def calculate_total(cost: float, tax_rate: float) -> float:
         return cost * (1 + tax_rate)
     ```
   - **Rationale**: Type annotations make it clear what types are expected, which can help prevent bugs and improve readability. 

---

Following these guidelines helps ensure code that is easy to read, maintain, and understand across teams.


---
---


</details>


## Debugging Strategies


**1. Read the Error Message Carefully**

* Look at the **exact line number** and description.
* Identify whether the error is a **syntax error, runtime error, or logic error**.
* Focus first on the line mentioned, then check lines directly above it.

**2. Trace the Program Step-by-Step**

* Walk through the program **line by line**.
* Track variable values and program flow.
* Use paper or a table to simulate what the program does.

**3. Use Print Statements**

* Insert temporary `print` statements to display:

  * variable values
  * function outputs
  * checkpoints in the code
* This helps locate where the program behavior becomes incorrect.

Example:

```
print("Value of score:", score)
```

**4. Test with Simple Inputs**

* Start with **small, predictable test cases**.
* Use values where you already know the expected output.
* Gradually test more complex inputs.

**5. Isolate the Problem**

* Comment out or temporarily remove sections of code.
* Test smaller pieces individually.
* Determine **which specific section causes the issue**.

**6. Check Variables and Data Types**

* Confirm variables contain the **values you expect**.
* Verify correct **data types** (number, string, boolean, list).
* Look for accidental reassignment of variables.

**7. Review Logic and Conditions**

* Check `if` statements and loops carefully.
* Verify conditions are written correctly.
* Look for common mistakes:

  * incorrect comparison operators
  * misplaced parentheses
  * incorrect loop conditions.

**8. Rubber Duck Debugging**

* Explain the code **out loud** step-by-step.
* Pretend you are teaching the program to someone else.
* Often the mistake becomes obvious while explaining.

**9. Use Incremental Development**

* Write and test **small pieces of code at a time**.
* Ensure each part works before adding more features.

**10. Take a Break and Revisit**

* Step away briefly when stuck.
* Returning with fresh eyes often reveals simple mistakes.

**11. Ask for Help with Evidence**

Before asking a teacher or peer, students should be able to explain:

* What the program is **supposed to do**
* What it is **actually doing**
* What they **already tried to fix it**


### Student Debugging Checklist

Before asking for help, you should check the following:

☐ Read the error message

☐ Checked the line number and nearby code

☐ Added print/debug statements

☐ Tested with simple inputs

☐ Traced variables step-by-step

☐ Explained the code out loud (Rubber Ducky)


---


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

In Python, **variables** are used to store data, which can be used and manipulated throughout a program. **Data types** specify the kind of value a variable holds, determining what operations can be performed on it. <mark>Python automatically assigns a data type based on the value assigned to a variable</mark>.

**Python Variables**
A **variable** is essentially a name given to a memory location where data is stored. In Python, you **do not** need to declare the data type of a variable; you just assign a value to it, and Python infers the type.

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

## String Methods


**Beginner-Friendly String Methods**

| Method               | Description                     | Example                               |
| -------------------- | ------------------------------- | ------------------------------------- |
| `.lower()`           | Converts to lowercase           | `"HELLO".lower()` → `"hello"`         |
| `.upper()`           | Converts to uppercase           | `"hello".upper()` → `"HELLO"`         |
| `.strip()`           | Removes leading/trailing spaces | `"  hello  ".strip()` → `"hello"`     |
| `.replace(old, new)` | Replaces parts of a string      | `"cat".replace("c", "b")` → `"bat"`   |
| **`.split(separator)`**  | Splits string into list         | `"a b c".split()` → `["a", "b", "c"]` |
| **`len()`**              | Returns length of string        | `len("hello")` → `5`                  |

```python
if name.lower() == "admin":
    print("Welcome, admin!")
```


**Intermediate Methods (Great with Practice)**

| Method              | Description                           | Example                                         |
| ------------------- | ------------------------------------- | ----------------------------------------------- |
| `.find(substring)`  | Returns index of substring, or -1     | `"apple".find("p")` → `1`                       |
| `.count(substring)` | Counts occurrences                    | `"banana".count("a")` → `3`                     |
| `.startswith(text)` | Checks if string starts with text     | `"hello".startswith("he")` → `True`             |
| `.endswith(text)`   | Checks if string ends with text       | `"file.txt".endswith(".txt")` → `True`          |
| **`.capitalize()`**    | Capitalizes the first letter          | `"python".capitalize()` → `"Python"`            |
| `.title()`          | Capitalizes first letter of each word | `"my name is joe".title()` → `"My Name Is Joe"` |


**Optional for Advanced Learners**

| Method        | Description                               | Example                                          |
| ------------- | ----------------------------------------- | ------------------------------------------------ |
| **`.isalpha()`**  | Checks if all characters are letters      | `"abc".isalpha()` → `True`                       |
| **`.isdigit()`**  | Checks if all characters are numbers      | `"123".isdigit()` → `True`                       |
| `.isalnum()`  | Letters or numbers only                   | `"abc123".isalnum()` → `True`                    |
| **`.join(list)`** | Joins a list into a string with separator | `" ".join(["Hello", "world"])` → `"Hello world"` |



**At minimum, you should know the following:**

* `.lower()`
* `.upper()`
* `.strip()`
* `.replace()`
* `len()`
* `.split()`


---


**Indexing in Python**

**Definition**: Indexing lets you access individual characters in a string using square brackets `[]`.

***Note**: Python uses **zero-based indexing** – the first character is at position `0`.

**Examples:**

```python
name = "Alice"
print(name[0])  # Output: 'A' (first character)
print(name[1])  # Output: 'l'
print(name[4])  # Output: 'e' (fifth character)
```

**Negative Indexing:**

```python
print(name[-1])  # Output: 'e' (last character)
print(name[-2])  # Output: 'c' (second to last)
```


**Slicing in Python**

**Definition**: Slicing lets you extract a **substring** using a start and end index:

```python
string[start:end]
```

The **start is included**, but the **end is excluded**.

**Examples:**

```python
word = "Python"
print(word[1:4])  # Output: 'yth' (characters at index 1, 2, 3)
print(word[:3])   # Output: 'Pyt' (start at 0 by default)
print(word[2:])   # Output: 'thon' (go to end)
print(word[:])    # Output: 'Python' (entire string)
```

**With Negative Indices:**

```python
print(word[-4:-1])  # Output: 'tho' (characters from index -4 to -2)
```


**Quick Visualization:**

| Character | P  | y  | t  | h  | o  | n  |
| --------- | -- | -- | -- | -- | -- | -- |
| Index     | 0  | 1  | 2  | 3  | 4  | 5  |
| Negative  | -6 | -5 | -4 | -3 | -2 | -1 |

---


**Practice Programs to test your understanding:**

```python
"Mad Libs" with string concatenation
Greeting program that capitalizes user input
Word counter using .split() and len()
Simple login screen with string comparison
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


---

**Operator Precedence in Python**

Python’s precedence rules are designed to make expressions behave intuitively. Here’s the order of precedence, from highest to lowest:

1. **Parentheses** (`()`)
2. **Exponentiation** (`**`)
3. **Arithmetic Operators**: Multiplication (`*`), Division (`/` and `//`), and Modulus (`%`)  
4. **Arithmetic Operators**: Addition (`+`) and Subtraction (`-`)
5. **Relational Operators**: `<`, `<=`, `>`, `>=`, `==`, `!=`
6. **Logical Operators**: `not`, `and`, `or`

Understanding this precedence order and the **left-to-right** evaluation rule allows for correctly interpreting complex expressions in Python. Following these rules helps ensure that Python evaluates each part of an expression as intended, providing accurate and predictable results.

The following table summarizes the [**operator precedence**](http://docs.python.org/py3k/reference/expressions.html#expression-lists) from *highest to lowest*. A complete table for the entire language can be found in the Python Documentation.  

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
print(result)  # Output: 10.0
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




> ***NOTE:*** **Why Division Returns a Float**: In Python 3, the `/` operator always returns a float, even if both operands are integers. This is to provide accurate results without unexpected truncation. For integer-only results, Python offers the `//` operator (floor division).
> 
> The `/` operator preserves fractional results, which is especially helpful in complex calculations, while `//` discards the decimal part.
> 
> **Example**:
>             ```python
>                result = 7 / 2  # Output: 3.5 (float)
>                result = 7 // 2  # Output: 3 (integer)
>             ```

---

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



<details><summary>Compound Boolean Expressions</summary> 


**Compound Boolean Expressions**

Compound Boolean expressions are used when you need to make a decision that depends on multiple conditions being true or false. They’re particularly useful in programming and data queries to add complex logic to condition-checking statements. 

1. Using **AND**
   ```python
   age = 25
   has_license = True
   is_eligible = age >= 18 and has_license
   ```
   **Explanation**: Here, `is_eligible` will be `True` only if both conditions are `True`. In this case, `age >= 18` and `has_license` both need to be `True` for `is_eligible` to be `True`. If `age` is less than 18 or `has_license` is `False`, `is_eligible` will be `False`.

2. Using **OR**
   ```python
   temperature = 35
   raining = False
   go_for_walk = temperature >= 20 or raining
   ```
   **Explanation**: The variable `go_for_walk` will be `True` if either `temperature >= 20` or `raining` is `True`. With `OR`, only one of the conditions needs to be `True` for the overall expression to evaluate as `True`.

3. Combining **AND** and **OR**
   ```python
   is_weekend = True
   has_free_time = False
   is_tired = False
   can_go_hiking = is_weekend and (has_free_time or not is_tired)
   ```
   **Explanation**: In this case, `can_go_hiking` is `True` if it is the weekend (`is_weekend` is `True`) **and** either there is free time (`has_free_time`) **or** the person is not tired (`not is_tired`). This example shows how parentheses can group parts of a compound Boolean expression to control evaluation order.

4. Using **NOT**
   ```python
   is_student = False
   has_discount = not is_student
   ```
   **Explanation**: The expression `not is_student` reverses the Boolean value of `is_student`. If `is_student` is `False`, `has_discount` will be `True`. The **NOT** operator is useful for negating a condition.

5. Complex Condition with Multiple **AND/OR/NOT**
   ```python
   age = 30
   is_member = True
   has_discount_coupon = False
   gets_discount = (age > 25 or is_member) and not has_discount_coupon
   ```
   **Explanation**: This expression checks if someone can get a discount. They qualify if they are older than 25 or are a member, but they should not have a discount coupon already. The expression `(age > 25 or is_member)` will evaluate first, and then `not has_discount_coupon` will apply, which must be `True` for `gets_discount` to be `True`.

6. Nested Compound Boolean Expression
   ```python
   score = 80
   attendance = 90
   has_passed = (score >= 70 and attendance >= 80) or (score >= 60 and attendance >= 90)
   ```
   **Explanation**: Here, `has_passed` will be `True` if either of these conditions is met:
   - The score is at least 70 and attendance is at least 80.
   - The score is at least 60 and attendance is at least 90.
   
   This kind of expression is useful when there are multiple pathways to meet a requirement.

</details>

----------------------------------------------------------------------



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


* **AP CSP Standards:**

  * **AAP-2.E:** Develop algorithms using sequencing, selection, and iteration.

    * *Example:* `math.sqrt()` can be part of a calculation sequence or algorithm.
  * **AAP-2.F:** Use mathematical operations in algorithms.

    * *Example:* Using arithmetic operations, powers, or square roots.

  * **AAP-2.E:** Develop algorithms using sequencing, selection, and iteration.

    * *Example:* `random.randint()` used in loops or conditional logic.
  * **AAP-2.G:** Use abstraction to manage complexity in algorithms.

    * *Example:* Wrapping random logic in a function to simplify code.

  * **AAP-3.A:** Collect and represent data digitally.

    * *Example:* Parsing JSON into Python dictionaries or lists.
  * **AAP-3.B:** Use abstractions to organize and process data.

    * *Example:* Using dictionaries or lists to hold JSON data.
  * **AAP-3.C:** Analyze data to draw conclusions.

    * *Example:* Accessing JSON fields and performing calculations or counts.
   

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

```
math Module: Provides mathematical functions.
    Example:

    import math
    print(math.sqrt(16))  # Output: 4.0

datetime Module: Handles date and time manipulations.
    Example:

    import datetime
    print(datetime.datetime.now())  # Output: Current date and time

random Module: Used for generating random numbers.
    Example:

    import random
    print(random.randint(1, 10))  # Output: Random integer between 1 and 10

os Module: Provides functions to interact with the operating system.
    Example:

    import os
    print(os.getcwd())  # Output: Current working directory

sys Module: Provides access to system-specific parameters and functions.
    Example:

    import sys
    print(sys.version)  # Output: Python version

re Module: Used for working with regular expressions.
    Example:

    import re
    pattern = r"\bword\b"
    text = "Find the word in this sentence."
    match = re.search(pattern, text)
    print(match.group())  # Output: 'word'

json Module: Used for parsing JSON data.
    Example:

    import json
    data = '{"name": "John", "age": 30}'
    parsed_data = json.loads(data)
    print(parsed_data['name'])  # Output: John

collections Module: Provides specialized container data types, like Counter, defaultdict, and namedtuple.
    Example:

    from collections import Counter
    data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(Counter(data))  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

numpy Package (external): Used for numerical computations, especially for array operations.
    Example:

    import numpy as np
    array = np.array([1, 2, 3])
    print(np.mean(array))  # Output: 2.0

pandas Package (external): Used for data analysis and manipulation.
    Example:

    import pandas as pd
    data = {'Name': ['John', 'Jane'], 'Age': [28, 24]}
    df = pd.DataFrame(data)
    print(df)

tkinter Module: Used for creating graphical user interfaces (GUIs) in Python.
    Example:

    import tkinter as tk

    # Create the main window
    root = tk.Tk()
    root.title("Simple Tkinter Window")

    # Create a label
    label = tk.Label(root, text="Enter your name:")
    label.pack()

    # Create an entry box
    entry = tk.Entry(root)
    entry.pack()

    # Create a button that updates the label with the entry text
    def update_label():
        name = entry.get()
        label.config(text=f"Hello, {name}!")

    button = tk.Button(root, text="Greet Me", command=update_label)
    button.pack()

    # Start the GUI event loop
    root.mainloop()
```

---

> **Summary**
> Modules are single files with Python code, useful for organizing and reusing functions, classes, or variables.  
> Packages are directories containing multiple related modules and an __init__.py file, which make large projects
> more manageable and prevent naming conflicts.  Using modules and packages keeps Python code modular, readable,
> and reusable, making it easier to structure and manage projects.


---


## Control Flow & Conditional Statements

**Control flow** determines **which code runs, when, and how often**.
It allows your program **make decisions**, **repeat actions**, or **branch** based on the conditions.


1. **What Is Control Flow?**

Control flow structures include:

* **Conditional Statements** → Decide *which* block of code to run
* **Loops** → Repeat code *while* a condition holds
* **Branching Keywords** → Jump or skip parts of the code


2. **Conditional Statements**

Used to **test conditions** (True or False) and run specific code blocks.

**Basic `if` Statement**

```python
if condition:
    # code runs if condition is True
```

**Example:**

```python
age = 18
if age >= 18:
    print("You're an adult.")
```


**`if-else` Statement**

```python
if condition:
    # if True
else:
    # if False
```

**Example:**

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```



**`if-elif-else` (Multiple Conditions)**

```python
if condition1:
    # if condition1 is True
elif condition2:
    # if condition1 is False and condition2 is True
else:
    # if none are True
```

**Example:**

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```



3. **Comparison Operators**

Used to form conditions.

| Operator | Meaning          | Example  |
| -------- | ---------------- | -------- |
| `==`     | equal to         | `x == 5` |
| `!=`     | not equal to     | `x != 5` |
| `>`      | greater than     | `x > 5`  |
| `<`      | less than        | `x < 5`  |
| `>=`     | greater or equal | `x >= 5` |
| `<=`     | less or equal    | `x <= 5` |



4. **Logical Operators**

Used to combine multiple conditions.

| Operator | Meaning                   | Example                         |
| -------- | ------------------------- | ------------------------------- |
| `and`    | both must be True         | `x > 0 and x < 10`              |
| `or`     | at least one must be True | `x < 0 or x > 10`               |
| `not`    | reverses a condition      | `not(x > 5)` → True if `x <= 5` |



**Nested Conditionals**

Putting one conditional inside another.

```python
if score >= 70:
    if score >= 90:
        print("A or A+")
    else:
        print("Pass")
else:
    print("Fail")
```

> 💡 Nesting too much can make code hard to read — consider using `elif` instead when possible.



6. **Indentation Matters in Python**

Python uses **indentation** (usually 4 spaces) to show what code is **inside** the `if`, `else`, or loop block.

```python
if is_sunny:
    print("Wear sunglasses")  # indented = inside
print("Have a nice day!")     # outside
```



**Control Flow Summary**

| Concept            | Description                                |
| ------------------ | ------------------------------------------ |
| `if`               | Runs code if condition is True             |
| `else`             | Runs code if condition is False            |
| `elif`             | Adds extra conditions                      |
| `==`, `!=`, etc.   | Compare values                             |
| `and`, `or`, `not` | Combine or modify conditions               |
| Indentation        | Controls which code belongs to which block |



**Example: Simple Login Check**

```python
username = input("Enter username: ")

if username == "admin":
    print("Access granted")
else:
    print("Access denied")
```

---
---


### Loops


Loops let you **repeat blocks of code**.  This is useful when working with lists, strings, or running a task multiple times.

**Types of Loops in Python**

1. **`for` Loop**

Used to loop through a **sequence** (like a list, string, or `range()`).

**Basic Syntax:**

```python
for item in sequence:
    # code to repeat
```

**Example:**

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

**With `range()`:**

```python
for i in range(3):
    print(i)
```

> Output: `0 1 2`

---

2. **`while` Loop**

Repeats code **while a condition is `True`**.

**Basic Syntax:**

```python
while condition:
    # code to repeat
```

**Example:**

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

---

**Loop Control Keywords**

| Keyword    | Purpose                               | Example               |
| ---------- | ------------------------------------- | --------------------- |
| `break`    | Exit the loop early                   | `if x == 3: break`    |
| `continue` | Skip to the next iteration            | `if x == 2: continue` |
| `pass`     | Placeholder that does nothing         | `if x == 2: pass`     |
| `else`     | Runs if loop finishes without `break` | `else: print("Done")` |

---

### Nested Loops

A **nested loop** is a loop **inside another loop**. The inner loop completes **all its iterations for each outer loop cycle**.

**Syntax:**

```python
for outer in outer_range:
    for inner in inner_range:
        # nested loop body
```



**Example 1: Nested `for` Loops (Multiplication Table)**

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()  # new line after inner loop
```

**Output:**

```
1 2 3 
2 4 6 
3 6 9
```



**Example 2: Nested Loops with Strings**

```python
words = ["hi", "hello"]
for word in words:
    for letter in word:
        print(letter, end=" ")
    print()
```

**Output:**

```
h i 
h e l l o 
```



**Example 3: Nested `while` + `for`**

```python
x = 0
while x < 2:
    for y in range(3):
        print(f"x={x}, y={y}")
    x += 1
```


**Choosing the Right Loop**

| Use this | When...                                      |
| -------- | -------------------------------------------- |
| `for`    | You know how many times to loop (e.g. lists) |
| `while`  | You loop until something changes             |
| Nested   | You need combinations, grids, or pairs       |



**Summary**

| Keyword     | Description                       |
| ----------- | --------------------------------- |
| `for`       | Loop through a sequence           |
| `while`     | Loop while a condition is true    |
| `break`     | Exit loop immediately             |
| `continue`  | Skip to next iteration            |
| `pass`      | Do nothing (placeholder)          |
| `else`      | Runs if loop ends without `break` |
| Nested loop | Loop inside another loop          |


---


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


**Sample Output**

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


#### More Methods

As was stated before, **methods** are functions that belong to `objects` and are used to operate on those objects. They are similar to functions but have a special relationship with the object they belong to, known as the **instance**.

Let's break down the key concepts:

1. **Instance Methods**
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

2. **Class Methods**
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

3. **Static Methods**
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

4. **Special Methods (Magic Methods)**
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

5. **Method Chaining**
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

**Key Points to Remember**
- *Instance Methods*: Operate on individual objects and use `self`.
- *Class Methods*: Operate on the class itself and use `cls`.
- *Static Methods*: Do not operate on instances or the class; they're independent but grouped within the class.
- *Special Methods*: Have specific purposes within Python's syntax (e.g., `__init__` for initialization, `__str__` for string representation).

Methods make object-oriented programming in Python powerful, allowing objects to encapsulate both data and functionality.


---


### Procedures

In Python, a **procedure** is a function that performs a task **without returning a value**. It's called for its **side effects**, such as printing text, updating a file, or modifying a global variable. *It doesn't give anything back to the caller.*


---


**Python Procedure**

```python
def greet_user():
    print("Welcome to the program!")
```

How to call a procedure:

```python
greet_user()
```

**Sample Output**
```
Welcome to the program!
```



#### Comparing Function Members

| Term          | Python Form                         | Returns a Value? | Used For                           | Example                               |
| ------------- | ----------------------------------- | ---------------- | ---------------------------------- | ------------------------------------- |
| **Method**    | Function **inside an object/class** | ✅/❌ Depends      | Performing actions on objects      | `"hello".upper()` → returns `"HELLO"` |
| **Procedure** | `def` without `return`              | ❌ No             | Doing a task with side effects     | `print("Hi")` or `greet_user()`       |
| **Function**  | `def` with `return`                 | ✅ Yes            | Calculating and returning a result | `def add(a, b): return a + b`         |



---

## Data Structures


Python provides a variety of built-in data structures to store and organize data, each optimized for specific types of operations. Here’s an overview of the core data structures in Python and examples of how and when each might be used in real-world applications.

**AP CSP Standards**

**AAP-3.A: Collect and represent data digitally.**
*Example:* Use variables, lists, or dictionaries to store information.

```python
# List of student names
students = ["Alice", "Bob", "Charlie"]

# Dictionary mapping names to ages
ages = {"Alice": 14, "Bob": 15, "Charlie": 14}
```

**AAP-3.B: Use abstractions to organize and process data.**
*Example:* Use a list of dictionaries to manage multiple records instead of separate variables.

```python
students = [
    {"name": "Alice", "age": 14},
    {"name": "Bob", "age": 15},
    {"name": "Charlie", "age": 14}
]
```

**AAP-3.C: Analyze data to draw conclusions.**
*Example:* Loop through a list or dictionary to compute averages or counts.

```python
# Count students age 14
count = sum(1 for student in students if student["age"] == 14)
print(count)  # Output: 2
```

**AAP-2.E: Develop algorithms using sequencing, selection, and iteration.**
*Example:* Iterate over data structures to implement logic.

```python
for student in students:
    if student["age"] > 14:
        print(student["name"])
```

**AAP-2.G: Use abstraction to manage complexity in algorithms.**
*Example:* Wrap repeated operations on data structures in functions.

```python
def count_age(students, age):
    return sum(1 for student in students if student["age"] == age)

print(count_age(students, 14))  # Output: 2
```


**1. Lists (`list`)**
A **list** is an ordered, mutable collection that allows duplicate elements. It’s the most versatile data structure in Python and can store any data type.

**Real-World Example: Shopping Cart in E-commerce**
In an online shopping cart, each item the user adds can be stored in a list. Since the order and the ability to add/remove items matter, a list is ideal here.

```python
shopping_cart = ["laptop", "mouse", "keyboard"]
shopping_cart.append("headphones")  # Add an item
shopping_cart.remove("mouse")       # Remove an item
print(shopping_cart)  # Output: ['laptop', 'keyboard', 'headphones']
```

**Why Use a List?**
- **Best for**: Ordered, changeable collections.
- **When to Use**: Managing items in a specific order where additions and removals are frequent.

**2. Tuples (`tuple`)**
A **tuple** is an ordered, immutable collection, which means its values cannot be changed after creation. Tuples are often used to store related data.

**Real-World Example: GPS Coordinates**
Tuples are ideal for storing data that shouldn’t change, such as latitude and longitude coordinates for locations.

```python
coordinates = (40.7128, -74.0060)  # New York City
print(coordinates)  # Output: (40.7128, -74.0060)
```

**Why Use a Tuple?**
- **Best for**: Fixed sets of related data.
- **When to Use**: When you need a collection that shouldn’t be modified, like configuration data or coordinate points.

**3. Sets (`set`)**
A **set** is an unordered collection with no duplicate elements. Sets are useful when you need to eliminate duplicate data or perform set operations like union, intersection, and difference.

**Real-World Example: Unique Users in a System**
In a web application, sets can store unique user IDs to ensure each user appears only once.

```python
user_ids = {101, 102, 103, 101}  # Duplicate '101' is ignored
print(user_ids)  # Output: {101, 102, 103}
```

**Why Use a Set?**
- **Best for**: Collections of unique elements.
- **When to Use**: When duplicates need to be removed, or you need to perform set operations.

**4. Dictionaries (`dict`)**
A **dictionary** is an unordered collection of key-value pairs. It’s useful for storing data that you want to look up by a unique key.

**Real-World Example: Product Catalog in E-commerce**
Dictionaries are perfect for storing product information where each product ID maps to a product’s details.

```python
product_catalog = {
    "P001": {"name": "Laptop", "price": 1000},
    "P002": {"name": "Mouse", "price": 25},
    "P003": {"name": "Keyboard", "price": 50}
}
print(product_catalog["P001"]["name"])  # Output: Laptop
```

**Why Use a Dictionary?**
- **Best for**: Key-value pair data.
- **When to Use**: Fast lookups of values by keys, such as a database record by ID or configuration settings.

**5. Stacks (`list` or `collections.deque`)**
A **stack** follows the Last-In, First-Out (LIFO) principle. You can implement a stack using a `list` (with `.append()` and `.pop()` methods) or with `deque` from the `collections` module.

**Real-World Example: Undo Feature in Text Editor**
In text editors, the undo functionality is often implemented with a stack where each user action is stored as a new item on the stack. When the user presses "undo," the most recent action is popped from the stack.

```python
actions = ["type A", "type B", "type C"]
actions.append("type D")   # Latest action
last_action = actions.pop()  # Undo the last action
print(last_action)  # Output: type D
```

**Why Use a Stack?**
- **Best for**: Last-In, First-Out operations.
- **When to Use**: Undo/redo features, function call tracking, and navigation history.

**6. Queues (`collections.deque` or `queue.Queue`)**
A **queue** follows the First-In, First-Out (FIFO) principle. You can implement a queue with `deque` from `collections` or `Queue` from `queue` module for thread-safe operations.

**Real-World Example: Print Queue in Office**
In an office printer system, documents to be printed are often handled with a queue where the first document sent is printed first.

```python
from collections import deque

print_queue = deque(["Document1", "Document2", "Document3"])
print_queue.append("Document4")  # Add a document to the queue
first_document = print_queue.popleft()  # Print (remove) the first document
print(first_document)  # Output: Document1
```

**Why Use a Queue?**
- **Best for**: First-In, First-Out operations.
- **When to Use**: Task scheduling, order processing, and any process where items need to be processed in the order received.

**7. Linked Lists (Custom Implementation)**
Python does not have a built-in linked list, but you can implement one. Linked lists are useful for dynamic memory allocation and data that frequently changes size.

**Real-World Example: Music Playlist**
In a music player, a playlist could be implemented as a linked list where each song node points to the next song. This allows easy addition or removal of songs.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

# Usage
playlist = LinkedList()
playlist.append("Song 1")
playlist.append("Song 2")
```

**Why Use a Linked List?**
- **Best for**: Data that needs frequent insertion and deletion.
- **When to Use**: Implementing playlists, managing memory in embedded systems, or when resizing overhead is a concern.

**8. Heaps (`heapq`)**
A **heap** is a special tree structure used to maintain a priority queue. In Python, `heapq` implements a min-heap by default.

**Real-World Example: Priority Queue for Emergency Services**
In emergency dispatch, a priority queue (heap) could prioritize patients by the severity of their condition.

```python
import heapq

emergency_queue = []
heapq.heappush(emergency_queue, (2, "Patient B"))  # Priority 2
heapq.heappush(emergency_queue, (1, "Patient A"))  # Priority 1 (higher)
heapq.heappush(emergency_queue, (3, "Patient C"))  # Priority 3

# Remove the patient with the highest priority (lowest number)
highest_priority_patient = heapq.heappop(emergency_queue)
print(highest_priority_patient)  # Output: (1, 'Patient A')
```

**Why Use a Heap?**
- **Best for**: Priority-based operations.
- **When to Use**: Scheduling tasks based on priority, pathfinding algorithms, and load balancing.

**Summary Table**

| Data Structure | Best Use Case                           | Real-World Instance                                |
|----------------|----------------------------------------|---------------------------------------------------|
| List           | Ordered collections                    | Shopping cart, to-do list                         |
| Tuple          | Immutable sets of data                 | GPS coordinates, fixed configuration              |
| Set            | Unique elements                       | Unique usernames, eliminating duplicates          |
| Dictionary     | Key-value mappings                     | Product catalog, contact list                     |
| Stack          | LIFO operations                        | Undo in text editor                               |
| Queue          | FIFO operations                        | Print queue, task scheduling                      |
| Linked List    | Frequent insertions/deletions          | Music playlist, dynamic data size                 |
| Heap           | Priority-based operations              | Emergency dispatch, priority scheduling           |



Choosing the right data structure depends on the specific needs of the application, such as order, mutability, uniqueness, or priority.

---


## Lists and List Manipulation

*AP CSP Learning Goals*
- AAP-4.A: Use data abstractions to manage complexity.

For this class, we will not be using tuples, but you should be familiar with how they are used and the difference of a list.

|      | Indexing | Ordered | Mutable | Duplicate |
|------------|---------------|----------------|------------------------------------|----------------|
| List | <ul><li><mark>[X] Yes</mark></li><li>[ ] No</li></ul> | <ul><li><mark>[X] Yes</mark></li><li>[ ] No</li></ul> | <ul><li><mark>[X] Yes</mark></li><li>[ ] No</li></ul> | <ul><li><mark>[X] Yes</mark></li><li>[ ] No</li></ul> |
| Tuple | <ul><li><mark>[X] Yes</mark></li><li>[ ] No</li></ul> | <ul><li><mark>[X] Yes</mark></li><li>[ ] No</li></ul> | <ul><li>[ ] Yes</li><li>[X] No</li></ul> | <ul><li><mark>[X] Yes</mark></li><li>[ ] No</li></ul> |
| Set |  <ul><li>[ ] Yes</li><li>[X] No</li></ul> | <ul><li>[ ] Yes</li><li>[X] No</li></ul> | <ul><li>[ ] Yes</li><li>[X] No</li></ul> | <ul><li>[ ] Yes</li><li>[X] No</li></ul> |
| Dictionary |  <ul><li>[ ] Yes</li><li>[X] No</li></ul> | <ul><li><mark>[X] Yes</mark></li><li>[ ] No</li></ul> | <ul><li><mark>[X] Yes</mark></li><li>[ ] No</li></ul> | <ul><li>[ ] Yes</li><li>[X] No</li></ul> |


In Python, lists are **indexed** collections, meaning each item in a list has a specific position. Python uses **zero-based indexing**, which means the first element is accessed with index `0`, the second with `1`, and so on. Python also supports **negative indexing**, where `-1` refers to the last item, `-2` to the second-to-last, and so forth.

**Example of indexing POTATO**

```
__________________________________________________
string1 =    |  P  |  O  |  T  |  A  |  T  |  O  |

pos_index #  0     1     2     3     4     5     6
neg_index # -7    -6    -5    -4    -3    -2    -1
__________________________________________________
```


Take a look at the program snippets below:


**1. Program to Print the Index of the First Occurrence of the Letter 'T' in "POTATO"**

This program finds the index of the first occurrence of 'T' in the word "POTATO."

```python
word = "POTATO"
index_of_T = word.index("T")  # Finds the first occurrence of 'T'
print("Index of first 'T' in POTATO:", index_of_T)
```

**Output**:
```
Index of first 'T' in POTATO: 2
```

**2. Program to Print All Instances (Indices) of 'T' in "POTATO"**

This program will find and print the index of each occurrence of 'T' in the word "POTATO."

```python
word = "POTATO"
indices_of_T = [index for index, letter in enumerate(word) if letter == "T"]

print("All indices of 'T' in POTATO:", indices_of_T)
```

**Output**:
```
All indices of 'T' in POTATO: [2, 4]
```

**3. Program to Print the First 3 Letters of the Word "POTATO"**

This program extracts and prints the first 3 letters of the word "POTATO" using slicing.

```python
word = "POTATO"
first_three_letters = word[:3]  # Slicing to get the first three letters
print("First 3 letters of POTATO:", first_three_letters)
```

**Output**:
```
First 3 letters of POTATO: POT
```

**4. Program to Print "TOP" Using Reverse Indexing**

Using reverse indexing, this program prints the letters "T," "O," and "P" in reverse order to form "TOP."

```python
word = "POTATO"
reverse_top = word[-6:-3] # Reverse indexing to get 'T', 'O', 'P'
print("TOP using reverse indexing:", reverse_top)
```

**Output**:
```
TOP using reverse indexing: TOP
```

Explanation:
- `word[-3]` starts at end of index negative three but does not include the item within -3.
- `word[-4]` accesses the negative fourth letter in the index, "T".
- `word[-5]` accesses the negative fifth letter in the index, "O".
- `word[-6]` accesses the negative sixth letter in the index, "P".

<mark>NEED COMMENT ON PROGRAM INDEXs ABOVE</mark>

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

*AP CSP Learning Goal:*
- AAP-2.B: Use data stored in files.


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


### Classes/ Objects


In Python, the concepts of classes, objects, attributes, methods, and constructors are fundamental to object-oriented programming (OOP). 

**1. Class**

A **class** in Python is like a blueprint for creating objects (an instance of). It defines attributes (properties) and methods (functions) that objects created from the class will have.  A class encapsulates data and functions that operate on that data.

**Keyword**: `class`

**Example:**

```python
class Car:
    pass  # Empty class definition for now
```

**2. Object**

An **object** is an instance of a class. It's a specific, individual entity created based on the 
blueprint (class). You can think of it as a real-world object that embodies the attributes and behaviors 
of its class.

**Creating an Object**:
To create an object, you instantiate the class.

**Example:**

```python
my_car = Car()  # Creating an object (instance) of class Car
```

**3. Attributes**

Attributes are variables that belong to a class or an object. They represent the state or 
properties of an object. There are two types of attributes:

* **Instance Attributes**: These are unique to each instance of a class.
* **Class Attributes**: These are shared across all instances of the class.

**Keyword**: `self`

**Example:**

```python
class Car:
    def __init__(self, make, model, year):  # Constructor to initialize attributes
        self.make = make  # Instance attribute
        self.model = model  # Instance attribute
        self.year = year  # Instance attribute
```

**4. Methods**

Methods are functions that belong to a class and define behaviors that the objects of the 
class can perform. Methods typically take the `self` parameter, which refers to the current instance 
of the class.

**Keyword**: `def`

**Example:**

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now running.")
    
    def stop_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now off.")
```

**5. Constructors**

A **constructor** is a special method called `__init__` in Python that is automatically invoked when an 
object is created from a class. It’s used to initialize the attributes of the new object.

**Keyword**: `__init__`

**Example:**

```python
class Car:
    def __init__(self, make, model, year):  # Constructor
        self.make = make
        self.model = model
        self.year = year
```

---

#### Putting It All Together

**Multiple Classes, Objects, Constructors, Methods, and Attributes**

**Class 1: `Car`**

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make  # Instance Attribute
        self.model = model  # Instance Attribute
        self.year = year  # Instance Attribute

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now running.")

    def stop_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now off.")
```

**Class 2: `Person`**

```python
class Person:
    def __init__(self, name, age, occupation):
        self.name = name  # Instance Attribute
        self.age = age  # Instance Attribute
        self.occupation = occupation  # Instance Attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I am a {self.occupation}.")

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")
```

**Creating Objects and Using Methods**

```python
# Creating objects (instances of classes)
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2020)

person1 = Person("Alice", 30, "Engineer")
person2 = Person("Bob", 25, "Designer")

# Using methods
car1.start_engine()
car2.stop_engine()

person1.greet()
person2.have_birthday()
```

**Output:**

```
The 2022 Toyota Corolla's engine is now running.
The 2020 Honda Civic's engine is now off.
Hello, my name is Alice and I am an Engineer.
Happy Birthday, Bob! You are now 26 years old.
```

---

**Key Vocabulary:**

* **Class**: A blueprint for creating objects.
* **Object**: An instance of a class.
* **Attributes**: Variables that store data associated with objects (can be instance or class attributes).
* **Methods**: Functions that define behaviors associated with objects (usually take `self` as the first argument).
* **Constructor**: A special method `__init__` that initializes attributes when a new object is created.


---

**Creating Input for the user using OOP**

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make  # Instance Attribute
        self.model = model  # Instance Attribute
        self.year = year  # Instance Attribute

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now running.")

    def stop_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now off.")

class Person:
    def __init__(self, name, age, occupation):
        self.name = name  # Instance Attribute
        self.age = age  # Instance Attribute
        self.occupation = occupation  # Instance Attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I am a {self.occupation}.")

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")


# Function to create a car object based on user input
def create_car():
    print("\nEnter the details for the car:")
    make = input("Make: ")
    model = input("Model: ")
    year = int(input("Year: "))
    return Car(make, model, year)

# Function to create a person object based on user input
def create_person():
    print("\nEnter the details for the person:")
    name = input("Name: ")
    age = int(input("Age: "))
    occupation = input("Occupation: ")
    return Person(name, age, occupation)

# Main program to create and interact with the objects
def main():
    # Create Car and Person objects based on user input
    car1 = create_car()
    car2 = create_car()
    
    person1 = create_person()
    person2 = create_person()

    # Use the methods on the objects
    car1.start_engine()
    car2.stop_engine()

    person1.greet()
    person2.have_birthday()

# Run the main program
if __name__ == "__main__":
    main()
```



1. **User Input for Car**: The `create_car()` function asks the user for the car's make, model, and year.
2. **User Input for Person**: The `create_person()` function prompts the user for the person's name, age, and occupation.
3. **Creating Objects**: The objects (`Car` and `Person`) are created by calling these functions, which return the new objects with the user-specified attributes.
4. **Using Methods**: The methods for `Car` and `Person` objects are called as before, but now with user-provided data.


**Example Output:**

```
Enter the details for the car:
Make: Ford
Model: Mustang
Year: 2021

Enter the details for the car:
Make: Chevrolet
Model: Camaro
Year: 2020

Enter the details for the person:
Name: Sarah
Age: 29
Occupation: Doctor

Enter the details for the person:
Name: John
Age: 35
Occupation: Artist

The 2021 Ford Mustang's engine is now running.
The 2020 Chevrolet Camaro's engine is now off.
Hello, my name is Sarah and I am a Doctor.
Happy Birthday, John! You are now 36 years old.
```

---

Another example and explanation of a program that demonstrates the use of classes, objects, and constructors.

**A Simple Bank Account System**

```python
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

""" -------------------------** Module ** ------------------------- """
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

```

**Explanation**

1. **Main Program**:
   - The main program creates an account, displays account information, performs deposits and withdrawals, and handles invalid transactions gracefully.

2. **Class**:
   - `class BankAccount:` defines a class named `BankAccount`. A class is a blueprint for creating objects, encapsulating data and methods that operate on that data.

3. **Constructor**:
   - The `__init__` method is a special method called the constructor. It is invoked when an object of the class is created. In this example, it initializes the account holder's name and balance:
     - `account_holder`: A string representing the name of the account holder.
     - `balance`: A float representing the initial balance of the account (default is 0).

4. **Instance Variables**:
   - `self.account_holder` and `self.balance` are instance variables that store the account holder's name and balance for each instance of the `BankAccount` class.

5. **Methods**:
   - `deposit(amount)`: This method adds a specified amount to the account balance, ensuring the amount is positive.
   - `withdraw(amount)`: This method subtracts a specified amount from the balance, ensuring the withdrawal does not exceed the current balance.
   - `get_balance()`: Returns the current balance of the account.
   - `display_account_info()`: Displays the account holder's information and current balance.

6. **Objects**:
   - `account1 = BankAccount("Alice Smith", 1000)`: This line creates an instance (object) of the `BankAccount` class with "Alice Smith" as the account holder and an initial balance of $1000.


Copy and paste this code into a Python environment. It will create a bank account for "Alice Smith," allowing you to see how deposits and withdrawals affect the balance.


Below is a program that demonstrates the use of objects and classes to represent dogs. It includes constructors with no arguments, one argument, and two arguments.

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

### Basic Lambda Syntax


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


---


## Recursion

Recursion is a fundamental concept in programming where a function calls itself to solve smaller instances of a problem. In Python 3.x, recursion is straightforward but needs careful handling to avoid infinite loops or exceeding the recursion limit. Let’s break it down.

---

## How Recursion Works

1. **Base Case**: This is the condition under which the recursive function stops calling itself. Without it, recursion would go on indefinitely.
2. **Recursive Case**: This is where the function calls itself with a smaller or simpler input.

Python keeps track of each function call on the **call stack**, so each call has its own local variables and execution state. When a base case is reached, Python unwinds the stack, returning results back up the chain.

---

**Example 1: Factorial**

Factorial of `n` (denoted `n!`) is `n * (n-1) * ... * 1`.

```python
def factorial(n):
    if n == 0:  # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive call

print(factorial(5))  # Output: 120
```

**Explanation**:

* `factorial(5)` calls `factorial(4)`, which calls `factorial(3)` … until `factorial(0)`.
* Then the stack starts returning results: `1 → 1*1 → 2*1 → 3*2 → 4*6 → 5*24 → 120`.

---

**Example 2: Fibonacci Sequence**

Fibonacci numbers: `0, 1, 1, 2, 3, 5, 8…`

```python
def fibonacci(n):
    if n <= 1:  # base case
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # recursive calls

print(fibonacci(6))  # Output: 8
```

**Explanation**:

* `fibonacci(6)` calls `fibonacci(5)` and `fibonacci(4)` and so on, breaking the problem into smaller subproblems.

> **Note:** This naive Fibonacci recursion has exponential time complexity. Iterative or memoized approaches are better for large `n`.

---

**Example 3: Sum of a List**

```python
def sum_list(lst):
    if not lst:  # base case: empty list
        return 0
    else:
        return lst[0] + sum_list(lst[1:])  # recursive call on the rest of the list

print(sum_list([1, 2, 3, 4]))  # Output: 10
```

---

> **Key Points**
>
> * Python has a recursion limit (`sys.getrecursionlimit()`), default ~1000. Deep recursion can cause `RecursionError`.
> * Recursive functions are elegant for problems naturally defined in smaller subproblems (like trees, graphs, divide-and-conquer algorithms).
> * Always define a base case to prevent infinite recursion.


**Recursive Call Stack for `factorial(3)`**

```
factorial(3)
  -> 3 * factorial(2)
           -> 2 * factorial(1)
                     -> 1 * factorial(0)
                               -> 1 (base case)
```

**Unwinding the Stack (Returning Values)**

```
factorial(0) returns 1
factorial(1) returns 1 * 1 = 1
factorial(2) returns 2 * 1 = 2
factorial(3) returns 3 * 2 = 6
```

**Visual Diagram** 

```
Call Stack (Top -> Bottom):

| factorial(3) |  <- waiting for factorial(2)
| factorial(2) |  <- waiting for factorial(1)
| factorial(1) |  <- waiting for factorial(0)
| factorial(0) |  <- base case reached
```

* Each layer waits for the next recursive call to return.
* Once the base case is hit, Python **pops the stack** and computes the result as it returns.


---


## Mini Minesweeper Project

**Project Overview**

In this project, you will build a simplified version of the classic **Minesweeper game** using Python and Tkinter.  The player will click cells in a grid trying to **avoid hidden mines**. Safe cells show the number of nearby mines. The player may also **place flags** where they believe a mine exists.  You will implement the logic that makes the game work.

**Project Objectives**

1. Generate a game board - 6 × 6 grid
2. Place mines randomly
3. Count adjacent mines
4. Allow player moves
5. Score that increases for safe clicks
6. List that records player moves
7. Game over if a mine is clicked
8. Reveal tiles
9. Determine win or loss
10. Try Again” button to reset the game


---


*AP CSP Learning Goals*
- AAP-2.E: Develop algorithms using sequencing, selection, and iteration.
- AAP-4.A: Use data abstractions to manage complexity.
- CRD-2.B: Implement algorithms in a programming language.
- CRD-2.J: Test and debug programs.

**Concepts Used**

- Lists and 2D Lists
- Nested Loops
- Conditional Logic
- Random Numbers
- Algorithms

**2D Grid Using Lists:** Grid structure stored as a ***list of lists***. 

Example board:
```python
board = [
    [" "," "," "],
    [" ","*"," "],
    [" "," "," "]
]
```

```python
self.buttons[r][c]
```

---

**Random Mine Placement:** Places mines in random grid locations.

Example:

```python
import random

row = random.randint(0,2)
col = random.randint(0,2)

board[row][col] = "*"
```

---

**List for Tracking Moves:** Stores every location the player has clicked.

```python
self.moves = []
self.moves.append((r,c))
```

---


**Score Tracking:** Score increases when the player safely clicks a square.

```python
self.score += 1
```

---

**Random Mine Placement:** Places mines in random grid locations.

```python
random.randint(0, SIZE-1)
```

---

**Student Project Extensions:**

* Add **flagging system (right-click 🚩)**
* Limit number of flags
* Reveal **empty regions automatically**
* Show **high score**
* **timer scoring system**
* Add **win screen**
* **save/load high score file**
* Change grid level of difficulty
  * Easy (6×6)
  * Medium (8×8)
  * Hard (10×10)


---


**Student Starter Code:**

Complete sections marked **TODO**.

```python
import tkinter as tk
import random

class Minesweeper:

    def __init__(self, root):

        self.root = root
        self.root.title("<<YOUR NAME>> Minesweeper")

        self.size = 6
        self.mines = 6

        # TODO
        # Create variables for:
        # score
        # high score
        # moves list
        # flags set

        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack()

        self.create_board()

    # ---------------------------------
    # Create Grid
    # ---------------------------------

    def create_board(self):

        self.buttons = []

        for r in range(self.size):

            row = []

            for c in range(self.size):

                btn = tk.Button(self.grid_frame,
                                width=3,
                                height=1)

                btn.grid(row=r, column=c)

                # left click
                btn.bind("<Button-1>", lambda e, r=r, c=c: self.click(r,c))

                # right click
                btn.bind("<Button-3>", lambda e, r=r, c=c: self.flag(r,c))

                row.append(btn)

            self.buttons.append(row)

        self.place_mines()

    # ---------------------------------
    # Place Mines
    # ---------------------------------

    def place_mines(self):

        self.mine_locations = set()

        # TODO
        # Write code that randomly places mines
        # into mine_locations


    # ---------------------------------
    # Count Nearby Mines
    # ---------------------------------

    def count_mines(self, r, c):

        count = 0

        # TODO
        # Write algorithm that checks surrounding cells
        # Return number of nearby mines

        return count


    # ---------------------------------
    # Click Cell
    # ---------------------------------

    def click(self, r, c):

        # TODO
        # Prevent clicking flagged cells

        # TODO
        # Check if the cell contains a mine
        # If it does -> end game

        # TODO
        # Otherwise show number of nearby mines

        # TODO
        # Update score


        count = self.count_mines(r,c)

        self.buttons[r][c].config(text=str(count))

        # TODO
        # If count == 0
        # reveal surrounding cells


    # ---------------------------------
    # Reveal Empty Region
    # ---------------------------------

    def reveal_empty(self, r, c):

        # TODO
        # Create recursive algorithm that reveals
        # surrounding cells when there are no mines nearby

        pass


    # ---------------------------------
    # Flagging System
    # ---------------------------------

    def flag(self, r, c):

        # TODO
        # Add flag if square not revealed
        # Limit number of flags

        pass


    # ---------------------------------
    # Game Over
    # ---------------------------------

    def game_over(self):

        # TODO
        # Reveal all mines
        # Disable board

        pass


root = tk.Tk()
game = Minesweeper(root)
root.mainloop()
```


---

**Grading Rubric (10 Points)**

| Criteria                                      | Points |
| --------------------------------------------- | ------ |
| Mine placement algorithm works correctly      | 1      |
| Nearby mine counting algorithm works          | 2      |
| Flagging system implemented and limited       | 2      |
| Empty region reveal algorithm                 | 2      |
| Use of lists/sets to track game data          | 1      |
| Program runs correctly and is tested/debugged | 1      |
| Reflection (txt file)                         | 1      |
| **Total Points**                              | 10     |


**Reflection: 1-page explanation:** 

* their mine counting algorithm
* how recursion works in the reveal function
* how lists are used for data abstraction
