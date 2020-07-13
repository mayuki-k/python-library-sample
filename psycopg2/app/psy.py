import psycopg2
from psycopg2.extras import DictCursor
from env import const

def get_connection():
    dsn = const.DATABASE_URL
    return psycopg2.connect(dsn)

def create_table():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('CREATE TABLE fruits(id INTEGER, name TEXT, price INTEGER)')

def insert_data(id, name, price):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO fruits(id, name, price)VALUES(%s, %s, %s)', (id, name, price,))


def get_datas():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM fruits')
            rows = cursor.fetchall()
            print(rows)

def get_datas_with_column():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM fruits')
            rows = cursor.fetchall()
            col_names = [col.name for col in cursor.description]
            print(col_names)
            print(rows)


get_datas_with_column()

