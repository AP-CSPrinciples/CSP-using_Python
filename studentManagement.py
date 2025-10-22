# student_management.py

# Student class definition
class Student:
    def __init__(self, name: str, studentID: int, grade: float):
        self.name = name
        self.studentID = studentID
        self.grade = grade

    # Getter and Setter for name
    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    # Getter and Setter for studentID
    def get_studentID(self):
        return self.studentID

    def set_studentID(self, studentID: int):
        self.studentID = studentID

    # Getter and Setter for grade
    def get_grade(self):
        return self.grade

    def set_grade(self, grade: float):
        self.grade = grade

    # Display student details
    def display(self):
        print(f"ID: {self.studentID}, Name: {self.name}, Grade: {self.grade:.2f}")


# StudentManager class definition
class StudentManager:
    def __init__(self):
        self.students = []

    # Add a student
    def add_student(self, name: str, studentID: int, grade: float):
        if self.find_student(studentID):
            print("Error: Student with this ID already exists.")
            return
        student = Student(name, studentID, grade)
        self.students.append(student)
        print("Student added successfully.")

    # Display all students
    def display_all_students(self):
        if not self.students:
            print("No students in the system.")
            return
        for student in self.students:
            student.display()

    # Find a student by ID
    def find_student(self, studentID: int):
        for student in self.students:
            if student.get_studentID() == studentID:
                return student
        return None

    # Remove a student by ID
    def remove_student(self, studentID: int):
        student = self.find_student(studentID)
        if student:
            self.students.remove(student)
            print("Student removed successfully.")
        else:
            print("Student not found.")

    # Update student grade by ID
    def update_grade(self, studentID: int, new_grade: float):
        student = self.find_student(studentID)
        if student:
            student.set_grade(new_grade)
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    # Sort students by name or grade
    def sort_students(self, by: str):
        if by == "name":
            self.students.sort(key=lambda s: s.get_name())
        elif by == "grade":
            self.students.sort(key=lambda s: s.get_grade(), reverse=True)
        else:
            print("Invalid sort key.")
            return
        print(f"Students sorted by {by}.")

    # Search by name, grade or ID
    def search_students(self, keyword):
        results = []
        keyword = str(keyword).lower()
        for student in self.students:
            if (
                keyword in student.get_name().lower()
                or keyword == str(student.get_studentID())
                or keyword == str(student.get_grade())
            ):
                results.append(student)

        if not results:
            print("No matching students found.")
        else:
            print("Search results:")
            for student in results:
                student.display()


# Console UI
def main():
    manager = StudentManager()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Find Student by ID")
        print("4. Remove Student by ID")
        print("5. Update Student Grade")
        print("6. Sort Students")
        print("7. Search Students")
        print("8. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            try:
                name = input("Enter student name: ").strip()
                studentID = int(input("Enter student ID: "))
                grade = float(input("Enter student grade: "))
                manager.add_student(name, studentID, grade)
            except ValueError:
                print("Invalid input. Please enter correct data types.")
        elif choice == 2:
            manager.display_all_students()
        elif choice == 3:
            try:
                studentID = int(input("Enter student ID to find: "))
                student = manager.find_student(studentID)
                if student:
                    student.display()
                else:
                    print("Student not found.")
            except ValueError:
                print("Invalid input.")
        elif choice == 4:
            try:
                studentID = int(input("Enter student ID to remove: "))
                manager.remove_student(studentID)
            except ValueError:
                print("Invalid input.")
        elif choice == 5:
            try:
                studentID = int(input("Enter student ID to update grade: "))
                new_grade = float(input("Enter new grade: "))
                manager.update_grade(studentID, new_grade)
            except ValueError:
                print("Invalid input.")
        elif choice == 6:
            sort_by = input("Sort by 'name' or 'grade': ").lower()
            manager.sort_students(sort_by)
        elif choice == 7:
            keyword = input("Enter name, ID, or grade to search: ")
            manager.search_students(keyword)
        elif choice == 8:
            print("Exiting Student Management System.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 8.")


# Test Cases
def run_test_cases():
    print("\nRunning test cases...\n")
    manager = StudentManager()
    manager.add_student("Alice", 1001, 88.5)
    manager.add_student("Bob", 1002, 92.3)
    manager.add_student("Charlie", 1003, 78.0)
    print("\nDisplay all students:")
    manager.display_all_students()

    print("\nFind student by ID 1002:")
    student = manager.find_student(1002)
    if student:
        student.display()

    print("\nUpdate grade for student 1001:")
    manager.update_grade(1001, 90.0)
    manager.find_student(1001).display()

    print("\nRemove student with ID 1003:")
    manager.remove_student(1003)
    manager.display_all_students()

    print("\nSort students by name:")
    manager.sort_students("name")
    manager.display_all_students()

    print("\nSearch students with keyword 'Alice':")
    manager.search_students("Alice")

    print("\nSearch students with grade '90.0':")
    manager.search_students("90.0")


if __name__ == "__main__":
    run_test_cases()

    # Run the main program
    main()





