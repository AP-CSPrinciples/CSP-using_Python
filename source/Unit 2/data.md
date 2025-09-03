# Data


#### Unit 2 Vocabulary

<details><summary>Click Here</summary>

 
**1. Data Representation**

* **Bit**: The smallest unit of data in a computer, represented as either 0 or 1.
* **Byte**: A group of 8 bits. It is the basic unit of storage.
* **Binary**: A number system using only two digits: 0 and 1. It's used to represent data in computers.
* **Hexadecimal**: A base-16 number system often used to represent binary data in a more human-readable form (using digits 0-9 and letters A-F).
* **Character Encoding**: A system for representing characters (letters, digits, symbols) as binary data. Examples include **ASCII** and **Unicode**.

**2. Encoding and Decoding**

* **ASCII (American Standard Code for Information Interchange)**: A character encoding standard that represents text in computers using 7 or 8 bits. It covers characters like letters, digits, punctuation, and control characters.
* **Unicode**: A character encoding standard that represents a wider range of characters, including non-English letters, symbols, and emoji. It's commonly used in modern programming languages.
* **Encoding**: The process of converting data from a human-readable format into a machine-readable format (e.g., converting text into binary).
* **Decoding**: The process of converting machine-readable data (binary) back into a human-readable format (e.g., converting binary back into text).

**3. Compression and Efficiency**

* **Data Compression**: The process of reducing the size of data in order to save storage space or transmission time. There are two types:

  * **Lossless Compression**: Data is compressed without losing any information (e.g., ZIP files, Huffman coding).
  * **Lossy Compression**: Some data is lost in the compression process, but the file size is significantly reduced (e.g., JPEG images, MP3 audio).
* **Huffman Coding**: A lossless data compression algorithm that assigns shorter binary codes to more frequent characters and longer codes to less frequent characters. It's often used in file formats like PNG and ZIP.

**4. Data Processing and Transformation**

* **Data Abstraction**: Simplifying complex data by providing only the essential details. For example, representing a large text file as a string of characters or reducing data to a set of important metrics.
* **Data Visualization**: The graphical representation of data, such as charts, graphs, or maps, to help make the information easier to understand.
* **Data Transformation**: The process of changing data from one format to another. For example, converting CSV data into JSON format for easier processing in a web application.

**5. File Formats and Storage**

* **File Format**: A specification that defines how data is encoded and stored in a file. Common formats include CSV (Comma-Separated Values), JSON (JavaScript Object Notation), XML (Extensible Markup Language), and binary formats.
* **CSV (Comma-Separated Values)**: A simple text-based file format for storing tabular data, where each line represents a row, and each value is separated by a comma.
* **JSON (JavaScript Object Notation)**: A lightweight, text-based format for storing and exchanging data, commonly used in web development.
* **XML (Extensible Markup Language)**: A markup language used for encoding documents in a format that is both human-readable and machine-readable.

**6. Algorithms and Problem-Solving**

* **Algorithm**: A step-by-step procedure or formula for solving a problem or completing a task, especially when processing data.
* **Efficiency**: How well an algorithm performs, often measured in terms of time (how quickly it runs) and space (how much memory it uses). Students should understand concepts like **big-O notation** to describe algorithm efficiency, especially in terms of time complexity (e.g., O(n), O(log n)).
* **Data Structures**: The organization and storage of data for efficient access and modification. Common structures include arrays, lists, stacks, queues, and trees.

**7. Security and Privacy**

* **Encryption**: The process of encoding data to protect it from unauthorized access. Data is converted into an unreadable format, and only someone with the correct key can decrypt it.
* **Decryption**: The process of converting encrypted data back into its original, readable format.
* **Hashing**: The process of converting data into a fixed-size value (a hash). Hashes are commonly used for verifying data integrity (e.g., checking if a file has been tampered with).

**8. Data Representation in Networks**

* **Packet**: A small chunk of data sent over a network, which may be part of a larger message.
* **IP Address**: A unique identifier assigned to each device on a network. It's used for routing packets of data to the correct destination.
* **Protocol**: A set of rules governing how data is transmitted over a network. Examples include **HTTP** (HyperText Transfer Protocol), **FTP** (File Transfer Protocol), and **TCP/IP** (Transmission Control Protocol/Internet Protocol).

**9. Big Data Concepts**

* **Big Data**: Large and complex data sets that traditional data processing software can't handle efficiently. Often involves analyzing data from various sources like sensors, social media, and logs.
* **Cloud Computing**: The delivery of computing services (storage, processing power, etc.) over the internet, often used for managing big data.

**10. Data Ethics**

