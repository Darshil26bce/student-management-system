# Student Management System

## Introduction

This project is a Python-based program for keeping track of students, courses, and their marks.
I made it as a command-line application, so all the operations are performed by entering choices in the terminal. Instead of using a database, the program saves the information in CSV files.
The main idea of the project is to have one place where basic academic information can be added, updated, searched, and viewed.

## What Can Be Done With The Program?

After starting the program, a menu is displayed from which different operations can be selected.

### Student Details

The student section allows the user to work with student records.

Some of the available options are:

* Register a student
* Display the list of students
* Find a particular student using their ID

For every student, the program stores their ID, name, email, department, and year of enrollment.

### Course Details

Courses can also be added to the system.

For each course, the following information is stored:

* Course ID
* Course name
* Department
* Number of credits

The added courses can be viewed whenever required.

### Adding Marks

Marks can be entered after the required student and course have been added.

The program performs some checks before saving the marks. For example, it checks whether the entered student and course actually exist. It also does not accept marks outside the range of 0 to 100.

This helps prevent incorrect entries from being stored in the file.

## Reports

The report section is used to get some useful information from the stored data.

### Student Result

By selecting a student, their academic information and marks can be displayed. The report also calculates the percentage and assigns a grade.

The grades are calculated according to this range:

90 - 100    A+
80 - 89     A
70 - 79     B
60 - 69     C
50 - 59     D
Below 50    F


### Average Marks

The program can calculate the average of the marks that have been entered.

### Top Students

The system can also find the students with the highest percentages and display up to five of them.

## Data Files

No separate database is used in this project. Three CSV files are used for storing the information:

1. students.csv
2. courses.csv
3. marks.csv


The files have different purposes:

1. students.csv → student records
2. courses.csv → course records
3. marks.csv → marks entered for students

The files are automatically used by the program when data is added or read.

## Running The Program

Make sure Python 3 is installed on the computer.
The program will then show the main menu.


===============================================================

#            STUDENT MANAGEMENT SYSTEM

===============================================================

1. MANAGE STUDENTS
2. MANAGE COURSES
3. ENTER MARKS
4. VIEW REPORTS
5. EXIT


Select an option by entering its number and pressing Enter.

## Simple Example

Suppose a student with ID 101 is added to the system.

<br>
ID: 101
<br>
Name: Rahul
<br>
Email: rahul@gmail.conn
<br>
Department: CSE
<br>
Year: 2026
<br>


A course can then be created and marks can be entered for Rahul.

Once the marks are saved, the report section can be used to see the result and calculated grade.

## Technologies Used

* **Python 3**
* **CSV**
* **Command Line Interface**

The project mainly uses Python's built-in csv module, so installing external packages is not required.

## Concepts Used

While developing this project, I used several basic Python concepts, including:

* Functions
* Loops
* Conditional statements
* Lists
* User input
* File handling
* CSV reading and writing
* Calculations
* Menu-driven programming

## Final Note

This project was made to practice Python programming by building something that can actually store and use data.

Working on it helped me understand how functions, conditions, loops, and file handling can work together in a single program. It also gave me an idea of how a simple academic record system can be organized without using a database.

