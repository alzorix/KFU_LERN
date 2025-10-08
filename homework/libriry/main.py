

books = [
    {"id": 1, "title": "Мастер и Маргарита", "author": "Булгаков", "year": 1966},
    {"id": 2, "title": "Преступление и наказание", "author": "Достоевский", "year": 1866},
    {"id": 3, "title": "Война и мир", "author": "Толстой", "year": 1869},
    {"id": 4, "title": "Анна Каренина", "author": "Толстой", "year": 1877},
    {"id": 5, "title": "Собачье сердце", "author": "Булгаков", "year": 1925}
]

# поиск по названию книги
def find_book_by_title(title):
    global books
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    return None



#  поиск всех книг автора
def find_books_by_author(author):
    global books
    result = []
    for book in books:
        if book["author"].lower() == author.lower():
            result.append(book)
    return result
from copy import deepcopy

# сортировка пузырьком по году издания
def sort_books_by_year():
    global books
    books_sorted = deepcopy(books)
    n = len(books_sorted)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if books_sorted[j]["year"] > books_sorted[j + 1]["year"]:
                books_sorted[j], books_sorted[j + 1] = books_sorted[j + 1], books_sorted[j]
                swapped = True
        if not swapped:
            break
    return books_sorted





# фильтрация по диапазону лет
def find_books_by_year_range( start_year, end_year):
    global books
    result = []
    for book in books:
        if start_year <= book["year"] <= end_year:
            result.append(book)
    return result


def binary_search_start_year(books, start_year):
    left, right = 0, len(books) - 1
    result = None
    while left <= right:
        mid = (left + right) // 2

        if books[mid]["year"] >= start_year:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


def binary_search_end_year(books, end_year):
    left, right = 0, len(books) - 1
    result = None
    while left <= right:
        mid = (left + right) // 2

        if books[mid]["year"] <= end_year:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

def binary_search( start_year, end_year):
    global books
    start = binary_search_start_year(books, start_year)
    end = binary_search_end_year(books, end_year)
    if start <= end:

        print(books[start:end + 1])

print("Поиск книги по названию:")
print(find_book_by_title( "Война и мир"))

print("\nКниги Булгакова:")
print(find_books_by_author( "Булгаков"))

print("\nСортировка книг по году издания:")
print(sort_books_by_year())

print("\nКниги, изданные между 1900 и 1970 годами:")
print(binary_search( 1900, 1970))
