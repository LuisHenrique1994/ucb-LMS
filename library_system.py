import os
import sys
from students_system import *
from staff_system import *


def clear():
    os.system('cls')

def main_menu():
    print('''
            [0] SAVE AND EXIT
            [1] STUDENTS LOGIN
            [2] STAFF LOGIN
            ''')

class Library():
    
    def __init__(self):
        pass
    
    while True:
        clear()
        print('-=-' *7, "WELCOME to The BIRMINGHAM's library", '-=-' * 7)
        main_menu()
        user_input = int(input('Select one option: '))
        if user_input == 0:
            sys.exit(0)
        elif user_input == 1:
            Students.students_menu(Students.students_login, Students.print_students_options)
            
        elif user_input == 2:
            Staff.staff_menu(Staff.staff_login, Staff.print_staff_options, Staff.print_manage_books, Staff.print_manage_students)
            
        else:
            print(f"\n You've typed {user_input}. It's an incorrect input, try again.")


object_library = Library()
