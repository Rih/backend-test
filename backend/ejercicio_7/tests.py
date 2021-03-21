# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from account.factories import UserAccountFactory
from ejercicio_7.models import Countries, Continents, Employees
from django.urls import reverse
from django.test.utils import override_settings
from rest_framework.test import APITestCase, APIClient
from django.conf import settings


@override_settings(
    ENVIRONMENT='UNIT_TESTING'
)
class Ejercicio07Test(APITestCase):

    fixtures = ['continents', 'countries', 'employees']

    def setUp(self):
        ''' Check coverage
            coverage3 run --source='.' manage.py test ejercicio_7
        '''
        pass

    def test_api_select_employees(self):
        # python3.7 manage.py test ejercicio_7.tests.Ejercicio07Test.test_api_select_employees
        employees = Employees.objects.all()
        continents = Continents.objects.all()
        countries = Countries.objects.all()
        employee_5000 = Employees.objects.filter(
            salary__lte=5000
        )
        self.assertTrue(len(employees) > 0)
        self.assertTrue(len(employee_5000) > 0)
        self.assertTrue(len(continents) > 0)
        self.assertTrue(len(countries) > 0)

