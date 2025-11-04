diskette = 1.44
pages = 100
lines = 50
chars = 25
bytes = 4

chars_per_book = pages * lines * chars
book_size = chars_per_book * bytes

diskette_size = diskette * 1024 * 1024
books_count = int(diskette_size // book_size)

print("Количество книг, помещающихся на дискету:", books_count)