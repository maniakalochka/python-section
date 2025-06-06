class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read_details(self):
        return f"Title: {self.title}, Author: {self.author}"


class ReferenceBook(Book):
    def read_details(self):
        """"
        Базовый класс предоставляет контракт для чтения деталей книги, но
        переопределенный метод в классе ReferenceBook нарушает принцип LSP,
        так как он не позволяет читать книгу в традиционном смысле, а возбуждает исключение.
        """
        raise NotImplementedError("Reference books cannot be read in the traditional sense.")
