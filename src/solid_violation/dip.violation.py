class PSQLDatabase:
    def connect(self):
        print("Connecting to PostgreSQL database...")


class LibraryService:
    def __init__(self):
        """
        Здесь мы видим жесткую зависимость конкретной реализации базы данных,
        что нарушает принцип инверсии зависимостей, надо быть зависимым
        от абстракции, а не конкретной реализации.
        """
        self.database = PSQLDatabase()

    def get_books(self):
        self.database.connect()
        print("Get books from the database.")
