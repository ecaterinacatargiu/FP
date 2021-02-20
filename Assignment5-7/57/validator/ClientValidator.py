from domain.Client import Client

class ClientValidator:

    def validID(self, ID):
        #NZZ
        if len(ID) != 3:
            return False
        for i in ID:
            if i < '0' or i > '9':
                return False
        return True

    def validate(self, client):
        """Validate if provided Client instance is valid
        client - Instance of Client type
        Return List of validation errors. An empty list if instance is valid."""
        if isinstance(client, Client) == False:
            raise TypeError("Inexisting client!")
        errors = []
        if self.validID(client.clientID) == False:
            errors.append("Invalid ID!")
        if len(client.name) == 0:
            errors.append("Invalid name!")
        if len(errors) != 0:
            raise ValueError(errors)