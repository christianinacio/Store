import sqlite3
from sqlite3 import Error

# from .connection import create_connection

def read_file(path):
    with open(path, "r") as sql_file:
        return sql_file.read()

# def create_tables():
#     conn = create_connection()
#     path = "database/sql/table.sql"
#     with open(path, "r") as sql_file:
#         sql = sql_file.read()

#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         conn.commit()
#         return True
#     except Error as e:
#         print("Error create table")
#     finally:
#         if conn:
#             cur.close()
#             conn.close()