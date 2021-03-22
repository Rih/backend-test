# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import SimpleTestCase
import json
from ejercicio_4.connection import ConnectDB
from ejercicio_4.delivery import Delivery
from ejercicio_4.mock_api import result_api
from django.test.utils import override_settings

# Create your tests here.

@override_settings(
    ENVIRONMENT='UNIT_TESTING'
)
class Ejercicio04Test(SimpleTestCase):

    fixtures = ['usuario']

    def setUp(self):
        ''' Check coverage
            coverage3 run --source='.' manage.py test ejercicio_4
        '''

    def test_connection_insert_handler(self):
        # python3 manage.py test ejercicio_4.tests.Ejercicio04Test.test_connection_insert_handler
        result = ConnectDB(table='person').insert_handler(result_api)
        print(result)
