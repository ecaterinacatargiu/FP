from repository.BookRepository import *
from repository.RepositoryException import *
from domain.Book import *

class BookTextFileRepo(BookRepository):

    def __init__(self, fileName="books.txt"):
        BookRepository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, obj):
        BookRepository.addBook(self, obj)
        self._saveFile()

    def remove(self, objID):
        BookRepository.removeBook(self, objID)
        self._saveFile()

    def update(self, obj):
        BookRepository.updateBook(self, obj)
        self._saveFile()

    def _saveFile(self):
        try:
            f = open(self._fileName, "w")
            for s in BookRepository.getAll(self):
                f.write(str(s.getBookID) + "," + str(s.getTitle) + "," + str(s.getDescription) + "," + str(s.getAuthor))
        except Exception as e:
            raise RepositoryError("The file cannot be open")
        finally:
            f.close()

    def _loadFile(self):
        try:
            #self._fileName = "D:\\INFO2018-2019\\~INFO\\FP\\Assignments\\AICIASS5-7\\57\\repository\\"+ self._fileName
            f = open(self._fileName, "r")
            s = f.readline()
            while len(s) > 1:
                tok = s.split(",")
                book = Book(int(tok[0]), tok[1], tok[2], tok[3])
                BookRepository.addBook(self, book)
                s = f.readline()
            f.close()
        except Exception as e:
            raise RepositoryError("The file cannot be open")
