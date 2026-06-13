import mysql.connector


class DBConnector:
    def __init__(self):
        self.milon = {
            "host": "127.0.0.1",
            "port": "3306",
            "password": "1234",
            "user": "root",
            "database": "library_db"
        }
        self.connection = None
        self.cursor = None
    
    def connct(self):
        self.connection = mysql.connector.connect(**self.milon)
        self.cursor = self.connection.cursor(dictionary=True)


    def create_tables(self):
        self.cursor.execute("""create table books(id int auto_increment primary key,
                            title varchar(50) not null, 
                            author varchar(50) not null,
                            genre enum('fiction', 'non-fiction', 'science', 'history', 'other') not null, 
                            is_available boolean not null default TRUE, 
                            borrowed_by_member_id int)""")
    
        self.cursor.execute("""create table members(id int auto_increment primary key,
                            name varchar(50) not null,
                            email varchar(100) unique not null,
                            is_active boolean not null default FALSE,
                            total_borrows int not null default 0)""")


d1 = DBConnector()
d1.connct()
d1.create_tables()