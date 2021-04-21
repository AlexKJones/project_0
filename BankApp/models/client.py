class Client:

    def __init__(self, client_id=0, name="", accounts="", account_zero=0, active=True):
        self.client_id = client_id
        self.name = name
        self.accounts = accounts
        self.account_zero = account_zero
        self.active = active

    def json(self):
        return {
            'clientId': self.client_id,
            'name': self.name,
            'accounts': self.accounts,
            'account_zero': self.account_zero,
            'active': self.active
        }

    @staticmethod
    def json_parse(json):
        client = Client()
        client.client_id = json["clientId"] if "clientId" in json else 0
        client.name = json["name"]
        client.accounts = json["accounts"]
        client.account_zero = json["account_zero"]
        client.active = json["active"] if "active" in json else True

        return client

    def __repr__(self):
        return str(self.json())
