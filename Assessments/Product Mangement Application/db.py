import mysql.connector

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',  # Put your MySQL password if any
                database='product_management'
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print("Connection error:", err)

    def execute(self, query, values=None):
        try:
            self.cursor.execute(query, values or ())
            self.conn.commit()
            return self.cursor
        except mysql.connector.Error as err:
            print("Execution error:", err)
            return None

    def fetchall(self):
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.conn.close()


'''ALTER TABLE users 
ADD COLUMN can_manage_stock BOOLEAN DEFAULT NULL,
ADD COLUMN can_view_stock BOOLEAN DEFAULT NULL;'''