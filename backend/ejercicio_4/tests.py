# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import SimpleTestCase
import json
from ejercicio_4.connection import ConnectDB
from ejercicio_4.delivery import DeliveryJob
from django.test.utils import override_settings

# Create your tests here.

@override_settings(
    ENVIRONMENT='UNIT_TESTING'
)
class Ejercicio04Test(SimpleTestCase):

    fixtures = ['usuario']

    def setUp(self):
        ''' Check coverage
            coverage3 run --source='.' manage.py test account
        '''

    def test_create_delivery(self):
        # python3.7 manage.py test ejercicio_4.tests.Ejercicio04Test.test_create_delivery
        job = DeliveryJob()
        result = job.create_delivery('123', '1234')
        print(result)
        self.assertEquals(422, result['status'])

    def test_connection_create(self):
        # python3.7 manage.py test ejercicio_4.tests.Ejercicio04Test.test_connection_create
        conn = ConnectDB(table='other').create_table()

    def test_connection_insert(self):
        # python3.7 manage.py test ejercicio_4.tests.Ejercicio04Test.test_connection_insert
        conn = ConnectDB(table='other').insert('asdf')

    def test_connection_select(self):
        # python3.7 manage.py test ejercicio_4.tests.Ejercicio04Test.test_connection_select
        conn = ConnectDB(table='person').select()
