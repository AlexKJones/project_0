import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
        conn = psycopg2.connect(
            database='postgres',
            user='alex',
            password='o50egunl',
            host='database-1.c4mxfnlldiel.us-east-2.rds.amazonaws.com',
            port='5432'
        )
        return conn
    except OperationalError as e:
        print(f"{e}")
        return conn


connection = create_connection()
