# Performance Task - Project 1

Create a console-based program to manage student data, such as names, grades, and student IDs. The program will store student data in multiple lists.  Appropriately comment throughout your program and provide test cases to verify that your program works as intended. Use function(s) with at least one parameter for this program.

 

**Tasks**:
1. Create a Student list(s) that includes:
   - `String name`
   - `int studentID`
   - `float grade`

2. Create a StudentManager function that will do the following:
   - Allow the user to:
     - Add a new student to the List.
     - View all students in the list.
     - Find a student by their ID.
     - Remove a student by their ID.
     - Update a student’s grade.
     - exit the program

3. Additional features:
   - Sort students by grade or name.
   - Search for students based on different criteria (e.g., by grade, name, or ID).
   - Implement input validation and handle exceptions for edge cases (e.g., entering invalid data).

Example Features:
- **Add Student**: Input name, ID, and grade, and add the student to the list.
- **Display All Students**: Print out all students’ information.
- **Update Grade**: Update the grade of an existing student by their ID.
- **Remove Student**: Remove a student based on their ID.


Example:

```python
Student Management System
Choose one of the following: 
The user can choose -> 1. Add a Student
The user can choose -> 2. Display All Students
The user can choose -> 3. Find a Student by ID
The user can choose -> 4. Remove a Student by ID
The user can choose -> 5. Update Student Grade
The user can choose -> 6. Exit
```


Example User Input & Output:
```python
#1. Add Student

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 1
Enter student name: John Doe
Enter student ID: 101
Enter student grade: 85.5


#2. Display All Students/

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 2
ID: 101, Name: John Doe, Grade: 85.5


#3. Find Student by ID

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 3
Enter student ID to find: 101
ID: 101, Name: John Doe, Grade: 85.5


#4. Remove Student by ID

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 4
Enter student ID to remove: 101


#5. Update Student Grade

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 5
Enter student ID to update grade: 101
Student not found.


#6. Exit

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 6

```
Submit your program files (.py) include appropriate comments within your program.  Include Test Cases that demonstrate the program works as intended.
