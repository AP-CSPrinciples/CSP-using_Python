**Performance Task: Develop a Snake Game using Pygame (AP CSP)**

### Objective:
The goal of this performance task is for students to design and implement a fully functional Snake game using Python and Pygame. Students are expected to use key programming concepts such as lists, conditionals, iteration, keyboard inputs, and collision detection in their code.

### Instructions:

1. **Set up the Environment**:
   - Install Python and Pygame if not already done. Ensure the Pygame library is correctly installed and functioning.
   - Create a new Python file to develop your Snake game.

2. **Create the Snake**:
   - Initialize a snake using a list of coordinates. This can be a static or dynamic list that represents the positions of the segments of the snake.
   - The snake should begin with a small length (e.g., 3 segments).
   - The snake should grow by one segment each time it eats food.

3. **Game Window and Display**:
   - Set up the Pygame window with a size of your choice (e.g., 600x400).
   - Display a game title or logo.
   - Include a score display that updates as the snake eats food.

4. **Movement of the Snake**:
   - Use iteration and conditionals to control the movement of the snake.
   - The snake should be able to move up, down, left, and right using keyboard inputs (arrow keys or WASD).
   - The game should update the position of the snake on the screen based on user input.

5. **Food Generation**:
   - Randomly generate the position of the food using random coordinates.
   - Ensure the food does not appear inside the snake’s body.
   - The snake should eat the food when it collides with it, causing the snake to grow by one segment.

6. **Collision Detection**:
   - Implement collision detection for the snake. The game should end if:
     - The snake collides with the wall.
     - The snake collides with itself (body collision).
   - When a collision occurs, display a "Game Over" message.

7. **Game Over and Restart**:
   - When the game ends, show the final score and allow the player to restart the game by pressing a specific key (e.g., "R").

8. **Use of Lists**:
   - Use lists to store and manage the positions of the snake's body segments.
   - Use a dynamic list that updates every time the snake moves (adding a new head and removing the tail).
   - The list can be static for simpler versions but should dynamically grow with each piece of food eaten.

9. **Iterative Design**:
   - Your game loop should run continuously to update the game’s state (snake position, food, etc.) and handle user input.
   - Inside the loop, update the game state based on the player's actions and interactions with the environment.

10. **Conditionals**:
   - Use conditionals to check for:
     - Whether the snake has eaten food.
     - Whether the snake has hit the wall or itself.
     - Directional movement based on user input.

11. **Keyboard Input**:
   - Ensure the snake can move in all four directions based on user input via the keyboard (e.g., arrow keys or WASD).
   - Only one direction can be chosen at a time (no backward movement).

12. **Final Submission**:
   - Submit the Python file with the game logic fully implemented.
   - Include any necessary comments in the code explaining key parts of your logic.
   - Ensure the code runs without errors and the game is fully functional.

### Grading Criteria:
- **Functionality**: The game should run without errors, include all necessary features, and meet the objective of a fully playable Snake game.
- **Code Structure**: The code should be well-organized, with appropriate use of functions, lists, and conditionals.
- **Creativity**: Any additional features, such as different levels, backgrounds, or game mechanics, will be positively considered.
- **Documentation**: Clear comments explaining how the game works and what each part of the code does.

Good luck with your Snake game project!https://github.com/CAMS-Software-Design-and-Development/SDD.githttps://github.com/CAMS-Software-Design-and-Development/SDD.git

### **Project Management Structure: SCRUM for Snake Game Development**

For the development of the Snake game, we will use the SCRUM methodology to manage the project effectively. SCRUM is an agile framework that breaks down tasks into manageable units, promotes collaboration, and ensures incremental progress. The team will consist of four members, each with a designated role. The roles will help keep the team organized, ensure clear communication, and achieve project milestones.

### **SCRUM Roles for 4 Members:**

1. **Product Owner**:
   - **Responsibilities**:
     - Acts as the primary point of contact for the project and ensures the development aligns with the project vision.
     - Defines and prioritizes the project features (Game requirements) that need to be implemented.
     - Manages the Product Backlog, which includes all the features, bug fixes, and improvements for the Snake game.
     - Communicates project goals and requirements to the team.
     - Provides feedback on features and progress during Sprint Review meetings.
   
   - **Skills Needed**: Strong understanding of the overall game concept, good communication skills, ability to make decisions about the game features and scope.
   
   - **Expected Outcome**: Clear direction and prioritization for the team.

2. **Scrum Master**:
   - **Responsibilities**:
     - Facilitates the SCRUM process and ensures the team follows the SCRUM framework.
     - Organizes daily stand-ups, sprint planning meetings, and sprint reviews.
     - Removes any obstacles or issues that may impede the team's progress.
     - Ensures the team is focused and works in short, focused intervals (Sprints).
     - Helps the team stay within the project scope and timeline.
   
   - **Skills Needed**: Strong leadership and communication skills, ability to manage conflicts, knowledge of SCRUM practices.
   
   - **Expected Outcome**: Smooth and efficient workflow, addressing team blockers promptly.

