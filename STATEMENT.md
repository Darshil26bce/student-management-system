# Student Management System

## Introduction

This project is a simple Student Management System made using Python. The main idea behind making this project was to create a program where student details, courses and marks can be managed from one place.
The program is completely terminal based. When we run it, a menu is shown and we can select what we want to do. I used CSV files for storing the information, so the data does not disappear when the program is closed.

## What the Program Does

The program is divided into a few different sections.

### Student Management

In this section, we can add a new student by entering details like the student's ID, name, email, department and enrollment year.
We can also display the students that are already saved and search for a student using their ID.

### Course Management

This part is used to keep the course details. A course can be added with its course ID, name, department and credits.
The saved courses can also be displayed whenever needed.

### Entering Marks

Marks can be entered by giving the student ID, course ID and marks.
Before saving the marks, the program checks whether the student and course are already present. It also makes sure that the marks entered are between 0 and 100.

### Reports

The report section is used to see the academic performance of students.
It can show a particular student's marks and calculate their percentage and grade. It can also calculate the average marks of the class and display the top five performers.

## Files Used

I have used three CSV files in this project:

1. students.csv
2. courses.csv
3. marks.csv


The student information is stored in students.csv, course information is stored in courses.csv, and the marks are stored separately in marks.csv.
Using separate files makes the data easier to manage and also keeps the different types of information organised.

## Python Concepts Used

While making this project, I used different Python concepts that I have learned, such as:

* Functions
* Variables
* Lists
* Loops
* Conditions
* User input
* CSV file handling
* Searching and sorting
* Calculations
* Basic error handling

I mainly used Python's built-in csv module, so there is no need to install any extra library to run the program.

## Purpose of the Project

The main purpose of this project was to understand how the Python concepts we learn individually can be used together to make an actual working program.
Making this project also gave me practice with storing data in files, taking input from the user and checking the data before saving it.
The current version covers the basic requirements of an academic management system. In the future, features like editing and deleting records, better reports or a graphical interface could also be added.

## Conclusion

Overall, this project is a basic way of managing student academic information using Python and CSV files. It is a simple terminal program, but it helped me understand how different parts of Python can be connected together to make something useful.
