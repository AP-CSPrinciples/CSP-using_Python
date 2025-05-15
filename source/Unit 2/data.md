# Data

---
### Unit 2 Vocabulary

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

---

---


### Data Project 1 - Data Communication and Compression:

The project will simulate a "Data Communication and Compression" system where you process, compress, and extract information from a text-based dataset. The project will be divided into sections based on the core topics and you will build a program in Python to demonstrate these concepts.


**1. Binary Representation of Data**

**Objective:** Convert text into binary format (ASCII encoding).
* **Concepts Covered:** Binary, ASCII, Data Representation.

**Task:**
* Write a function that converts a given string of text into binary representation using the ASCII encoding system.
* Each character in the text will be converted into its ASCII value, and then the ASCII value will be converted into binary.

**Instructions:**

1. Create a function that accepts a message (the text you want to convert).

2. Create an **empty list** to store the binary versions of each character.

3. For each letter in the message:

   * Use a method to find its **ASCII code** (a number that represents that letter).
   * Format that number into **binary** with 8 digits.
   * Add this binary version to your list.

4. After all letters are processed:

   * Join the list of binary values together, with **spaces** in between.
   * **Return** the final string from your tool.

5. Call your function by giving it some text like `"Hello, World!"` and **show the result** on screen with a label.


**Expected Output:**
```
What phrase would you like to convert? Hello World

Binary Representation: 01001000 01100101 01101100 01101100 01101111 00101100 00100000 01010111 01101111 01110010 01101100 01100100 00100001
```

**2. ASCII Encoding and Decoding**

**Objective:** Convert binary back to ASCII text.
* **Concepts Covered:** ASCII, Data Decoding, Data Extraction.

**Task:**
* Write a function that takes a string of binary numbers (representing ASCII values) and converts it back into readable text.

**Python Example:**

```python
def binary_to_text(binary):
    binary_values = binary.split(' ')  # Split the binary input into separate characters
    text = ''.join([chr(int(bv, 2)) for bv in binary_values])  # Convert binary to decimal, then to char
    return text

binary_data = '01001000 01100101 01101100 01101100 01101111 00101100 00100000 01010111 01101111 01110010 01101100 01100100 00100001'
decoded_text = binary_to_text(binary_data)
print(f"Decoded Text: {decoded_text}")
```

**Expected Output:**
```
Decoded Text: Hello, World!
```



**3. Data Compression using Huffman Encoding**

**Objective:** Implement basic data compression using Huffman encoding.
* **Concepts Covered:** Data Compression, Encoding, Efficiency.

**Task:**
* Implement Huffman coding, a common algorithm for lossless data compression. In this part, you’ll write a program to:

  1. Calculate the frequency of each character in a string.
  2. Build a Huffman tree.
  3. Generate the Huffman codes for each character.
  4. Compress the text using the generated Huffman codes.

**Python Example (simplified version):**

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
* **Concepts Covered:** Binary Data, ASCII, Data Compression, Extraction.

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


## 🧠 **Data Project 1: "Data Detectives – Investigating Real-World Trends"**

🎯 **Objective**

Students will investigate a real-world issue using data. They'll collect or access a dataset, clean and organize the data, analyze it, and present their findings with visualizations and a written explanation.

---

🧩 **Big Idea 2 Concepts**

* **Data Acquisition**: Students obtain or access a dataset (e.g., from open data portals or surveys).
* **Data Representation**: Students convert raw data into usable formats.
* **Data Analysis**: Students filter, sort, and compute statistics to identify patterns or trends.
* **Visualization**: Students create graphs or infographics to communicate insights clearly.

---

📋 **Project Steps**

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

📝 **Rubric (suggested categories)**

| Category                                  | Points     |
| ----------------------------------------- | ---------- |
| Relevant topic and data source            | 10         |
| Clean and organized data                  | 10         |
| Meaningful analysis (insights/statistics) | 15         |
| Visualization quality and clarity         | 15         |
| Written explanation                       | 10         |
| Creativity and effort                     | 10         |
| **Total**                                 | **70 pts** |

---

Would you like a sample version of this project for students or a Google Docs template?

## Binary/ ASCII/ and other fun things

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