3. **Development Team Members (2 Developers)**:
   - **Responsibilities**:
     - Actively work on implementing game features, coding, and testing.
     - Collaborate on the technical aspects of the Snake game, including:
       - Designing the snake's movement.
       - Implementing collision detection.
       - Handling food generation and snake growth.
       - Managing keyboard inputs and screen updates.
     - Contribute to the refinement of the game based on feedback.
     - Test the game after each Sprint to ensure that it meets quality standards and project requirements.
     - Participate in the Sprint Planning, daily stand-ups, and Sprint Review meetings.
   
   - **Skills Needed**: Proficiency in Python, especially with libraries like Pygame; ability to work collaboratively on code; knowledge of game development fundamentals.
   
   - **Expected Outcome**: Functional game features, successful completion of tasks in sprints.

4. **Tester/QA Specialist**:
   - **Responsibilities**:
     - Responsible for testing and validating the game features after they are implemented.
     - Identifies bugs, glitches, and issues in the game and communicates them to the developers.
     - Ensures that the game performs correctly, especially for collision detection, food spawning, keyboard input handling, and the user interface.
     - Works closely with the Development Team to ensure that issues are addressed in subsequent sprints.
     - Prepares the game for final deployment by performing final tests for quality assurance.
     - Writes and executes test cases based on the game requirements (such as edge cases for collision, user input, and food consumption).
   
   - **Skills Needed**: Detail-oriented, ability to think through different user interactions, knowledge of game testing methodologies.
   
   - **Expected Outcome**: A polished, bug-free game ready for submission.

---

### **SCRUM Workflow for the Snake Game Project:**

1. **Sprint Planning**:
   - At the beginning of each Sprint (typically 1-2 weeks), the team will meet to discuss and plan the tasks for the Sprint.
   - The Product Owner will present the prioritized features and updates that need to be developed (from the Product Backlog).
   - The Development Team members will break down tasks into manageable units and decide which tasks they will work on during the Sprint.
   - The Tester will prepare a testing strategy for the new features.

2. **Daily Stand-up Meetings**:
   - Each team member will provide a brief update on their progress:
     - What they accomplished yesterday.
     - What they plan to work on today.
     - Any blockers or issues they are facing.
   - The Scrum Master facilitates the meeting and ensures that any blockers are addressed promptly.

3. **Sprint Execution**:
   - Developers will work on the tasks they committed to during the Sprint Planning.
   - The Tester will test new features as they are implemented.
   - The Scrum Master will check in regularly with the team to ensure smooth progress and remove any obstacles.

4. **Sprint Review**:
   - At the end of the Sprint, the team will meet to review the completed tasks.
   - The Product Owner will give feedback and approve or provide suggestions for any necessary changes.
   - The Development Team will demonstrate the working features of the Snake game.
   - The Tester will provide insights into the quality of the game and any remaining bugs.

5. **Sprint Retrospective**:
   - After the Sprint Review, the team will hold a Retrospective meeting to discuss:
     - What went well during the Sprint.
     - What could have been improved.
     - Any process changes that could make the next Sprint more efficient.

6. **Final Testing and Deployment**:
   - After all features have been implemented and tested, the Tester will perform the final round of testing to ensure that everything is working as expected.
   - The Development Team will fix any bugs or issues found during final testing.
   - The game will be ready for final deployment or submission.

---

### **Sprint Timeline Example:**

**Sprint 1:**
- **Goal**: Implement basic Snake movement, food generation, and collision detection with the walls.
- **Tasks**: 
  - Set up Pygame environment.
  - Create the basic Snake object and movement.
  - Generate food randomly.
  - Implement wall collision detection.
  - Testing basic functionality.

**Sprint 2:**
- **Goal**: Implement snake growth, collision with itself, and score tracking.
- **Tasks**:
  - Snake grows after eating food.
  - Self-collision detection.
  - Display score during the game.
  - Testing game mechanics (snake movement, growth, collision).

**Sprint 3:**
- **Goal**: Finalize the game’s UI, add restart functionality, and polish the game.
- **Tasks**:
  - Add a “Game Over” screen and restart option.
  - Refine game interface and animations.
  - Final quality assurance testing.
  - Bug fixes and code optimization.

---

### **Conclusion:**

By adopting SCRUM, the team will break down the Snake game project into manageable, iterative tasks, allowing for continuous development and feedback. This method ensures that all features are implemented systematically and that the game is continuously tested for quality. The roles and responsibilities within the team will help ensure that everyone works toward the common goal while maintaining clarity and communication throughout the project.
