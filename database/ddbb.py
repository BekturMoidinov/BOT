import sqlite3
from database import query

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()
    def create_table(self):
        if self.connection:
            print("Db  connected successfully")
        self.connection.execute(query.CREATE_USER_TABLE)
        self.connection.execute(query.CREATE_ANSWER_TABLE)
        self.connection.execute(query.CREATE_BAN_TABLE)
        self.connection.commit()
    def insert_user(self,telegram_id,username,first_name,last_name):
        self.cursor.execute(query.INSERT_USER_TABLE, (None,telegram_id,username,first_name,last_name))
        self.connection.commit()
    def insert_answer(self,telegram_id,name,type,model,exp):
        self.cursor.execute(query.INSERT_ANSWER_TABLE, (None,telegram_id,name,type,model,exp))
        self.connection.commit()
    def inseert_ban(self,tg_id,first_name):
        self.cursor.execute(query.INSERT_BAN_TABLE, (None,tg_id,first_name,0))
        self.connection.commit()
    def select_count_bun_table(self,tg_id):
        self.cursor.execute(query.SELECT_BAN_TABLE_COUNT, (tg_id,))
        return self.cursor.fetchone()
    def update_count_bun_table(self,tg_id):
        self.cursor.execute(query.UPDATE_BAN_TABLE_COUNT,(tg_id,))
        self.connection.commit()
    def delete_user(self,tg_id):
        self.cursor.execute(query.DELETE_USER,(tg_id,))
        self.connection.commit()
    def select_user(self):
        self.cursor.execute(query.SELECT_FROM_USER_TABLE)
        rows = self.cursor.fetchall()
        return rows
    def seletc_from_ban(self):
        self.cursor.execute(query.SELECT_USER_FROM_BAN)
        rows = self.cursor.fetchall()
        return rows
    def select_user_answer(self,tg_id):
        self.cursor.execute(query.SELECT_USER_FROM_ANSWER,(tg_id,))
        row = self.cursor.fetchone()
        return row
    def select_all_user_answer(self):
        self.cursor.execute(query.SELECT_ANSWER_TABLE)
        rows = self.cursor.fetchall()
        return rows
    def update_user_answer(self,transport_type,model,experience,telegram_user_id):
        self.cursor.execute(query.UPDATE_ANSWER_TABLE,(transport_type,model,experience,telegram_user_id))
        self.connection.commit()
    def select_all_id_answer(self):
        self.cursor.execute(query.SELECT_ALL_ID_ANSWER)
        rows = self.cursor.fetchall()
        return rows