from abc import abstractmethod, ABC

class ClientDAO(ABC):

    @staticmethod
    def create_client(self, client):
        pass

    @staticmethod
    def get_client(self, client_id):
        pass

    @staticmethod
    def all_clients(self):
        pass

    @staticmethod
    def update_client(self, change):
        pass

    @staticmethod
    def delete_client(self, client_id):
        pass
