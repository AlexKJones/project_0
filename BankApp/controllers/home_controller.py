from flask import request, jsonify

from BankApp.models.user import User
from BankApp.daos.user_dao_impl import UserDAOImpl as u_dao


def route(app):
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        return "Welcome to the bank!"

    @app.route("/users", methods=['POST'])
    def get_user():
        user = User.json_parse(request.json)
        # Bad practice here
        returned_user = u_dao.get_user(user)
        return jsonify(returned_user)
