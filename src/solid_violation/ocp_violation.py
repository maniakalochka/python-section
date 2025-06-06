class LibraryCalculator:
    def calculate(self, book_type: str, days_late: int):
        """
        В данном случае при добавлении нового типа книги потреббуется изменить
        этот метод, что нарушает принцип открытости/закрытости.
        """
        if book_type == "regular":
            return days_late * 0.5
        elif book_type == "new":
            return days_late * 1.0
        elif book_type == "rare":
            return days_late * 2.0
        else:
            return 0
