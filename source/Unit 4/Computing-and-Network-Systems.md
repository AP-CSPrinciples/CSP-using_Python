# Computing and Network Systems

Great request! I’ll design you a **comprehensive AP CSP unit** on *Understanding Computer & Network Systems (Big Idea 4)* with lessons, projects, and activities that fit the AP CSP framework, keep students engaged, and prepare them for the AP exam.

Here’s a structured unit you can use right away:

---

**Unit: Understanding Computer & Network Systems (Big Idea 4)**

**Unit Goals**

* Explain how the Internet works (IP addresses, DNS, packets, protocols).
* Demonstrate the importance of fault tolerance, redundancy, and scalability.
* Explore parallel and distributed computing with real-world applications.
* Apply concepts through simulations, unplugged activities, coding projects, and reflections.

---

**Lesson Sequence**

**Lesson 1: What is the Internet? (4.1)**

**Objectives**:

* Understand IP addresses, DNS, packets, and protocols.
* Visualize how a request moves across the internet.

**Activities**:

1. **Unplugged Simulation** – "Passing Packets" game: students pass envelopes with parts of a message, simulating dropped/reordered packets.
2. **Mini Lab** – Use `ping` and `tracert`/`traceroute` on school computers to see how packets travel.
3. **Discussion** – Why do we need DNS? What happens if DNS fails?

**Project/Check**:

* Draw a **diagram of how a browser request works** (user → DNS → server → back to user).
* Quick-write: "What role do IP addresses and DNS play in making the Internet usable?"

---

**Lesson 2: Protocols and Communication (4.1)**

**Objectives**:

* Explore TCP/IP, HTTP, HTTPS.
* See why protocols are critical for interoperability.

**Activities**:

1. **Classroom Protocol Game** – students pass secret notes with different "rules" for communication; only when they follow a shared set of rules can the message be read.
2. **Wireshark or Online Demo** – (if allowed) capture network packets and see TCP/HTTP in action.

**Project/Check**:

* Create an infographic or short video explaining **one protocol** (HTTP, HTTPS, TCP, UDP) in plain English.

---

**Lesson 3: Fault Tolerance & Redundancy (4.2)**

**Objectives**:

* Understand how redundancy improves reliability.
* Explore routing and rerouting of data.

**Activities**:

1. **Unplugged Simulation** – students act as routers; if one path is blocked, data finds another route.
2. **Case Study** – Look at a real-world event (e.g., Google outage, submarine cable cut, DNS outage). Discuss: what went wrong, how did redundancy help/fail?

**Project/Check**:

* Create a one-page **visual explanation of fault tolerance**: why redundancy matters, with examples.

---

**Lesson 4: Scalability (4.2)**

**Objectives**:

* Learn how networks grow to handle more users.
* Explore bottlenecks (bandwidth, servers, congestion).

**Activities**:

1. **Bandwidth Demo** – have students send messages with limited “bandwidth” (e.g., only 2 characters per round) vs. full sentences to simulate congestion.
2. **Discussion** – What happens when millions of people stream Netflix or join Zoom?

**Project/Check**:

* Students research and present: *How do big companies like YouTube, Netflix, or Amazon scale their systems?*

---

**Lesson 5: Parallel & Distributed Computing (4.3)**

**Objectives**:

* Compare sequential vs. parallel vs. distributed computing.
* Recognize real-world uses (scientific research, AI, climate modeling, SETI@Home).

Parallel and distributed computing are two models used to perform complex computations efficiently. While they share similarities, they differ in structure and functionality.

**Key Differences**

***Parallel Computing***
- Structure: Involves multiple processors that work on tasks simultaneously. These processors can share memory.
- Functionality: Tasks are divided into smaller sub-tasks, which are processed at the same time.
- Examples: Supercomputers, smartphones, and artificial intelligence applications.

***Distributed Computing***
- Structure: Comprises multiple autonomous computers that communicate over a network. Each computer has its own memory.
- Functionality: A single task is divided among different computers, which work together to achieve a common goal.
- Examples: Cloud computing services, online applications like Google Docs, and cryptocurrency mining.

Advantages and Challenges
Advantages
| Feature |	Parallel Computing | Distributed Computing |
| ------- | :------------------: | :---------------------: |
| Speed	| Faster execution due to simultaneous processing	| Fault tolerance; failure of one node does not halt the entire system |
| Resource Utilization | Efficient use of processing units | Can leverage multiple locations and resources |

|      | Challenges |
| ---- | :-------: |
| Parallel Computing | Requires synchronization between processors, which can complicate programming and increase overhead. |
| Distributed Computing | Faces issues like network latency and the need for robust communication protocols. |

Understanding these differences helps in choosing the right model for specific computational tasks.

**Activities**
- Binary Messages
- Let's Make a cake
  

**Reflection:**

*Why are parallel and distributed computing essential for modern problems like AI, space exploration, or healthcare?*


---


**Lesson 6: Review & Synthesis**

**Objectives**:

* Bring together internet structure, protocols, fault tolerance, scalability, parallel/distributed computing.
* Prepare for AP-style questions.

**Activities**:

1. **Concept Map** – students create a visual showing connections among IP, DNS, packets, protocols, fault tolerance, and distributed computing.
2. **Practice AP CSP Exam Questions** – multiple choice and short-answer style.

---

**Projects & Performance Tasks**

1. **"Life of a Packet" Storyboard/Video**

   * Students create a comic, animation, or video that shows how data travels across the internet, including DNS, IP, packets, and protocols.

2. **Network Outage Case Study**

   * Research a real-world outage (DNS failure, DDoS attack, cable break).
   * Present what happened, how redundancy helped (or didn’t), and lessons learned.

3. **Parallel/Distributed Simulation Project**

   * Students simulate solving a problem (like word counting, searching, or sorting) using sequential, parallel, and distributed strategies.
   * Write a reflection on efficiency and scalability.

4. **Scalability Research Project**

   * Students research how a major service (YouTube, Netflix, Zoom, Fortnite servers) handles massive numbers of users.
   * Create a presentation or infographic.

---

**Assessment Options**

* **Formative**: exit tickets, diagrams, reflections, class simulations.
* **Summative**:

  * Project presentation (Life of a Packet, Network Outage Case Study, or Scalability Research).
  * Unit test with multiple choice + short answer (aligned to AP CSP style).

---



