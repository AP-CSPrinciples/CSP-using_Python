# Python Basics
```Revised August 2026 — Reorganized for CSP-First-Semester / PCEP-Second-Semester```

Python is an open-source, high-level programming language that is widely considered one of the best first languages to learn. It supports multiple programming paradigms — including **procedural**, **functional**, and **object-oriented programming (OOP)** — and is backed by an enormous standard library and community. As of 2024, it is one of the most in-demand languages in the job market, used in web development, data science, artificial intelligence, IoT, and cybersecurity.

This course is designed to prepare you for:
- 🎯 **AP Computer Science Principles (AP CSP)** — College Board performance task and exam
- 🏅 **PCEP™ – Certified Entry-Level Python Programmer** (Exam PCEP-30-02, OpenEDG Python Institute)

> **How to use this document — READ THIS FIRST:** Topics are now organized around **when you need them for the AP CSP Create Performance Task (CPT)**, not around the PCEP exam blueprint. Everything you need to write, test, and explain your CPT program lives in the main body of this document (Sections 1–4, File Operations, Data Structures, OOP). PCEP-only exam content that isn't required for the CPT — numeral systems, bitwise operators, built-in functions like `map`/`filter`, lambda functions, frozensets, and the full exception hierarchy tree — has been moved to **[PCEP Certification Path — Semester 2](#pcep-certification-path-semester-2)** at the end of this document, where you'll study it at a slower pace *after* the CPT is done, over the second half of the year. PCEP exam objectives are labeled `🔖 PCEP` and AP CSP standards are labeled `📋 AP CSP`. Activities and projects are marked with `###`. New this revision: **🤔 Thinking Question** checkpoints after every new concept, a **📌 Worked Example** before every assignment, and **🧩 Scaffolding** checkpoints for multi-day projects.

---

## 📅 Python Pacing Guide — Semester 1 (AP CSP Focus)

`Aug 17 – Dec 18, 2026`

| Week | Dates | Content Focus | Notebook Spread | Activities / Projects | PT / CPT In-Class Time | Weekly Min |
|:---:|:---:|:---|:---:|:---|:---:|:---:|
| 1 | Aug 17–21 | How Python Works; Style; Debugging; Variables & Data Types | Spreads 1 & 2 | — | — | 216 |
| 2 | Aug 24–28 | Variables (cont.); Operators | Spread 3 | Movie Ticket Eligibility Checker | — | 216 |
| 3 | Aug 31–Sep 4 | Print Statements & Input/Output | Spread 4 | Hello, World! Variations | — | 216 |
| 4 | Sep 7–11 | Conditional Statements | Spread 5 | Grade Calculator | — | 216 |
| 5 | Sep 14–18 | Loops | Spread 6 | Nested Loop Pattern Design Studio | — | 216 |
| 6 | Sep 21–25 | Strings | Spread 7 | Receipt Formatter | — | 216 |
| 7 | Sep 28–Oct 2 | Lists | Spread 8 | — | — | 216 |
| 8 | Oct 5–9 | Tuples & Dictionaries; **Practice PT 1 Introduced** | Spread 9 | Student Contact Book | 40 min (Fri) *Practice* | 216 |
| 9 | Oct 12–16 | Functions; Practice PT 1 in-class work | Spread 10 | Math Operations Calculator; Recursion Practice — Three Levels | 176 min (2×88) *Practice* | 216 |
| 10 | Oct 19–23 | Functions (cont.); Modules and Packages; Practice PT 1 in-class work | — | **Project:** Random Trivia Quiz Generator | 176 min (2×88) *Practice* | 216 |
| 11 | Oct 26–30 | Exception Handling; **Practice PT 1 Due (Fri)** | Spread 11 | Safe Calculator | 88 min (1×88) *Practice* | 216 |
| 12 | Nov 2–6 | File Operations; Data Structures (Sets, Stacks/Queues); **Practice PT 2 Introduced** | Spread 12 | Student Roster File Manager | 176 min (2×88) *Practice* | 216 |
| 13 | Nov 9–13 | OOP | Spread 13 | OOP Zoo (3 options) | 128 min (88+40) *Practice* | 216 |
| 14 | Nov 16–20 | **CPT Checklist Review & Practice PT 2 Workshop** (Mon/Wed); **Practice PT 2 Due (Fri)** | — | — | 40 min (Fri) *Practice* | 216 |
| 15 | Nov 23–27 | **THANKSGIVING — No School** | — | — | — | — |
| 16 | Nov 30–Dec 4 | AP CSP CPT — Brainstorming Workshop | Spread 15 | CPT Brainstorming: students develop an **original** program idea | 216 min **Official CPT** | 216 |
| 17 | Dec 7–11 | AP CSP CPT — Writing Code, Recording Video, Developing PPR Responses | — | Official CPT Program (original idea, in progress) | 216 min **Official CPT** | 216 |
| 18 | Dec 14–18 | AP CSP CPT — Final Coding/Submission; **CPT Due (Fri, Dec 18)**; End-of-Course Reflection | Spread 16 | Official CPT Program (original idea, due) | 216 min **Official CPT** | 216 |

> **Practice PT 1 & 2** are formative — students write a full program to an actual College Board–style CPT prompt so they've rehearsed the task before the real one, but this time is **not counted** toward the AP CPT's official minimum. Practice PT 1 total ≈ 480 min (Weeks 8–11). Practice PT 2 total ≈ 344 min (Weeks 12–14). See **[AP CSP Performance Task Preparation](#ap-csp-performance-task-preparation)** below for idea lists for both.
>
> **Per AP College Board CPT requirements, the official CPT must be an original student idea.** Students may **not** submit Practice PT 1, Practice PT 2, or any other program they've already completed as their CPT — the program developed during Weeks 16–18 must be new. The Final Project Options (A/B/C) may still be offered as optional starting frameworks/scaffolds, but each student's actual CPT submission — the idea, the implementation, and the individual creative work behind it — must be their own original work developed within the official CPT window.
>
> **Official AP CSP CPT (the actual, submitted Create Performance Task) happens entirely in December**: Week 16 = brainstorming/planning an original idea, Week 17 = coding + video + PPR written responses, Week 18 = final coding, submission (due Fri, Dec 18), and course wrap-up — all three are full 5-day weeks.
> **Total Official CPT Time: 216 + 216 + 216 = 648 min (≈10.8 hrs) — clears the 9-hour College Board minimum with room to spare, entirely within December, even after setting aside time on the last day for End-of-Course Reflection.**
>
> ⚠️ **What changed from the previous version:** The old Week 14 PCEP exam-prep cram day is gone. PCEP-specific exam content (numeral systems, bitwise operators, built-in functions, lambdas, frozensets, the full exception hierarchy) has been pulled out of Semester 1 entirely — see the note above the pacing table. That gives Weeks 1–14 room to slow down, add more worked examples, and add the CPT-checklist workshop in Week 14 instead of a PCEP cram session. PCEP prep now happens at a sustainable pace across Semester 2 (Jan–June) in **[PCEP Certification Path — Semester 2](#pcep-certification-path-semester-2)**, after the CPT is behind you.

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

## Debugging Strategies

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

## Section 1 — Computer Programming and Python Fundamentals
`📋 AP CSP: CRD-2.A, CRD-2.B`

### How Python Works

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

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** Your program runs without crashing, but it prints the wrong total every time. Is this most likely a syntax error, a runtime error, or a logic error — and how do you know?

**Answer:** A **logic error**. Python ran the code successfully (no crash, no error message), so the syntax was fine and nothing "broke" at runtime — the program just did something other than what you intended. You'd fix this by tracing your math/logic step by step, not by looking for a typo.
</details>

## Python Keywords and Structure

`🔖 PCEP 1.2` — Understand Python's logic and structure

**Keywords** are reserved words that Python uses for specific purposes. You cannot use them as variable names. This is a reference table you'll come back to all year — bookmark it.

```
False    None     True     and      as       assert
async    await    break    class    continue def
del      elif     else     except   finally  for
from     global   if       import   in       is
lambda   nonlocal not      or       pass     raise
return   try      while    with     yield
```

**What each keyword does (quick-reference glossary):**

| Keyword | Purpose |
|---|---|
| `True` / `False` | The two Boolean values |
| `None` | Represents "no value" |
| `and` / `or` / `not` | Logical operators for combining/reversing conditions |
| `if` / `elif` / `else` | Conditional branching |
| `for` / `while` | Loop constructs |
| `break` / `continue` / `pass` | Loop control — exit early, skip an iteration, or do nothing |
| `def` | Defines a function |
| `return` | Sends a value back from a function |
| `class` | Defines a class (blueprint for objects) |
| `import` / `from` / `as` | Bring in code from modules |
| `try` / `except` / `finally` / `raise` | Exception handling |
| `in` | Membership test (`x in list`) or loop iteration (`for x in list`) |
| `is` | Identity comparison (same object in memory, not just equal value) |
| `global` / `nonlocal` | Change which variable scope a name refers to |
| `lambda` | Defines a small anonymous function *(PCEP deep dive — see Semester 2)* |
| `del` | Deletes a variable, list item, or dictionary key |
| `with` | Opens a resource (like a file) and guarantees it's closed afterward |
| `assert` | Checks that a condition is true; raises an error if not (used in testing) |
| `yield` / `async` / `await` | Advanced generator/async syntax — not used in this course |

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

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** You write `if True print("hi")` and Python refuses to run it before ever touching the print statement. What's missing, and what category of error is this?

**Answer:** The colon `:` after the condition is missing — every `if`, `for`, `while`, `def`, and `class` header needs one. This is a **syntax error**: Python can't even understand the structure of the line, so it never gets far enough to try running it.
</details>

### Variables and Data Types

`🔖 PCEP 1.3` — Introduce literals and variables
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

> 🔖 **PCEP note:** binary/octal/hex numeral systems (writing integers in different bases) are a PCEP-only topic and are covered in depth in **[PCEP Certification Path — Semester 2](#pcep-certification-path-semester-2)**. You don't need them for the CPT.

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** `age = "25"` then later `total = age + 5`. What happens, and why?

**Answer:** Python raises a `TypeError`, because `age` is a **string** `"25"`, not an integer — Python won't automatically add a string and an int together. You'd need `total = int(age) + 5` to cast the string to an int first. This exact bug is extremely common with `input()`, since `input()` always returns a string.
</details>

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

**`==` vs. `is`**

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

> <mark>**Rule of thumb:** use `is` / `is not` only for identity checks — most importantly `x is None` (the Python standard, preferred over `x == None`). Use `==` for comparing values (numbers, strings, list contents, etc.).</mark>

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

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** `age = 17` and `has_ticket = False`. Evaluate `age >= 18 or has_ticket` and `age >= 18 and has_ticket` by hand before running any code. Are they the same?

**Answer:** No. `or` only needs **one** side to be `True`; here both sides are `False` (`17 >= 18` is `False`, `has_ticket` is `False`), so `or` evaluates to `False`. `and` needs **both** sides `True`, so it's also `False` here — but that's a coincidence of these particular values. Try `age = 20`: `or` → `True` (first side is true), `and` → `False` (second side is still false). The two operators behave very differently once one side is `True`.
</details>

> 📌 **Worked Example — compound booleans in a different context (game achievement unlock)**
>
> ```python
> player_level = int(input("Enter player level: "))
> completed_tutorial = input("Completed the tutorial? (yes/no): ")
> difficulty = input("Difficulty (easy/normal/hard): ")
>
> # Unlocked if the player is high level, OR a beginner who finished the tutorial on easy
> is_veteran = player_level >= 10
> is_ready_beginner = completed_tutorial == "yes" and difficulty == "easy"
>
> achievement_unlocked = is_veteran or is_ready_beginner
>
> if achievement_unlocked:
>     print("Achievement unlocked!")
> else:
>     print("Keep playing to unlock this achievement.")
> ```
> Notice the strategy: break a complex rule into smaller boolean variables (`is_veteran`, `is_ready_beginner`) *before* combining them with `or`. That "smaller pieces first" approach is what you'll use to build the Movie Ticket assignment's own — different — discount rule below.

### Activity: Movie Ticket Eligibility Checker

Write a program that determines whether a person can buy a discounted movie ticket, using **compound boolean expressions** (`and`, `or`, `not`).

**🧩 Scaffolding — build it in this order:**
1. First, just get `age` and `has_id` from the user and `print()` them back to confirm your input works.
2. Write and test the `is_child_or_senior` condition alone — print it and check against a few ages by hand.
3. Write and test the `is_discounted_student` condition alone the same way.
4. Combine them into `gets_discount` and print the correct message.
5. Only then add the second theater/adult-present check from Requirement 4 below.

**Requirements:**

1. Ask the user for their age and whether they have a student ID (`yes`/`no`).
2. A ticket is discounted if the person is **under 13, OR over 65, OR (between 13–25 AND has a student ID)**.
3. Store the result of that full condition in a single boolean variable, e.g. `gets_discount = ...`, then print `"Discount applies!"` or `"Full price."` based on its value.
4. Add a second check: the theater is closed to anyone under 6 with **no adult present** — ask a follow-up question and use `not` to write the condition for "an adult is NOT present."
5. Print a trace of your boolean logic as a comment above each condition, explaining what it evaluates in plain English (this mirrors how you'll need to explain conditions in your AP CSP written responses).

**Starter code:**
```python
#       Assignment:  Program 1: Movie Ticket Eligibility Checker
#       Author:      [Your Name]
#       Course Name: AP Computer Science Principles
#       Description: Determines movie ticket discount eligibility using
#                    compound boolean expressions.
#       Language:    Python 3.x

# TODO 1) Get age (as int) and has_id ("yes"/"no") from the user

# TODO 2) Build is_child_or_senior

# TODO 3) Build is_discounted_student

# TODO 4) Combine into gets_discount and print the result

# TODO 5) Add the under-6/no-adult-present check
```

**Submit your .py file and test cases showing that your program worked as intended.**

*PCEP: 1.4 | AP CSP: AAP-2.F*

---

### Assignment — Print Statements and Input/Output

📋 **AP CSP: CRD-2.B** — Implement algorithms in a programming language.

**What is an f-string?**

An f-string ("formatted string literal") lets you embed variables and expressions directly inside a string, instead of gluing pieces together with `+` or placeholders. You create one by putting the letter `f` right before the opening quote:

```python
name = "Maya"
age = 15

print(f"{name} is {age} years old.")
# Output: Maya is 15 years old.
```

Anything inside curly braces `{ }` gets evaluated as Python code, and the result is inserted into the string as text — even if it wasn't a string to begin with. That's why `age` (an int) doesn't need `str()` conversion here — the f-string handles that automatically.

**Why "f"?**

The `f` tells Python "this string has live code inside it." Without the `f`, curly braces are just literal characters:

```python
print("{name} is {age} years old.")
# Output: {name} is {age} years old.   ← not what you want!

print(f"{name} is {age} years old.")
# Output: Maya is 15 years old.        ← the f makes the magic happen
```

**You can put more than just variables inside `{ }`**

Since the braces run real Python code, you can do math, call functions, or even index into things:

```python
print(f"Next year you'll be {age + 1}.")
# Output: Next year you'll be 16.

print(f"Your name in caps: {name.upper()}")
# Output: Your name in caps: MAYA
```

**Formatting numbers with `:`**

A colon inside the braces lets you control *how* the value looks — decimal places, padding, commas, etc.

```python
pi = 3.14159
print(f"Pi rounded: {pi:.2f}")
# Output: Pi rounded: 3.14

big_number = 1000000
print(f"With commas: {big_number:,}")
# Output: With commas: 1,000,000
```

This is one of the biggest advantages f-strings have over `.format()` and concatenation.

**Comparing all three methods side by side**

```python
name = "Maya"
age = 15

# f-string
print(f"{name} is {age} years old.")

# .format()
print("{} is {} years old.".format(name, age))

# concatenation
print(name + " is " + str(age) + " years old.")
```

All three print the same thing, but notice:

- **f-string** — variables live right where they're used, so it's the easiest to read, and no manual type conversion is needed.
- **`.format()`** — variables are listed separately at the end, so for a long sentence you have to count placeholders to match them up.
- **concatenation** — works, but gets messy fast, and you must remember `str()` for anything that isn't already a string (a common bug source — forgetting it raises a `TypeError`).


**NOTE:** f-strings became the preferred style starting in Python 3.6.

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** Why does `print(name + " is " + age + " years old.")` crash if `age` is an `int`, but `print(f"{name} is {age} years old.")` works fine with the exact same `age` variable?

**Answer:** The `+` operator for strings requires **both sides to already be strings** — Python won't silently convert an `int` for you with `+`, so it raises a `TypeError`. An f-string's `{ }` braces run an implicit conversion to text for whatever value lands inside them, so `age` doesn't need to be pre-converted. This is one of the biggest practical advantages of f-strings.
</details>


**Overview**

Python gives you several ways to build and display output. In this assignment
you'll practice four of them — f-strings, the `format()` method, string
concatenation, and the `sep=`/`end=` keyword parameters — by completing the
TODOs embedded in the starter code below. This time, `name` and `age` come
from the user instead of being hardcoded, so you'll also practice reading
input from the console.


**NOTE: User Input**

```python
name = input("Enter your name: ")          # always returns a string
age  = int(input("Enter your age: "))      # convert to int
price = float(input("Enter price: "))      # convert to float
```

---

**`sep`** = — controls what goes between multiple arguments

By default, print() joins multiple comma-separated arguments with a single space. **`sep=`** lets you override that separator.

```python
print("A", "B", "C")            # A B C   (default **`sep=`**" ")
print("A", "B", "C", sep="-")   # A-B-C
print("A", "B", "C", sep="")    # ABC
print(2026, 8, 20, sep="/")     # 2026/8/20
```

Each comma-separated item is a separate argument — **`sep`** only affects the space between them, not anything else about the string.

**`end`**= — controls what goes after the whole print call

By default, print() ends every call with a newline ("\n"), which is why each print() normally starts a new line. <mark>end= replaces that trailing newline with whatever string you give it.</mark>

```python
print("Hello")
print("World")
```
**Sample Output:** 
```python
Hello
World
```

```python
print("Hello", end="! ")
print("World")
```
**Sample Output:**
```python
Hello! World
```

Here, the first print() doesn't move to a new line — it ends with "! " instead — so the second print() continues right where the first left off.

Together:

```python
print("A", "B", "C", sep="-", end=" | ")
print("D", "E", "F", sep="-")
```
**Sample Output**
A-B-C | D-E-F

---


**Starter code**

```python
"""
Activity:    Print Statements and Input/Output
Author:      [Your Name]
Course Name: AP Computer Science Principles
Date:        M/D/Yr
Description: Practice using f-string, .format(), concatenation, & sep/ end
Language:    Python 3.x
"""

# TODO 0) Use input() to ask the user for their name, and store it in a
#         variable called name. Then use input() again to ask for their
#         age, and store it in a variable called age.
#         Remember: input() always returns a string — you'll need to
#         convert age to an int before you can use it in math, but the
#         examples below only print it, so str()/f-string formatting
#         will handle that part for you.


# TODO 1) f-strings (most readable — preferred method)
#         Use an f-string to print a sentence that includes both
#         `name` and `age`.


# TODO 2) format() method
#         Print the same sentence as TODO 1, but built with the
#         .format() method instead of an f-string.


# TODO 3) Concatenation
#         Print the same sentence again, this time using the + operator
#         to concatenate strings. Remember: non-string values (like age)
#         must be converted with str() before you can concatenate them.


# TODO 4) sep= keyword parameter
#         Print the letters "A", "B", and "C" as three separate
#         arguments to print(), using sep="-" so the output reads:
#         A-B-C


# TODO 5) end= keyword parameter
#         Print "Hello" using end="! " so that it does NOT start a new
#         line, then print "World" right after it on the same line.
#         The combined output should read:
#         Hello! World
```

**Requirements**

- [ ] TODO 0) Collect `name` and `age` using `input()`
- [ ] TODO 1) Print `name` and `age` in a sentence using an f-string
- [ ] TODO 2) Print the same sentence using the `.format()` method
- [ ] TODO 3) Print the same sentence using string concatenation (`+`), converting `age` with `str()`
- [ ] TODO 4) Print `"A"`, `"B"`, `"C"` as separate arguments with `sep="-"` so the output reads `A-B-C`
- [ ] TODO 5) Print `"Hello"` with `end="! "`, then print `"World"` so the output reads `Hello! World` on one line
- [ ] **Submit your .py file and test cases showing that your program worked as intended.**

