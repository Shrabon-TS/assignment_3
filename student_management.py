# _____________________________________________
# Student Management System
# This program is used to manage and store student information.
# _____________________________________________

class Student:
    def __init__(self, name, student_id, email, age, department, marks=None):
        self.name = name
        self.student_id = student_id
        self.__email = email          
        self.age = age
        self.department = department
        self.__marks = marks or []    

    def get_email(self):
        return self.__email


    def set_email(self, email):
        self.__email = email

    
    def add_marks(self, *marks):
        """
        Adds one or multiple marks.
        Example:
            student.add_marks(80)
            student.add_marks(70, 85, 90)
        """
        for mark in marks:
            if 0 <= mark <= 100:
                self.__marks.append(mark)
            else:
                print(f"Invalid mark: {mark}")

    def calculate_result(self):
        """Calculate average marks and result."""
        if not self.__marks:
            return "No marks available"

        average = sum(self.__marks) / len(self.__marks)

        if average >= 80:
            grade = "A+"
        elif average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        return f"Average: {average:.2f}, Grade: {grade}"

    def get_student_type(self):
        return "General Student"

    def display_info(self):
        print("\n----- Student Information -----")
        print(f"Name       : {self.name}")
        print(f"Student ID : {self.student_id}")
        print(f"Email      : {self.__email}")
        print(f"Age        : {self.age}")
        print(f"Department : {self.department}")
        print(f"Type       : {self.get_student_type()}")
        print(f"Result     : {self.calculate_result()}")


class UndergraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        semester,
        marks=None
    ):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department,
            marks
        )
        self.semester = semester



 # Method overriding

    def get_student_type(self):
        return f"Undergraduate Student - Semester {self.semester}"


    def display_info(self):
        super().display_info()
        print(f"Semester   : {self.semester}")


class GraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        research_topic,
        marks=None
    ):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department,
            marks
        )
        self.research_topic = research_topic

    
    def get_student_type(self):
        return "Graduate Student"

    
    def display_info(self):
        super().display_info()
        print(f"Research   : {self.research_topic}")



if __name__ == "__main__":

    
    student1 = Student(
        "Shrabon",
        "758448",
        "chshrabon10@gmail.com",
        22,
        "Computer Science & Technology"
    )

    student2 = UndergraduateStudent(
        "Ishrak",
        "758450",
        "shrabonobscura18@gmail.com",
        22,
        "Computer Science & Technology",
        7
    )

    student3 = GraduateStudent(
        "Choyon Hosen",
        "758452",
        "choyonhosen10@gmail.com",
        25,
        "Computer Science & Technology",
        "mechanical engineering"
    )



 # Adding marks for each student

    student1.add_marks(89, 92, 85)
    student2.add_marks(90, 85, 88, 92)
    student3.add_marks(82, 86, 91)


    student1.display_info()
    student2.display_info()
    student3.display_info()

    print("\n----- Polymorphism Demonstration -----")

    students = [student1, student2, student3]

    for student in students:
        print(
            f"{student.name} -> "
            f"{student.get_student_type()}"
        )


    print("\n----- Encapsulation Demonstration -----")
    print("Student email:", student1.get_email())

    student1.set_email("Shrabonts18@gmail.com")

    print("Updated email:", student1.get_email())
