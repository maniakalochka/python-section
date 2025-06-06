class BookManager:
    """
    Упрощенный класс для представления книг в библиотеке.
    """
    def __init__(self) -> None:
        self._books = []

    def add_book(self, book) -> None:
        self._books.append(book)

    def print_catalog(self) -> None:
        for book in self._books:
            print(f"Title: {book.title}, Author: {book.author}")

    def plan_event(self, event_name: str, date: str) -> None:
        """
        Плохая практика: метод, который не относится к управлению книгами,
        но находится в классе BookManager.
        """
        print(f"Planning event '{event_name}' on {date}.")