**Reflection question**

All three of TODO 1–3 produce the *same* sentence on screen, but they're
written three different ways. Which method did you find easiest to read and
write, and why do you think f-strings are considered the preferred method in
modern Python?

> <mark>**Reminder:** `input()` always returns a `str`. You must use `int()` or `float()` to convert it for math operations.</mark>

---

### Assignment: Mad Libs — String Formatting Showdown

> **Standards:** Output formatting — f-strings, string concatenation, `.format()`, `print()` `sep`/`end` parameters
> 
> ***Objective***
> 
> Students will build a **Mad Libs**–style story generator that collects user input and displays the finished story using **four different output-formatting techniques** in > > > Python: f-strings, string concatenation, the `.format()` method, and `print()`'s `sep`/`end` parameters. By the end of the assignment, students should be able to explain the > tradeoffs between each method and choose the right one for a given situation.
> 
> **Overview**
> 
> Students write a program that:
> 1. Prompts the user for a series of words (nouns, verbs, adjectives, etc.) using `input()`
> 2. Builds a **10-sentence story** using those words
> 3. Prints the story back to the user — but very the "block" sequence of the story. You must use a *different* formatting method for each sentence.  Consecutive sentences cannot use the same format.  
> 
> **Requirements**
> 
> | Sentences | Required Technique | Notes |
> |---|---|---|
> | 1–4 | f-strings | `f"You went to the {place}..."` |
> | 1–2 | String concatenation (`+`) | Must convert non-strings with `str()` where needed |
> | 1–4 | `.format()` method | Use either positional `{}` or named `{noun}` placeholders |
> | 1–2 | `print()` with `sep` and `end` | Build the sentence from multiple `print()` arguments, not a single string |
> 
> - **10 sentences**, forming a single coherent(ish) story — silliness encouraged
> - At least **8 different user inputs** collected (nouns, adjectives, verbs, adverbs, numbers, exclamations, etc.)
> - Every input variable must be used **at least once**
> - Story must include at least one number input, displayed correctly in all four formatting styles at some point (tests `str()`/type-awareness)
> 
> **Steps**
> 
> 1. Plan your story on paper first — write the 10 sentences with blanks, and decide which 8+ words you'll ask for.
> 2. Write all your `input()` statements first and store them in clearly named variables.
> 3. Build the story section by section, following the technique table above.
> 4. Test by running the program and filling in silly words — does the story read correctly and grammatically?
> 5. Add the required header block (below) to the top of your file.
> 6. Submit your `.py` file with test cases.
> 
> **Grading Focus**
> 
> - Correct, working use of all four formatting techniques (not just syntactically present — actually executed correctly)
> - Appropriate `str()` conversions where needed to avoid type errors
> - Code comments marking each section
> - Story is complete, coherent, and uses every collected input
> - Header block present and filled out
> 
> 
> **Header Block**
> 
> Place this at the top of your `.py` file before any code:
> 
> ```python
> """
> Activity:    Mad Libs using f-String
> Author:      [Your Name]
> Course Name: AP Computer Science Principles
> Date:        M/D/Yr
> Description: Mad Libs
> Language:    Python 3.x
> """
> ```
>


<details>
  
<summary>MadLibs Example</summary>



```
================================================================================
Activity:     Mad Libs using f-String
Author:       [EXEMPLAR — NOT A STUDENT SUBMISSION]
Course Name:  AP Computer Science Principles
Date:         2026-08-25
Description:  Demonstrates f-strings, string concatenation, the .format()
              method, and print() sep/end parameters within one Mad Libs
              story. Built to model the REQUIRED FORMAT of the assignment —
              not to be copied.
Language:     Python 3.14
================================================================================

  ****************************  TEACHER NOTE  *********************************
  This file is an EXEMPLAR only. Students must CANNOT submit this story, these
  variable names, or this sentence structure as their own work. Copying this
  story (with words swapped) or reusing this exact sentence pattern is a
  violation of the assignment's originality requirement — students must write
  their OWN 10-sentence story with their OWN chosen blanks. Use this only to
  see how the four formatting techniques should look when executed correctly.
  *******************************************************************************
```
```
# -----------------------------------------------------------------------
# SECTION 1: Collect user input
# -----------------------------------------------------------------------
name = input("Enter a person's name: ")
place = input("Enter a place: ")
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb (past tense): ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
adjective2 = input("Enter another adjective: ")
number = int(input("Enter a number: "))
exclamation = input("Enter an exclamation (e.g. Wow!): ")

# -----------------------------------------------------------------------
# SECTION 2: The story — technique VARIES every sentence.
# No two consecutive sentences use the same formatting method:
#   Sentence:   1  2  3  4  5  6  7  8  9  10
#   Technique:  F  M  F  C  M  P  F  C  M  P
#   (F = f-string, M = .format(), C = concatenation, P = print sep/end)
# -----------------------------------------------------------------------

# Sentence 1 — f-string
print(f"Once upon a time, {name} went to {place}.")

# Sentence 2 — .format()
print("{} was feeling very {} that day, and carried a {}.".format(
    name, adjective1, noun1))

# Sentence 3 — f-string
print(f"Suddenly, {name} {verb1} right past {number} {animal}s crossing the road!")

# Sentence 4 — string concatenation (+)
line4 = name + " skidded to a stop and shouted, " + '"' + exclamation + '"'
print(line4)

# Sentence 5 — .format()
print("There were exactly {0} {1}s staring back.".format(number, animal))

# Sentence 6 — print() with sep and end
print(name, "reached into a bag and pulled out a", food, sep=" ", end=".\n")

# Sentence 7 — f-string
print(f"The {adjective2} {animal} sniffed the {food} suspiciously.")

# Sentence 8 — string concatenation (+)
line8 = name + " counted all " + str(number) + " of them twice, just to be sure."
print(line8)

# Sentence 9 — .format()
print("{} laughed, dropped the {} and ran...".format(name, noun1))

# Sentence 10 — print() with sep and end
print("all", number, "the way back to", place, sep=" ", end="!\n")


--------------------------------------------------------------------------
SAMPLE RUN (inputs a student might type at each prompt, in order):
--------------------------------------------------------------------------
Enter a person's name: Priya
Enter a place: the grocery store
Enter an adjective: wobbly
Enter a noun: kazoo
Enter a verb (past tense): sprinted
Enter an animal: goose
Enter a food: burrito
Enter another adjective: suspicious
Enter a number: 7
Enter an exclamation (e.g. Wow!): Yikes!

--------------------------------------------------------------------------
RESULTING OUTPUT:
--------------------------------------------------------------------------
Once upon a time, Priya went to the grocery store.
Priya was feeling very wobbly that day, and carried a kazoo.
Suddenly, Priya sprinted right past 7 gooses crossing the road!
Priya skidded to a stop and shouted, "Yikes!"
There were exactly 7 gooses staring back.
Priya reached into a bag and pulled out a burrito.
The suspicious goose sniffed the burrito suspiciously.
Priya counted all 7 of them twice, just to be sure.
Priya laughed, dropped the kazoo and ran...
all 7 the way back to the grocery store!
--------------------------------------------------------------------------
```

</details>

*AP CSP: CRD-2.B*

---

## Section 2 — Control Flow: Conditional Blocks and Loops
`📋 AP CSP: AAP-2.E` — Develop algorithms using sequencing, selection, and iteration.

---


### Python Tutor – Code Visualizer

