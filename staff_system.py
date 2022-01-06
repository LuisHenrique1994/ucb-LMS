import os
import sys
import csv
from time import sleep
from books_system import *
from students_system import *


with open('staff.csv') as staff:
    staff_list = [{key: value for key, value in row.items()}
    for row in csv.DictReader(staff, skipinitialspace=True)]


def clear():
    os.system('cls')


class Staff(Books):
    
    def __init__(self):
        pass
    
    def print_staff_options():
        print('''
                [0] LOGOUT
                [1] MANAGE BOOKS
                [2] MANAGE STUDENTS''')
    
    def print_manage_books():
        print('''
                [0] LOGOUT
                [1] LIST OF BOOKS
                [2] ADD A NEW BOOK
                [3] UPDATE A BOOK
                [4] DELETE A BOOK''')
    
    def print_manage_students():
        print('''
                [0] LOGOUT
                [1] LIST OF STUDENTS
                [2] ADD A NEW STUDENT
                [3] UPDATE A STUDENT
                [4] DELETE A STUDENT''')
    
    def staff_login():
        clear()
        print('-=-' * 7, 'STAFF LOGIN', '-=-' * 7)
        while True:
            staff_id = input('STAFF LOGIN ID: ')
            staff_password = input('STAFF PASSWORD: ')
            if any(member['username'] == staff_id for member in staff_list) and any(member['password'] == staff_password for member in staff_list):
                print('Login Succesfull')
                sleep(0.5)
                break
            else:
                print('Login details not found.')
                sleep(0.7)
                user_input = int(input('\n Exit [0] | Try Again [1]: '))
                if user_input == 0:
                    sys.exit(0)
                
                elif user_input == 1:
                    pass
                
                else:
                    print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")
    
    def staff_menu(staff_login, print_staff_options, print_manage_books, print_manage_students):
        staff_login()
        
        while True:
            clear()
            print('-=-' * 7, 'Welcome to the Staff options', '-=-' * 7)
            
            print_staff_options()
            user_input = int(input('\n Select one option: '))
            
            if user_input == 0:
                break
            
            elif user_input == 1:
                clear()
                print('-=-' * 7, 'Manage books options', '-=-' * 7)
                print_manage_books()
                user_input = int(input('\n Select one option: '))
                
                if user_input == 0:
                    break
                
                elif user_input == 1:
                    print('')
                    object_books.display()
                    
                    while True:
                        user_input = int(input('\n Main menu [0] | Staff options [1]: '))
                        if user_input == 0:
                            return
                        elif user_input == 1:
                            break
                        else:
                            print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")
                
                elif user_input == 2:
                    Books.add_book(books)
                    
                    while True:
                        user_input = int(input('\n Main menu [0] | Staff options [1]: '))
                        if user_input == 0:
                            return
                        elif user_input == 1:
                            break
                        else:
                            print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")
                
                elif user_input == 3:
                    Books.update_book(books)
                    
                    while True:
                        user_input = int(input('\n Main menu [0] | Staff options [1]: '))
                        if user_input == 0:
                            return
                        elif user_input == 1:
                            break
                        else:
                            print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")
                
                elif user_input == 4:
                    Books.delete_book(books)
                    
                    while True:
                        user_input = int(input('\n Main menu [0] | Staff options [1]: '))
                        if user_input == 0:
                            return
                        elif user_input == 1:
                            break
                        else:
                            print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")
            
            elif user_input == 2:
                clear()
                print('-=-' * 7, 'Manage students options', 7 * '-=-')
                print_manage_students()
                user_input = int(input('\n Select one option: '))
                
                if user_input == 0:
                    break
                
                elif user_input == 1:
                    object_students.display_students()
                    
                    while True:
                        user_input = int(input('\n Main menu [0] | Staff options [1]: '))
                        if user_input == 0:
                            return
                        elif user_input == 1:
                            break
                        else:
                            print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")
                
                elif user_input == 2:
                    object_students.add_student()
                    
                    while True:
                        user_input = int(input('\n Main menu [0] | Staff options [1]: '))
                        if user_input == 0:
                            return
                        elif user_input == 1:
                            break
                        else:
                            print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")
                
                elif user_input == 3:
                    object_students.update_student()
                    
                    while True:
                        user_input = int(input('\n Main menu [0] | Staff options [1]: '))
                        if user_input == 0:
                            return
                        elif user_input == 1:
                            break
                        else:
                            print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")
                
                elif user_input == 4:
                    object_students.delete_student()
                    
                    while True:
                        user_input = int(input('\n Main menu [0] | Staff options [1]: '))
                        if user_input == 0:
                            return
                        elif user_input == 1:
                            break
                        else:
                            print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")


object_staff = Staff()
