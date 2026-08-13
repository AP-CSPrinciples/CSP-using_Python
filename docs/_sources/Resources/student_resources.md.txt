# Student Resources


## The Six Benefits of Documentation

[Link](https://cindyscheung.medium.com/pleeeeaase-explain-your-code-e1fdfdf19566 )

1. **Documentation quickly reminds the creator of what he did in the past**.

Have you ever reviewed a script that you coded months ago and forgot exactly what you did? Did you spend hours trying to figure it out again? I have. If the summaries and comments in the code were diligently and consistently kept, the review time should be significantly reduced.

2. **Documentation allows anyone who takes over the code to learn faster**.

In the same vein, anyone else who needs to take over the code would spend less time learning the code because documentation eases the learning curve. And the less time someone spends reviewing old code, the more time he can spend being productive in creating the new one.

3. **Documentation tracks what has been done to the code (i.e. versioning)**.

It doesn’t make any sense to me why I would find updated code with outdated comments within the same script.
Each programmer is responsible for updating both the code and comments at the same time. Each time a section of code is finished and working, the programmer ought to edit the comments and save the script as a new version. So I am NOT saying that the programmer must edit the comments while he is still trying to figure out the code. I am saying that once he is satisfied with his completed code, he should update his comments too. Not later. Immediately. By updating the code and comments in incremental versions, everyone can keep track of what had already been done before.

4. **Documentation helps those not as proficient at coding**.

Not everyone is a programmer. Many of us, like yours truly, may have coded before but would not consider ourselves expert programmers. And at some point, one of us will be required to at least study the scripts. Without comments or any project specific documentation, the best resource would be the people who developed the script.
But what if they no longer exist in the office? We end up resorting to general programming resources, then figure out how to implement the information to the actual project. This can be time-consuming and risks revealing company proprietary information when external people ask for specifics in order to provide a solution.

5. **Documentation helps technical people translate the code to business value**.

What about the people whose primary interest is the bottom line? Writing summaries for the code allows the programmer to see his work at a higher level. Rather than staying in the comfort of the nitty-gritty, programmers will have the chance to contemplate how his work fits into the bigger picture. As an engineer and a writer, I want to innovate and speak my mind. But all too often, technical people develop state-of-the-art products that have no value to the company or their customers. Groundbreaking products that do not fulfill a need will be rendered useless. Summarizing the code into laymen’s terms keeps the programmer from going off course. Explanations to business executives would be easier because the connection between the code and the customer need would be clearer.

6. **Documentation keeps a record of lessons learned**.
   
Proper project management includes discussions and documentation of lessons learned. This should not only apply to the team as a whole, but it also applies to individual contributors. In fact, a friend of mine keeps a lessons log for her personal life. Lessons learned does not only document things that should not be repeated. It also documents the things that CAN — and maybe should — be repeated. Taking the time to review the document at the beginning of the project could prevent repeating mistakes. I mean, isn’t it less excruciating to review lessons learned than staring at the code to find a bug that could have been prevented? But don’t wait until the end of the project to record the lessons. It is crucial to take responsibility and record them once they are recognized. Otherwise, they could be long forgotten. So if not immediately, at least by the end of the close of business.

---

## How to Read an Error Message

When your code breaks, the error message isn't your enemy. It's the most specific hint you're going to get. Learning to actually read it (instead of scrolling past it in a panic) is one of the fastest ways to level up as a programmer.

1. **Start at the bottom, not the top.**

Python (and most languages) print the *type* of error and the final explanation at the very bottom of the traceback. That's the headline. Everything above it is backstory, so read the bottom first, then work your way up if you need more context.

2. **The error type tells you the category of problem.**

A `SyntaxError` means Python couldn't even understand your code's structure. A `NameError` means you used a variable that doesn't exist (yet, or ever; check your spelling). A `TypeError` means you tried to do something with a value that doesn't support it, like adding a number to a string. Knowing the category narrows your search dramatically.

3. **The line number is a starting point, not a guarantee.**

Sometimes the actual mistake is a line or two *above* the line listed, especially with missing colons, parentheses, or quotation marks. If the flagged line looks fine, check just before it.

4. **Read the message like a sentence, not a code.**

`"list index out of range"` is Python telling you, in plain English, that you asked for an item in a list that doesn't exist at that position. Most error messages are more readable than they look at first glance, so slow down and read them as English.

5. **One error at a time.**

Fixing one error can reveal another underneath it. That's normal, not a sign you made things worse. Fix the first one, rerun, and repeat.

6. **Copying the exact error into a search engine is a real debugging skill, not cheating.**

Professional developers do this constantly. The skill isn't memorizing every error; it's knowing how to search effectively and evaluate whether the answer you find actually applies to your situation.

---

## The Debugging Mindset

Debugging isn't a sign that you did something wrong. It's a normal, expected part of writing code. Every programmer, at every skill level, spends real time debugging. The goal isn't to avoid it; it's to get faster and calmer at it.

1. **Reproduce the problem first.**

Before you try to fix anything, make sure you can consistently make the bug happen. If you can't reproduce it, you can't confirm you've actually fixed it.

2. **Isolate before you fix.**

Narrow down *where* the problem lives before you start changing code. Comment out sections, test small pieces individually, or add print statements to see what your program actually thinks is happening at each step.

3. **Compare what you expected to what actually happened.**

The gap between "what I expected" and "what actually printed" is where the bug is hiding. Say both out loud (or write them down); the gap becomes much easier to see.

4. **Change one thing at a time.**

If you change five things at once and the bug disappears, you won't know which change fixed it, or whether you introduced a new problem. Make one change, test, then decide your next move.

5. **Take a break before you get frustrated, not after.**

Staring harder rarely works. Stepping away for even two minutes, or explaining the problem out loud to someone else (or to no one; this is called "rubber duck debugging"), often surfaces the answer.

6. **Every bug you fix is a bug you'll recognize faster next time.**

Debugging skill is cumulative. The second time you see a certain error, you'll already have a hunch. That's the payoff for pushing through the first time.

---

## Growth Mindset in Computer Science

How you talk to yourself about mistakes in this course will shape how much you actually learn in it.

1. **"I can't code" and "I can't code *yet*" are different sentences.**

The second one is true and useful. The first one just isn't accurate. Nobody can code the first time they try, and that's not evidence of a fixed limit.

2. **Struggling with a problem is where the learning happens, not a sign you're behind.**

If a problem felt easy, you probably already knew how to solve it. The productive struggle, the part that feels uncomfortable, is usually exactly where new understanding gets built.

3. **Comparing your first draft to someone else's finished product isn't a fair comparison.**

You're seeing their final version, not their false starts, their deleted code, or their debugging process. Compare your work to your own last attempt instead.

4. **Confusion is data, not failure.**

If something doesn't make sense, that's useful information about what to ask about next, not proof you're not cut out for this.

5. **Effective effort looks like trying an approach, testing it, and adjusting, not just spending time.**

Sitting with a problem for an hour without changing your approach isn't the same as productive effort. Growth mindset isn't "try harder." It's "try differently."

6. **Ability in this course is built through practice, not something you either have or don't.**

Every skill in this class (reading errors, breaking down problems, writing clean code) is trainable. Nobody starts with it.

---

## What Is Abstraction, Really?

Abstraction is one of the core ideas in computer science, and it's simpler than it sounds: it means hiding unnecessary detail so you can focus on what matters right now.

1. **You use abstraction every day without thinking about it.**

When you drive a car, you don't need to understand the combustion engine to turn the key and go. The dashboard *abstracts away* the engine's complexity into a few simple controls.

2. **In code, a function is an abstraction.**

When you call a function like `print()`, you don't need to know how Python actually draws characters on your screen. You just need to know what to give it and what it gives back.

3. **Abstraction happens in layers.**

A website you click on sits on top of HTML, which sits on top of network protocols, which sit on top of electrical signals. Each layer hides the complexity of the layer below it. You interact with the top layer without needing to think about the bottom ones.

4. **Good abstraction lets you manage problems that would otherwise be too big to hold in your head.**

No single person understands every layer of a modern computer, from the transistors to the app on your phone. Abstraction is what makes that possible: it lets teams and individuals build on top of work they don't need to fully re-understand.

5. **The trade-off is that abstraction can hide details you sometimes *do* need.**

When something breaks, understanding what's happening "underneath" the abstraction, even just one layer down, is often the key to debugging it.

---

## How the Internet Actually Works

The internet feels like magic until you see the basic idea underneath it: your data doesn't travel in one piece, and it doesn't need a single unbroken path to get where it's going.

1. **Data travels in small pieces called packets.**

Before your message, image, or video leaves your device, it gets broken into small chunks. Each chunk is labeled with where it's going and where it came from.

2. **Packets don't all take the same route.**

Different packets from the same message can travel through completely different paths across the network and still end up arriving at the right destination, where they're reassembled in order.

3. **This design is intentionally redundant.**

If one path is congested or a connection fails, packets can be rerouted through a different path. No single point of failure can take down the whole system; that redundancy is a deliberate design choice, not an accident.

4. **Protocols are the agreed-upon rules that make this work.**

A protocol is just a shared set of rules two systems agree to follow so they can understand each other, similar to how a shared language lets two people communicate. TCP/IP is the core protocol suite the internet runs on.

5. **"The internet" and "the web" are not the same thing.**

The internet is the physical and logical network of connected devices. The web (what you access through a browser) is just one of many services that runs *on top of* the internet; email and streaming are examples of others.

6. **Scale is the whole story.**

None of these ideas are exotic on their own. What makes the internet remarkable is that this system reliably works at the scale of billions of devices, all the time.

---

## Algorithms and Efficiency, Without the Math Panic

An algorithm is just a precise, step-by-step way of solving a problem, and some ways of solving the same problem are meaningfully better than others.

1. **You already write algorithms outside of class.**

A recipe is an algorithm. Directions to your house are an algorithm. If you've ever explained step-by-step how to do something, you've written one.

2. **"Efficient" doesn't mean "fast" in the way you'd think of a fast car.**

In computer science, efficiency usually means how the amount of work grows as the amount of data grows. An algorithm that works fine on 10 items but grinds to a halt on 10,000 has an efficiency problem.

3. **You can compare algorithms without running the code.**

Just by looking at how many steps an approach takes relative to the size of the input, you can predict which of two solutions will scale better, before you even test them.

4. **Small inefficiencies matter more as data grows.**

A slow approach might feel identical to a fast one on a tiny practice dataset, then completely fall apart on a real-world dataset with millions of entries. This is why efficiency is a design concern, not just an optimization afterthought.

5. **There's usually more than one correct algorithm for the same problem.**

"Correct" and "efficient" are separate questions. A working solution that's slow is still worth writing first; you can improve its efficiency once you know it produces the right answer.

---

## Data, Privacy, and You

Every app, site, and service you use collects data about you. Understanding how and why is part of being a responsible computer scientist, and a responsible user.

1. **Data can identify you even without your name attached.**

Location history, browsing patterns, and even how you scroll can be enough to identify a specific person, even in datasets that were supposedly "anonymized."

2. **"Free" services are usually funded by your data, not by nothing.**

If you're not paying money for a product, your attention or your data is very often part of what's being exchanged for the service.

3. **Data breaches are common, not rare.**

Companies you trust with your information can still lose control of it. Understanding this is part of why strong, unique passwords and multi-factor authentication matter.

4. **Metadata can reveal more than the content itself.**

Even without reading a message, knowing *who* messaged *whom*, *when*, and *for how long* can reveal a surprising amount about a relationship or a pattern of behavior.

5. **Privacy settings are a starting point, not a guarantee.**

Adjusting your settings reduces your exposure, but it doesn't eliminate it; data you share can still be copied, screenshotted, or shared onward by others.

6. **Thinking about data use is part of designing software, not just using it.**

As you build projects this year, you'll make real decisions about what data to collect and how to handle it. Those are design choices with real consequences, not just technical details.

---

## Bias in Algorithms

Algorithms don't automatically produce fair or neutral results just because they're "just math." The people who build them, and the data used to train or design them, shape what they produce.

1. **Bias usually enters through the training data, not through malicious intent.**

If a dataset reflects historical inequalities, an algorithm trained on it will tend to reproduce those same patterns, even if no one involved intended that outcome.

2. **A biased algorithm can look objective while still being unfair.**

Because the output comes from a calculation rather than a person's stated opinion, it can carry a false sense of neutrality that makes the bias harder to notice and harder to challenge.

3. **Small design decisions can have large downstream effects.**

Choices as specific as which features a model considers, or how a category is defined, can quietly shape who benefits from a system and who doesn't.

4. **Real-world examples exist across hiring, lending, and criminal justice tools.**

Automated systems used to screen resumes, assess loan applications, or predict recidivism have all been documented producing unequal outcomes across different demographic groups.

5. **Recognizing bias is a skill you can practice, not just a topic to memorize.**

As you evaluate the projects and systems you encounter this year, it's worth regularly asking: who collected this data, who's represented in it, and who might be left out?

6. **This isn't a reason to distrust all algorithms. It's a reason to build them thoughtfully.**

Understanding where bias comes from is what makes it possible to design around it.

---

## Pair Programming, Not Scrum

You don't need a full team process to collaborate well. You need two clear roles and a habit of switching between them.

1. **One person drives, one person navigates.**

The **driver** is at the keyboard, actually typing the code. The **navigator** is reading along, thinking ahead, catching typos, and asking questions about the approach.

2. **The navigator's job is not to stay silent.**

A good navigator is actively thinking a step or two ahead, spotting a logic issue before it becomes a bug, or suggesting a cleaner way to structure something.

3. **Switch roles regularly.**

Trading the keyboard every 10–15 minutes (or at a natural stopping point) keeps both people engaged and makes sure both partners understand the whole solution, not just their half of it.

4. **Talk out loud while you work.**

Narrating your thinking, saying something like "I'm going to check if this list is empty first," gives your partner the chance to catch mistakes in your *reasoning*, not just in your syntax.

5. **Disagreement is normal and useful.**

If you and your partner have different ideas about how to solve something, that's a chance to compare approaches, not a problem to avoid. Try one, see how it goes, and stay open to switching.

6. **The goal is a better solution and a shared understanding, not just finishing faster.**

Two people who both understand the final code is a better outcome than one person doing all the thinking while the other watches.

---

## Academic Integrity & Collaboration Rules for the Create Performance Task

The Create Performance Task (PT) is individually authored and submitted to the College Board, which makes the line between "getting help" and "academic integrity violation" more important than it is on regular classwork.

1. **You may discuss ideas and concepts with others, but you may not share code.**

Talking through *how* an algorithm might work is collaboration. Sending, showing, or typing someone else's actual code into your project is not.

2. **Your program code must be your own, individual work.**

Even code that was "just inspired by" a classmate's specific implementation can cross the line. Understand a concept well enough to write it yourself in your own way.

3. **Using outside resources (tutorials, documentation, AI tools) is allowed, but must be properly acknowledged.**

The College Board requires you to document collaboration and the resources you used in your submission. Not disclosing help you received is the violation; using help isn't, as long as it's disclosed and the code itself is yours.

4. **Copy-pasting code from any source without attribution and understanding is a violation, even if you "fixed it a little."**

Changing variable names or reformatting someone else's code doesn't make it your original work.

5. **Two students submitting suspiciously similar programs will both be flagged, not just one.**

The scoring process is specifically designed to detect this. It's not worth the risk to either of you.

6. **When in doubt, ask before you submit, not after.**

If you're unsure whether something crosses a line, it's always better to check with me before the Create PT is submitted than to find out afterward.

---

## Reading Code Before Writing Code

Before you edit or extend a piece of code, yours or someone else's, take the time to actually understand what it currently does. This single habit prevents a huge number of avoidable bugs.

1. **Trace through the code by hand before you run it.**

Pick a sample input and walk through each line, tracking what each variable holds as you go. Predict the output before you run the program and check yourself.

2. **Read for structure before you read for detail.**

Identify the major sections first, such as where variables are set up, where the main logic happens, and where output is produced, before getting lost in the specifics of any one line.

3. **Ask what each variable represents, not just what it's named.**

A variable named `count` should represent something specific, so figure out *what* it's counting before you trust your assumptions about it.

4. **Look for the parts you don't understand and name them specifically.**

"I don't get this" is hard to act on. "I don't understand why this loop uses `i < len(list) - 1` instead of `i < len(list)`" is something you can look up or ask about directly.

5. **Predicting wrong is more useful than predicting nothing.**

If your hand-traced prediction turns out to be wrong, that mismatch tells you exactly where your understanding of the code breaks down, which is far more useful than skipping straight to running it.

6. **This habit transfers directly to debugging.**

Every debugging strategy above assumes you can read code closely. Practicing this on working code makes it much easier to do under pressure when code is broken.
In the end, it all boils down to this: Documentation builds empathy for future efforts. It is selfish and irresponsible to only think in the here-and-now and not consider new members who will take over the work or who need to translate it to the bottom line. By creating concise, meaningful documentation, future team members can be more productive and free to innovate. Be smart about it.

---

