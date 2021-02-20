from repository.BookRepository import *
from domain.Book import *
import pickle

class BookPickleFileRepo(BookRepository):

    def __init__(self,fileName="books.pickle"):
        self._fileName=fileName
        BookRepository.__init__(self)
        #self._loadBinaryFile(self._fileName)
        self.readBinaryFile(self._fileName)

    def addBook(self,other):
        BookRepository.addBook(self,other)
        self._saveFile()

    def removeBook(self,bookID):
        book = BookRepository.removeBook(self,bookID)
        self._saveFile()
        return book

    def updateBook(self,book):
        BookRepository.updateBook(self, book)
        self._saveFile()

    def _saveFile(self):
        """f = open(self._fileName, "wb")
        list=BookRepository.getAll(self)
        for c in list:
            pickle.dump(c,f)
        f.close()"""

        f = open(self._fileName, "wb")
        pickle.dump(self._books, f)
        f.close()


    """def _loadBinaryFile(self,fileName):
        for c in self.readBinaryFile(fileName):
            print("a")
            self.add(c)"""

    def readBinaryFile(self,fileName):
        with open(fileName, 'rb') as f:
            while True:
                try:
                    self._books = pickle.load(f)
                except EOFError:
                    break

