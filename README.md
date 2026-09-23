Student Management System
Project Overview

This is a simple Student Management System developed using Python and Object-Oriented Programming (OOP).

The system manages general, undergraduate, and graduate students. It can store student information, add marks, calculate results, and display student details.

Classes
Student

The parent class containing common student information such as:

Name

Student ID

Email

Age

Department

Marks

UndergraduateStudent

Inherits from the Student class and adds:

Semester

It also overrides the get_student_type() method.

GraduateStudent

Inherits from the Student class and adds:

Research Topic

It also overrides the get_student_type() method.

OOP Concepts Used :-

Class & Object 

Inheritance 

Polymorphism 

Method Overriding 

Method Overloading 

Encapsulation 

Features

Add and store student information

Add multiple marks

Calculate average marks

Assign grades automatically

Display student information

Support undergraduate semester information

Support graduate research topics

Validate marks between 0 and 100

Grading System
Average	Grade
80-100	A+
70-79	A
60-69	B
50-59	C
40-49	D
Below 40	F


How to Run

Open the project in VS Code and run:

python student_management.py

Project Structure
Assignment-3
── student_management.py
── README.md

Technology

Python 3.14.7

Object-Oriented Programming
