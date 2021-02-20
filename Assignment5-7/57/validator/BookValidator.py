from domain.Book import Book

class BookValidator:

    def validID(self, ID):
        #NZZ
        if len(ID) != 3:
            return False
        for i in ID:
            if i < '0' or i > '9':
                return False
        return True

    def validate(self, book):
        """Validate if provided Book instance is valid
        book - Instance of Book type
        Return List of validation errors. An empty list if instance is valid."""
        if isinstance(book, Book) == False:
            raise TypeError("Inexisting book!")
        errors = []
        if self._validID(book.bookID) == False:
            errors.append("Invalid ID!")
        if len(book.title) == 0:
            errors.append("Invalid title!")
        if len(book.description) == 0:
            errors.append("Invalid description!")
        if len(book.author) == 0:
            errors.append("Invalid author!")
        if len(errors) != 0:
            raise ValueError(errors)


