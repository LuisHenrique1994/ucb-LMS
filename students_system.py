import os
import sys
import csv
from time import sleep
from books_system import *


def read_students():
    with open('students.csv') as students:
        students_list = [{key: value for key, value in row.items()}
        for row in csv.DictReader(students, skipinitialspace=True)]
    return students_list
students_list = read_students()


def clear():
    os.system('cls')


class Students(Books):
    
    def __init__(self):
        pass
    
    def display_students(self):
        students_list = read_students()
        message = ''
        for student in students_list:
            id = student['id']
            username = student['username']
            password = student['password']
            message = f' ID:{id} | username: {username} | password: {password}'
            print(message)
    
    def add_student(students_list):
        students_list = read_students()
        new_student = {}
        new_student['id'] = int(students_list[len(students_list)-1]['id']) + 1
        new_student['username'] = input('\nNew student username: ')
        new_student['password'] = input('New student password: ')
        
        with open('students.csv', 'a+', newline='') as students:
            field_names = ['id', 'username', 'password']
            csv_writer = csv.DictWriter(students, fieldnames=field_names)
            csv_writer.writerow(new_student)
        
        print('New student add successfully.')
    
    def update_student(students_list):
        students_list = read_students()
        object_students.display_students()
        
        id = int(input("\n Cancel [0] | Student's [ID] UPDATE: "))
        if id == 0:
            return
        
        update_student = {}
        update_student['id'] = id
        
        new_id = input("\n Leave Blank to SKIP | New Student's ID: ")
        if new_id != '':
            update_student['_id'] = new_id
        
        new_username = input("\n Leave Blank to SKIP | New Student's username: ")
        if new_username != '':
            update_student['username'] = new_username
        
        new_password = input("\n Leave Blank to SKIP | New Student's password: ")
        if new_password != '':
            update_student['password'] = new_password
        
        count = 0
        for student in students_list:
            count += 1
            if int(student['id']) == update_student['id']:
                break
        
        students_list[count-1]['id'] = update_student['_id']
        students_list[count-1]['username'] = update_student['username']
        students_list[count-1]['password'] = update_student['password']
        
        with open('students.csv', 'w', newline='') as students:
            writer = csv.DictWriter(students, fieldnames=students_list[0].keys())
            writer.writeheader()
            writer.writerows(students_list)
            students.close()
        
        print('\n Student UPDATED successfully.')
    
    def delete_student(students_list):
        students_list = read_students()
        object_students.display_students()
        
        id = int(input("\n Cancel [0] | Student's [ID] DELETE: "))
        if id == 0:
            return
        
        count = 0
        for student in students_list:
            count += 1
            if int(student['id']) == id:
                break
        
        students_list.pop(count-1)
        print('Student deleted successfully.')
        
        with open('students.csv', 'w', newline='') as students:
            writer = csv.DictWriter(students, fieldnames=students_list[0].keys())
            writer.writeheader()
            writer.writerows(students_list)
            students.close()
    
    def print_students_options():
        print('''
                [0] LOGOUT
                [1] LIST OF BOOKS
                [2] BORROW A BOOK
                [3] RETURN A BOOK''')
    
    def students_login():
        clear()
        print('-=-' * 7, 'STUDENTS LOGIN', '-=-' * 7)
        
        while True:
            user_name = input('USERNAME: ')
            user_password = input('PASSWORD: ')
            if any(member['username'] == user_name for member in students_list) and any(member['password'] == user_password for member in students_list):   
                print('Login Succesfull')
                sleep(0.5)
                break
            else:
                print('Login details not found.')
                sleep(1.2)
                user_input = int(input('\n Exit [0] | Try Again [1]: '))
                if user_input == 0:
                    sys.exit(0)
                elif user_input == 1:
                    pass
                else:
                    print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")
    
    def students_menu(students_login, print_students_options):
        students_login()
        
        while True:
            clear()
            print('-=-' * 7, 'Welcome to the Students options', '-=-' * 7)
            
            print_students_options()
            user_input = int(input('\n Select one option: '))
            
            if user_input == 0:
                break
            
            elif user_input == 1:
                print('')
                object_books.display()
                
                while True:
                    user_input = int(input('\n Main menu [0] | Students options [1]: '))
                    if user_input == 0:
                        return
                    elif user_input == 1:
                        break
                    else:
                        print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")
            
            elif user_input == 2:
                print('')
                object_books.display()
                object_books.borrow_book()
                
                while True:
                    user_input = int(input('\n Main menu [0] | Students options [1]: '))
                    if user_input == 0:
                        return
                    elif user_input == 1:
                        break
                    else:
                        print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")
            
            elif user_input == 3:
                print('')
                object_books.display()
                object_books.return_book()
                
                while True:
                    user_input = int(input('\n Main menu [0] | Students options [1]: '))
                    if user_input == 0:
                        return
                    elif user_input == 1:
                        break
                    else:
                        print(f"\n You've typed {user_input}. It's an incorrect input, please try again.")


object_students = Students()
