from BankApp.models.user import User
from BankApp.util.db_connection import connection


class UserDAOImpl:

    @staticmethod
    def get_user(user: User):
        sql = "SELECT * FROM users WHERE username = '" + user.username + "' and password = '" + user.password + "'"

        cursor = connection.cursor()
        cursor.execute(sql)

        connection.commit()

        record = cursor.fetchone()

        user = User(record[0], record[1])

        return user.__dict__

