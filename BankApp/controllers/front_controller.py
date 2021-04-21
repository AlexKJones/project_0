from BankApp.controllers import client_controller, home_controller


def route(app):
    # Calls all other other controllers
    client_controller.route(app)
    home_controller.route(app)
