from BankApp.daos.client_dao_impl import ClientDAOImpl
from time import time
from BankApp.exceptions.resource_unavailable import ResourceUnavailable


class ClientService:
    client_dao = ClientDAOImpl()

    @classmethod
    def create_client(cls, client):
        return cls.client_dao.create_client(client)

    @classmethod
    def all_clients(cls):
        return cls.client_dao.all_clients()

    @classmethod
    def get_client_by_id(cls, client_id):
        return cls.client_dao.get_client(client_id)

    @classmethod
    def get_client_above_amount(cls, account_zero):
        clients = cls.all_clients()

        refined_search = []

        for client in clients:
            if client["account_zero"] >= account_zero:
                refined_search.append(client)

        return refined_search

    @classmethod
    def update_client(cls, client):
        # We should probably test that the client_id exists in teh DB first. And throw ResourceNotFound if so.
        return cls.client_dao.update_client(client)

    @classmethod
    def delete_client(cls, client_id):
        return cls.client_dao.delete_client(client_id)

    @classmethod
    def checkout_client(cls, client_id):
        client = cls.client_dao.get_client(client_id)
        if client.active:
            client.active = False
            client.return_date = int(time() + 604800)
            cls.update_client(client)
            return client.name
        else:
            raise ResourceUnavailable(f"Account is innactive. Expected return: {client.return_date}")

    @classmethod
    def activate_client(cls, client_id):
        client = cls.client_dao.get_client(client_id)
        if not client.active:
            client.active = True
            client.return_date = 0
            cls.update_client(client)
            return client.name
        else:
            raise ResourceUnavailable(f"Account is active. Cannot be activated.")
