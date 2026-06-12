import mysql.connector


class DBConnector:
    def __init__(self):
        self.milon = {
            "host": "127.0.0.1",
            "port": "3306",
            "user": "root",
            "database": "library"
        }
        self.connection = None
        self.cursor = None
    
    def connct(self):
        self.connection = mysql.connector.connect(self.milon)
        self.cursor = self.connection.cursor(dictionary=True)
        