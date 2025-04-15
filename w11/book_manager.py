# implement the main function
titles = ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice']
authors = ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen']
status = ['available'] * 4

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if   choice == 1: list_all()
        elif choice == 2: add_book()
        elif choice == 3: edit_book()
        elif choice == 4: delete_book()
        elif choice == 5: borrow_book()
        elif choice == 6: return_book()
        elif choice == 7: running = False
        else: print('Invalid choice. Please try again.')
    
    print('Thank you for using the Book Manager! Goodbye!')

def print_menu():
    print('Book Manager')
    print('1. List all books')
    print('2. Add a new book')
    print('3. Edit a book')
    print('4. Delete a book')
    print('5. Borrow a book')
    print('6. Return a book')
    print('7. Exit')

def list_all():
    print('+' * 50)
    for i in range(len(titles)):
        print(f'{i + 1}. {titles[i]} by {authors[i]} - {status[i]}')
    print('+' * 50)

def add_book():
    print('\nEnter a new book')
    title = input('Enter the title: ')
    author = input('Enter the author: ')
    
    # add the book to the lists
    status.append('available')
    titles.append(title)
    authors.append(author)

    print(f'Book {title} by {author} added successfully!\n\n')

def edit_book():
    print('\nEdit a book')
    book_number = int(input('Enter the book number to edit: '))
    # validate the book number
    if book_number < 1 or book_number > len(titles):
        print('Invalid book number. Please try again.')
        return
    # update the book details
    new_title = input('Enter the new title: ')
    new_author = input('Enter the new author: ')
    # update the lists with the new details
    titles[book_number - 1] = new_title     # -1 because list index starts from 0
    authors[book_number - 1] = new_author
    print(f'Book {book_number} updated successfully!\n\n')

def delete_book():
    print('\nDelete a book')
    book_number = int(input('Enter the book number to delete: '))
    # validate the book number
    if book_number < 1 or book_number > len(titles):
        print('Invalid book number. Please try again.')
        return
    # check if the book is borrowed
    if status[book_number - 1] == 'borrowed':
        print('Cannot delete a borrowed book. Please return it first.')
        return
    # delete the book from the lists
    titles.pop(book_number - 1)
    authors.pop(book_number - 1)
    status.pop(book_number - 1)

    print(f'Book {book_number} deleted successfully!\n\n')

def borrow_book():
    # enter the book number to borrow
    book_number = int(input('Enter the book number to borrow: '))
    # check if the book number is valid
    if book_number < 1 or book_number > len(titles):
        print('Invalid book number. Please try again.')
        return
    # check if the book is borrowed then print error message
    if status[book_number - 1] == 'borrowed':
        print('This book is already borrowed. Please return it first.')
        return

    # change the status of the book to borrowed
    status[book_number - 1] = 'borrowed'

    # print success message
    print(f'You have borrowed "{titles[book_number - 1]}" by {authors[book_number - 1]} successfully!\n\n')

def return_book():
    # enter the book number to return
    book_number = int(input('Enter the book number to return: '))

    # check if the book number is valid
    if book_number < 1 or book_number > len(titles):
        print('Invalid book number. Please try again.')
        return

    # check if the book is available then print error message
    if status[book_number - 1] == 'available':
        print('This book is already available. Please borrow it first.')
        return
    # change the status of the book to available
    status[book_number - 1] = 'available'

    # print success message
    print(f'You have returned "{titles[book_number - 1]}" by {authors[book_number - 1]} successfully!\n\n')


if __name__ == '__main__':
    main()