* **Bias in Data**: When data collection or processing methods lead to unfair or skewed results. For example, biased data could lead to discriminatory algorithms.
* **Privacy**: The protection of individuals' personal information. Ethical data use includes ensuring that data is collected and shared responsibly, with attention to privacy laws (like GDPR).

</details>



---


### Data Project 1 - Data Communication and Compression:

The project will simulate a "Data Communication and Compression" system where you process, compress, and extract information from a text-based dataset. The project will be divided into sections based on the core topics and you will build a program in Python to demonstrate these concepts.

<details><summary> ASCII Table </summary>

**Binary/ ASCII/ and other things**

| Dec | Char | Dec | Char | Dec | Char | Dec | Char |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| 0 | NUL (null) |                       32 | SPACE  |   64 | @   |      96  | ` |
| 1 | SOH (start of heading) |           33 |!       |   65 | A   |     97   | a |
| 2 | STX (start of text)   |            34 | \"     |   66 | B   |       98 | b |
| 3 | ETX (end of text)   |              35 |#       |   67 |  C   |      99 | c |
| 4 | EOT (end of transmission)  |       36 | $      |   68 |  D   |    100  | d |
| 5 | ENQ (enquiry)                |     37 | %      |   69 |  E  |      101 |  e|
| 6  | ACK (acknowledge)           |     38 | &      |   70 | F      |  102 | f |
| 7 |  BEL (bell)                  |     39 | \'     |   71 | G     |   103 | g |
| 8 |  BS  (backspace)             |     40 | (      |   72 | H    |    104 | h |
| 9  | TAB (horizontal tab)         |    41 | )      |   73 | I   |     105 | i |
| 10 |  LF  (NL line feed, new line) |   42 | *   |      74 | J |      106  | j |
| 11 |  VT  (vertical tab)           |   43 | +   |      75 | K  |      107| k |
| 12 |  FF  (NP form feed, new page) |   44 | \,  |      76 | L   |    108 | l |
| 13 |  CR  (carriage return)        |   45 | -   |      77 | M     |   109 | m |
| 14 |  SO  (shift out)             |    46 | .   |      78 | N      |  110 | n |
| 15 |  SI  (shift in)             |     47 | \/  |      79 | O       | 111 | o |
| 16 |  DLE (data link escape)     |     48 | 0   |      80 | P      |  112 | p |
| 17 |  DC1 (device control 1)      |    49 | 1   |      81 | Q     |   113 | q |
| 18 |  DC2 (device control 2)     |     50 | 2   |      82 | R    |   114  | r |
| 19 |  DC3 (device control 3)     |     51 | 3   |      83 | S   |    115 | s |
| 20 |  DC4 (device control 4)     |     52 | 4   |      84 | T  |     116 | t |
| 21 |  NAK (negative acknowledge) |     53 | 5   |      85 | U   |     117 |  u |
| 22 |  SYN (synchronous idle)     |     54 | 6   |      86 | V    |    118 | v |
| 23 |  ETB (end of trans. block)  |     55 | 7   |      87 | W    |    119 | w |
| 24 |  CAN (cancel)               |     56 | 8   |      88 | X   |     120 | x |
| 25 |  EM  (end of medium)       |      57 | 9   |      89 | Y  |      121 | y |
| 26 |  SUB (substitute)          |      58 | :   |      90 | Z  |      122 | z |
| 27 |  ESC (escape)             |       59 | ;   |      91 | [   |     123 | { |
| 28 |  FS  (file separator)     |       60 | <   |      92 | \\   |     124 | \| |
| 29 |  GS  (group separator)    |       61 | =   |      93 | ]   |     125  | } |
| 30 |  RS  (record separator)   |       62 | >   |      94 | ^  |      126  | ~ |
| 31 |  US  (unit separator)      |      63 | ?   |      95 | _   |     127 | DEL |


</details>

---


**1. Binary Representation of Data**

**Objective:** Write a function that converts a given string of text into binary representation using the ASCII encoding system. Each character in the text will be converted into its ASCII value, and then the ASCII value will be converted into binary.

**Directions:**

1. Create a function with one parameter that accepts a message (the text you want to convert).
2. Create an **empty list** to store the binary versions of each character.
3. For each letter in the message:
   * Use a method to find its **ASCII code** (a number that represents that letter).
   * Format that number into **binary** with 8 digits.
   * Add this binary version to your list.
4. After all letters are processed:
   * Join the list of binary values together, with **spaces** in between.
   * **Return** the final string.
5. Call your function by giving it some text like `"Hello, World!"` and **show the result** on screen with a label.


**Expected Output:**
```
What phrase would you like to convert to binary? Hello World

