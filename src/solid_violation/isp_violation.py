class Librarian:
    def work(self):
        pass

    def arrange_book(self):
        pass

    def manage_event(self):
        pass


class LibraryWorker(Librarian):
    def work(self):
        pass

    def arrange_book(self):
        print("А уборщице разве нужно расставлять книги?")

    def manage_event(self):
        print("А уборщице разве нужно управлять событиями в библиотеке?")
