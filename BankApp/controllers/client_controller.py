from flask import jsonify, request
from werkzeug.exceptions import abort

from BankApp.exceptions.resource_not_found import ResourceNotFound
from BankApp.exceptions.resource_unavailable import ResourceUnavailable
from BankApp.models.client import Client
from BankApp.services.client_service import ClientService


def route(app):
    @app.route("/clients", methods=['GET'])
    def get_all_clients():
        return jsonify(ClientService.all_clients()), 200

    @app.route("/clients/<client_id>", methods=['GET'])
    def get_client(client_id):
        try:
            client = ClientService.get_client_by_id(int(client_id))
            return jsonify(client.json()), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/clients/search", methods=['GET'])
    def get_client_above_amount():
        account_zero = request.args["account_zero"]
        print(account_zero)
        clients = ClientService.get_client_above_amount(float(account_zero))
        return jsonify(clients)

    @app.route("/clients", methods=["POST"])
    def post_client():
        client = Client.json_parse(request.json)
        client = ClientService.create_client(client)
        return jsonify(client.json()), 201

    @app.route("/clients/<client_id>", methods=["PUT"])
    def put_client(client_id):
        client = Client.json_parse(request.json)
        client.client_id = int(client_id)
        client = ClientService.update_client(client)
        return jsonify(client.json()), 200

    @app.route("/clients/<client_id>", methods=["DELETE"])
    def del_client(client_id):
        ClientService.delete_client(int(client_id))
        return '', 204

    @app.route("/clients/<client_id>", methods=["PATCH"])
    def patch_client(client_id):
        action = request.json['action']

        if action == 'activate' or action == 'deactivate':
            try:
                title = ClientService.deactivate_client(
                    int(client_id)) if action == 'deactivate' else ClientService.activate_client((int(client_id)))
                return f"Successfully set activation to {'active' if action == 'activate' else 'inactive'} client: {name}", 200
            except ResourceUnavailable as e:
                return e.message, 422
        else:
            abort(400, "Body must contain a JSON with an action property and values of activate or deactivate")
