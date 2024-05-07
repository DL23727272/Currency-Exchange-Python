import uuid
import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="currency_db"
        )
        self.cursor = self.connection.cursor()

    
    def signup(self, username, password):
        try:
            insert_user_query = "INSERT INTO users(username, password) VALUES(%s, %s)"
            self.cursor.execute(insert_user_query, (username, password))
            self.connection.commit()
            return True
        except mysql.connector.IntegrityError:
            return False

        
    def check_user(self, username, password):
        check_user_query = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(check_user_query, (username, password))
        user = self.cursor.fetchone()
        if user:
            return True
        else:
            return False
    def insert_conversion(self, from_currency, to_currency, amount, result):
        try:
            insert_query = "INSERT INTO conversion_history (from_currency, to_currency, amount, result) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(insert_query, (from_currency, to_currency, amount, result))
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print("Error inserting conversion:", err)
            return False
    def close_db_connection(self):
         self.con.close()
