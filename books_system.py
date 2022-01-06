import pandas as pd


def read_books():
    books = pd.read_csv(r'C:\Users\henri\Desktop\Data Engineering\assessment\books.csv')
    books = books.set_index('ID')
    return books
books = read_books()


class Books():
    
    def  __init__(self):
        self.display_books = books
    
    def display(self):
        books = read_books()
        print(books)
    
    def borrow_book(self):
        book_borrowed = int(input('\n Select a book to borrow by the ID: '))
        if not 'Unavailable' in books.Status[book_borrowed]:
            books.loc[[book_borrowed],['Quantity']] -= 1
            books.loc[books['Quantity'] <= 0, 'Status'] = 'Unavailable'
            books.to_csv('books.csv')
            print(f"You've borrowed the book {book_borrowed}.")
        else:
            print('Book not available.')
    
    def return_book(self):
        book_returned = int(input('\n Select a book to return by the ID: '))
        books.loc[[book_returned],['Quantity']] += 1
        books.loc[books['Quantity'] > 0, 'Status'] = 'Available'
        books.to_csv('books.csv')
        print(f"You've returned the book {book_returned}.")
    
    def add_book(books):
        books = read_books()
        last_id = books.index[-1].astype(int)
        id = last_id + 1
        title = input("What's the Title for the new book: ").title().strip()
        author = input("Who is the Author for the new book: ").title().strip()
        published = input("When the book was published: ").title().strip()
        quantity = int(input("How many books in stock: "))
        if quantity <= 0:
            status = 'Unavailable'
        else:
            status = 'Available'
        
        new_book = pd.DataFrame(data=[[id, title, author, published, quantity, status]],columns=['ID', 'Title', 'Author', 'Published', 'Quantity', 'Status'])
        new_book = new_book.set_index('ID')
        books = books.append(new_book)
        books.to_csv('books.csv')
        
        print(f"\n New book '{title}' added succesfully.")
        print('-' * 50)
        print('\n', new_book)
        print('-' * 50)
        print('\n', books)
    
    def update_book(books):
        books = read_books()
        print('\n', books)
        
        id = int(input("\n Cancel [0] | Book's [ID] UPDATE: "))
        if id == 0:
            return
        
        new_title = input("\n Leave Blank to SKIP | New book's Title: ").strip().title()
        if new_title != '':
            books.loc[id, 'Title'] = new_title
            print('New title ok!')
        
        new_author = input("\n Leave Blank to SKIP | New book's Author: ").strip().title()
        if new_author != '':
            books.loc[id, 'Author'] = new_author
            print('New author ok!')
        
        new_published = input("\n Leave Blank to SKIP | New book's Published date: ").strip().title()
        if new_published != '':
            books.loc[id, 'Published'] = new_published
            print('New published ok!')
        
        try:
            new_quantity = int(input("\n Leave Blank to SKIP | New book's stock quantity: "))
            if new_quantity != int() or new_quantity == 0:
                books.loc[id, 'Quantity'] = new_quantity
                print('New quantity ok!')
        
        except ValueError:
            pass
        
        else:
            if new_quantity > 0:
                new_status = 'Available'
                print('\n Status set to Available.')
                books.loc[id, 'Status'] = new_status
            else:
                new_status = 'Unavailable'
                print('\n Status set to Unavailable')
                books.loc[id, 'Status'] = new_status
            
            answer = input("\n For Change availability manually [Y/N]: ").upper().strip()
            if answer in 'Y':
                user_input = input("\n Leave Blank to SKIP | New book's availability: ").strip().capitalize()
                if user_input != '':
                    books.loc[id, 'Status'] = user_input
                    print('New status ok!')
        
        finally:
            new_id = input("\n Leave Blank to SKIP | New book's ID: ")
            if new_id != '':
                books.reset_index(inplace=True)
                books['ID'].replace(id, value=int(new_id), inplace=True)
                print('New ID ok!')
                books = books.set_index('ID')
            books.to_csv('books.csv')
            print(f'\n Book updated successfully.')
    
    def delete_book(books):
        books = read_books()
        print('\n', books)
        
        id = int(input("\n Cancel [0] | Book's [ID] DELETE: "))
        if id == 0:
            return
        
        print('livro deletado')
        print(f'Book {books.iloc[id-1].values[0]} deleted successfully.')
        books = books.drop(id)
        books.to_csv('books.csv')
        print(books)


object_books = Books()
