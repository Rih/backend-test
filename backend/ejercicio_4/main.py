# -*- coding: utf-8 -*-
try:
    from delivery import Delivery
except ModuleNotFoundError:
    from ejercicio_4.delivery import Delivery


if __name__ == '__main__':
    print(f"\n*********************************************")
    print(f"Executing exercise 3. ")
    print(f"First you'll be asked to name a table into enviame.db SQLite")
    print(f"If it's not created tell me")

    name_your_table = input('The name of the table?: ')
    delivery = Delivery(table=name_your_table)
    exists = input('Do you need to create the table first? (y/n): ')
    if exists.lower().index('y') != -1 or exists.lower().index('yes') != -1:
        delivery.create_db()
    print('Creating delivery! please wait...')
    delivery.create('BLX')
    print("You can see the result of api rest in backend/enviame.db")
    print("with your preferred DB browser.")
