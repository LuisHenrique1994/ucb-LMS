import pandas as pd
import csv
from students_system import *

# books = pd.read_csv(r'C:\Users\henri\Desktop\Data Engineering\assessment\books.csv')
# books = books.set_index('ID')
# print(books)

# book_id = int(input("\n Cancel [0] | Book's [ID] UPDATE: "))
# # new_title = input('New title: ')
# # books.loc[book_id, 'Title'] = new_title
# books = books.drop(book_id)
# # books = books.drop(books.index[book_id-1])

# print(books)

# print(f'Achei seu titulo: {books.iloc[book_id - 1].values[0]}')
# print(f'Achei de novo: {books.iat[book_id -1, 0]}')
# print(f"Ora ora oq temos aqui: {books.at[books.index[book_id-1], 'Title']}")
# print(books['Title'].values[book_id-1])

# print('\n', books.loc[book_id])
# print('\n', books)

# books.to_csv('books.csv')


# last_id = books.index[-1].astype(int)
# last_id = pd.DataFrame([last_id]).astype(int)
# id = last_id + 1
# print(id)

# book_borrowed = int(input('\n Select a book to borrow by the ID: '))
# if not 'Unavailable' in books.Status[book_borrowed]:
#     books.loc[[book_borrowed],['Quantity']] -= 1
#     print(f"You've borrowed the book {book_borrowed}.")
#     books.loc[books['Quantity'] <= 0, 'Status'] = 'Unavailable'
# else:
#     print('Book not available.')


# print(books)



# df = pd.DataFrame([[1, 2, 254], [3, 4, 1], [10, 20, 30]],
# columns=['ID', 'Title', 'Qty'])
# df = df.set_index('ID')


# print('\n', df)

# user_input = int(input('Qual livro vc quer imprestar ID: '))
# print(df.loc[user_input].at['Qty'])

# df.at[user_input, 'Qty'] -= 1

# print(df.at[1, 'Qty'])



# list_of_members = [{'username': 'luis', 'password': 's123'}, {'username': 'Dawood', 'password': '123'}]
# print(list_of_members)

# user_name = input('What is your username: ')
# user_password = input('What is your password: ')
# # and any(member['password'] == user_password
# if any(member['username'] == user_name for member in list_of_members) and any(member['password'] == user_password for member in list_of_members):
#     print(user_name, user_password)
# else:
#     print('Something else')

# if user_name in list_of_members:
#     print(f'{user_name} and {user_password}')
#     print('succesfull login')
# else:
#     print('Login details does not match.')

# for item in list_of_members:
#     if item['username'] == user_name:
#         print('ok')
#         print(f"I've find you, {user_name}, now i need your password")
#         password = input('Your password please: ')
#         if item['password'] == password:
#             print('ok2')
#             print(item[password])


# print('finished')

# with open('students.csv') as students:
#     students_list = [{key: value for key, value in row.items()}
#     for row in csv.DictReader(students, skipinitialspace=True)]

# def add_student():
#     object_students.display_students()
    
#     new_student = {}    
    
#     new_student['id'] = int(students_list[len(students_list)-1]['id']) + 1
#     new_student['username'] = input('New student username: ')
#     new_student['password'] = input('New student password: ')
#     print(new_student)
#     # students_list.append(new_student)

#     with open('students.csv', 'a+', newline='') as students:
#         field_names = ['id', 'username', 'password']
#         csv_writer = csv.DictWriter(students, fieldnames=field_names)
#         csv_writer.writerow(new_student)
#         students.close

# add_student()

def read_students():
    with open('students.csv') as students:
        students_list = [{key: value for key, value in row.items()}
        for row in csv.DictReader(students, skipinitialspace=True)]
    return students_list
students_list = read_students()

def update_student():
    students_list = read_students()
    object_students.display_students()

    for index in range(len(students_list)):
        for key in students_list[index]:
            print(students_list[index][key])
    
    for key, value in enumerate(students_list, start=1):
        print(key, value)
    
    print(students_list)
    # id = int(input("\n Cancel [0] | Student's [ID] UPDATE: "))
    # if id == 0:
    #     return
    
    # # print(students_list[id-1])
    
    # new_username = input("\n Leave Blank to SKIP | New Student's username: ")
    # if new_username != '':
    #     students_list[id-1]['username'] = new_username
    
    # print(students_list)
    
    # new_password = input("\n Leave Blank to SKIP | New Student's password: ")
    # if new_password != '':
    #     students_list[id-1]['password'] = new_password
    
    # print(students_list)
update_student()
