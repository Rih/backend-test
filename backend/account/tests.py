# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from account.factories import UserAccountFactory
from django.urls import reverse
from django.db.models import Q
from django.test.utils import override_settings
from rest_framework.test import APITestCase, APIClient
from django.conf import settings
from account.models import User


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage',
    EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend',
    MEDIA_ROOT='/app/test_media/',
    ENVIRONMENT='UNIT_TESTING'
)
class AccountTest(APITestCase):

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
        self.client.login(username='test@test.com', password='pass')
        self.client = APIClient()

    def test_api_login_user(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_login_user
        '''
        url = reverse('token_obtain_pair')
        payload = {
            'email': 'test@test.com',
            'password': 'pass',
        }
        response = self.client.post(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertTrue('access' in data)
        self.assertTrue('refresh' in data)

    def test_api_get_user(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_get_user
        '''
        url = reverse('api:users', kwargs={'pk': self.user.pk})
        self.client.force_authenticate(self.user)
        response = self.client.get(
            url,
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals('test@test.com', data.get('username'))
        self.assertEquals('test@test.com', data.get('email'))
        self.assertEquals('John', data.get('first_name'))
        self.assertEquals('Doe', data.get('last_name'))
