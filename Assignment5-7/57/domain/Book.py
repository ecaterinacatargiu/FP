class Book:

    def __init__(self, bookID, title, description, author):
        self._bookID = bookID
        self._title = title
        self._description = description
        self._author = author

    def __str__(self):
        return "BookID:" + str(self.getBookID) + ", Title: " + self.getTitle + ", Desccription: " + self.getDescription + ", Author: " + self.getAuthor

    def __repr__(self):
        return str(self)

    @property
    # BookId getter
    def getBookID(self):
        return self._bookID

    @property
    # Title getter
    def getTitle(self):
        return self._title

    #@title.setter
    # Title setter
    def setTitle(self, newTitle):
        self._title = newTitle

    @property
    def getDescription(self):
        return self._description

    @property
    def getAuthor(self):
        return self._author


