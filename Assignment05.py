# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot, 1/1/2030, Created Script
#   ABelhumeur, 11/12/2023, Began Assignment05
#   ABelhumeur, 11/13/2023, Small edits / polish pass
# ------------------------------------------------------------------------------------------ #

# Import libraries
import json

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = {}  # A dictionary of student data
students: list = []  # A table of student data

# On start, read the file's data as a two-dimensional list table (a list of dictionary rows)
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    for student_data in students:
        print(f'{student_data['first_name']} {student_data['last_name']}, {student_data['course_name']}')
    file.close()
except FileNotFoundError as e:
    print("JSON file not found.")
    print('---Technical Information---')
    print(e, e.__doc__, type(e), sep='\n')
    print("Creating file since it doesn't exist.")
    file = open(FILE_NAME, 'w')
    json.dump(students, file)
except Exception as e:
    print("There was an error reading from the document.")
    print('---Technical Information---')
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file.closed:
        file.close()


# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name can only contain alphabetic characters.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name can only contain alphabetic characters.")
            course_name = input("Enter the name of the course: ")
            student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)
            print('---Technical Information---')
            print(e.__doc__, type(e), sep='\n')
            print("User entered invalid information. Showing menu options again...")
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student_data in students:
            print(f"Student {student_data['first_name']} {student_data['last_name']} is enrolled in {student_data['course_name']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=1)
            print("All entries have been saved to the file 'Enrollments.json'.")
            file.close()
        except Exception as e:
            print("There was an error writing to the document.")
            print('---Technical Information---')
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
        
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")