Binary Representation: 01001000 01100101 01101100 01101100 01101111 00101100 00100000 01010111 01101111 01110010 01101100 01100100 00100001
```
<details><summary>Are you stuck?  Click Here!</summary>

**Key Concepts**

* `ord()` → built-in function to get ASCII code of a character
* `format()` → formats numbers into binary, decimal, hex, etc.
* `'08b'` → format specifier: 0-padded, 8 digits, binary
* `list.append()` → adds an item to a list


```python
ascii_value = ord(char)         # Step 1: Convert character to ASCII number
binary_string = format(ascii_value, '08b')  # Step 2: Convert number to binary
binary_data.append(binary_string)          # Step 3: Add to list
```
**Pseudocode**
```
'A' → 65 → 01000001
```


**Things to Know**
* Character → ASCII (with `ord()`)
* ASCII → Binary (with `format()`)
* Binary → Decimal (with `int(..., 2)`)
* Decimal → Character (with `chr()`)


</details>

---

**2. Binary to ASCII Decoder**

**Objective:** Write a function that takes a string of binary numbers (representing ASCII values) and converts it back into readable text.


1. Create a Function with One Parameter
     * The parameter should accept a **binary string** with groups of 8 digits separated by spaces.
     * This will be the message you want to decode.
2. Split the Message into Parts
     * Use a method to **split** the long binary message into a **list** of smaller strings.
     * Each piece should be exactly **8 digits long** — representing one character.
3. Create an Empty String to Store the Result
     * You’ll build your decoded message **one letter at a time**, so start with an empty string.
4. For Each Binary Group:
     * Convert it from **binary to decimal** (this gives you the ASCII number).
     * Convert that decimal number to a **character** (letter, number, or symbol).
     * Add the character to your decoded message string.
5. Return the Final Text
     * Once every group has been processed, return the final sentence made from all the characters.
     * Call your function and pass the binary message:
     * Display the result on screen using a **label** or print statement.  It should reveal a **readable sentence**!


**Pseudocode**

```
Define a function that receives a binary message
    Break the message into a list of binary pieces
    Create an empty string for the decoded text
    For each binary piece:
        Convert it to a base-10 number
        Convert that number to a letter or symbol
        Add the letter or symbol to the decoded text
    Give back the final decoded text
```


**Expected Output:**
```
What binary string do you want to convert to ASCII? 01001000 01100101 01101100 01101100 01101111 00101100 00100000 01010111 01101111 01110010 01101100 01100100 00100001
Decoded text:  Hello, World!
```

<details><summary>Are you stuck?  Click Here!</summary>

**Key Concepts**

* List comprehensions
* `int(..., 2)` to convert binary to decimal
* `chr()` to get character from ASCII code
* `''.join()` to combine a list of strings into one

```python
text = ''                            # Start with empty string
for bv in binary_values:
    decimal = int(bv, 2)             # Step 1: Binary → Decimal
    character = chr(decimal)         # Step 2: Decimal → Character
    text += character                # Step 3: Add character to message
```

**Things to Know**
* Character → ASCII (with `ord()`)
* ASCII → Binary (with `format()`)
* Binary → Decimal (with `int(..., 2)`)
* Decimal → Character (with `chr()`)


</details>



**3. Data Compression using Huffman Encoding**

**Goals:** 
    * Understand how Huffman coding compresses data
    * Build a Huffman tree physically with peers
    * Optionally write or trace a small piece of code

**Task:**
* Implement Huffman coding, a common algorithm for lossless data compression. In this part, you’ll write a program to:

  1. Calculate the frequency of each character in a string.
  2. Build a Huffman tree.
  3. Generate the Huffman codes for each character.
  4. Compress the text using the generated Huffman codes.

Words for Huffman Coding Activity:

| Word Bank       |                 |
| --------------- | --------------- |
|  **SASSAFRAS**  | **CONNECTICUT**    |
| **TENNESSEE**   | **COMMITTEE**	      |
| **SUCCESS**     | **ILLINOIS**	       |
| **BALLOON**     | **KENTUCKY**	       |
| **ASSESS**      | **ALABAMA**	        |
| **BANANA**      | **MINNESOTA**	      |
| **BOOKKEEPER**  | **PENNSYLVANIA**	   |
| **PEPPERCORN**  | **TATTOO**          |

**Part 1: Physical Huffman Coding Activity**

**Setup:**

* Use the following string: `"MISSISSIPPI"`
* Create a **frequency chart**:

| Letter | Frequency |
| ------ | --------- |
| M      | 1         |
| I      | 4         |
| S      | 4         |
| P      | 2         |

**Step 1: Make Cards**

Make index cards (or slips of paper) for each **letter with its frequency**.

Example:

```
[M:1]  [I:4]  [S:4]  [P:2]
```

**Step 2: Build the Tree (Greedy Step-by-Step)**

Each "node" will be a group of cards.

1. Find **two lowest frequency nodes** and combine them into a new node.
2. The new node’s frequency is the sum.
3. Label the left branch as `0` and the right branch as `1`.

Repeat until only one node (the full tree) is left.


**Example Tree for "MISSISSIPPI":**

```
        [11] 
       /    \
     [4]    [7]
    (I)    /   \
         [3]   (S:4)
        /   \
    (M:1) (P:2)
