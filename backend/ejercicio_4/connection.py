import sqlite3


class ConnectDB:

    def __init__(self, **kwargs):
        self.table = kwargs.get('table', 'person')

    def create_table(self):
        try:
            sqlite_conn = sqlite3.connect('enviame.db')
            print("Successfully Connected to SQLite")
            cursor = sqlite_conn.cursor()
            sqlite_create_query = """CREATE TABLE """ + self.table + """
                                  (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
                                  """
            count = cursor.execute(sqlite_create_query)
            sqlite_conn.commit()
            print(f"Successfully created {self.table} table")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to use sqlite table", error)
        finally:
            if sqlite_conn:
                sqlite_conn.close()
                print("The SQLite connection is closed")

    def insert(self, name):
        try:
            sqlite_conn = sqlite3.connect('enviame.db')
            print("Successfully Connected to SQLite")
            cursor = sqlite_conn.cursor()
            sqlite_insert_query = """INSERT INTO """ + self.table + """
                                  (id, name)
                                   VALUES
                                  (2,'"""+ name +"""')"""

            count = cursor.execute(sqlite_insert_query)
            sqlite_conn.commit()
            print(f"Record inserted successfully into {self.table} table {cursor.rowcount} affected")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to use sqlite table", error)
        finally:
            if sqlite_conn:
                sqlite_conn.close()
                print("The SQLite connection is closed")

    def select(self):
        try:
            sqlite_conn = sqlite3.connect('enviame.db')
            print("Successfully Connected to SQLite")
            cursor = sqlite_conn.cursor()
            sqlite_select_query = """SELECT * FROM """+ self.table + """;"""
            cursor.execute(sqlite_select_query)
            result = cursor.fetchall()
            print("Record fetched successfully into person table ", cursor.rowcount)
            cursor.close()
            return result


        except sqlite3.Error as error:
            print("Failed to use sqlite table", error)
        finally:
            if sqlite_conn:
                sqlite_conn.close()
                print("The SQLite connection is closed")


if __name__ == '__main__':
    conn = ConnectDB().create_table_person()

