# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from account.factories import UserAccountFactory
from ejercicio_2.factories import CompanyFactory
from ejercicio_2.models import Company
from django.urls import reverse
from django.db.models import Q
from django.test.utils import override_settings
from rest_framework.test import APITestCase, APIClient
from django.conf import settings


@override_settings(
    ENVIRONMENT='UNIT_TESTING'
)
class Ejercicio02Test(APITestCase):

    fixtures = ['usuario']

    def setUp(self):
        ''' Check coverage
            coverage3 run --source='.' manage.py test account
        '''
        self.user = UserAccountFactory(
            username='test@test.com',
            email='test@test.com'
        )
        self.user.set_password('pass')
        self.user.save()
        self.batch_size = 10
        self.companies = CompanyFactory.create_batch(size=self.batch_size)
        self.client.login(username='test@test.com', password='pass')
        self.client = APIClient()

    def test_api_fake_companies(self):
        '''
       python3 manage.py test ejercicio_2.tests.Ejercicio02Test.test_api_fake_companies
       '''
        url = reverse('api:company_faker')
        length = 20
        payload = {
            'batch_number': length
        }
        self.client.force_authenticate(self.user)
        response = self.client.post(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(length, len(data))

    def test_api_get_companies(self):
        '''
        python3 manage.py test ejercicio_2.tests.Ejercicio02Test.test_api_get_companies
        '''
        url = reverse('api:companies')
        self.client.force_authenticate(self.user)
        response = self.client.get(
            url,
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(self.batch_size, len(data))

    def test_api_post_company(self):
        '''
        python3 manage.py test ejercicio_2.tests.Ejercicio02Test.test_api_post_company
        '''
        url = reverse('api:companies')
        self.client.force_authenticate(self.user)
        # success
        payload = {
            'name': 'Compañia',
            'rut': '15915915',
            'dv': '9',
            'year_constitution': '2020',
            'address': 'Calle #123',
            'contact_phone': '55554321'
        }
        response = self.client.post(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.content)
        payload.update({'estado': Company.ACTIVE})
        self.assertEquals(response.status_code, 201)
        self.assertTrue(data['id'] > 0)
        del data['created']
        del data['last_modified']
        del data['id']
        self.assertDictEqual(data, payload)
        # failed
        del payload['name']
        response = self.client.post(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 400)
        self.assertDictEqual({'name': ['Este campo es requerido.']}, data)

    def test_api_put_company(self):
        '''
        python3 manage.py test ejercicio_2.tests.Ejercicio02Test.test_api_put_company
        '''
        url = reverse('api:company', kwargs={
            'pk': self.companies[0].pk
        })
        self.client.force_authenticate(self.user)
        # success
        payload = {
            'name': 'Compania 22',
            'rut': '15915915',
            'dv': '9',
            'year_constitution': '2021',
            'address': 'Calle #321',
            'contact_phone': '55554321',
        }
        response = self.client.put(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 201)
        self.assertDictEqual(data, payload)

        # failed
        del payload['name']
        response = self.client.put(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 400)
        self.assertDictEqual({'name': ['Este campo es requerido.']}, data)

    def test_api_patch_company(self):
        '''
        python3 manage.py test ejercicio_2.tests.Ejercicio02Test.test_api_patch_company
        '''
        url = reverse('api:company', kwargs={
            'pk': self.companies[1].pk
        })
        self.client.force_authenticate(self.user)
        # success
        payload = {
            'name': 'Compañia 23',
            'rut': '15915915',
        }
        response = self.client.patch(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        self.assertEquals(response.status_code, 206)
        data = json.loads(response.content)
        print(data)
        self.assertEquals(data['name'], payload['name'])
        self.assertEquals(data['rut'], payload['rut'])

        # empty
        response = self.client.patch(
            url,
            json.dumps({}),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 206)

    def test_api_delete_company(self):
        '''
        python3 manage.py test ejercicio_2.tests.Ejercicio02Test.test_api_delete_company
        '''
        url = reverse('api:company', kwargs={
            'pk': self.companies[2].pk
        })
        self.client.force_authenticate(self.user)
        # success
        response = self.client.delete(
            url,
            content_type='application/json'
        )
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEquals(data['estado'], Company.DELETE)
        self.assertTrue(data['id'] > 0)

        url = reverse('api:company', kwargs={
            'pk': 999
        })
        self.client.force_authenticate(self.user)
        # failed
        response = self.client.delete(
            url,
            content_type='application/json'
        )
        self.assertEquals(response.status_code, 400)
        data = json.loads(response.content)
        self.assertDictEqual({'id': ['Registro no encontrado']}, data)
