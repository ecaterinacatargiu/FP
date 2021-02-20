import unittest
from domain.Client import Client
from validator.ClientValidator import ClientValidator
from repository.ClientRepository import ClientRepository

class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self._clientID=344
        self._Name="Ana"
        self._client = Client(344, "Ana")
        self._validator = ClientValidator()

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_Model(self):
        self.assertEqual(self._client.getClientID, self._clientID)
        self.assertEqual(self._client.getName, self._Name)


    """def test_Repo(self):
        self.assertEqual(len(self.__ClientRepository),0)
        self._newclient1 = Client(556, "Maria")
        self._newclient2 = Client(556, "Maria")
        self._newclient3 = Client(556, "Maria")

        try:
            self._ClientRepository.addClient(self._newclient1)
            assert len(self._ClientRepository) == 1
            self._ClientRepository.addClient(self._newClient2)
            self._ClientRepository.addClient(self.newClient3)
            assert False
        except:
            assert str(re) == "Student ID already taken"""
