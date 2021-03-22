# -*- coding: utf-8 -*-
import sqlite3
import json
import random


class ConnectDB:

    def __init__(self, **kwargs):
        self.table = kwargs.get('table', 'person')
        self.db_mapping = [
            {'db_name': 'id', 'json': False},
            {'db_name': 'identifier', 'json': 'identifier'},
            {'db_name': 'imported_id', 'json': 'imported_id'},
            {'db_name': 'tracking_number', 'json': 'tracking_number'},
            {'db_name': 'status__name', 'json': {'status': 'name'}},
            {'db_name': 'status___code', 'json': {'status': 'code'}},
            {'db_name': 'customer__email', 'json': {'customer': 'email'}},
            {'db_name': 'country', 'json': 'country'},
            {'db_name': 'carrier', 'json': 'carrier'},
            {'db_name': 'service', 'json': 'service'},
            {'db_name': 'label__PDF', 'json': {'label': 'PDF'}},
            {'db_name': 'deadline_at', 'json': 'deadline_at'},
            {'db_name': 'payload', 'json': True},
        ]

    def create_table(self):
        try:
            sqlite_conn = sqlite3.connect('enviame.db')
            print("Successfully Connected to SQLite")
            cursor = sqlite_conn.cursor()
            columns = ','.join(list(map(lambda x: f'{x["db_name"]} TEXT NOT NULL', self.db_mapping[1:])))
            sqlite_create_query = """CREATE TABLE """ + self.table + """
                                  (id INTEGER PRIMARY KEY, """ + columns + """); """
            count = cursor.execute(sqlite_create_query)
            sqlite_conn.commit()
            print(f"Successfully created {self.table} table")
            cursor.close()
            return True
        except sqlite3.Error as error:
            print("Failed to use sqlite table", error)
        finally:
            if sqlite_conn:
                sqlite_conn.close()
                print("The SQLite connection is closed")
        return False

    def insert_handler(self, result):
        db_names = []
        db_values = []
        input = result['data']['data']
        for m in self.db_mapping:
            if isinstance(m['json'], str):
                db_names.append(m['db_name'])
                val = '\'' + str(input[m['json']]) + '\''
            if isinstance(m['json'], dict):
                key, value = next(iter(m['json'].items()))
                db_names.append(m['db_name'])
                val = '\'' + str(input[key][value]) + '\''
            if isinstance(m['json'], bool):
                db_names.append(m['db_name'])
                if m['json']:
                    val = '\'' + json.dumps(result) + '\''
                else:
                    # its pk
                    val = str(random.randint(0, 9999999))
            db_values.append(val)
        names = ','.join(db_names)
        values = ','.join(db_values)
        return f'({names})', f'({values})'

    def insert(self, result):
        affected = 0
        try:
            sqlite_conn = sqlite3.connect('enviame.db')
            print("Successfully Connected to SQLite")
            cursor = sqlite_conn.cursor()
            keys, values = self.insert_handler(result)
            sqlite_insert_query = """INSERT INTO """ + self.table + """
                                  """ + keys + """ VALUES """ + values +""";"""
            count = cursor.execute(sqlite_insert_query)
            sqlite_conn.commit()
            affected = cursor.rowcount
            print(f"Record inserted successfully into {self.table} table {affected} affected")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to use sqlite table", error)
        finally:
            if sqlite_conn:
                sqlite_conn.close()
                print("The SQLite connection is closed")
        return affected