🔗 [Python Tutor Code Visualizer](https://pythontutor.com/visualize.html#mode=edit)

Python Tutor lets you watch your code run one step at a time instead of just seeing the final output. Paste in your code, hit "Visualize Execution," and then step forward and backward through each line while a diagram shows exactly what's happening behind the scenes — variable values, list contents, function calls, and how they change on every pass through a loop.

**Why it's useful:**
- **See loops in action** – Watch a variable's value update on each iteration instead of guessing what it "should" be.
- **Track variables visually** – Every variable appears in a box with its current value, updated live as the code executes.
- **Understand function calls** – See a new "frame" appear on the call stack each time a function is called, and watch it disappear when the function returns.
- **Debug faster** – When your code isn't doing what you expect, step through it to find the exact line where things go wrong.
- **No installation needed** – Runs entirely in your browser.

**How to use it:**
1. Paste your Python code into the editor.
2. Click **Visualize Execution**.
3. Use **Next >** and **< Back** to step through your program line by line.
4. Watch the variables and stack frames update in the visualization panel on the right.

**Best for:** <mark>Debugging loops (`for`/`while`), tracing small recursive functions, understanding how variables change over time, and figuring out why your code isn't producing the output you expect.</mark>

---

Want me to tailor this further — e.g., shorter for a slide, or expanded with a specific example (like tracing a `for` loop) matched to a lesson in your PCEP/AP CSP curriculum?

### Conditional Statements

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

> 📌 **Worked Example — before you build the Grade Calculator below**
>
> ```python
> temperature = int(input("Enter the temperature: "))
>
> if temperature >= 90:
>     print("Heat warning!")
> elif temperature >= 70:
>     print("Nice day.")
> elif temperature >= 50:
>     print("A bit cool.")
> else:
>     print("Bundle up!")
> ```
> 
> Trace it by hand:
> if `temperature` is `65`, Python checks `>= 90` (False),
> then `>= 70` (False),
> then `>= 50` (**True**) — so it prints `"A bit cool."` and skips every branch after.
> Only ONE branch of an `if-elif-else` chain ever runs.
> 

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

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** In an `if-elif-else` chain ordered from highest score to lowest (like the Grade Calculator above), what would go wrong if you accidentally wrote the conditions from lowest to highest instead (`score >= 60`, then `score >= 70`, etc.)?

**Answer:** Every score of 60 or above would immediately match the *first* branch (`score >= 60`) and print `"D"`, since Python stops at the first `True` condition in the chain and never checks the rest — a 95 would incorrectly get a "D" instead of an "A". Order matters in `elif` chains whenever the conditions overlap.
</details>

### Activity: Grade Calculator

Write a grade calculator that accepts a numerical score and outputs:
- The letter grade (A–F)
- Whether the student passed or failed
- A motivational message for scores below 70

Use `if-elif-else` and at least one nested conditional.

**🧩 Scaffolding — build it in this order:**
1. Get the score and print just the letter grade using `if-elif-else`.
2. Add the pass/fail message as a **separate** `if-else` (or nest it inside, per the requirements).
3. Add the motivational message only for scores below 70 — test with a score of exactly 69 and exactly 70 to make sure your boundary is correct.

**Starter code:**
```python
#       Assignment:  Program 2: Grade Calculator
#       Description: Prints a letter grade, pass/fail status, and a
#                    motivational message for low scores.
#       Language:    Python 3.x

score = int(input("Enter your score: "))

# TODO 1) if-elif-else chain for letter grade A-F

# TODO 2) pass/fail message (score >= 60 passes)

# TODO 3) motivational message only if score < 70
```

*AP CSP: AAP-2.E | PCEP: 2.1*

---

## Loops

`🔖 PCEP 2.2` — Perform different types of iterations
`📋 AP CSP: AAP-2.E` — Iteration; `AAP-2.K` — For loops

**The `for` Loop**

**Structure**

```python
for item in iterable:
    # code block (loop body)
    # runs once per item in the iterable
```

- **`item`** — a variable created by the loop; holds the current value on each pass
- **`iterable`** — any sequence or object you can step through: `range()`, a list, a string, a tuple, a dictionary, etc.
- The body must be indented (4 spaces, PEP 8) — indentation defines the block

**Common Forms**

```python
# Iterate over a range of numbers
for i in range(5):
    print(i)          # 0, 1, 2, 3, 4

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate with both index and value
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Iterate over a string, character by character
for char in "hello":
    print(char)

# Iterate over dictionary keys, values, or both
grades = {"Ana": 92, "Ben": 85}
for name, score in grades.items():
    print(name, score)
```

**When to Use a `for` Loop**

Use `for` when you know **what you're iterating over** — a fixed collection, a range of numbers, or anything with a defined, countable set of items. The loop naturally stops when it runs out of items, so you don't have to manage a stopping condition yourself.

**Reach for `for` when:**
- You're processing every item in a list, string, tuple, or dictionary
- You know (or can calculate) exactly how many times to repeat something
- You're building a new collection from an existing one
- You need a counter-controlled loop (`for i in range(n)`)

**Rule of thumb:** if you can describe the task as "for each item in this collection..." — it's a `for` loop.

**PCEP-30-02 / AP CSP Connection**

- `for` loops map to the **Control Flow** exam block (iteration statements)
- Understanding `range()` and `enumerate()` is directly tested on PCEP-30-02
- AP CSP frames this as **iteration over a defined data set** (Big Idea: Algorithms and Programming)

---


**The `while` Loop**

**Structure**

```python
while condition:
    # code block (loop body)
    # runs as long as condition is True
    # something inside the loop must eventually make condition False
```

- **`condition`** — any expression that evaluates to `True` or `False`
- The loop checks the condition **before** each pass; if it's `False` on the first check, the body never runs
- The body must contain something that changes the condition's outcome, or the loop never ends (an **infinite loop**)

**Common Forms**

```python
# Basic counter-controlled while loop
count = 0
while count < 5:
    print(count)
    count += 1        # without this line, the loop never ends

# Sentinel-controlled loop (runs until a specific value appears)
response = ""
while response != "quit":
    response = input("Type 'quit' to exit: ")

# Flag-controlled loop
running = True
while running:
    if some_condition:
        running = False

# Intentional infinite loop with a break
while True:
    user_input = input("Enter a number (or 'q' to stop): ")
    if user_input == "q":
        break
    print(int(user_input) ** 2)
```

**When to Use a `while` Loop**

Use `while` when you **don't know in advance how many times** the loop needs to run — the loop depends on a condition that changes based on user input, external data, or logic evaluated during execution.

**Reach for `while` when:**
- You're waiting for a specific user input (validation loops, menus)
- You're repeating until some condition in your program's state becomes true/false
- You don't have a fixed collection to iterate over
- You need to keep going until an event happens, not until you run out of items

**Rule of thumb:** if you can describe the task as "keep doing this **until**..." — it's a `while` loop.

## `for` vs. `while` — Quick Comparison

| Situation | Use |
|---|---|
| Known number of repetitions | `for` |
| Iterating over a collection | `for` |
| Repeating until a condition changes | `while` |
| Validating user input | `while` |
| Counter-controlled with a fixed range | `for` |
| Unknown/variable number of repetitions | `while` |

**PCEP-30-02 / AP CSP Connection**

- `while` loops fall under the **Control Flow** exam block, alongside conditional statements
- PCEP-30-02 tests infinite loop recognition and `break`/`continue` interaction with `while`
- AP CSP frames this as **iteration controlled by a Boolean condition** (Big Idea: Algorithms and Programming)

**Loop Control Keywords**

| Keyword | Purpose | Example |
|---|---|---|
| `break` | Exit loop immediately | `if x == 3: break` |
| `continue` | Skip to next iteration | `if x % 2 == 0: continue` |
| `pass` | Placeholder — does nothing | `if x == 2: pass` |
| `else` | Runs if loop ends without `break` | `for..else:` |

---


**`for...else` and `while...else`**

Python allows an `else` clause on both `for` and `while` loops — a feature many languages don't have. It's easy to misread, so this page focuses on exactly when the `else` block runs.

**The Rule**

> The `else` block runs **only if the loop completes normally** — that is, it runs to the end **without hitting a `break`**.

If a `break` statement fires, the `else` block is **skipped**. If the loop finishes on its own (or never runs at all, in the case of `while`), the `else` block **executes**.

**`for...else` Structure**

```python
for item in iterable:
    # loop body
    if some_condition:
        break
else:
    # runs only if the loop never hit 'break'
    pass
```

**Example — Searching for a Value**

```python
numbers = [4, 7, 11, 2, 9]
target = 15

for n in numbers:
    if n == target:
        print("Found it!")
        break
else:
    print("Target not found in the list.")
```

Here, the loop checks every number, never finds `15`, never breaks — so the `else` block runs and prints `"Target not found in the list."`

**`while...else` Structure**

```python
while condition:
    # loop body
    if some_condition:
        break
else:
    # runs only if the loop exited because condition became False
    # (not because of a break)
    pass
```

**Example — Countdown with a Cancel Option**

```python
count = 5
while count > 0:
    print(count)
    if count == 3:
        cancel = input("Type 'stop' to cancel: ")
        if cancel == "stop":
            break
    count -= 1
else:
    print("Countdown finished normally!")
```

If the user types `"stop"`, the `break` fires and `"Countdown finished normally!"` never prints. If they don't, the loop runs its course and the `else` block executes.

**Why This Trips People Up**

The keyword `else` here does **not** mean "otherwise, if the condition was false" the way it does with `if`. It means:

> **"Run this if the loop was *not* interrupted by a `break`."**

A helpful mental rewrite: think of it as **`nobreak`** instead of `else` — that's literally what it checks for.

**When to Use It**

- **Searching** a collection for a match, where you want a "not found" message only if you never broke out early (classic `for...else` use case)
- **Validating input in a loop**, where you want a success message only if the loop wasn't cancelled by a `break`
- Anytime you'd otherwise use a separate flag variable (`found = False`) just to check afterward whether a `break` happened — the `else` clause replaces that flag

**Rule of thumb:** if your instinct is to set a boolean flag before the loop and check it after, that's a strong sign a `for...else` or `while...else` could replace it.

**PCEP-30-02 / AP CSP Connection**

- The `for...else` / `while...else` construct is explicitly tested on PCEP-30-02 under the **Control Flow** block — expect questions asking whether the `else` block executes given a specific `break` placement
- This is a Python-specific feature with no direct AP CSP pseudocode equivalent; frame it for students as "Python's built-in flag variable"

---


**Nested Loops**

**Nested `for` Loops**

**Structure**

```python
for outer_item in outer_iterable:
    # outer loop body
    for inner_item in inner_iterable:
        # inner loop body
        # runs completely, start to finish, for EVERY pass of the outer loop
```

- The **outer loop** controls how many times the **entire inner loop** runs
- The **inner loop** runs all the way through before the outer loop advances to its next item
- Total iterations = `(outer iterations) × (inner iterations)`

**Common Forms**

```python
# Basic nested loop — multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()  # newline after each row

# Nested loop over two lists — all combinations (pairs)
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
for color in colors:
    for size in sizes:
        print(f"{color} - {size}")

# Nested loop over a 2D structure (list of lists / grid)
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in grid:
    for value in row:
        print(value, end=" ")
    print()

# Nested loop building a pattern
for row in range(5):
    for col in range(row + 1):
        print("*", end="")
    print()
```

**Tracing Execution — Why Order Matters**

```python
for i in range(2):        # outer: runs 2 times
    for j in range(3):    # inner: runs 3 times PER outer pass
        print(i, j)
```

Output:
```
0 0
0 1
0 2
1 0
1 1
1 2
```

The inner loop resets and runs fully **every time** the outer loop advances — this is the single most important thing to trace correctly when reading nested loop code.

## `break` and `continue` in Nested Loops

A `break` or `continue` inside the inner loop only affects the **inner loop** — it has no effect on the outer loop.

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break      # exits only the inner loop
        print(i, j)
```

There is no built-in way to break out of both loops at once; common workarounds are a flag variable, a function with `return`, or restructuring the logic.

**When to Use Nested `for` Loops**

**Reach for nested loops when:**
- Working with **2D data**: grids, matrices, tables, game boards
- Generating **all combinations/pairs** between two collections
- Building **patterns** where each row depends on a repeated inner sequence
- Comparing **every item to every other item** in a collection

**Caution:** nested loops multiply your run time (`O(n²)` for two nested loops over `n` items). For large datasets, check whether a single loop, a dictionary lookup, or a library function (e.g. `itertools`) can replace one of the loops before defaulting to nesting.

**PCEP-30-02 / AP CSP Connection**

- Nested loops fall under **Control Flow**, and PCEP-30-02 frequently tests tracing nested loop output (predict-the-output questions)
- AP CSP frames nested iteration in the context of **2D lists / data structures** (Big Idea: Algorithms and Programming) and in **image/grid manipulation** tasks

---


<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** What's the difference between `break` and `continue` inside a loop that's printing only even numbers from a list?

**Answer:** `continue` skips **just the current iteration** and moves on to the next item — the loop keeps going. `break` **exits the loop entirely**, even if there were more items left to check. If you used `break` instead of `continue` the moment you hit an odd number, the loop would stop checking the rest of the list entirely, missing any even numbers that came after it.
</details>

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

> 📌 **Worked Example — nested loops in a different context (seating chart labels)**
> ```python
> rows = 3
> seats_per_row = 4
>
> for row in range(1, rows + 1):
>     for seat in range(1, seats_per_row + 1):
>         print(f"R{row}S{seat}", end=" ")
>     print()
> ```
> Output:
> ```
> R1S1 R1S2 R1S3 R1S4
> R2S1 R2S2 R2S3 R2S4
> R3S1 R3S2 R3S3 R3S4
> ```
> Trace it: the **outer loop (`row`) picks which row you're on**, and the **inner loop (`seat`) does something once per column within that row** — the same outer/inner relationship you'll need for the shape patterns below, just applied to seat labels instead of a printed shape.

**Guided example — hollow rectangle (Tier 2 difficulty):**

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

> **The Studio Project — Design Your Own**
> 
> Design and code **4 original patterns**. "Original" means not shown in class, not copied from a classmate. > For each pattern, choose one option from each category below (no repeating the exact same combination twice):
> 
> | Category | Options |
> |---|---|
> | **Fill type** | Solid / Hollow |
> | **Content** | ASCII character (your choice) / Sequential numbers / Repeating digit tied to row number |
> | **Orientation** | Grows then stays / Grows then shrinks (diamond/hourglass) / Right-aligned / Shifts diagonally (parallelogram) |
> | **Input** | At least one of your 4 patterns must accept user input for size |
> 
> **🧩 Scaffolding — suggested difficulty progression (do them in this order):**
> - Tier 1 — Solid, fixed growth (e.g., a solid right triangle — see Worked Example above)
> - Tier 2 — Hollow (border-only conditional logic — see Guided Example above)
> - Tier 3 — Numeric (a value that changes per row)
> - Tier 4 — Your choice / mirrored or diagonal shape
> 
> **Think through the process (before coding):** sketch the pattern on grid paper, answer the four warm-up questions for your own design, and write pseudocode for the outer loop, inner loop, and the row-vs-column relationship — *then* code it.
> 
> **Deliverable:** 4 working programs, final code, and one paragraph explaining what the outer loop controls vs. what the inner loop controls.
> 
> **Rubric (8 pts per pattern, 32 pts total):**
> 
> | Criteria | Points |
> |---|---|
> | Sketch and pseudocode completed *before* code, and match the final output | 2 |
> | Pattern runs without errors and matches the intended design | 2 |
> | Nested loop logic is correct (not hard-coded repeated `print()` statements) | 2 |
> | At least one pattern correctly uses user input to control size | 1 |
> | Written explanation correctly identifies the role of outer vs. inner loop | 1 |
>

*AP CSP: AAP-2.E | PCEP: 2.2*

---


### Project: Loop Concepts Activity Project

> These three activities, isolate each loop concept while layering `if`/`elif`/`else` for decision logic. Redundancy across activities is intentional — you will see the same control-flow ideas resurface in a new pathway context.  Read through each project idea.  Choose **1** idea that you would like to develop. 
> 
> | Activity | Concept Focus | Pathway |
> |---|---|---|
> | 1 — Bridge Load Capacity Simulator | `for` loop, `while` loop | Engineering |
> | 2 — Network Intrusion Scanner | `for...else`, `while...else` | CS / Cybersecurity |
> | 3 — Petri Dish Contamination Scan | nested `for`, `break`, `continue` | Bio-Technology |
> 
> = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
> 
> **Activity 1: Bridge Load Capacity Simulator**
> 
> **Concept:** `for` loop vs. `while` loop solving related problems, `if`/`elif`/`else`
> 
> **Scenario:** Students are structural engineers running a virtual stress test on a bridge design. The bridge has a maximum rated capacity. Part A runs a **fixed, known number** of standardized load tests (a job for `for`). Part B keeps adding load **until failure**, an unknown number of steps (a job for `while`) — this contrast is the whole point of the activity.
> 
> ```python
> """
> Activity:    Bridge Load Capacity Simulator
> Author:      [Your Name]
> Course Name: AP Computer Science Principles
> Date:        M/D/Yr
> Description: Simulate a structural stress test on a bridge design using
>              both a for loop (fixed round of standardized tests) and a
>              while loop (load applied until failure), classifying each
>              reading with if/elif/else.
> Language:    Python 3.x
> """
> 
> MAX_CAPACITY_LBS = 10000   # bridge fails at or above this load
> LOAD_STEP_LBS = 750        # how much load is added each round
> 
> 
> def classify_load(current_load, max_capacity):
>     """Return a status string based on % of capacity used."""
>     percent_used = (current_load / max_capacity) * 100
> 
>     # TODO: use if/elif/else to return one of:
>     #   "SAFE"      -> percent_used < 60
>     #   "WARNING"   -> 60 <= percent_used < 90
>     #   "CRITICAL"  -> percent_used >= 90
>     pass
> 
> 
> def run_standardized_tests(num_tests, max_capacity):
>     """
>     Part A - FOR loop
>     Run a FIXED number of standardized load tests (num_tests rounds),
>     increasing load by LOAD_STEP_LBS each round. Print the round number,
>     current load, and status (via classify_load) for each test.
>     """
>     # TODO: for loop, exactly num_tests iterations
>     pass
> 
> 
> def run_to_failure(max_capacity):
>     """
>     Part B - WHILE loop
>     Keep adding LOAD_STEP_LBS until current load meets or exceeds
>     max_capacity. We don't know in advance how many rounds this takes —
>     that's why it can't be a for loop. Return the number of rounds it
>     took and the final load applied.
>     """
>     # TODO: while loop, condition based on max_capacity
>     pass
> 
> 
> def main():
>     print("=== PART A: Standardized Test Battery (for loop) ===")
>     run_standardized_tests(5, MAX_CAPACITY_LBS)
> 
>     print("\n=== PART B: Load-to-Failure Test (while loop) ===")
>     rounds, final_load = run_to_failure(MAX_CAPACITY_LBS)
>     print(f"Bridge failed after {rounds} rounds at {final_load} lbs.")
> 
> 
> if __name__ == "__main__":
>    main()
> ```
> 
> **Sample expected output (Part A, first 2 lines):**
> ```
> Round 1: Load = 750 lbs (7.5%)  -> SAFE
> Round 2: Load = 1500 lbs (15.0%) -> SAFE
> ```
> 
> **Extension:** Can ***Part A*** be forced into a `while` loop but Part B *cannot* be written cleanly as a `for` loop without first calculating the answer? *i.e., why the tool > should match the problem.*
> 
> = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
> 
> **Activity 2: Network Intrusion Scanner**
> 
> **Concept:** `for...else`, `while...else`, nested `if`
> 
> **Scenario:** Students act as security analysts. The `else` clause on a loop only runs if the loop finished **without hitting a `break`** — that's the exact semantics of "scan completed clean" vs. "scan interrupted because we found something." This activity forces students to feel that distinction rather than memorize it.
> 
> ```python
> """
> Activity:    Network Intrusion Scanner
> Author:      [Your Name]
> Course Name: AP Computer Science Principles
> Date:        M/D/Yr
> Description: Use for...else to scan connection logs for a blacklisted IP,
>              and while...else to simulate a limited-attempt access code
>              check, demonstrating that the else clause only fires when
>              no break occurs.
> Language:    Python 3.x
> """
> 
> BLACKLISTED_IPS = ["10.0.0.13", "192.168.1.66", "172.16.0.99"]
> CONNECTION_LOG = [
>     "203.0.113.5", "198.51.100.2", "10.0.0.13", "203.0.113.9"
> ]
> 
> VALID_ACCESS_CODE = "7734"
> MAX_ATTEMPTS = 3
> 
> 
> def scan_connection_log(log, blacklist):
>     """
>     FOR...ELSE
>     Walk through each IP in the log. If a blacklisted IP is found,
>     print an ALERT and break immediately (no need to keep scanning).
>     If the loop finishes without ever breaking, the else clause runs
>     and should print that the log is clean.
> 
>     Bonus: use a nested if to classify severity -- if the matched IP
>     is the FIRST item in blacklist, treat it as "CRITICAL", otherwise
>     "HIGH".
>     """
>     # TODO: for ip in log: ... break ... else: ...
>     pass
> 
> 
> def check_access_code(get_attempt_func, valid_code, max_attempts):
>     """
>     WHILE...ELSE
>     Allow up to max_attempts guesses (get_attempt_func() returns the
>     next guess string -- already provided for you, don't rewrite it).
>     Break out as soon as the correct code is entered. If the while
>     condition becomes false (attempts run out) without ever finding
>     the right code, the else clause should print "ACCESS DENIED."
>     """
>     # TODO: while attempts_used < max_attempts: ... break ... else: ...
>     pass
> 
> 
> def main():
>     print("=== Scanning connection log ===")
>     scan_connection_log(CONNECTION_LOG, BLACKLISTED_IPS)
> 
>     print("\n=== Access code check ===")
>     fake_attempts = iter(["1111", "2222", "7734"])
>     check_access_code(lambda: next(fake_attempts), VALID_ACCESS_CODE, MAX_ATTEMPTS)
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> **Sample expected output:**
> ```
> === Scanning connection log ===
> ALERT: Blacklisted IP detected -> 10.0.0.13 (CRITICAL)
> 
> === Access code check ===
> Attempt 1: 1111 -- incorrect
> Attempt 2: 2222 -- incorrect
> Attempt 3: 7734 -- ACCESS GRANTED
> ```
> 
> **Extension:** Change `fake_attempts` so all three guesses are wrong and predict — before running — which branch (`break` body or `else` body) will fire, then verify.
> 
>  = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
> 
> **Activity 3: Petri Dish Contamination Scan**
> 
> **Concept:** nested `for` loops, `break`, `continue`
> 
> **Scenario:** Students act as lab techs scanning a grid of petri dish samples (rows x columns). Each cell holds a reading: `0` = clean, a positive number = contamination level. `continue` skips clean cells (nothing to report). `break` stops scanning the **current row** early once 2 contaminated cells are found in it (containment protocol — no need to keep checking that row).
> 
> ```python
> """
> Activity:    Petri Dish Contamination Scan
> Author:      [Your Name]
> Course Name: AP Computer Science Principles
> Date:        M/D/Yr
> Description: Scan a 2D grid of petri dish sample readings with nested
>              for loops, using continue to skip clean cells and break to
>              halt a row early once a containment threshold is reached.
> Language:    Python 3.x
> """
> 
> # Each row is one sample strip; each value is a contamination reading.
> # 0 = clean. Positive values = contamination level.
> SAMPLE_GRID = [
>     [0, 0, 3, 0, 6],
>     [0, 2, 0, 5, 9],
>     [0, 0, 0, 0, 0],
>     [4, 0, 8, 1, 0],
> ]
> 
> ROW_CONTAINMENT_LIMIT = 2   # stop scanning a row after this many hits
> 
> 
> def classify_reading(level):
>     """Nested if/elif/else severity classification."""
>     # TODO:
>     #   level == 0        -> "clean"
>     #   1 <= level <= 4    -> "low"
>     #   5 <= level <= 8    -> "moderate"
>     #   level >= 9         -> "severe"
>     pass
> 
> 
> def scan_grid(grid, limit):
>     """
>     Outer for loop -> each row (a sample strip)
>    Inner for loop -> each cell in that row
> 
>     - If a cell is clean (0), `continue` to the next cell immediately.
>     - Otherwise print row/col position and severity via classify_reading.
>     - Track how many contaminated cells found THIS row; once it hits
>       `limit`, print a containment message and `break` out of the
>       inner loop (stop scanning that row, move on to the next row).
>     """
>     # TODO: nested for loops with continue and break
>     pass
> 
> 
> def main():
>     scan_grid(SAMPLE_GRID, ROW_CONTAINMENT_LIMIT)
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> **Sample expected output (first row only):**
> ```
> Row 0:
>   Col 2: level 3 -> low
>   Col 4: level 6 -> moderate
>   Containment limit reached on Row 0 -- halting scan of this row.
> ```
> 
> **Extension (harder):** Add an *outer* `break` — if any single cell reads `>= 9` ("severe"), halt the **entire** scan immediately (whole dish is compromised), not just the > current row. This requires either a flag variable or restructuring into a function that `return`s early — a good bridge to why `break` alone can't exit two loops at once.
>

**Loop Concepts Activity Project — Grading Rubric**


<details>
  <summary>Click Here for Project Rubric</summary>

************************************************************************************

**Standards Alignment Reference**

| Code | Standard | Where it shows up in this project |
| --- | --- | --- |
| `AP CSP AAP-2.E` | Develop algorithms using sequencing, selection, and iteration | Core loop + `if/elif/else` logic in all three activities |
| `AP CSP AAP-2.K` | For loops | Activity 1 Part A; Activity 2 log scan; Activity 3 outer/inner loops |
| `AP CSP AAP-3.B` | Use procedures/functions to manage complexity | Function decomposition (`classify_load`, `run_standardized_tests`, etc.) |
| `AP CSP CRD-2.B` | Implement algorithms in a programming language | Overall program implementation |
| `AP CSP CRD-2.J` | Identify, test, and correct errors in algorithms and programs | Test cases / sample runs; boundary conditions |
| `PCEP 2.1` | Conditional statements | `if/elif/else` classification functions |
| `PCEP 2.2` | Perform different types of iterations | `for`, `while`, `for...else`, `while...else`, nested loops, `break`/`continue` |
| `PCEP 4.1` | Decompose code using functions | Functions with docstrings, single responsibility |

**Applies to the following projects:** 

- Activity 1 (Bridge Load Capacity Simulator)
- Activity 2 (Network Intrusion Scanner)
- Activity 3 (Petri Dish Contamination Scan) 

**Total: 40 points** — 24 pts *Common Criteria* (all activities) + 16 pts *Concept-Specific Core Logic* (grade only the row matching the student's chosen activity).

************************************************************************************

**Common Criteria (24 pts — all activities)**

| Criteria | Points |
| --- | --- |
| Header block complete (Assignment, Author, Description, etc.) and PEP 8 style followed | 3 |
| Program runs without crashing on normal input | 3 |
| Logic correctly decomposed into functions (no core logic crammed into `main()`) | 3 |
| Custom functions include docstrings describing their purpose | 2 |
| `if/elif/else` classification function (`classify_load`, severity check, or `classify_reading`) returns correct category for all threshold boundaries, including edge values | 4 |
| Output format matches the sample output shown for the chosen activity (spacing, labels, rounding) | 4 |
| Test cases / sample runs submitted, including at least one boundary or edge case (not just a "happy path" run) | 4 |
| Code comments explain *what the loop is doing and why* at each key step, not just restating the code | 1 |

************************************************************************************

**Concept-Specific Core Logic (16 pts — score only the row that matches)**

**Activity 1 — Bridge Load Capacity Simulator (`for` vs. `while`)**

| Criteria | Points |
| --- | --- |
| `run_standardized_tests()` correctly uses a `for` loop for a **fixed** number of iterations (`num_tests`) | 4 |
| `run_to_failure()` correctly uses a `while` loop that continues until load meets/exceeds capacity — condition-based, not counter-based | 4 |
| Both functions correctly call `classify_load()` and report round/load/status each iteration | 4 |
| Extension question answered correctly: explains *why* Part A could be forced into `while` but Part B cannot cleanly become a `for` loop without first computing the answer | 4 |

**Activity 2 — Network Intrusion Scanner (`for...else`, `while...else`)**

| Criteria | Points |
| --- | --- |
| `scan_connection_log()` correctly uses `for...else`: loop breaks on a blacklist match, `else` fires only when no match is ever found | 6 |
| `check_access_code()` correctly uses `while...else` with an attempt counter: breaks on correct code, `else` fires only when attempts run out with no correct guess | 6 |
| Nested `if` correctly classifies severity (CRITICAL vs. HIGH based on blacklist position) | 2 |
| Extension question answered correctly: predicts, before running, which branch (`break` body vs. `else` body) fires when all attempts are wrong | 2 |

**Activity 3 — Petri Dish Contamination Scan (nested `for`, `break`, `continue`)**

| Criteria | Points |
| --- | --- |
| `scan_grid()` correctly nests two `for` loops (outer = row, inner = cell) and tracks position accurately | 4 |
| `continue` correctly skips clean (`0`) cells without printing or counting them | 4 |
| `break` correctly halts only the **inner** loop once the row's containment limit is reached, and scanning resumes on the next row | 4 |
| `classify_reading()` correctly categorizes clean/low/moderate/severe at all boundary values | 2 |
| Extension (harder) attempted: an outer break/flag or restructured function correctly halts the *entire* scan on a severe (`>= 9`) reading | 2 |

************************************************************************************

**Scoring Summary**

| Section | Points |
| --- | --- |
| Common Criteria | 24 |
| Concept-Specific Core Logic (chosen activity only) | 16 |
| **Total** | **40** |

</details>


---


## Section 3 — Data Collections: Lists, Tuples, Dictionaries, and Strings

`📋 AP CSP: AAP-4.A` — Use data abstractions to manage complexity.

### Strings

`🔖 PCEP 3.4 — Operate with strings` `📋 AP CSP: DAT-1.A`

Strings are **ordered, immutable** sequences of characters.

```
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

```
print("She said \"Hello\"")  # She said "Hello"
print("Line 1\nLine 2")      # newline
print("Col1\tCol2")          # tab
print("Backslash: \\")       # \
```

**Multi-line Strings**

```
poem = """
Roses are red,
Violets are blue.
"""
```

**Beginner String Methods**

| Method               | Description        | Example                                |
| -------------------- | ------------------- | --------------------------------------- |
| `.lower()`           | Lowercase           | `"HELLO".lower()` → `"hello"`           |
| `.upper()`           | Uppercase           | `"hello".upper()` → `"HELLO"`           |
| `.strip()`           | Remove whitespace   | `"  hi  ".strip()` → `"hi"`             |
| `.replace(old, new)` | Replace text        | `"cat".replace("c","b")` → `"bat"`      |
| `.split(sep)`        | Split into list     | `"a b c".split()` → `["a","b","c"]`     |
| `len()`               | Length              | `len("hello")` → `5`                    |
| `.find(sub)`         | Index of substring  | `"apple".find("p")` → `1`               |
| `.count(sub)`        | Count occurrences   | `"banana".count("a")` → `3`             |
| `.startswith(text)`  | Starts with?        | `"hello".startswith("he")` → `True`     |
| `.endswith(text)`    | Ends with?          | `"file.txt".endswith(".txt")` → `True`  |
| `.isalpha()`         | All letters?        | `"abc".isalpha()` → `True`              |
| `.isdigit()`         | All digits?         | `"123".isdigit()` → `True`              |
| `.title()`           | Capitalize the first letter of each word |	"marco reyes".title() → "Marco Reyes" |

**🤔 Thinking Question — check your answer**

**Question:** `name = "  Ada Lovelace  "`. What does `name.strip().upper()` return, and why does the order of the two method calls matter here?

**Answer:** `"ADA LOVELACE"`. `.strip()` removes the leading/trailing whitespace first, then `.upper()` capitalizes the result. Because strings are immutable, each method returns a **new** string rather than modifying `name` in place — that's why you can "chain" methods like this, each one operating on the result of the one before it. Order rarely matters for `.strip()`/`.upper()` specifically, but it does for methods that depend on exact spacing, like `.startswith()`.

> 📌 **Worked Example — string methods in a different context (library due-date slip)**
>
> ```
> book_title = "  the hobbit   "
> library_name = "westview public library"
> due_date = "09/15"
>
> clean_title = book_title.strip().title()      # "The Hobbit"
> header = library_name.upper()                  # "WESTVIEW PUBLIC LIBRARY"
>
> print(header)
> print(f"{clean_title}\tDue: {due_date}")
> print("\"Please return on time to avoid fees.\"")
> ```
>
> This shows the same *techniques* the Receipt Formatter asks for — `.strip()` to clean messy input, `.upper()`/`.title()` for capitalization, `\t` for column alignment, and a quoted message with `\"` — applied to a library slip instead of a receipt.

---

#### Practice Drills — Strings

`Quick single-concept reps, 10–15 min each — do these before or alongside Receipt Formatter below.`



**S1 — String Slicer**

Given `phrase = "Computer Science Principles"`, without hardcoding letters, use slicing/indexing to print: (1) just `"Computer"`, (2) just `"Principles"`, (3) the whole phrase reversed, (4) every other character.

```
phrase = "Computer Science Principles"

# TODO 1) print "Computer" using slicing
# TODO 2) print "Principles" using slicing
# TODO 3) print the phrase reversed
# TODO 4) print every other character
```

#############################################################################


**S2 — Name Formatter**

Ask the user for their first and last name in **one** `input()` call (e.g. `"marco reyes"`), typed messily (any case, extra spaces). Use `.strip()`, `.split()`, and `.title()` to print it cleanly as `"Reyes, Marco"`.

```
full_name = input("Enter your first and last name: ")

# TODO 1) strip() the input
# TODO 2) split() into first and last
# TODO 3) print as "Last, First" using .title()
```

#############################################################################


**S3 — Palindrome Checker**

Ask the user for a word. Using slicing (`[::-1]`) — no loops needed — check if it reads the same forwards and backwards. Ignore case.

```
word = input("Enter a word: ").lower()

# TODO: compare word to its reversed slice, print True/False
```

#############################################################################


**S4 — Vowel Counter**

Ask for a sentence. Count how many vowels (`a, e, i, o, u`, either case) it contains using `.count()`.

```
sentence = input("Enter a sentence: ")

# TODO: count vowels using .count() for each vowel letter
```

#############################################################################


**S5 — Find and Replace Censor**

Ask for a sentence and a "banned word." Use `.find()` to check if the word appears, then `.replace()` to swap every occurrence with asterisks matching its length (e.g., `"spam"` → `"****"`).

```
sentence = input("Enter a sentence: ")
banned = input("Enter a word to censor: ")

# TODO 1) use .find() to check if banned word is present
# TODO 2) if present, use .replace() to swap it with "*" * len(banned)
```

#############################################################################


**S6 — Acronym Generator**

Ask for a multi-word phrase (e.g., `"as soon as possible"`). Use `.split()` to get the words, grab the first letter of each with a loop or comprehension, and `.join()` them into an uppercase acronym.

```
phrase = input("Enter a phrase: ")

# TODO: split the phrase into words, take the first letter of each,
#       join them into an uppercase acronym
```

**Sample:** `"as soon as possible"` → `ASAP`

#############################################################################


**S7 — Pig Latin Translator**

Pig Latin Translator**

Ask the user for a full sentence. Use `.split()` to break it into words, translate **each word** to Pig Latin, then `.join()` them back into a sentence:
- If a word starts with a vowel, add `"way"` to the end.
- If a word starts with a consonant, move just the **first letter** to the end, then add `"ay"`.

```
sentence = input("Enter a sentence: ").lower()
vowels = "aeiou"

# TODO 1) split the sentence into a list of words
# TODO 2) loop through the words; for each word:
#         - if word[0] is a vowel: translated = word + "way"
#         - if word[0] is a consonant: translated = word[1:] + word[0] + "ay"
#         - append translated to a new list
# TODO 3) join the translated words back into a sentence with " "
# TODO 4) print the translated sentence
```

**Sample:** `"the pig ran"` → `"hetay igpay anray"`

**Extension — Decode Pig Latin back to English:** Given a Pig Latin sentence, translate it back to English. For each word: if it ends in `"way"`, strip `"way"` off (it started with a vowel). Otherwise, strip `"ay"` off the end, then move the **last remaining letter** back to the front (it was the consonant that got moved).

```
pig_sentence = input("Enter a Pig Latin sentence: ").lower()

# TODO 1) split into words
# TODO 2) loop through the words; for each word:
#         - if it ends with "way": original = word without the "way"
#         - otherwise: strip the "ay", then move the LAST letter of
#           what's left back to the front:
#           original = remainder[-1] + remainder[:-1]
# TODO 3) join and print the decoded sentence
```

**Try it:** decode `"hetay igpay anray"` — you should get back `"the pig ran"`.

**🤔 Discussion:** Try encoding a word that starts with the letter **w**, like `"wave"` → `"aveway"`. Now try decoding `"aveway"` — does it come back as `"wave"`? *(It won't! The decoder sees it ends in `"way"` and assumes it started with a vowel, since that's the exact same ending a consonant-`w` word produces. This is a nice bug to trace by hand: a single moved letter can accidentally recreate the "started with a vowel" signal. Real ciphers need to guarantee their encoding is unambiguous to decode — this is why, in the XOR cipher extension from the steganography lab, we cared about avoiding collisions too.)*

#############################################################################


**Submit your .py file and test cases showing that your program worked as intended.**

```python
#       Assignment:  String Practice
#       Author:      [Your Name]
#       Course Name: AP Computer Science Principles
#       Description: Using string methods to manipulate strings
#       Language:    Python 3.x
```

*PCEP: 3.4 | AP CSP: DAT-1.A*

---

### Activity: Receipt Formatter

Write a program that formats a store receipt using string methods and escape characters.

**🧩 Scaffolding — build it in this order:**

1. Get store name, item name, and price from the user; print them raw (unformatted) first to confirm input works.
2. Add `.upper()` for the store header and `.title()` for the item name.
3. Add the `\t` / `\n` formatting and the quoted thank-you message.
4. Add the `.strip()` demonstration and `.replace()` discount label last — these are the trickiest requirements.

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

### Lists

`🔖 PCEP 3.1 — Collect and process data using lists` `📋 AP CSP: AAP-4.A — Lists for data abstraction`

A **list** is an **ordered, mutable** sequence. It is the most versatile data collection in Python — and the collection type the AP CSP CPT specifically requires you to use.

```
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
print(fruits[-1])      # cherry
print(fruits[1:3])     # ['banana', 'cherry']
```

**Common List Methods**

```
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

```
for item in fruits:
    print(item)

for i, item in enumerate(fruits):
    print(f"{i}: {item}")
```


<details><summary>Enumerate Explained</summary>


**`enumerate(fruits)`**
`fruits` is a list, like `["apple", "banana", "cherry"]`. Normally when you loop through a list, you just get each item — you don't automatically know its position (index). `enumerate()` fixes that: it goes through the list and gives you **two things at once** for each item — its position number and the value itself.

**`for i, item in enumerate(fruits):`**
This loop grabs both of those things each time around:
- `i` = the index (position), starting at 0
- `item` = the actual fruit at that position

So for `["apple", "banana", "cherry"]`, the loop runs three times:

| i | item |
|---|--------|
| 0 | apple |
| 1 | banana |
| 2 | cherry |

**`print(f"{i}: {item}")`**
This is an `f-string` — a way to insert variables directly into a string. It prints the index, a colon, then the item.

**Putting it together**, the output would be:
```python
0: apple
1: banana
2: cherry
```

**Why use `enumerate` instead of just `for item in fruits`?**
Sometimes you need the position too — like if you want to number a list for students, or you need to know "this is the 3rd item" while also using its value. Without `enumerate`, you'd have to manually track a counter variable yourself (`i = 0`, then `i += 1` each loop) — `enumerate` does that bookkeeping for you.

`enumerate` hands you a stack of index cards, each one labeled with a number and taped to a fruit — you just read off both labels as you go through the stack.

</details>


**`in` and `not in` Operators**

```
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

```
# Traditional loop
squares = []
for x in range(10):
    squares.append(x ** 2)

# Equivalent list comprehension
squares = [x ** 2 for x in range(10)]
```

```
squares     = [x ** 2 for x in range(10)]
evens       = [x for x in range(20) if x % 2 == 0]
upper_words = [word.upper() for word in ["hi", "bye"]]
```

> ==**When to use which:** list comprehensions are great for simple, one-line transformations. If your loop needs multiple steps, `print()` statements along the way, or complex logic, a traditional `for` loop is usually more readable — don't force a comprehension just because it's shorter. Readability counts, per PEP 8.==

**Copying vs. Cloning**

```
original = [1, 2, 3]
alias    = original        # NOT a copy — both point to same list
clone    = original.copy() # Independent copy
clone2   = original[:]     # Also a copy (slicing)
```

**2D Lists (Matrices)**

```
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

**🤔 Thinking Question — check your answer**

**Question:** `original = [1, 2, 3]` then `alias = original` then `alias.append(4)`. What does `print(original)` show, and why?

**Answer:** `[1, 2, 3, 4]`. `alias = original` did **not** create a copy — it made `alias` point to the exact same list object in memory as `original`. Modifying `alias` (with `.append()`) modifies the one and only list both names refer to. To get an independent copy, you'd need `alias = original.copy()` or `alias = original[:]`. This is the same idea as the `is` vs `==` distinction from Section 1.

---

#### Practice Drills — Lists

`Quick single-concept reps, 10–15 min each — this is the Week 7 activity block.`

**L1 — Shopping List Builder**

Start with an empty list. Use `.append()` to add 5 grocery items one at a time (hardcoded, not input). Then: `.insert()` a forgotten item at index 0, `.remove()` one item by name, and print the final list.

```
groceries = []

# TODO 1) append 5 items
# TODO 2) insert a 6th item at the front
# TODO 3) remove one item by name
# TODO 4) print the final list
```

**L2 — List Stats (No Built-ins)**

Given a hardcoded list of test scores, find the **highest**, **lowest**, and **average** score using a `for` loop and running variables — **without** using Python's built-in `max()`, `min()`, or `sum()` functions.

```
scores = [88, 95, 72, 100, 64, 91]

# TODO 1) loop through scores to find the highest (no max())
# TODO 2) loop through scores to find the lowest (no min())
# TODO 3) loop through scores to compute the average (no sum())
```

**L3 — Duplicate Remover**

Given a list with repeated values, build a **new** list containing only the first occurrence of each value (preserve original order — don't just use `set()`, since sets don't preserve order). Use `in`/`not in` to check membership as you build the new list.

```
raw = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# TODO: build "unique" list containing each value only once, in
#       first-seen order
```

**L4 — List Slicing Practice**

Given `numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`, use slicing (no loops) to print: (1) the first three numbers, (2) the last three numbers, (3) every other number starting from index 0, (4) the list reversed.

```
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# TODO 1-4: four print statements, each using a different slice
```

**L5 — High Score Tracker**

Start with a list of 5 hardcoded high scores. Add a new score with `.append()`, then use `.sort(reverse=True)` to rank them highest-to-lowest. Use `.pop()` to drop the lowest score off the list (keeping only the top 5), and print the final ranked list with placements (`"1st: 100"`, etc.) using `enumerate()`.

```
high_scores = [72, 88, 95, 61, 84]

# TODO 1) append a new score (e.g., 90)
# TODO 2) sort descending
# TODO 3) pop the lowest score off the end
# TODO 4) print ranked with enumerate() -- "1st: 95", "2nd: 90", etc.
```

**L6 — 2D List Grid Scanner**

Given a 3x3 grid (list of lists) of numbers, use nested loops to find the **total sum** of all values and print each row on its own line.

```
grid = [
    [4, 8, 1],
    [6, 2, 9],
    [3, 5, 7]
]

# TODO 1) print each row on its own line
# TODO 2) compute and print the total sum of every value in the grid
```

**L7 — Grade Curve Adjuster**

Given a list of test scores, use a **list comprehension** to add 5 bonus points to every score — but cap any result at 100 (no score can exceed it). This combines list comprehensions with a conditional expression inside the expression part.

```
scores = [78, 95, 88, 99, 62]

# TODO: build a new list "curved" where each score gets +5,
#       capped at 100 (hint: use "x if condition else y" inside
#       the comprehension's expression)
```

**Sample:** `[78, 95, 88, 99, 62]` → `[83, 100, 93, 100, 67]`

*PCEP: 3.1 | AP CSP: AAP-4.A*


#############################################################################

### Activity: Playlist Manager

**Unit:** Data Collections (Lists) — PCEP-30-02 Block 3 / AP CSP Big Idea 3
**Prerequisite:** Strings unit / Receipt Formatter activity

Write a program that manipulates a premade list of songs using list methods and slicing.

**Starter list (give this to students — don't let them type it in):**
```python
playlist = ["Blinding Lights", "Levitating", "As It Was", "Flowers", "Anti-Hero",
            "Unholy", "Cruel Summer", "Vampire", "Espresso", "Paint The Town Red",
            "Snooze", "Lovin On Me", "Fortnight", "Please Please Please", "Birds Of A Feather",
            "Not Like Us", "Texas Hold Em", "I Had Some Help", "Good Luck Babe!", "Beautiful Things"]
```

#############################################################################

## 🧩 Scaffolding — build it in this order

1. Print the raw list, its `len()`, and the first/last song using indexing — confirm the list loads and indexing works before doing anything fancy.
2. Use slicing to print the "Top 5" (`playlist[:5]`) and the "Bottom 5" (`playlist[-5:]`).
3. Add songs with `.append()` and `.insert()` — one at the end, one at a specific chart position.
4. Add `.remove()` and `.pop()` — one that removes by name, one that removes by position and *keeps* the removed value in a variable to print ("Removed from playlist: ...").
5. Add `.sort()` (alphabetical) and `.sort(reverse=True)`, printing the list each time so students see it mutate in place.
6. Add `.index()`, `.count()`, and the `in` keyword last — these require the trickiest thinking (what happens if the song isn't there?).

#############################################################################

## Requirements

1. Start from the given `playlist` list. Print it, its length, and the song at index `0` and index `-1`.
2. Use slicing to display a "Top 5" and a "Bottom 5" sublist without modifying the original list.
3. Ask the user for a new song to add. Use `.append()` to add it to the end, then use `.insert()` to add a *second* new song at position `3` (like inserting it into the #4 chart slot).
4. Ask the user which song to remove. Use `.remove()` to take it out by name — wrap it so the program doesn't crash if the song isn't in the list (`if song in playlist:`).
5. Use `.pop(0)` to remove the current #1 song, store it in a variable, and print `"Dropped from #1: <song>"`.
6. Use `.sort()` to alphabetize the list and print it, then use `.sort(reverse=True)` and print it again — label each printout so it's clear which order is which.
7. Ask the user for a song title and use `.index()` to report its chart position (add 1 so it reads as a human rank, not a 0-based index) — handle the case where it isn't found instead of crashing.
8. Use `.count()` to check whether the user accidentally added a duplicate song, and print a warning if `count > 1`.
9. Use `len()` one more time at the end to print the final total number of songs on the playlist.
10. **Bonus:** Use `.reverse()` to flip the current order in place (different from `sort(reverse=True)` — ask them to explain the difference in a comment).
11. **Bonus:** Use a list comprehension to print only the songs that contain the word "Love" (case-insensitive) or another keyword of their choice.

#############################################################################

## Sample interaction

```
--- Current Playlist ---
['Blinding Lights', 'Levitating', 'As It Was', ... ]
Total songs: 20
#1: Blinding Lights
Last song: Beautiful Things

Top 5: ['Blinding Lights', 'Levitating', 'As It Was', 'Flowers', 'Anti-Hero']
Bottom 5: ['Not Like Us', 'Texas Hold Em', 'I Had Some Help', 'Good Luck Babe!', 'Beautiful Things']

Enter a new song to add: Golden
Enter another new song to insert at #4: Die With A Smile

Enter a song to remove: Snooze
Removed "Snooze" from the playlist.

Dropped from #1: Blinding Lights

--- Alphabetical Order ---
[...]
--- Reverse Alphabetical Order ---
[...]

Enter a song to look up: Espresso
"Espresso" is currently ranked #7

Final playlist total: 21 songs
```

#############################################################################

## Grading Rubric (1 pt per standard)

| Requirement | Points |
|---|---|
| Raw list, `len()`, indexing (`[0]`, `[-1]`) | 1 |
| Slicing — Top 5 / Bottom 5 | 1 |
| `.append()` | 1 |
| `.insert()` at a specific position | 1 |
| `.remove()` with `in` safety check | 1 |
| `.pop()` storing removed value | 1 |
| `.sort()` and `.sort(reverse=True)` | 1 |
| `.index()` with not-found handling | 1 |
| `.count()` duplicate check | 1 |
| Final `len()` output | 1 |
| Bonus: `.reverse()` with explanatory comment | +1 |
| Bonus: list comprehension keyword filter | +1 |

**Total: 10 pts (12 with bonus)**


<details>
<summary>▶ Common student errors to watch for</summary>

- **`.remove()` without an `in` check** → `ValueError` crash if the song isn't spelled exactly as in the list (case-sensitive).
- **Confusing `.pop()` and `.remove()`** → `.pop()` takes an *index*, `.remove()` takes a *value*. Students often pass a song name to `.pop()`.
- **Forgetting `.sort()` and `.reverse()` return `None`** → `playlist = playlist.sort()` silently sets `playlist` to `None`. Emphasize these mutate in place and don't need reassignment.
- **Off-by-one on `.index()`** → `.index()` is 0-based, so remind them to `+1` when displaying a "rank" to the user.
- **Slicing confusion** → `playlist[:5]` vs `playlist[5:]` — walk through this on the board if Top 5 / Bottom 5 come out wrong.

</details>


#############################################################################


### Tuples

`🔖 PCEP 3.2 — Collect and process data using tuples`

A **tuple** is an **ordered, immutable** sequence — values cannot be changed after creation.

```
coords     = (40.7128, -74.0060)    # GPS: New York City
rgb        = (255, 128, 0)
single     = (42,)                  # Note the comma for single-element tuple

print(coords[0])    # 40.7128
print(len(rgb))     # 3
```

**Tuples vs. Lists**

| Feature    | List          | Tuple          |
| ---------- | ------------- | -------------- |
| Ordered    | ✅            | ✅             |
| Indexed    | ✅            | ✅             |
| Mutable    | ✅            | ❌             |
| Duplicates | ✅            | ✅             |
| Use when   | Data changes  | Data is fixed  |

**Lists inside Tuples and Tuples inside Lists**

```
mixed = ([1, 2, 3], [4, 5, 6])   # tuple of lists
nested = [(1, "a"), (2, "b")]     # list of tuples
```

**🤔 Thinking Question — check your answer**

**Question:** Would you store a student's GPA history (which changes every semester) in a list or a tuple? What about a single student's date of birth (month, day, year)?

**Answer:** GPA history → **list**, because new entries get added over time (mutable data). Date of birth → **tuple**, because once set it never changes — the immutability of a tuple communicates "this is fixed data" to anyone reading your code.


**Practice Drills — Tuples**

`Quick single-concept reps, 10–15 min each — do these before Student Contact Book below.`

**T1 — Coordinate Pair Basics**

**Packing** means putting several values into one tuple. Python does this automatically when you list values separated by commas:

```
point = (3, 7)        # packing: 3 and 7 are packed into one tuple
point = 3, 7          # same thing; the parentheses are optional
```

**Unpacking** is the reverse: taking the values out of a tuple and storing each one in its own variable, all in one line. The variables on the left get matched to the values on the right **by position**:

```
point = (3, 7)
x, y = point          # unpacking: x gets point[0], y gets point[1]

print(x)              # 3
print(y)              # 7
```

That one line does the same job as these two:

```
x = point[0]
y = point[1]
```

⚠️ The number of variables must match the number of values in the tuple. `x, y = (3, 7, 9)` causes a `ValueError: too many values to unpack`.

**Your task:** Store a GPS coordinate as a tuple `(latitude, longitude)`. Unpack it into two separate variables in a single line and print a formatted sentence using them.

```
location = (34.0522, -118.2437)

# TODO: unpack location into lat, lon in one line, then print
#       f"Latitude: {lat}, Longitude: {lon}"
```

**Sample output:**

```
Latitude: 34.0522, Longitude: -118.2437
```


> The number of variables on the left must match the number of items in the tuple, or Python raises a ValueError.

```python
location = (34.0522, -118.2437)
```

**TODO: unpack location into lat, lon in one line, then print**
      
```python
f"Latitude: {lat}, Longitude: {lon}"
```

Store a GPS coordinate as a tuple `(latitude, longitude)`. Unpack it into two separate variables in a single line and print a formatted sentence using them.


**T2 — RGB Color Mixer**

Store two colors as RGB tuples, e.g. `red = (255, 0, 0)`. Write a function `average_color(c1, c2)` that takes two RGB tuples and returns a **new tuple** representing their averaged color (average each channel, round to an int). Test it by mixing two colors.

```
red = (255, 0, 0)
blue = (0, 0, 255)

def average_color(c1, c2):
    # TODO: return a new tuple with each channel averaged (rounded)
    pass

print(average_color(red, blue))
```

**T3 — Proving Immutability**

Create a tuple `dimensions = (12, 24)`. Try to change the first value with `dimensions[0] = 15` and run it — read the error Python gives you. Then write one sentence (as a comment) explaining, in your own words, what the error message means and why lists don't have this problem.

```
dimensions = (12, 24)

# TODO 1) uncomment the line below, run it, and read the error
# dimensions[0] = 15

# TODO 2) add a comment explaining the error in your own words
```

**T4 — List of Tuples: Grade Records**

Store 5 students as a **list of tuples**: `(name, grade)`. Loop through the list and print only the students with a grade of `90` or higher. This is a deliberate contrast to the "list of dictionaries" pattern used below in Student Contact Book — same idea (bundling related data), different structure.

```
records = [
    ("Ava", 92), ("Liam", 78), ("Noah", 95),
    ("Mia", 88), ("Zoe", 91)
]

# TODO: loop through records, unpack each tuple, print names
#       with grade >= 90
```

**T5 — Swap and Min/Max Return**

Two parts, both showing what tuples are *for*: (1) swap two variables' values in one line using tuple packing — no temp variable; (2) write a function `min_max(numbers)` that returns **both** the smallest and largest value as a single tuple, then unpack the result at the call site.

```
a, b = 5, 12

# TODO 1) swap a and b in one line using tuple packing/unpacking

def min_max(numbers):
    # TODO 2) return a tuple (smallest, largest)
    pass

low, high = min_max([4, 19, 2, 8, 11])
print(low, high)
```

**Sample output:** `2 19`

*PCEP: 3.2*

---

### Dictionaries

`🔖 PCEP 3.3 — Collect and process data using dictionaries` `📋 AP CSP: AAP-3.B — Use abstractions to organize data.`

A **dictionary** stores **key-value pairs**. Keys must be unique and immutable. Dictionaries are **ordered** (Python 3.7+) and **mutable**.

```
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

```
if "name" in student:
    print("Key exists!")
```

**Dictionary Methods**

```
student.keys()     # dict_keys(['name', 'age', ...])
student.values()   # dict_values(['Alice', 17, ...])
student.items()    # dict_items([('name','Alice'), ...])
```

**Iterating**

```
for key, value in student.items():
    print(f"{key}: {value}")
```

**List of Dictionaries (real-world pattern)**

```
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

**🤔 Thinking Question — check your answer**

**Question:** Why is a "list of dictionaries" (like `students` above) usually a better data abstraction for the CPT than several separate parallel lists like `names = [...]`, `ages = [...]`?

**Answer:** With parallel lists, `names[2]` and `ages[2]` only stay linked to the same student if you're extremely careful to keep every list in sync — one mistaken `.remove()` on just one list breaks the connection. A list of dictionaries keeps each student's data bundled together in one object, so there's no way for a name and age to get separated. This is exactly the kind of data abstraction the CPT written responses ask you to explain.

> 📌 **Worked Example — list of dictionaries in a different context (playlist)**
>
> ```
> playlist = []
>
> new_song = {"title": "Clair de Lune", "artist": "Debussy", "duration": "5:12"}
> playlist.append(new_song)
>
> for song in playlist:
>     if song["title"] == "Clair de Lune":
>         print(f"Found: {song['title']} by {song['artist']} ({song['duration']})")
> ```
>
> This is the pattern (append a dict to a list, then search with a loop + `if`) you'll build into a full menu-driven program below — just applied to songs instead of contacts.

---

#### Practice Drills — Dictionaries

`Quick single-concept reps, 10–15 min each — do these before Student Contact Book below.`

**D1 — Inventory Tracker**

Start with a dictionary of 3 hardcoded inventory items and their quantities (`{"pencils": 30, ...}`). Add a new item, update an existing quantity, remove one item with `del`, and print the final dictionary using a `for key, value in ...items()` loop.

```
inventory = {"pencils": 30, "notebooks": 12, "erasers": 20}

# TODO 1) add a new item
# TODO 2) update an existing item's quantity
# TODO 3) delete one item
# TODO 4) print every item with a for loop over .items()
```

**D2 — Word Frequency Counter**

Given a sentence, build a dictionary counting how many times each word appears. Use `.split()` to get the words, and `if word in freq:` to decide whether to add a new key or increment an existing one.

```
sentence = "the cat sat on the mat the cat ran"
words = sentence.split()

freq = {}

# TODO: loop through words, building the freq dictionary
```

**D3 — Safe Key Lookup**

Given a dictionary of student grades, ask the user for a name. If the name is a key `in` the dictionary, print their grade; if not, print `"Student not found."` — without letting the program crash with a `KeyError`. Then repeat the same lookup using `.get()` with a default value instead of `in`, and compare the two approaches.

```
grades = {"Ava": "A", "Liam": "C", "Noah": "B"}
name = input("Enter a student name: ")

# TODO 1) look up name using "in" and if/else
# TODO 2) look up the same name again using .get() with a default
#         of "Student not found."
```

**D4 — Nested Dictionary Mini-Database**

Build a dictionary of dictionaries representing a small class roster: each key is a student name, and each value is a dictionary with `"grade"` and `"attendance"`. Print a formatted line for each student by looping through `.items()` and accessing the nested values.

```
roster = {
    "Ava": {"grade": "A", "attendance": 0.98},
    "Liam": {"grade": "C", "attendance": 0.85},
    "Noah": {"grade": "B", "attendance": 0.92}
}

# TODO: loop through roster.items(), print each student's grade
#       and attendance as a formatted f-string line
```

**D5 — Dictionary Comprehension Intro**

Given a list of numbers, build a dictionary mapping each number to its square using a **dictionary comprehension** (parallel structure to the list comprehensions already covered). Then rewrite the same thing as a traditional loop, so you can see both side by side.

```
numbers = [1, 2, 3, 4, 5]

# TODO 1) build squares_dict using a dictionary comprehension
#         {n: n**2 for n in numbers}

# TODO 2) build the same dictionary again using a traditional
#         for loop, storing it as squares_dict_loop
```

**D6 — Merge and Invert**

Given two dictionaries of student scores from different quizzes, merge them into one using `.update()` (later quiz overwrites duplicates). Then build a second dictionary that's **inverted** — scores as keys, names as values — using a dictionary comprehension.

```
quiz1 = {"Ava": 88, "Liam": 91}
quiz2 = {"Liam": 95, "Noah": 79}

# TODO 1) merge quiz2 into quiz1 using .update()
# TODO 2) build an inverted dict: {score: name for name, score in ...}
```

**Sample:** merged → `{'Ava': 88, 'Liam': 95, 'Noah': 79}`, inverted → `{88: 'Ava', 95: 'Liam', 79: 'Noah'}`

*PCEP: 3.3 | AP CSP: AAP-3.B*

---

### Activity: Student Contact Book

Build a program that stores a contact book as a **list of dictionaries**. Each contact has a name, phone number, and email. The user can:

1. Add a new contact
2. Search by name
3. Delete a contact
4. Display all contacts

Use a `while` loop for the menu and a `for` loop to search/display.

**🧩 Scaffolding — build it in this order:**

1. Hard-code one contact into the list and get "Display all" working first.
2. Add "Add a new contact" (append to the list).
3. Add "Search by name" (loop + `if`).
4. Add "Delete a contact" last — it's the trickiest, since you must find the right item before removing it.

**Starter code:**

```
#       Assignment:  Program: Student Contact Book
#       Description: Menu-driven contact book using a list of dictionaries.
#       Language:    Python 3.x

contacts = []

while True:
    print("\n1) Add  2) Search  3) Delete  4) Display All  5) Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        # TODO: build a dict from user input, append to contacts
        pass
    elif choice == "2":
        # TODO: ask for a name, loop through contacts, print matches
        pass
    elif choice == "3":
        # TODO: ask for a name, find and remove the matching contact
        pass
    elif choice == "4":
        # TODO: print every contact
        pass
    elif choice == "5":
        break
    else:
        print("Invalid option.")
```

*AP CSP: AAP-3.B, AAP-2.E | PCEP: 3.3*

---

### Mixed Review — Quick Check (all four types)

A 4-question exit ticket for wrapping up the section — one short question per data type, answerable in a sentence or two, no coding required.

1. **String:** You have `name = "  DANA  "`. What does `name.strip().lower()` return?
2. **List:** What's the difference between `.remove("apple")` and `.pop(0)` on a list?
3. **Tuple:** Why would you choose a tuple over a list to store a birthdate?
4. **Dictionary:** What error would `student["gpa"]` raise if `"gpa"` isn't a key — and what method avoids that crash?

*(Answer key: pull straight from the corresponding Thinking Questions above for Strings/Lists/Tuples/Dictionaries.)*

---

**Section 3 — Standards Alignment Reference**

| Code             | Standard                                       | Where it shows up in this section            |
| ---------------- | ----------------------------------------------- | ---------------------------------------------- |
| `AP CSP AAP-4.A` | Use data abstractions to manage complexity      | Section intro, Lists, Tuples (T4)              |
| `AP CSP DAT-1.A` | Explain how data can be represented using bits  | Strings, Drills S1–S7, Receipt Formatter       |
| `AP CSP AAP-3.B` | Use abstractions to organize data                | Dictionaries, Drills D1–D6, Student Contact Book |
| `PCEP 3.1`       | Collect and process data using lists             | Lists, Drills L1–L7                             |
| `PCEP 3.2`       | Collect and process data using tuples            | Tuples, Drills T1–T5                            |
| `PCEP 3.3`       | Collect and process data using dictionaries      | Dictionaries, Drills D1–D6, Student Contact Book |
| `PCEP 3.4`       | Operate with strings                             | Strings, Drills S1–S7, Receipt Formatter        |




---

## Section 4 — Functions and Exceptions
`📋 AP CSP: AAP-3.B` — Use procedures/functions to manage complexity.

### Functions, Methods, and Procedures

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

> 📌 **Worked Example — functions in a different context (rectangle area)**
> ```python
> def calculate_area(length, width):
>     return length * width
>
> def main():
>     l = float(input("Enter length: "))
>     w = float(input("Enter width: "))
>     area = calculate_area(l, w)
>     print(f"Area = {area}")
>
> main()
> ```
> This shows the shape you'll reuse five times below: a function that takes parameters and `return`s a result (no `print()` inside it), called from `main()`, with the result stored in a variable and printed with an f-string. Get this pattern solid here before writing `get_sum()`, `get_difference()`, and the rest.

### Activity: Math Operations Calculator

Write a Python program called `math_operations.py` that performs addition, subtraction, multiplication, division, and modulo on two numbers entered by the user — using a separate function for each operation.

**🧩 Scaffolding — build it in this order:**
1. Write `get_sum()` and call it from `main()` — confirm it prints correctly.
2. Copy that pattern to write `get_difference()`, `get_product()`, `get_modulo()`.
3. Write `get_quotient()` last — it needs the extra care described in Requirement 4 below.
4. Only after everything works, add the stretch-challenge `try/except` for divide-by-zero.

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

**Default Parameter Values**

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

**Variable Scope and `global`**

```python
counter = 0             # global variable

def increment():
    global counter      # must declare to modify global
    counter += 1

increment()
print(counter)          # 1
```

> <mark>**Name Hiding (Shadowing):** A local variable with the same name as a global hides (shadows) the global inside the function.</mark>

```python
x = 10

def show():
    x = 99   # local x shadows global x
    print(x)

show()       # 99
print(x)     # 10 — global unchanged
```

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** Why does the course style guide (Guideline #11 above) tell you to avoid global variables and use function parameters/return values instead?

**Answer:** Functions that rely on `global` are harder to test and reason about in isolation — you have to know the current state of a variable defined somewhere else in the file to predict what the function will do, and any function can silently change that shared state. A function that takes parameters and returns a value is self-contained: give it the same inputs, and you always get the same output, regardless of what else is happening in the program. This "no hidden side effects" property is exactly what the CPT's Prompt 3c is asking you to explain about your own function.
</details>

**Recursion**

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

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** What happens if you write a recursive function and forget the base case entirely?

**Answer:** The function calls itself forever (or until Python hits its recursion limit and raises a `RecursionError`), because there's never a condition that tells it to stop and start returning values back up the call stack. Every recursive function you write should let you point to the exact line that is the base case, and explain why the recursive case is guaranteed to reach it eventually.
</details>

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

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** What's the practical difference between `import random` and `from random import randint`, in terms of how you'd call the function afterward?

**Answer:** With `import random`, you must prefix every call with the module name: `random.randint(1, 10)`. With `from random import randint`, you import just that one function directly into your file's namespace, so you call it as `randint(1, 10)` with no prefix. The first style is safer in larger programs (it's always clear which module a function came from); the second is more convenient for one or two functions you'll use constantly.
</details>

---

### Project: Random Trivia Quiz Generator

Build a trivia quiz program that pulls together **modules, functions, lists, dictionaries, and string formatting** — everything you've learned so far — into one working project.

**🧩 Scaffolding — build it across several days:**
- **Day 1:** Hard-code your 8 questions as a list of dictionaries; write `ask_question()` and test it on ONE question.
- **Day 2:** Write `run_quiz()` to loop through all questions and track score; get the raw score printing correctly.
- **Day 3:** Add `random` (shuffle questions), `datetime` (timing), and the percentage-formatted score. Add the three import styles last.
- **Day 4 (stretch):** Add the `json` save/load high-score feature.

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

> 📌 **Worked Example — try/except in a different context (library checkout days)**
> ```python
> try:
>     days = int(input("How many days do you want to borrow this book? "))
>     if days > 21:
>         raise ValueError("Max borrow period is 21 days.")
>     days_of_slack = 21 - days
> except ValueError as e:
>     print(f"Invalid entry: {e}")
> else:
>     print(f"Checked out. {days_of_slack} days of slack before the 21-day limit.")
> finally:
>     print("Checkout attempt logged.")
> ```
> Run this in your head with `days = "abc"`, then `days = 30`, then `days = 10` — three different paths through the same `try/except/else/finally` block, just like the calculator you're about to build will handle three different kinds of bad input.

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

> <mark>**Rule of thumb:** Order `except` blocks from **most specific to most general**. Python checks them in order and runs the first match.</mark>

```python
try:
    x = int("abc")
except ValueError:          # caught here — most specific
    print("Value error")
except Exception:           # broader fallback
    print("Some error")
```

**Propagating Exceptions**

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

> 🔖 **PCEP note:** the full `BaseException` → `Exception` hierarchy tree (PCEP 4.3, exam-level memorization) is covered in **[PCEP Certification Path — Semester 2](#pcep-certification-path-semester-2)**. For the CPT, knowing the common exceptions table above and how to order `except` blocks is enough.

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** Why does a well-designed program almost always use `try/except` instead of just trusting that user input will be valid?

**Answer:** You can't control what a user types — they might enter letters where a number is expected, leave a field blank, or divide by zero by accident. `try/except` lets your program catch that bad input and respond gracefully (with a clear message) instead of crashing outright. For the CPT specifically, a program that crashes on unexpected input during your recorded video will hurt your score — exception handling is part of writing a robust, testable program.
</details>

### Activity: Safe Calculator

Build a calculator program that:
1. Accepts two numbers and an operator (`+`, `-`, `*`, `/`)
2. Handles `ZeroDivisionError` and `ValueError`
3. Loops until the user types `quit`
4. Uses a function for each operation
5. Uses `try-except-else-finally`

**🧩 Scaffolding — build it in this order:**
1. Write the four operation functions (reuse them from Math Operations Calculator if you've already built that).
2. Get ONE calculation working with `try/except` around it, no loop yet.
3. Wrap it in a `while` loop that exits on `"quit"`.
4. Add `else`/`finally` last.

**Starter code:**
```python
#       Assignment:  Program: Safe Calculator
#       Description: Menu-driven calculator with full exception handling.
#       Language:    Python 3.x

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b

while True:
    op = input("Enter operator (+, -, *, /) or 'quit': ")
    if op == "quit":
        break

    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        # TODO: call the right function based on `op`
        # TODO: handle an unrecognized operator too
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Can't divide by zero.")
    else:
        # TODO: print the result
        pass
    finally:
        print("Attempt complete.\n")
```

*AP CSP: CRD-2.J | PCEP: 4.4*

---

## File Operations

`📋 AP CSP: AAP-3.A, CRD-2.B, CRD-2.J` — Collect and represent data; implement and test programs.

**Explanation**

So far, every program you've written loses all its data the moment it stops running. **File operations** let a program **read** data that already exists on disk and **write** data that survives after the program ends — the difference between a program that "remembers" and one that starts from zero every time.

Python's `open()` function is the entry point for all file work. The safest way to use it is with a `with` block, which automatically closes the file for you — even if an error happens partway through.

```python
with open("filename.txt", "r") as file:
    content = file.read()
# file is automatically closed here, even if something went wrong
```

**Key Words**

| Term | Meaning |
|---|---|
| **File mode** | How you're opening the file: `"r"` read, `"w"` write (overwrites!), `"a"` append, `"r+"` read+write |
| **`with` statement** | Automatically closes the file when the block ends — always prefer this over manual `open()`/`close()` |
| **Stream** | The connection Python keeps open to the file while you're reading/writing it |
| **Newline character (`\n`)** | Marks the end of a line — `.readlines()` keeps these; `.strip()` removes them |
| **Text file** | Stores human-readable characters (`.txt`, `.csv`, `.py`) |
| **Delimiter** | The character that separates fields on a line (commonly `,` in `.csv` files) |

**File Modes**

| Mode | Meaning | If file doesn't exist | If file exists |
|---|---|---|---|
| `"r"` | Read only | Raises `FileNotFoundError` | Reads from the start |
| `"w"` | Write only | Creates it | **Erases existing content first** |
| `"a"` | Append | Creates it | Adds to the end, keeps existing content |
| `"r+"` | Read and write | Raises `FileNotFoundError` | Reads and writes without erasing |

> <mark>**Common trap:** `"w"` mode **erases the entire file** the instant you open it — even if you never write anything. If you need to keep existing content, use `"a"` (append) or `"r+"`.</mark>

**Reading Files — Three Ways**

```python
with open("data.txt", "r") as file:
    whole_thing = file.read()        # one big string, includes \n characters

with open("data.txt", "r") as file:
    all_lines = file.readlines()     # list of strings, one per line (keeps \n)

with open("data.txt", "r") as file:
    for line in file:                # loop line-by-line — best for large files
        print(line.strip())          # .strip() removes the trailing \n
```

**Writing and Appending**

```python
with open("output.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")

with open("output.txt", "a") as file:
    file.write("This gets added to the end\n")
```

**When Would You Use This?**

Any time your program needs to **outlive a single run** — saving a high score, loading a roster of students, or writing a log of every calculation a user made. File operations are also how real programs move data between each other: one program writes a file, another reads it.

**Best Practices**

- **Always use `with open(...) as file:`** — never call `open()` without it.
- **Always wrap file access in `try/except`**, catching `FileNotFoundError` at minimum.
- Double-check your **mode** before writing — `"w"` silently destroys existing content.
- Use `.strip()` on every line you read from a text file to remove the trailing `\n` before you use the value.

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** You want to add a new high score to the end of an existing scores file without erasing the old scores. Which file mode do you use, and what would go wrong if you used `"w"` instead?

**Answer:** Use `"a"` (append). `"w"` mode erases the entire existing file the moment you open it, so every previous score would be gone before you ever wrote the new one — you'd end up with a file containing only the newest score.
</details>

> 📌 **Worked Example — file loading in a different context (favorite colors)**
> ```python
> def load_colors(filename):
>     try:
>         with open(filename, "r") as file:
>             return [line.strip() for line in file]
>     except FileNotFoundError:
>         return []
>
> colors = load_colors("colors.txt")
> print(f"Loaded {len(colors)} colors:", colors)
> ```
> This "try to load, fall back to an empty list" pattern is the backbone of the roster-loading function you'll write below — same technique, different data.

**Sample Program**

```python
# Append a new high score to a running log file, then print the full history

def log_score(name, score, filename="scores_log.txt"):
    with open(filename, "a") as file:
        file.write(f"{name},{score}\n")

def show_log(filename="scores_log.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                print(f"{name}: {score}")
    except FileNotFoundError:
        print("No scores logged yet.")

log_score("Alice", 91)
log_score("Bob", 76)
show_log()
```

### Activity: Student Roster File Manager

Write a program that manages a roster stored in a text file called `roster.txt` (one name per line).

**🧩 Scaffolding — build it in this order:**
1. Write `load_roster()` alone and test it (both with and without an existing `roster.txt`).
2. Write `add_student()` and confirm names actually persist between separate runs of the program.
3. Write `save_roster()` and wire it into the "remove" menu option.
4. Build the `main()` menu loop last, once all three functions work independently.

**Requirements:**

1. Write a function `load_roster(filename)` that reads the file and returns a list of names. If the file doesn't exist, catch `FileNotFoundError` and return an empty list instead of crashing.
2. Write a function `add_student(filename, name)` that **appends** a new name to the file (don't overwrite the existing roster!).
3. Write a function `save_roster(filename, roster)` that **overwrites** the file with the current contents of a roster list (one name per line) — used after removing a student.
4. In `main()`, build a menu (`while` loop) that lets the user: view the roster, add a student, remove a student (remove from the in-memory list, then call `save_roster()`), or quit.
5. Every write operation must use a `with` block. Every read must be wrapped in a `try/except FileNotFoundError`.

*AP CSP: AAP-3.A, CRD-2.B, CRD-2.J*

**Actual Program with Test Samples**

```python
#       Assignment:  File Operations — Student Roster File Manager
#       Description: Loads, adds to, removes from, and saves a student roster stored in a text file.
#       Language:    Python 3.x

def load_roster(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def add_student(filename, name):
    with open(filename, "a") as file:
        file.write(name + "\n")


def save_roster(filename, roster):
    with open(filename, "w") as file:
        for name in roster:
            file.write(name + "\n")


def main():
    filename = "roster.txt"
    roster = load_roster(filename)

    while True:
        print("\n1) View  2) Add  3) Remove  4) Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            print("Roster:", roster)
        elif choice == "2":
            name = input("Name to add: ")
            add_student(filename, name)
            roster.append(name)
        elif choice == "3":
            name = input("Name to remove: ")
            if name in roster:
                roster.remove(name)
                save_roster(filename, roster)
            else:
                print(f"{name} not found.")
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
```

**Sample Test Cases**

| Starting `roster.txt` | Action | Resulting Roster |
|---|---|---|
| *(file doesn't exist)* | `load_roster()` | `[]` (no crash) |
| `["Ava", "Liam"]` | `add_student("Noah")` | `["Ava", "Liam", "Noah"]` |
| `["Ava", "Liam", "Noah"]` | remove `"Liam"` → `save_roster()` | `["Ava", "Noah"]` |

---

## Data Structures Deep Dive

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

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** A teacher wants to know which students are enrolled in *both* Period 1 and Period 3. Would a `list` or a `set` make that check easier to write, and why?

**Answer:** A `set`, because set intersection (`&`) does exactly that check in one operation: `period_1 & period_3`. With lists you'd have to manually loop through one list and check membership in the other, writing several lines of code to do what a set does in one.
</details>

---

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

> 🔖 **PCEP note:** frozensets — an immutable version of `set` — are a PCEP-adjacent topic that build on this section. They're covered in **[PCEP Certification Path — Semester 2](#pcep-certification-path-semester-2)**, along with a capstone project that ties frozensets together with file operations, built-in functions, and lambdas.

---

## Object-Oriented Programming (OOP)

`📋 AP CSP: AAP-3.B` — Abstractions; `CRD-2.B` — Implement in a language.

> **Why OOP?** Real programs model real-world things — students, cars, bank accounts, game characters. OOP lets us **group data and behavior** together in reusable, organized units called **classes**.

### Core OOP Concepts

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

### Building a Class

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

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** What is `self`, really — why does every instance method need it as the first parameter?

**Answer:** `self` is how a method knows *which* object it's currently operating on. When you call `car1.start_engine()`, Python automatically passes `car1` in as `self`, so `self.make` inside the method refers to `car1`'s make specifically — not `car2`'s. Without `self`, a method would have no way to tell one object's data apart from another's.
</details>

### Types of Methods

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

### Inheritance

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

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** In the `animals` loop above, every object calls `.speak()` the same way, but `Dog` objects and `Cat` objects print different things. What's this called, and why is it useful?

**Answer:** This is **polymorphism** — different classes responding to the same method call in their own way. It's useful because the loop doesn't need to know or care whether each item is a `Dog` or a `Cat`; it just calls `.speak()` and trusts each object to know how to respond correctly. This lets you add a `Bird` class later without ever touching the loop.
</details>

### Magic / Dunder Methods

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

> 📌 **Worked Example — inheritance in a different context (vehicles)**
> ```python
> class Vehicle:
>     def __init__(self, brand, model, year):
>         self.brand = brand
>         self.model = model
>         self.year = year
>
>     def describe(self):
>         return f"{self.year} {self.brand} {self.model}"
>
> class Motorcycle(Vehicle):
>     def sound(self):
>         return f"The {self.model} roars to life."
>
> bike = Motorcycle("Harley-Davidson", "Iron 883", 2023)
> print(bike.describe())
> print(bike.sound())
> ```
> This is the minimum skeleton — one base class, one subclass, one object, with the subclass overriding/adding a method. Whichever OOP Zoo option you choose below (Zoo, Library, or RPG Party), you'll build that same base-class → subclass → container-class shape, just in your own domain.

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

**🧩 Scaffolding — build it in this order:**
1. Build `Animal` + one subclass + one object (see Worked Example above); confirm `.describe()` and `.speak()` both work.
2. Add the remaining subclasses.
3. Build `Zoo` with just `add_animal()` and `show_all()`; test with 2–3 animals.
4. Add `find_by_species()` last.

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

## AP CSP Performance Task Preparation

`📋 AP CSP: CRD-2` — Program Design and Development

> The **AP CSP Create Performance Task (CPT)** is 30% of your AP score. You write a program and submit written responses explaining it. Everything in Sections 1–4, File Operations, Data Structures, and OOP above was chosen and sequenced specifically to get you ready for this. This section ties it all together.

### CPT Requirements at a Glance

| Requirement | Description |
|---|---|
| **Program Purpose** | Clearly state what problem your program solves |
| **Algorithm** | Must include sequencing, selection, AND iteration |
| **Abstraction** | Must use a list (or other collection) and a procedure/function |
| **Procedure with parameter** | A function that takes input and affects behavior |
| **Output** | Must produce visible output based on input |

### CPT Checklist — Does Your Program Have?

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

> 📌 **Worked Example — a minimal (but complete) CPT-checklist-passing program, annotated**
> ```python
> def calculate_discount(price, is_member):        # ← function WITH a parameter
>     if is_member:                                # ← selection
>         return price * 0.8
>     return price
>
> prices = [12.99, 45.00, 8.50, 30.00]              # ← list (abstraction/collection)
> member_status = [True, False, True, False]
>
> total = 0
> for i in range(len(prices)):                      # ← iteration
>     final_price = calculate_discount(prices[i], member_status[i])   # ← function CALLED
>     print(f"Item {i+1}: ${final_price:.2f}")
>     total += final_price
>
> print(f"Total: ${total:.2f}")                      # ← output
>
> print(calculate_discount(20.00, True))              # ← SECOND call, different arguments
> ```
> Checklist walk-through: purpose (calculate discounted checkout totals) ✅, input (the `prices`/`member_status` lists stand in for real input — a live CPT would use `input()` or a data file) ✅, sequencing/selection/iteration ✅ (the `for` loop + `if`), abstraction (the `prices` list) ✅, function with a parameter that's called twice with different arguments ✅, visible output ✅. This is intentionally small — your actual CPT program should be a full, original idea, but every one of these six boxes has to be checkable in it exactly like this.

### CPT Written Response Tips

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

### Practice PT 1 — Idea List

Use these for the **Practice PT 1** window (Weeks 8–11). Each idea below already satisfies the CPT checklist — the point of Practice PT 1 is rehearsing the *process* (design → code → test → written responses) on a smaller, guided idea before the pressure of the real thing. Pick ONE, or propose your own and run it past your teacher.

| # | Idea | Input | List/Collection | Function + Parameter | Output |
|---|---|---|---|---|---|
| 1 | **Grade Book Averager** | Scores typed in one at a time | List of scores | `letter_grade(score)` — converts a score to a letter | Class average + list of letter grades |
| 2 | **Password Strength Checker** | A password string | List of the password's characters | `check_strength(password)` — returns a strength label | Strength rating + specific feedback |
| 3 | **Tip Calculator for a Group** | Bill amounts for each person | List of bill amounts | `calculate_tip(amount, percent)` — computes tip for one bill | Per-person tip + group total |
| 4 | **Word Frequency Counter** | A sentence or short paragraph | List of words (via `.split()`) | `count_word(word, word_list)` — counts occurrences | Most frequent word + its count |
| 5 | **Simple To-Do List Manager** | Task names typed in a loop | List of tasks | `mark_done(task, task_list)` — updates a task's status | Printed to-do list with statuses |

**🧩 Scaffolding for Practice PT 1 (Weeks 8–11):**
- **Week 8 (intro):** Choose your idea; sketch input/output on paper; identify your list and your function-with-parameter *before* writing any code.
- **Week 9:** Write the function alone and test it with at least 3 different inputs, by itself, before wiring it into the full program.
- **Week 10:** Build the full program around the function — the loop, the list, the two function calls with different arguments.
- **Week 11 (due Fri):** Test edge cases (empty input, unexpected input), then write your four written responses (3a–3d) using the CPT Written Response Tips above.

### Practice PT 2 — Idea List

Use these for the **Practice PT 2** window (Weeks 12–14). These are intentionally a step up from Practice PT 1 — most naturally pull in a **dictionary or list-of-dictionaries**, File Operations, or OOP (all covered by Week 12), which the official December CPT will likely also benefit from.

| # | Idea | Input | List/Collection | Function + Parameter | Output |
|---|---|---|---|---|---|
| 1 | **Student Roster Analyzer** | Names + scores, one student at a time | List of dictionaries (`{"name":..., "score":...}`) | `pass_or_fail(score)` — returns a status string | Class roster with pass/fail flags + class average |
| 2 | **Inventory Restock Alert** | Item names + current stock counts | List of dictionaries (`{"item":..., "stock":...}`) | `needs_restock(stock, threshold)` — returns True/False | List of items that need restocking |
| 3 | **Simple Save/Load High Score Game** | A guessed number, repeated | List of past guesses (this run) | `check_guess(guess, target)` — returns a hint string | Feedback per guess + score saved to file with File Operations |
| 4 | **Basic Animal Shelter Tracker** (OOP) | Animal name/species/age, one at a time | List of `Animal` objects | An `Animal` method or a function that takes an `Animal` as a parameter | Roster of animals + count by species |
| 5 | **Movie Recommendation Filter** | A list of movies with genre/rating | List of dictionaries | `matches_preference(movie, genre)` — returns True/False | Filtered list of recommended movies |

**🧩 Scaffolding for Practice PT 2 (Weeks 12–14):**
- **Week 12 (intro):** Choose your idea; if it uses File Operations, get a working `load()`/`save()` pair *before* building the rest.
- **Week 13:** Build the core loop and function; if it's the OOP option, get your class working standalone first (like the OOP Zoo Worked Example above).
- **Week 14 (due Fri):** CPT-checklist self-review workshop in class, then submit code + written responses.

---

# Final Project Options

### Option A — Text-Based Adventure Game (Beginner–Intermediate)

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

### Option B — Student Data Tracker (Intermediate)

Build a command-line tracker that:
- Stores student records as a list of dictionaries
- Supports add, delete, search, and update operations
- Calculates class average, highest/lowest scores
- Uses OOP (a `Student` class with methods)
- Handles all exceptions gracefully
- Optionally reads/writes to a `.json` file

**AP CSP Alignment:** CRD-2.B, AAP-3.A, AAP-3.B, AAP-3.C, AAP-4.A

---

### Option C — Mini Minesweeper (Advanced)

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

## PCEP Certification Path — Semester 2

`🏅 Semester 2, Jan – June`

> **What this section is:** everything that's specifically on the PCEP-30-02 exam but wasn't needed for the AP CSP CPT — pulled out of Semester 1 so it doesn't compete with CPT prep, and spread across Semester 2 at a pace that gives it room to actually stick. You already have a full year of general Python fluency (Sections 1–4, File Operations, OOP) under your belt by the time you start this section — that foundation is what makes this content approachable now instead of overwhelming back in the fall.

### 📅 PCEP Pacing Guide — Semester 2 (Tentative)

`Jan 5 – Jun (exam window TBD by district testing calendar)`

| Weeks | Content Focus | Activities |
|---|---|---|
| 1–3 | Numeral Systems; Bitwise Operators | Bitwise "Try It Yourself" trace practice |
| 4–6 | Built-In Functions (`map`, `filter`, `reduce`, `zip`, `any`, `all`) | Grade Report Refactor |
| 7–8 | Lambda Functions | Sort It Your Way |
| 9–10 | Frozensets | Class Roster Overlap |
| 11 | Exception Hierarchy Deep Dive | Hierarchy trace practice |
| 12–13 | Culminating Project: Library Catalog Analyzer | — |
| 14+ | PCEP practice exams; targeted review by exam section | — |

*(Remaining CSP Big Ideas not covered by the CPT continue in parallel per the department's existing January–April sequence — see [[cs-pathway-planning]].)*

---

### Numeral Systems

`🔖 PCEP 1.3` — Introduce numeral systems

Python supports writing integer literals in multiple bases:

```python
decimal     = 255        # base 10
binary      = 0b11111111 # base 2  → 255
octal       = 0o377      # base 8  → 255
hexadecimal = 0xFF       # base 16 → 255

print(binary, octal, hexadecimal)  # All print: 255 255 255
```

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** `0b1010` — what decimal value does this represent, and how do you get there?

**Answer:** `10`. Reading the binary digits right to left, each position is worth a power of 2: `1010` = `(1×8) + (0×4) + (1×2) + (0×1)` = `8 + 0 + 2 + 0` = `10`.
</details>

---

### Bitwise Operators

`🔖 PCEP 1.4`

**Why Bitwise Operators Matter**

Bitwise operators work directly on the **binary representation** of numbers — the individual `0`s and `1`s — rather than on the number's value as a whole. Most everyday Python code never needs them, but they matter for a few reasons worth knowing:

- **They're on the PCEP exam** — you're expected to trace what `&`, `|`, `^`, `~`, `<<`, and `>>` do to binary values.
- **They connect back to how computers actually store data** — ties directly to the binary/decimal/hex conversions you just learned.
- **They show up in real systems programming**: setting individual permission flags (read/write/execute), working with network protocols, compressing data, and low-level graphics/hardware code all lean on bitwise operations because they're extremely fast and memory-efficient.
- **Shifts are a fast way to multiply/divide by powers of 2**: `a << 1` doubles a number, `a >> 1` halves it (integer division) — a trick you'll sometimes see in performance-sensitive code.

Python numbers can be written in **binary** (base 2) using the `0b` prefix. Each digit (called a *bit*) is worth a power of 2, reading right to left: 1, 2, 4, 8, 16...

```python
a = 0b1010   # decimal 10
b = 0b1100   # decimal 12
```

```
a = 1 0 1 0   →  8+0+2+0 = 10
b = 1 1 0 0   →  8+4+0+0 = 12
```

Bitwise operators compare two numbers **column by column**, one bit at a time.

**AND (`&`) — "both must be 1"**

```python
print(a & b)   # 8
```
```
  1010
& 1100
------
  1000   → 8
```

**OR (`|`) — "at least one must be 1"**

```python
print(a | b)   # 14
```
```
  1010
| 1100
------
  1110   → 14
```

**XOR (`^`) — "exactly one, not both"**

```python
print(a ^ b)   # 6
```
```
  1010
^ 1100
------
  0110   → 6
```

**NOT (`~`) — flips every bit**

```
~a  =  -(a + 1)
```
```python
print(~a)   # -11
```

**Left shift (`<<`) — slide bits left, fill with 0s**

```python
print(a << 1)   # 20
```
```
1010  →  10100
```
Each left shift by 1 is the same as **multiplying by 2**.

**Right shift (`>>`) — slide bits right, drop the end**

```python
print(a >> 1)   # 5
```
```
1010  →  101
```
Each right shift by 1 is the same as **integer division by 2** (rounding down).

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** A student meant to write `if is_valid and has_permission:` but accidentally typed `if is_valid & has_permission:`. Will this usually still work? Why is it still bad practice?

**Answer:** With plain `True`/`False` booleans it will often *appear* to work, because `&` on booleans happens to behave like `and` in simple cases. But `&` is a **bitwise** operator, not a logical one — it doesn't short-circuit the way `and` does, and it behaves completely differently on non-boolean values (like actual integers). Mixing them up is a classic, hard-to-spot bug; always use `and`/`or`/`not` for logic and reserve `&`/`|`/`^`/`~` for actual bit manipulation.
</details>

**Try it yourself**

Before running the code, convert `a` and `b` to binary on paper and work out each operation by hand column by column. Then check your answers with `print()`.

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

---

### Built-In Functions

`📋 AP CSP: AAP-2.G, AAP-3.B` — Use existing abstractions to manage complexity.
`🔖 PCEP-adjacent` — not a separately numbered PCEP-30-02 objective, but shows up throughout the certification exam's code-reading questions.

**Explanation**

A **built-in function** is a function Python provides for you automatically — no `import`, no `def`, it's just there the moment Python starts. You've already been using several (`print()`, `len()`, `int()`, `range()`) without thinking of them as a category. This section introduces the built-ins that let you *transform*, *filter*, and *summarize* data in a single line, instead of writing a `for` loop every time.

**When Would You Use This?**

Any time you need to apply the same operation to every item in a collection (`map`), keep only the items that meet a condition (`filter`), combine every item into one result (`reduce`), pair up two lists (`zip`), or ask a yes/no question about an entire collection (`any`, `all`) — reach for a built-in before you reach for a loop.

**Key Built-In Functions**

| Function | What It Does | Example | Result |
|---|---|---|---|
| `map(func, iterable)` | Applies `func` to every item | `list(map(str.upper, ["hi","bye"]))` | `['HI', 'BYE']` |
| `filter(func, iterable)` | Keeps items where `func` returns `True` | `list(filter(lambda x: x % 2 == 0, range(10)))` | `[0, 2, 4, 6, 8]` |
| `reduce(func, iterable)` | Combines all items into one value (needs `from functools import reduce`) | `reduce(lambda a, b: a + b, [1,2,3,4])` | `10` |
| `zip(iter1, iter2)` | Pairs up items from two+ iterables | `list(zip([1,2],["a","b"]))` | `[(1,'a'), (2,'b')]` |
| `any(iterable)` | `True` if **at least one** item is truthy | `any([0, 0, 3])` | `True` |
| `all(iterable)` | `True` if **every** item is truthy | `all([1, 1, 0])` | `False` |
| `sorted(iterable, key=...)` | Returns a **new** sorted list | `sorted([3,1,2])` | `[1, 2, 3]` |
| `chr(n)` | Converts a Unicode code point to a character | `chr(65)` | `'A'` |
| `ord(c)` | Converts a character to its Unicode code point | `ord('A')` | `65` |

> <mark>**Exam-style trap:** `map()` and `filter()` return a **lazy iterator**, not a list — you must wrap them in `list(...)` to see or print the actual values. `sorted()` and `map()`/`filter()` never modify the original list; they hand you back a brand-new one.</mark>

**Example**

```python
scores = [55, 82, 91, 40, 76, 88]

passing = list(filter(lambda s: s >= 60, scores))     # keep passing scores
curved  = list(map(lambda s: s + 5, scores))           # add 5 to every score
top_3   = sorted(scores, reverse=True)[:3]             # highest 3 scores

print("Passing:", passing)   # [82, 91, 76, 88]
print("Curved:",  curved)    # [60, 87, 96, 45, 81, 93]
print("Top 3:",   top_3)     # [91, 88, 82]
```

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** `evens = filter(lambda x: x % 2 == 0, range(10))`. You immediately try `print(evens)` and it does NOT show `[0, 2, 4, 6, 8]`. What went wrong, and how do you fix it?

**Answer:** `filter()` returns a **lazy filter object**, not a list — printing it directly shows something like `<filter object at 0x...>`. You need to wrap it: `print(list(evens))`. This is a classic PCEP exam trap that applies to `map()` too.
</details>

**Best Practices**

- Wrap `map()`/`filter()` in `list()` before printing — otherwise you'll just see `<filter object at 0x...>`.
- If the built-in version is harder to read than a plain `for` loop, use the `for` loop.
- `sorted(iterable, key=func)` is the built-in most worth mastering.
- `reduce()` needs an explicit import (`from functools import reduce`).

### Activity: Grade Report Refactor

Take the **Grade Calculator** activity you built earlier (Section 2) and refactor part of it using built-in functions instead of a `for` loop.

**Requirements:**
1. Start with a list of at least 10 student scores (`int` values 0–100).
2. Use `filter()` to build a list of students who **passed** (score ≥ 70).
3. Use `map()` to build a list of the same scores **converted to a 4.0 GPA scale** (formula: `score / 25`, rounded to 2 decimal places with `round()`).
4. Use `sorted()` with a `key=` and `reverse=True` to print the scores from highest to lowest **without changing the original list**.
5. Use `any()` to check whether **any** student scored a perfect 100, and `all()` to check whether **every** student passed.
6. Print all five results with clear labels.

*AP CSP: AAP-2.G, CRD-2.B*

**Actual Program with Test Samples**

```python
#       Assignment:  Built-In Functions — Grade Report Refactor
#       Description: Analyzes a list of scores using map, filter, sorted, any, all.
#       Language:    Python 3.x

def analyze_scores(scores):
    passing   = list(filter(lambda s: s >= 70, scores))
    gpa_scale = list(map(lambda s: round(s / 25, 2), scores))
    ranked    = sorted(scores, reverse=True)
    perfect   = any(s == 100 for s in scores)
    all_pass  = all(s >= 70 for s in scores)
    return passing, gpa_scale, ranked, perfect, all_pass


def main():
    scores = [55, 82, 91, 40, 76, 88, 100, 63, 74, 59]
    passing, gpa_scale, ranked, perfect, all_pass = analyze_scores(scores)

    print("Passing scores:", passing)
    print("GPA scale:", gpa_scale)
    print("Ranked (high to low):", ranked)
    print("Original list unchanged:", scores)
    print("Any perfect score?", perfect)
    print("Did everyone pass?", all_pass)


if __name__ == "__main__":
    main()
```

**Sample Test Cases**

| Input `scores` | Passing (≥70) | Any 100? | All passed? |
|---|---|---|---|
| `[55, 82, 91, 40, 76, 88, 100, 63, 74, 59]` | `[82, 91, 76, 88, 100, 74]` | `True` | `False` |
| `[70, 71, 72, 73]` | `[70, 71, 72, 73]` | `False` | `True` |
| `[10, 20, 30]` | `[]` | `False` | `False` |

---

### Lambda Functions

`📋 AP CSP: AAP-2.G` `🔖 PCEP-adjacent`

**Explanation**

A **lambda** is a small, unnamed ("anonymous") function written in a single line. It's Python's shorthand for a function you only need once — usually as an argument to another function like `sorted()`, `map()`, or `filter()`. A lambda can only contain **one expression** and it automatically `return`s the result of that expression.

```python
square = lambda x: x ** 2

# Equivalent to:
def square(x):
    return x ** 2
```

**Key Words**

| Term | Meaning |
|---|---|
| **Lambda / anonymous function** | A function with no name, defined inline with the `lambda` keyword |
| **Expression** | A single computation that produces a value |
| **`key=` argument** | Tells `sorted()`/`min()`/`max()` *what to sort by* |
| **First-class function** | A function that can be passed around like any other value |

**Example**

```python
students = [("Alice", 91), ("Bob", 76), ("Charlie", 88)]

by_score = sorted(students, key=lambda s: s[1], reverse=True)
print(by_score)   # [('Alice', 91), ('Charlie', 88), ('Bob', 76)]
```

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** Why can't a lambda replace a `def` function that needs to print three different values and then return a result?

**Answer:** A lambda is restricted to a single **expression** — no `print()` statements, no multiple lines, no loops, no `if/else` blocks (only a limited conditional expression). Anything that needs multiple steps or side effects belongs in a real `def` function.
</details>

**Best Practices**

- Keep lambdas **short** — one expression.
- Never assign a lambda to a variable just to call it later — that's what `def` is for.
- The most common, most useful pattern is `sorted(iterable, key=lambda item: ...)`.

### Activity: Sort It Your Way

Given a list of dictionaries representing books (`title`, `author`, `year`, `pages`), write **three separate `sorted()` calls**, each using a different `lambda` key:

1. Sort by `year`, oldest first.
2. Sort by `pages`, longest first (`reverse=True`).
3. Sort by the **length of the title** (`len(title)`), shortest first.

Print each sorted list with a clear label before it.

*AP CSP: AAP-2.G*

**Actual Program with Test Samples**

```python
#       Assignment:  Lambda Functions — Sort It Your Way
#       Description: Sorts a list of book dictionaries three different ways using lambda keys.
#       Language:    Python 3.x

books = [
    {"title": "Dune", "author": "Herbert", "year": 1965, "pages": 412},
    {"title": "1984", "author": "Orwell", "year": 1949, "pages": 328},
    {"title": "The Hobbit", "author": "Tolkien", "year": 1937, "pages": 310},
]

by_year      = sorted(books, key=lambda b: b["year"])
by_pages     = sorted(books, key=lambda b: b["pages"], reverse=True)
by_title_len = sorted(books, key=lambda b: len(b["title"]))

print("By year (oldest first):")
for b in by_year:
    print(f"  {b['year']} — {b['title']}")

print("By pages (longest first):")
for b in by_pages:
    print(f"  {b['pages']}pp — {b['title']}")

print("By title length (shortest first):")
for b in by_title_len:
    print(f"  {len(b['title'])} chars — {b['title']}")
```

**Sample Test Cases**

| Sort Key | First Result | Last Result |
|---|---|---|
| `year` (ascending) | *The Hobbit* (1937) | *Dune* (1965) |
| `pages` (descending) | *Dune* (412pp) | *The Hobbit* (310pp) |
| `len(title)` (ascending) | *1984* (4 chars) | *The Hobbit* (10 chars) |

---

### Frozensets

`📋 AP CSP: AAP-3.A, AAP-3.B` `🔖 PCEP-adjacent`

**Explanation**

A **frozenset** is exactly what it sounds like: a `set` that's been frozen — **immutable**, just like a tuple is an immutable list. Once created, you cannot add, remove, or change its contents.

```python
colors = frozenset(["red", "green", "blue"])
# colors.add("yellow")   # AttributeError — frozensets have no .add()
```

**When Would You Use This?**

Use a `frozenset` any time you want the **uniqueness and fast-lookup** benefits of a set, but need the collection to be **unchangeable** — most often because it's being used as a **dictionary key** (regular sets can't be dict keys; frozensets can).

```python
schedule = {
    frozenset(["Mon", "Wed", "Fri"]): "Math",
    frozenset(["Tue", "Thu"]): "Science",
}
print(schedule[frozenset(["Tue", "Thu"])])   # Science
```

**Key Words**

| Term | Meaning |
|---|---|
| **Immutable** | Cannot be changed after creation |
| **Hashable** | Can be used as a dictionary key or set member (frozensets are hashable; sets are not) |
| **Set operations** | `\|` union, `&` intersection, `-` difference, `^` symmetric difference — all work on frozensets too |

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** Why can a `frozenset` be used as a dictionary key, but a regular `set` cannot?

**Answer:** Dictionary keys must be **hashable** — Python needs to compute a stable hash value for a key that never changes for the life of the object. A regular `set` is mutable (you could `.add()` to it after using it as a key, which would break the hash), so Python disallows it as a key. A `frozenset` is guaranteed immutable, so its hash is stable, making it a legal dictionary key.
</details>

**Best Practices**

- Use `set` for a collection you plan to **modify**; use `frozenset` for a collection meant to stay **constant**.
- Reach for a `frozenset` specifically when you need to use a collection as a **dictionary key**.

### Activity: Class Roster Overlap

Two teachers each have a frozenset of student names in their AP CSP class:

```python
period_1 = frozenset(["Ava", "Liam", "Noah", "Emma", "Mia"])
period_3 = frozenset(["Noah", "Emma", "Sofia", "Lucas"])
```

Write a program that prints:
1. Students in **both** periods (`&`)
2. Students in **either** period, with no duplicates (`|`)
3. Students **only** in Period 1, not Period 3 (`-`)
4. Students in **exactly one** of the two periods, not both (`^`)
5. Whether the two rosters share **any** student at all

*AP CSP: AAP-3.A, AAP-3.B*

**Actual Program with Test Samples**

```python
#       Assignment:  Frozensets — Class Roster Overlap
#       Description: Compares two class rosters using frozenset operations.
#       Language:    Python 3.x

def compare_rosters(period_1, period_3):
    both        = period_1 & period_3
    either      = period_1 | period_3
    only_p1     = period_1 - period_3
    exactly_one = period_1 ^ period_3
    overlaps    = len(both) > 0
    return both, either, only_p1, exactly_one, overlaps


def main():
    period_1 = frozenset(["Ava", "Liam", "Noah", "Emma", "Mia"])
    period_3 = frozenset(["Noah", "Emma", "Sofia", "Lucas"])

    both, either, only_p1, exactly_one, overlaps = compare_rosters(period_1, period_3)

    print("In both periods:", both)
    print("In either period:", either)
    print("Only in Period 1:", only_p1)
    print("In exactly one period:", exactly_one)
    print("Do the rosters overlap?", overlaps)


if __name__ == "__main__":
    main()
```

**Sample Test Cases**

| Operation | Result |
|---|---|
| `period_1 & period_3` | `frozenset({'Noah', 'Emma'})` |
| `period_1 - period_3` | `frozenset({'Ava', 'Liam', 'Mia'})` |
| `period_1 ^ period_3` | `frozenset({'Ava', 'Liam', 'Mia', 'Sofia', 'Lucas'})` |
| overlap check | `True` |

---

### Exception Hierarchy Deep Dive

`🔖 PCEP 4.3` — Python Built-In Exceptions Hierarchy

Section 4 back in the fall covered practical `try/except` and the common exceptions table — that's everything you needed for the CPT. The PCEP exam goes one level deeper and expects you to know the actual **class hierarchy** exceptions are organized into.

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

> <mark>**PCEP Exam Tip:** Order `except` blocks from **most specific to most general**. Python checks them in order and runs the first match — this is why `except ValueError` must come *before* `except Exception` in the same `try` block, never after.</mark>

```python
try:
    x = int("abc")
except ValueError:          # caught here — most specific
    print("Value error")
except Exception:           # broader fallback
    print("Some error")
```

<details><summary>🤔 Thinking Question — check your answer</summary>

**Question:** `ZeroDivisionError` and `IndexError` are both subclasses of `Exception`, but they're not subclasses of *each other*. Looking at the hierarchy tree above, what's the closest common ancestor they share?

**Answer:** `Exception` itself — `ZeroDivisionError` descends through `ArithmeticError`, and `IndexError` descends through `LookupError`, two separate branches that only reconnect at `Exception`. That means a single `except Exception:` block would catch both, but nothing more specific shared between them would.
</details>

---

### Culminating Project: Library Catalog Analyzer

Build a program that reads a small library catalog from a text file, analyzes it using built-in functions and lambdas, and uses frozensets to answer genre questions — pulling together **File Operations (Semester 1), Built-In Functions, Lambda Functions, and Frozensets (all above)** into one working project. This is the natural capstone of the PCEP Certification Path.

**Setup — `catalog.txt` format:** one book per line, comma-separated: `title,author,year,genre1|genre2`

```
Dune,Frank Herbert,1965,Sci-Fi|Adventure
1984,George Orwell,1949,Sci-Fi|Dystopian
The Hobbit,J.R.R. Tolkien,1937,Fantasy|Adventure
Klara and the Sun,Kazuo Ishiguro,2021,Sci-Fi|Drama
```

**🧩 Scaffolding — build it in this order:**
1. Write `load_catalog()` alone and print the raw list of dictionaries it produces.
2. Add the `sorted()`/`filter()`/`map()` lines one at a time, printing after each.
3. Add the frozenset union/intersection logic.
4. Write `save_report()` last.

**Requirements:**

1. Write `load_catalog(filename)` that reads `catalog.txt` line by line (using `with`, wrapped in `try/except FileNotFoundError`) and returns a **list of dictionaries**, each with keys `"title"`, `"author"`, `"year"` (as `int`), and `"genres"` (as a **frozenset** built by splitting on `|`).
2. Use `sorted()` with a `lambda` key to print the catalog **sorted by year**, oldest first.
3. Use `filter()` with a `lambda` to print only books published **after 2000**.
4. Use `map()` with a `lambda` to print a list of just the **titles**, in upper case.
5. Use frozenset operations to find and print:
   - Every **unique genre** across the whole catalog (union `|` of all books' genre frozensets)
   - All books that include **both** "Sci-Fi" and "Adventure" as genres
6. Write `save_report(filename, catalog)` that writes a summary report to `report.txt` — total book count, oldest and newest year, and the full unique-genre list — using a `with` block in `"w"` mode.
7. Include a full program header block.

**Actual Program with Test Samples**

```python
#       Assignment:  Culminating Project — Library Catalog Analyzer
#       Description: Reads a book catalog from file, analyzes it with map/filter/sorted/lambda,
#                    and uses frozensets to compare genres, then writes a summary report.
#       Language:    Python 3.x

def load_catalog(filename):
    catalog = []
    try:
        with open(filename, "r") as file:
            for line in file:
                title, author, year, genres = line.strip().split(",")
                catalog.append({
                    "title": title,
                    "author": author,
                    "year": int(year),
                    "genres": frozenset(genres.split("|")),
                })
    except FileNotFoundError:
        print(f"{filename} not found — starting with an empty catalog.")
    return catalog


def save_report(filename, catalog, all_genres):
    years = [book["year"] for book in catalog]
    with open(filename, "w") as file:
        file.write(f"Total books: {len(catalog)}\n")
        file.write(f"Oldest year: {min(years) if years else 'N/A'}\n")
        file.write(f"Newest year: {max(years) if years else 'N/A'}\n")
        file.write(f"Unique genres: {sorted(all_genres)}\n")


def main():
    catalog = load_catalog("catalog.txt")
    if not catalog:
        return

    by_year   = sorted(catalog, key=lambda b: b["year"])
    modern    = list(filter(lambda b: b["year"] > 2000, catalog))
    titles    = list(map(lambda b: b["title"].upper(), catalog))

    all_genres = frozenset()
    for book in catalog:
        all_genres = all_genres | book["genres"]

    scifi_adventure = [
        b["title"] for b in catalog
        if frozenset(["Sci-Fi", "Adventure"]) <= b["genres"]
    ]

    print("Sorted by year:", [b["title"] for b in by_year])
    print("Published after 2000:", [b["title"] for b in modern])
    print("Titles (upper case):", titles)
    print("All unique genres:", sorted(all_genres))
    print("Sci-Fi AND Adventure:", scifi_adventure)

    save_report("report.txt", catalog, all_genres)


if __name__ == "__main__":
    main()
```

**Sample Test Cases** *(using the four-book `catalog.txt` shown above)*

| Check | Result |
|---|---|
| Sorted by year (oldest first) | `['The Hobbit', '1984', 'Dune', 'Klara and the Sun']` |
| Published after 2000 | `['Klara and the Sun']` |
| Unique genres (union of all frozensets) | `['Adventure', 'Drama', 'Dystopian', 'Fantasy', 'Sci-Fi']` |
| Books with **both** Sci-Fi and Adventure | `['Dune']` |
| `report.txt` after running | `Total books: 4`, `Oldest year: 1937`, `Newest year: 2021` |

**Stretch challenge:** Add a `most_common_genre()` function that uses `max()` with a `key=lambda` to find which single genre appears in the most books — without importing any extra modules.

*AP CSP: AAP-3.A, AAP-3.B, AAP-2.G, CRD-2.B, CRD-2.J*

---

## Certification Alignment Reference

### PCEP-30-02 Exam Topic Map

| PCEP Objective | Topics | Covered In |
|---|---|---|
| **1.1** | Interpreter, compiler, lexis, syntax, semantics | Section 1 — How Python Works *(Semester 1)* |
| **1.2** | Keywords, indentation, comments | Section 1 — Python Structure *(Semester 1)* |
| **1.3** | Literals, variables, numeral systems, PEP-8 | Section 1 *(Semester 1)*; Numeral Systems *(Semester 2)* |
| **1.4** | Operators, precedence, Boolean, bitwise, type casting | Section 1 — Operators *(Semester 1)*; Bitwise Operators *(Semester 2)* |
| **1.5** | `print()`, `input()`, `sep=`, `end=`, `int()`, `float()` | Section 1 — I/O *(Semester 1)* |
| **2.1** | `if`, `if-else`, `if-elif-else`, nested conditionals | Section 2 — Conditionals *(Semester 1)* |
| **2.2** | `while`, `for`, `range()`, `break`, `continue`, `pass`, `else` | Section 2 — Loops *(Semester 1)* |
| **3.1** | Lists, indexing, slicing, methods, comprehensions, 2D lists | Section 3 — Lists *(Semester 1)* |
| **3.2** | Tuples, immutability, nesting | Section 3 — Tuples *(Semester 1)* |
| **3.3** | Dictionaries, keys/values/items, iteration | Section 3 — Dictionaries *(Semester 1)* |
| **3.4** | Strings, indexing, slicing, escaping, methods | Section 3 — Strings *(Semester 1)* |
| **4.1** | Functions, `return`, `None`, recursion | Section 4 — Functions *(Semester 1)* |
| **4.2** | Parameters, arguments, defaults, scope, `global`, shadowing | Section 4 — Functions *(Semester 1)* |
| **4.3** | Exception hierarchy: `BaseException`, `Exception`, `ValueError`, etc. | Exception Hierarchy Deep Dive *(Semester 2)* |
| **4.4** | `try-except`, ordering branches, propagation | Section 4 — Exceptions *(Semester 1)* |
| *Supplemental* | Built-in functions (`map`, `filter`, `sorted`, `zip`, `any`, `all`) | PCEP Certification Path — Built-In Functions *(Semester 2)* |
| *Supplemental* | Lambda (anonymous) functions | PCEP Certification Path — Lambda Functions *(Semester 2)* |
| *Supplemental* | Frozensets (immutable sets) | PCEP Certification Path — Frozensets *(Semester 2)* |
| *Supplemental* | File I/O (`open`, `with`, read/write/append modes) | File Operations *(Semester 1)* |

> <mark>Rows marked *Supplemental* aren't separately numbered objectives in the official PCEP-30-02 exam blocks (file I/O in particular is tested at the next certification level, PCAP) — they're included because they're core Python fluency and directly support both the CPT and the PCEP exam.</mark>

---

### AP CSP Standards Alignment

| AP CSP Standard | Description | Covered In |
|---|---|---|
| **CRD-2.A** | Program design and development | Throughout |
| **CRD-2.B** | Implement algorithms | Functions, OOP, Projects |
| **CRD-2.G** | Call procedures | Functions |
| **CRD-2.J** | Test and debug | Debugging, Exception Handling, File Operations |
| **AAP-2.E** | Sequencing, selection, iteration | Control Flow |
| **AAP-2.F** | Mathematical operations | Operators |
| **AAP-2.G** | Abstraction to manage complexity | Functions, Modules, OOP, Built-In Functions *(Semester 2)*, Lambda Functions *(Semester 2)* |
| **AAP-2.K** | List iteration | Lists |
| **AAP-3.A** | Collect and represent data | Data Structures, File Operations, Frozensets *(Semester 2)* |
| **AAP-3.B** | Use abstractions to organize data | Dictionaries, OOP, Lists, Frozensets *(Semester 2)* |
| **AAP-3.C** | Analyze data to draw conclusions | Data Structures |
| **AAP-4.A** | Data abstractions for complexity | Lists, 2D Lists, Classes |

---

*Document maintained for AP CSP and PCEP-30-02 certification alignment.*
*Reorganized August 2026 — CSP-first, PCEP-Second Semester structure.*
