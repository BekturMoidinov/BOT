import sqlite3
from database import query

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()
    def create_table_answer(self):
        if self.connection:
            print("Db answers connected successfully")
        self.connection.execute(query.CREATE_ANSWER_TABLE)
        self.connection.commit()
    def create_table(self):
        if self.connection:
            print("Db  connected successfully")
        self.connection.execute(query.CREATE_USER_TABLE)
        self.connection.commit()
    def insert_user(self,telegram_id,username,first_name,last_name):
        self.cursor.execute(query.INSERT_USER_TABLE, (None,telegram_id,username,first_name,last_name))
        self.connection.commit()
    def insert_answer(self,telegram_id,type,model,exp):
        self.cursor.execute(query.INSERT_ANSWER_TABLE, (None,telegram_id,type,model,exp))
        self.connection.commit()