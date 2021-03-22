# -*- coding: utf-8 -*-
try:
    from connection import ConnectDB
    from api import DeliveryAPI
except ModuleNotFoundError:
    from ejercicio_4.connection import ConnectDB
    from ejercicio_4.api import DeliveryAPI


class Delivery:

    def __init__(self, table):
        self.ws = DeliveryAPI()
        self.db = ConnectDB(table=table)

    # run once
    def create_db(self):
        self.db.create_table()
        print('Done.')
        return True

    def create(self, code):
        result = self.ws.create_delivery(code)
        affected = self.db.insert(result)
        print('Done.')
        return True if affected > 0 else False
