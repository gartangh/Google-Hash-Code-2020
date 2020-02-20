import math

import pandas as pd
from book import Book

columns = ['nr_of_books', 'books_per_day', 'setup_time', 'total_score', 'all_books']


def read(filename):
    with open(filename) as file:
        file_lines = file.readlines()

        # Read in general info
        info = file_lines[0].split(" ")
        nr_of_books = int(info[0])
        nr_of_libraries = int(info[1])
        nr_of_days = int(info[2])

        # Read in books
        books_scores = [int(book_score) for book_score in file_lines[1].split(" ")]
        books = []
        for book_id, book_score in enumerate(books_scores):
            book = Book(book_id, book_score)
            books.append(book)

        # Read in libraries
        libraries = []
        for library_id in range(nr_of_libraries):
            library_info = file_lines[2 + (2 * library_id)].split(" ")
            library_nr_of_books = int(library_info[0])
            library_nr_of_setup_days = int(library_info[1])
            library_nr_of_books_per_day = int(library_info[2])

            library_book_ids = [int(library_book_id) for library_book_id in
                                file_lines[2 + (2 * library_id + 1)].split(" ")]
            library_books = []
            t_score = 0
            for library_book_id in library_book_ids:
                book = books[library_book_id]
                library_books.append(book)
                t_score += book.score

            lst = [library_nr_of_books, library_nr_of_books_per_day, library_nr_of_setup_days, t_score, library_books]
            libraries.append(lst)

        df = pd.DataFrame(libraries, columns=columns)
        df['max_active_time'] =  df.nr_of_books / df.books_per_day + df.setup_time
        df['avg_score'] = df.total_score / df.max_active_time
        df.sort_values(by=['max_active_time'], ascending=[True])


    return df


def write(filename, df):
    # TODO change to this year
    with open(filename, "w+") as file:
        file.write(f"{len(df)}\n")
        for index, row in df.iterrows():
            file.write(f"{index} {len(row.all_books)}\n")
            books = row.all_books
            sorted_books = list(sorted(books, key=lambda book: book.score, reverse=True))
            file.write(" ".join([str(book.id) for book in sorted_books]) + "\n")
