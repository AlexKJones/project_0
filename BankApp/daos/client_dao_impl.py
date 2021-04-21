
from BankApp.exceptions.resource_not_found import ResourceNotFound
from BankApp.models.client import Client
from BankApp.util.db_connection import connection
from BankApp.daos.client_doa import ClientDAO


class ClientDAOImpl(ClientDAO):

    def create_client(self, client):
        sql = "INSERT INTO clients VALUES (DEFAULT,%s,%s,DEFAULT,NULL) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (client.name, client.account_zero, client.active))

        connection.commit()
        record = cursor.fetchone()

        new_client = Client(record[0], record[1], float(record[2]))
        return new_client

    def get_client(self, client_id):
        sql = "SELECT * FROM clients WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])

        record = cursor.fetchone()

        if record:
            return Client(record[0], record[1], float(record[2]))
        else:
            raise ResourceNotFound(f"Client with id: {client_id} - Not Found")

    def all_clients(self):
        sql = "SELECT * FROM clients"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        client_list = []

        for record in records:
            client = Client(record[0], record[1], float(record[2]))

            client_list.append(client.json())

        return client_list

    def update_client(self, change):
        sql = "UPDATE clients SET name=%s,account_zero=%s,active=%s WHERE id = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.name, change.account_zero, change.active, change.client_id))
        connection.commit()

        record = cursor.fetchone()

        new_client = Client(record[0], record[1], float(record[2]))
        return new_client

    def delete_client(self, client_id):
        sql = "DELETE FROM clients WHERE id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        connection.commit()


def _test():
    m_dao = ClientDAOImpl()
    clients = m_dao.all_clients()
    print(clients)

    print(m_dao.get_client(1))


if __name__ == '__main__':
    _test()
