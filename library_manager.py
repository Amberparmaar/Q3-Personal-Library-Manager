import json

# Load Library Data
def load_library():
    try:
        with open("library.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save Library Data
def save_library(library):
    with open("library.txt", "w") as file:
        json.dump(library, file)

# Initialize Library
db = load_library()

def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    year = input("Enter Publication Year: ")
    genre = input("Enter Genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    if title and author:
        db.append({"title": title, "author": author, "year": year, "genre": genre, "read": read_status})
        save_library(db)
        print(f'📖 "{title}" added successfully!')

def remove_book():
    if not db:
        print("Library is empty! Nothing to remove.")
        return

    titles = [book["title"] for book in db]
    print("Books available to remove:")
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")

    try:
        choice = int(input("Enter the number of the book to remove: ")) - 1
        if 0 <= choice < len(db):
            removed_book = db.pop(choice)
            save_library(db)
            print(f'❌ "{removed_book["title"]}" removed successfully!')
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input. Please enter a number.")

def search_book():
    search_query = input("Enter title or author to search: ").strip().lower()
    results = [book for book in db if search_query in book["title"].lower() or search_query in book["author"].lower()]

    if results:
        print("\nMatching Books:")
        for book in results:
            print(f'📖 {book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {"Read" if book["read"] else "Unread"}')
    else:
        print("No matching books found.")

def display_books():
    if not db:
        print("Library is empty!")
        return

    print("\n📚 Your Library:")
    for i, book in enumerate(db, 1):
        print(f'{i}. {book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {"Read" if book["read"] else "Unread"}')

def display_statistics():
    total_books = len(db)
    read_books = sum(1 for book in db if book["read"])

    if total_books > 0:
        percentage_read = (read_books / total_books) * 100
        print("\n📊 Library Statistics:")
        print(f'Total Books: {total_books}')
        print(f'Read Books: {read_books}')
        print(f'Percentage Read: {percentage_read:.2f}%')
    else:
        print("No books in the library.")

# Main menu loop
while True:
    print("\n📚 Personal Library Manager 📚")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search for a Book")
    print("4. Display All Books")
    print("5. Statistics")
    print("6. Exit")
    
    choice = input("Choose an option: ").strip()
    
    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        display_statistics()
    elif choice == "6":
        print("Exiting... Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.")