```

**Step 3: Build the Huffman Codes**

Trace paths from root to each letter:

* M: `1100`
* P: `1101`
* I: `0`
* S: `10`

Encode the full word `"MISSISSIPPI"` using these bits.

---

**Part 2: Programming Extension**

Part 1: Code Tracing

Give them Python code that builds a tree and ask:

* What’s the Huffman code for "S"?
* Which node will combine first?

Part 2: Partial Implementation

With the list of frequencies you physically created, write code that count character frequencies:

```python
def count_frequencies(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

print(count_frequencies("MISSISSIPPI"))
```

In Groups of 2 or 3 choose 2 more words and repeat the steps.


<details><Summary>Simplified Huffman Coding Example</Summary>


```python
import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    
    return codebook

# Example usage
text = "this is an example for huffman encoding"
huffman_tree = build_huffman_tree(text)
huffman_codes = generate_codes(huffman_tree)

print("Huffman Codes:", huffman_codes)
```


**Expected Output:**
The Huffman codes for the characters will be printed, which will be shorter for frequently occurring characters and longer for less frequent ones.


</details>




---

**4. Extracting Information from Data**

**Objective:** Extract meaningful data from a large dataset (e.g., a file).
* **Concepts Covered:** Data Extraction, File Processing.

**Task:**
* Write a program to read a text file, extract specific information (e.g., most frequent words, character count), and print the result.
* Example: Given a large text file, identify the most common word and character.

**Python Example:**

```python
from collections import Counter

def extract_information_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()  # Read and convert to lowercase
    
    words = text.split()
    word_count = Counter(words)  # Count frequency of each word
    most_common_word, count = word_count.most_common(1)[0]
    
    char_count = Counter(text)  # Count frequency of each character
    most_common_char = char_count.most_common(1)[0]
    
    print(f"Most common word: {most_common_word} ({count} occurrences)")
    print(f"Most common character: {most_common_char[0]} ({most_common_char[1]} occurrences)")

# Example usage (use an actual text file)
file_path = 'sample_text.txt'
extract_information_from_file(file_path)
```

**Expected Output:**

```
Most common word: the (34 occurrences)
Most common character: e (112 occurrences)
```


**5. Putting it All Together: A Simple File Communication System**

**Objective:** Create a small system that combines all of the previous concepts to compress and decompress a file.

**Task:**
* Implement a program that:

  1. Reads a text file and converts it to binary (ASCII).
  2. Compresses the data using Huffman encoding.
  3. Writes the compressed data to a new file.
  4. Decompresses the file and converts it back to text.

**Deliverables:**
1. **Code** for all the above tasks, including:
   * Functions for binary conversion, text encoding/decoding.
   * Huffman compression/decompression implementation.
   * A program that processes a file to extract information.

2. **Documentation:**
   * An explanation of how the code works.
   * A brief explanation of the theory behind binary, ASCII, Huffman encoding, and data extraction.
   * Sample input/output for each part of the project.


**Evaluation Criteria Rubric:**

1. **Functionality:** The program works as expected for each part of the task.
2. **Clarity:** Code is well-commented and easy to follow.
3. **Creativity:** The project demonstrates an understanding of data representation and compression, and possibly extends the basic implementation.

---


## Data Project 2: "Data Detectives – Investigating Real-World Trends"

**Objective**

Students will investigate a real-world issue using data. They'll collect or access a dataset, clean and organize the data, analyze it, and present their findings with visualizations and a written explanation.

---

**Big Idea 2 Concepts**

* **Data Acquisition**: Students obtain or access a dataset (e.g., from open data portals or surveys).
* **Data Representation**: Students convert raw data into usable formats.
* **Data Analysis**: Students filter, sort, and compute statistics to identify patterns or trends.
* **Visualization**: Students create graphs or infographics to communicate insights clearly.

**Project Steps**

1. **Pick a Topic (in pairs or solo)**

Students choose a topic of interest such as:

* Climate change
* COVID-19 statistics
* Music or movie popularity
* Social media usage
* Sports performance

2. **Find or Collect Data**

Sources can include:

* [Kaggle](https://www.kaggle.com/datasets)
* [Google Trends](https://trends.google.com/)
* [Data.gov](https://www.data.gov/)
* Survey data from peers (e.g., favorite apps, screen time, etc.)

3. **Prepare the Data**

* Convert data to CSV or use Google Sheets
* Remove duplicates, deal with missing data
* Reformat columns if needed (e.g., converting strings to numbers)

4. **Analyze the Data**

* Identify interesting questions like:

  * What trend is increasing the fastest?
  * Is there a correlation between two variables?
* Use basic stats: mean, median, mode, max, min, percentages

5. **Create Visualizations**

Use tools like:

* Google Sheets
* Python (pandas + matplotlib or seaborn)
* Tableau Public
* Canva or Infogram (for infographics)

6. **Present Your Findings**

Deliverables:

* A chart or graph (at least one)
* A technical written explanation interpreting the data
* A short presentation or recorded video

---

**Rubric (suggested categories)**

| Category                                  | Points     |
| ----------------------------------------- | ---------- |
| Relevant topic and data source            | 1          |
| Clean and organized data                  | 1          |
| Meaningful analysis (insights/statistics) | 2          |
| Visualization quality and clarity         | 2          |
| Written explanation                       | 2          |
| Creativity and effort                     | 2          |
| **Total**                                 | **10 pts** |


---

---


## Data Project 3 - Phishing


**Understanding and Preventing Phishing**


**Objective**:

Students will be able to:

* Define phishing and related cybersecurity vocabulary
* Identify real-life phishing threats
* Understand how their personal information is collected and used
* Apply basic to advanced protection measures
* Create a digital artifact to demonstrate their learning

---

**Vocabulary Words**:

| Term                                      | Definition                                                                          |
| ----------------------------------------- | ----------------------------------------------------------------------------------- |
| Personally Identifiable Information (PII) | Any data that could be used to identify an individual (e.g., name, address, SSN)    |
| Data Breach                               | When sensitive information is accessed or released without authorization            |
| Cookies                                   | Small files stored on your device to track activity and preferences                 |
| Phishing                                  | A cyber attack that tricks users into giving up personal or sensitive data          |
| Malware                                   | Malicious software designed to damage or gain unauthorized access to a system       |
| Keylogger                                 | A program that records everything you type, often used to steal passwords           |
| Rogue Access Point                        | A fake Wi-Fi network set up to trick people into connecting and stealing their data |

---

**Introduction**

**Discussion**:
"Have you ever received a suspicious email or message asking you to click a link or enter your password?"

* Learn more about [phishing emails](https://www.youtube.com/watch?v=Y7zNlEMDmI4) and websites.
* What clues make them suspicious?

**Instructions**:

* Explain phishing using a real-world analogy (e.g., someone pretending to be your friend to get your house key)
* Review all vocabulary words with examples

---

**Activity 1: PII Collection Table**

**Instructions**: What is PII?  Click on the link to learn more about [Personally Identifiable Information](https://www.youtube.com/watch?v=N1qdvQVke0s). Research and create a table like the one below.  Identify three websites or apps that you have used recently (e.g., Instagram, Google).

| Website or Application | PII Collected                      | How the information is used (Will they share it? With whom? Will they keep it forever?) |
| ---------------------- | ---------------------------------- | --------------------------------------------------------------------------------------- |
|      Amazon         | Email, phone number, location      | For ad targeting, may be shared with advertisers               | 
|         Website/ App Name 2        |         |                                     |
|       Website/ App Name 3         |          |                                     |

---


**What is Malware?**

**Malware** is short for **malicious software**. It refers to any software or code that is intentionally designed to harm, exploit, or otherwise compromise a computer system, network, or device without the user's informed consent.


**Purpose:** Steal data, damage systems, disrupt operations, spy on users, or gain unauthorized access.

**Forms of Malware:**

  * **Viruses** – Attach to clean files and spread.
  * **Worms** – Self-replicate and spread across networks.
  * **Trojans** – Disguise as legitimate software.
  * **Ransomware** – Locks data and demands payment.
  * **Spyware** – Secretly monitors user activity.
  * **Adware** – Displays unwanted ads, often with tracking.
  * **Rootkits** – Hide malicious activities from detection.

**How It Spreads:**
How does it affect your computer.  Click on the link to learn more about [Malware](https://www.youtube.com/watch?v=N1qdvQVke0s). 


**Protection Measures**

**Instructions**: In your own words, list and explain **at least 5 protection measures** from the list below:

1. **Be suspicious of links and attachments** 
2. **Use strong, unique passwords** 
3. **Enable two-factor authentication (2FA)** 
4. **Install and update antivirus software** 
5. **Avoid public Wi-Fi for sensitive tasks** 
6. **Check URLs carefully** 
7. **Review app permissions** 
8. **Regularly clear cookies and browser history** 
9. **Monitor your digital footprint** 

---

**Reflection Questions**

Students should respond to the following questions in writing or in a small group discussion:

1. **How does storing your information online facilitate convenience?**
   
2. **How is convenience online related to data loss?**
   
3. **What are some ways you can protect yourself online?**
   

---

**Digital Artifact**

**Objective**: Demonstrate what you’ve learned by creating a **digital poster, infographic, video, or slideshow** that includes:

* Definitions of phishing and at least 3 other vocabulary words
* Examples of phishing (screenshots, skits, or drawings)
* 5+ protection tips in student-friendly language
* One takeaway message or slogan (e.g., “Think Before You Click!”)

**Tools Suggestions**:

* **Canva** (infographic/poster)
* **Google Slides** (presentation)
* **Adobe Spark** or **Powtoon** (video)
* **Flip** (recorded video skit)

---

**Assessment Criteria**:

| Component                | Points |
| ------------------------ | ------ |
| Completed PII Table      | 2      |
| Protection Measures List | 2      |
| Reflection Questions     | 3      |
| Digital Artifact         | 3      |
| **Total**                | **10** |


---

## Data Project 4:  Encryption & Privacy

---

**Key concepts to learn**

* What encryption is and why it's essential for secure communication.
* How **Caesar cipher** works as a basic form of **substitution cipher**.
* The concept of **brute force attacks**.
* Introduction to **frequency analysis** and basic **crypto-analysis**.
* Understanding of **public-key cryptography** (RSA) and **private/public key** pairs.
* Vocabulary relevant to digital security and cryptography.

---

**Vocabulary**

| Term                      | Definition                                                                      |
| ------------------------- | ------------------------------------------------------------------------------- |
| **Brute Force**         | Trying all possible keys to decrypt a message.                                  |
| **Caesar Cipher**       | A substitution cipher that shifts letters by a fixed amount.                    |
| **Cipher**              | A method for performing encryption or decryption.                               |
| **Ciphertext**          | The encrypted (scrambled) message                                               |
| **Crypto-analysis**       | The art of decoding encrypted messages without the key.                         |
| **Decryption**          | Converting encrypted data back into readable form.                              |
| **Encryption**          | Converting information into a code to prevent unauthorized access.              |
| **Frequency Analysis**  | A method of breaking substitution ciphers by studying how often letters appear. |
| **Keyword**             | A word used to vary the shifts in the cipher                                    |
| **Modular Arithmetic**      | Calculations are done using modulo 26 (number of letters in the alphabet)               |
| **Modulus**             | A number used to link the public and private keys in RSA.                       |
| **Plaintext**           | The original readable message                                                   |
| **Polyalphabetic**      | Involving more than one substitution alphabet                                   |
| **Private Key**         | Used to decrypt data in RSA. Kept secret.                                       |
| **Public Key**          | Used to encrypt data in RSA encryption. Shared with everyone.                   |
| **Repeating Key**           | The keyword repeats to match the length of the message                                  |
| **Substitution Cipher** | A cipher that replaces each letter with another.                                |

---


### Why is Frequency Important in Cryptography?

**Frequency analysis** is one of the oldest and most powerful tools in **breaking substitution ciphers**. Here's how it helps:

1. **Languages Have Predictable Patterns**

* In English, letters like **E**, **T**, **A**, **O**, and **N** appear most often.
* If an encrypted message shows one letter (like "X") appearing frequently, it might represent "E" or "T".

2. **Cracks Simple Ciphers**

* Substitution ciphers (like Caesar or cryptograms) can often be broken by comparing **letter frequencies** in the ciphertext to known English frequency patterns.

3. **Foundation for Modern Crypto analysis**

*While modern encryption is more complex, the **principle of pattern recognition*** and analysis is still used in detecting weak encryption algorithms.

---

**Common English Letter Frequencies**

| Letter | Frequency (%)     | Letter | Frequency (%) |
| -------- | --------------- | ----- | ------------- |
| A        | 8.2%            | N        | 6.7%            |
| B        | 1.5%            | O        | 7.5%            |
| C        | 2.8%            | P        | 1.9%            |
| D        | 4.3%            | Q        | 0.1%            |
| E        | 12.7%           | R        | 6.0%            |
| F        | 2.2%            | S        | 6.3%            |
| G        | 2.0%            | T        | 9.1%            |
| H        | 6.1%            | U        | 2.8%            |
| I        | 7.0%            | V        | 1.0%            |
| J        | 0.2%            | W        | 2.4%            |
| K        | 0.8%            | X        | 0.2%            |
| L        | 4.0%            | Y        | 2.0%            |
| M        | 2.4%            | Z        | 0.1%            |



---


### Python Program: Letter Frequency Analyzer

```python
def letter_frequency(text):
    text = text.lower()  # normalize to lowercase
    frequency = {}

    for char in text:
        if char.isalpha():  # count only letters
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    total_letters = sum(frequency.values())

    print(" Letter Frequencies:\n")
    for letter in sorted(frequency):
        percent = (frequency[letter] / total_letters) * 100
        print(f"{letter.upper()} : {frequency[letter]} times ({percent:.2f}%)")

# Example usage
input_text = input("Enter a message to analyze: ")
letter_frequency(input_text)
```

---

**How to Use**

* Copy and paste the code into any Python environment.
* When prompted, paste your encrypted or regular text.
* The program will print a breakdown of how often each letter appears.


---

**Python Code: Caesar Cipher Program**

*Copy and place this in a working Python environment.*

```python
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def brute_force_caesar(text):
    for key in range(1, 26):
        print(f"Key {key}: {caesar_decrypt(text, key)}")

# Example usage:
print("1. Encrypt")
print("2. Decrypt")
print("3. Brute Force")
choice = input("Enter your choice: ")

if choice == "1":
    message = input("Enter message to encrypt: ")
    key = int(input("Enter shift key (1-25): "))
    print("Encrypted:", caesar_encrypt(message, key))
elif choice == "2":
    message = input("Enter message to decrypt: ")
    key = int(input("Enter shift key (1-25): "))
    print("Decrypted:", caesar_decrypt(message, key))
elif choice == "3":
    message = input("Enter message to brute-force: ")
    brute_force_caesar(message)
```

* Complete Caesar decryption for "Vkliw wkuhh" using Caesar shift of 3.
* Discuss why certain messages need encryption online.

---

**Practice**

* Try encrypting and decrypting a sentence using the Python code.
* Paste encrypted sentence into class doc with your key.


**Brute Force**

*Use the **brute force** option in the script above to decrypt:*

  ```python
  Guvf vf n rapelcgrq zrffntr. Lbh jvyy arire or noyr gb ernq vg!
  ```

*Discuss if the original message is easy to spot among the outputs.*


---


### Vigenère Cipher


**What Is the Vigenère Cipher?**

The **Vigenère Cipher** is a **polyalphabetic substitution cipher** that uses a **keyword** to encrypt a message.

* Unlike Caesar Cipher (which uses the same shift for every letter), Vigenère **changes the shift for each letter**, based on a repeating keyword.
* This makes it **much harder to crack** using simple frequency analysis.

---

***How It Works – Step-by-Step***

**Core Idea:**

* Each letter of the **plaintext** is shifted by an amount **based on the corresponding letter of the keyword**.

---
**Alphabet Reference**

You’re working with the alphabet:

**A B C D E F G H I J K L M N O P Q R S T U V W X Y Z**

Each letter is assigned a number:

| Letter | A | B | C | D | E | F | G | H | I | J | K  | L  | M  |
| ------ | - | - | - | - | - | - | - | - | - | - | -- | -- | -- |
| Number | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

| Letter | N  | O  | P  | Q  | R  | S  | T  | U  | V  | W  | X  | Y  | Z  |
| ------ | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| Number | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

---

**Keyword:**

A **keyword** is used to determine how much each letter in your message gets shifted.

Example keyword: **KEY**

We convert it to numbers using the alphabet reference:

* K = 10
* E = 4
* Y = 24

---

**Repeating the Keyword**

If your message is longer than the keyword, repeat the keyword to match the message length.

Example:

**Message:** A-T-T-A-C-K--A-T--D-A-W-N

**Keyword:** K-E-Y-K-E-Y--K-E--Y-K-E-Y


(Spaces are just for clarity; they’re not encrypted.)

---

**Encryption Formula**

To encrypt a message:

> **EncryptedLetter = (PlainLetter + KeyLetter) % 26**

Each letter of the message is converted to a number. Then, add the number from the keyword (also as a number). Use `% 26` (modulo 26) to make sure the result stays between 0 and 25.

---

Example: Encrypt "A" with key letter "K"

* A = 0
* K = 10
* Encrypted = (0 + 10) % 26 = 10
* 10 = K
  🔏 So A becomes **K**

---

**Decryption Formula**

To decrypt a message:

> **PlainLetter = (EncryptedLetter - KeyLetter + 26) % 26**

You subtract the keyword number from the encrypted letter number. Add 26 before the `% 26` to avoid negative numbers.

---

Example: Decrypt "K" with key letter "K"

* K = 10
* K = 10
* Decrypted = (10 - 10 + 26) % 26 = 0
* 0 = A
  So K becomes **A**

---

**Example: Encrypting “ATTACKATDAWN” with Key “KEY”**

| Position | Message | Key | Plain (Num) | Key (Num) | Encrypted (Num) | Encrypted Letter |
| -------- | ------- | --- | ----------- | --------- | --------------- | ---------------- |
| 1        | A       | K   | 0           | 10        | 10              | K                |
| 2        | T       | E   | 19          | 4         | 23              | X                |
| 3        | T       | Y   | 19          | 24        | 17              | R                |
| 4        | A       | K   | 0           | 10        | 10              | K                |
| 5        | C       | E   | 2           | 4         | 6               | G                |
| 6        | K       | Y   | 10          | 24        | 8               | I                |
| 7        | A       | K   | 0           | 10        | 10              | K                |
| 8        | T       | E   | 19          | 4         | 23              | X                |
| 9        | D       | Y   | 3           | 24        | 1               | B                |
| 10       | A       | K   | 0           | 10        | 10              | K                |
| 11       | W       | E   | 22          | 4         | 0               | A                |
| 12       | N       | Y   | 13          | 24        | 11              | L                |

**Encrypted Message**: `KXRKGIKXBKAL`


---



### RSA Educational Encryption and Decryption Program 

⚠️ This version is simplified for educational purposes only and not secure for real cryptographic use. It shows the core concepts of RSA: key generation, encryption, and decryption.


```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(e, phi):
    # Extended Euclidean Algorithm
    d_old, r_old = 0, phi
    d_new, r_new = 1, e
    while r_new != 0:
        quotient = r_old // r_new
        d_old, d_new = d_new, d_old - quotient * d_new
        r_old, r_new = r_new, r_old - quotient * r_new
    return d_old % phi

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_keys():
    print("\n Choose two prime numbers (p and q) such that their product n = p * q is greater than 255.")
    p = int(input("Enter prime p (e.g. 61): "))
    q = int(input("Enter prime q (e.g. 53): "))

    if not (is_prime(p) and is_prime(q)):
        print("Error: Both numbers must be prime.")
        return None, None, None

    n = p * q
    if n <= 255:
        print("Error: n must be greater than 255 to support all ASCII characters.")
        return None, None, None

    phi = (p - 1) * (q - 1)

    e = 3
    while gcd(e, phi) != 1:
        e += 2

    d = modinv(e, phi)

    print(f"\n Public Key: ({e}, {n})")
    print(f" Private Key: {d}")
    return e, d, n


def encrypt(message, e, n):
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

def decrypt(cipher, d, n):
    decrypted = ''.join([chr(pow(char, d, n)) for char in cipher])
    return decrypted

def main():
    print("RSA Cryptosystem")

    while True:
        print("\nMENU:")
        print("1. Generate Keys")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            e, d, n = generate_keys()

        elif choice == "2":
            msg = input("Enter your message: ")
            e = int(input("Enter recipient's public key e: "))
            n = int(input("Enter recipient's public key n: "))
            encrypted_msg = encrypt(msg, e, n)
            print("Encrypted message:", encrypted_msg)

        elif choice == "3":
            try:
                cipher_input = input("Paste the encrypted message list (e.g. [123, 456]): ")
                cipher = eval(cipher_input)
                d = int(input("Enter your private key d: "))
                n = int(input("Enter your modulus n: "))
                decrypted_msg = decrypt(cipher, d, n)
                print("Decrypted message:", decrypted_msg)
            except:
                print("Invalid input. Try again.")

        elif choice == "4":
            print("Exiting RSA program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")
```
    
---

### How to the RSA Program

**Generate Keys**
1.	Run the program and choose option 1 to generate RSA keys.
2.	Choose small primes (e.g. 17 and 23).
3.	Share public key (e, n).
4.	Keep private key (d) secret.

**Encrypt**
1.	Select option 2.
2.	Input your message.
3.	Input recipient’s public key (e, n).
4.	Share the encrypted list with the recipient.

**Decrypt**
1.	Select option 3.
2.	Paste the encrypted list.
3.	Enter your private key (d) and modulus (n).
4.	Get the decrypted message.


---



```python
def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# Example use
msg = input("Enter your message: ")
key = input("Enter the keyword: ")
mode = input("Encrypt (e) or Decrypt (d)? ").lower()

if mode == 'e':
    print("Encrypted:", vigenere_encrypt(msg, key))
else:
    print("Decrypted:", vigenere_decrypt(msg, key))
```


