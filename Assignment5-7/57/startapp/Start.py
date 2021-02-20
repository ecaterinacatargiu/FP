from Print.print import *
from repository.ClientRepository import ClientRepository
from repository.BookRepository import BookRepository
from UI.BookUI import *
from controller.BookController import *
from domain.Book import *
from domain.Rental import *
from validator.BookValidator import BookValidator
from UI.ClientUI import *
from datetime import date
from repository.RentalRepository import *
from controller.RentalController import *
from UI.RentalUI import *
from repository.BookTextFileRepo import *
from repository.ClientTextFileRepo import *
from repository.RentalTextFileRepo import *
from repository.BookPickleFileRepo import *
from repository.ClientPickleFileRepo import *
from repository.RentalPickleFileRepo import *



def initialBookList(repoBook):
    b1 = Book(100, "2666", "psyhoogy", "Roberto Bolaño")
    b2 = Book(101, "All About Love", "love", "Bell Hooks")
    b3 = Book(102,  "Desert Solitaire", "action", "Desert Solitaire")
    b4 = Book(103, "Geek Love", "drama", "Katherine Dunn")
    b5 = Book(104, "If on a Winter's Night a Traveler", "action", "Italo Calvino")
    b6 = Book(105, "The Left Hand of Darkness", "adventure", "Ursula K. Le Guin")
    b7 = Book(106, "To Kill a Mockingbird", "action/police", "Harper Lee")
    b8 = Book(107, "Half of a Yellow Sun", "phylosophy", "Chimamanda Ngozi Adichie")
    b9 = Book(108, "Invisible Cities", "history", "Italo Calvino")
    b10 = Book(109, "Hopscotch", "drama", "Julio Cortázar")

    repoBook.addBook(b1)
    repoBook.addBook(b2)
    repoBook.addBook(b3)
    repoBook.addBook(b4)
    repoBook.addBook(b5)
    repoBook.addBook(b6)
    repoBook.addBook(b7)
    repoBook.addBook(b8)
    repoBook.addBook(b9)
    repoBook.addBook(b10)



def initialClientList(repoClient):
    c1 = Client(200, "Alexandra")
    c2 = Client(201, "Cati")
    c3 = Client(202, "Korina")
    c4 = Client(203, "Andreea")
    c5 = Client(204, "Mihai")
    c6 = Client(205, "Tudor")
    c7 = Client(206, "Andreea")
    c8 = Client(207, "Cristine")
    c9 = Client(208, "Vale")
    c10 = Client(209, "Iulia")
    repoClient.addClient(c1)
    repoClient.addClient(c2)
    repoClient.addClient(c3)
    repoClient.addClient(c4)
    repoClient.addClient(c5)
    repoClient.addClient(c6)
    repoClient.addClient(c7)
    repoClient.addClient(c8)
    repoClient.addClient(c9)
    repoClient.addClient(c10)


def initialRentalList(repoRental):
    r1= Rental(300, 100, 201, date(2018, 8, 15), date(2018, 8, 25), None)
    r2 = Rental(301, 102, 202, date(2018, 8, 23), date(2018, 9, 1),  date(2018, 8, 30))
    r3 = Rental(302, 103, 203, date(2018, 9, 1), date(2018, 9, 8), None)
    r4 = Rental(303, 104, 205, date(2018, 9, 7), date(2018, 9, 14), date(2018, 8, 14))
    r5 = Rental(304, 105, 205, date(2018, 10, 1), date(2018, 10, 8),  date(2018, 10, 7))
    r6 = Rental(305, 102, 205, date(2018, 5, 1), date(2018, 5, 8),  date(2018, 10, 3))
    r7 = Rental(306, 106, 206, date(2018, 11, 1), date(2018, 12, 10),  None)
    r8 = Rental(307, 102, 204, date(2018, 1, 11), date(2018, 1, 21),  None)
    r9 = Rental(308, 104, 202, date(2018, 11, 5), date(2018, 12, 15),  None)
    r10 = Rental(309, 108, 209, date(2018, 11, 9), date(2018, 12, 19), None)

    repoRental.addRental(r1)
    repoRental.addRental(r2)
    repoRental.addRental(r3)
    repoRental.addRental(r4)
    repoRental.addRental(r5)
    repoRental.addRental(r6)
    repoRental.addRental(r7)
    repoRental.addRental(r8)
    repoRental.addRental(r9)
    repoRental.addRental(r10)


def readSettings():
    settings = {}
    f = open("settingsproperties", "r")
    tokens = f.read().split("\n")
    print(tokens)
    for token in tokens:
        t = token.split("=")
        if len(t) == 2:
            settings[t[0].strip()] = t[1].strip()
    return settings



def Start():
    settings = readSettings()

    repoBook = None
    repoClient = None
    repoRental = None

    if settings["repo_type"] == "memory":
        repoBook = BookRepository()
        repoClient = ClientRepository()
        repoRental = RentalRepository()
        initialBookList(repoBook)
        initialRentalList(repoRental)
        initialClientList(repoClient)

    elif settings["repo_type"] == "text":
        repoBook = BookTextFileRepo(settings["repo_fileb"])
        repoClient = ClientTextFileRepo(settings["repo_filec"])
        repoRental = RentalTextFileRepo(settings["repo_filer"])

    elif settings["repo_type"] == "pickle":
        p=settings["repo_fileb"].strip()
        repoBook = BookPickleFileRepo(p)
        repoClient = ClientPickleFileRepo(settings["repo_filec"])
        repoRental = RentalPickleFileRepo(settings["repo_filer"])



    valid = BookValidator()
    uc = UndoController()


    ctrlRental = RentalController(repoRental, repoBook, repoClient,uc)

    ctrlBook = BookController(valid, repoBook, ctrlRental,uc)
    uiBook = BookConsole(ctrlBook)


    repoRental = RentalRepository()
    initialRentalList(repoRental)

    uiRental = RentalConsole(ctrlRental)
    validatorc = ClientValidator()
    ctrlClient = ClientController(repoClient,validatorc, ctrlRental, uc)
    uiClient = ClientConsole(ctrlClient)

    uiBook.listBookUI()
    uiClient.listClientUI()
    uiRental.listRentalUI()


    PrintMenu()
    while True:
        option = int(input("Please enter your option: "))
        #print("hello!!")


        if option == 1:
            uiBook.addBookUI()
        elif option == 2:
            uiBook.removeBookUI()
        elif option == 3:
            uiBook.updateBookUI()
        elif option == 4:
            uiBook.listBookUI()
        elif option == 5:
            uiClient.addClientUI()
        elif option == 6:
            uiClient.removeClientUI()
        elif option == 7:
            uiClient.updateClientUI()
        elif option == 8:
            uiClient.listClientUI()
        elif option == 9:
            uiRental.addRentalUI()
        elif option == 10:
            uiRental.ReturnBookUI()
        elif option == 11:
            uiBook.searchBookUI()
        elif option == 12:
            uiClient.searchClientUI()
        elif option == 13:
            uiRental.listRentalUI()
        elif option == 14:
            uiRental.MostRentedBooksUI()
        elif option == 15:
            uiRental.MostActiveClientsUI()
        elif option == 16:
            uiRental.MostRentedAuthorUI()
        elif option == 17:
            uiRental.LateRentalsUI()
        elif option == 18:
            uiRental.removeRentalUI()
        elif option == 19:
            uc.undo()
        elif option == 20:
            uc.redo()
        elif option == 0:
            break

Start()

