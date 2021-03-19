# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from io import BytesIO
from PIL import Image
import json
from xstock.factories import UserFactory, EspecieFactory, EspecieParcelaFactory, \
MedicionFactory, MedicionOpcionFactory, OpcionFactory, ParcelaFactory, \
PredioFactory, PreguntaFactory, RodalFactory, SubTipoForestalFactory, \
SuscriptorFactory, TipoForestalFactory
from account.factories import UserAccountFactory, RoleFactory
from django.urls import reverse
from django.db.models import Q
from django.test.utils import override_settings
from rest_framework.test import APITestCase, APIClient
from django.conf import settings
from account.data import GENDER_OPTIONS, USER_TYPES
from account.bl.recaptcha import RECAPTCHA_TEST
from account.models import User, Role
from django.core.files.base import File
import os


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage',
    EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend',
    MEDIA_ROOT='/app/test_media/',
    ENVIRONMENT='UNIT_TESTING'
)
class AccountTest(APITestCase):

    fixtures = []

    @staticmethod
    def get_image_file(name, ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def setUp(self):
        ''' Check coverage
            coverage3 run --source='.' backend/manage.py test account
        '''
        self.user = UserFactory(username='test@xstock.com', email='test@xstock.com')
        self.user1 = UserAccountFactory(
            username='drigox90rih@gmail.com',
            email='drigox90rih@gmail.com'
        )
        self.role = RoleFactory(name='xstock_publico')
        self.user.set_password('pass')
        self.user.save()
        self.user1.set_password('pass1')
        self.user1.save()
        self.client.login(username='test@xstock.com', password='pass')
        self.client = APIClient()

    def test_api_user_get_correct(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_user_get_correct
        '''
        url = reverse('account:users', kwargs={'pk': self.user.pk})
        self.client.force_authenticate(self.user)
        response = self.client.get(
            url,
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(200, response.status_code)
        self.assertEquals('test@xstock.com', data.get('username'))
        self.assertEquals('test@xstock.com', data.get('email'))

    def test_api_get_user(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_get_user
        '''
        url = reverse('account:users', kwargs={'pk': 0})
        self.client.force_authenticate(self.user)
        response = self.client.get(
            url,
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals('test@xstock.com', data.get('username'))
        self.assertEquals('test@xstock.com', data.get('email'))
        self.assertEquals(1, data.get('gender'))
        self.assertEquals(1, data.get('user_type'))
        self.assertEquals(False, data.get('email_validated'))
        self.assertEquals('John2', data.get('first_name'))
        self.assertEquals('Doe2', data.get('last_name'))

    def test_api_user_get_not_found(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_user_get_not_found
        '''
        url = reverse('account:users', kwargs={'pk': 9999})
        self.client.force_authenticate(self.user)
        response = self.client.get(
            url,
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(404, response.status_code)
        self.assertEquals('No encontrado.', data.get('detail'))

    def test_api_account_put_profile(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_account_put_profile
        '''
        url = reverse('account:account_profile')
        self.client.force_authenticate(self.user)
        payload = {
            'first_name': 'Roderick',
            'last_name': 'Godrick',
            'gender': GENDER_OPTIONS[0][0],
            'user_type': USER_TYPES[0][0],
        }
        response = self.client.put(
            f'{url}?type=profile',
            json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(200, response.status_code)
        self.assertEquals('Roderick', data.get('first_name'))
        self.assertEquals('Godrick', data.get('last_name'))
        self.assertEquals(GENDER_OPTIONS[0][0], data.get('gender'))

    def test_api_account_put_password(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_account_put_password
        '''
        url = reverse('account:account_profile')
        self.client.force_authenticate(self.user)
        response = self.client.put(
            f'{url}?type=password',
            json.dumps({
                'password': '43215756'
            }),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(200, response.status_code)
        self.assertEquals('test@xstock.com', data.get('username'))
        result = self.client.login(username='test@xstock.com', password='43215756')
        self.assertTrue(result)

    def test_api_account_put_validate(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_account_put_validate
        '''
        url = reverse('account:account_profile')
        self.user.set_password('pass_valid')
        self.client.login(username='johny2', password='pass_valid_err')
        self.client.force_authenticate(self.user)
        response = self.client.put(
            f'{url}?type=validate',
            json.dumps({
                'password': 'pass_valid'
            }),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(200, response.status_code)
        self.assertEquals(False, data.get('result'))  # TODO: check true

    def test_api_account_validate_email_get(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_account_validate_email_get
        '''

        url = reverse('account:account_validation', kwargs={
            'pk': self.user1.pk,
            'token': self.user1.token_email
        })
        response = self.client.get(
            url,
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(200, response.status_code)
        self.assertEquals(self.user1.email, data.get('email'))
        self.assertEquals(True, data.get('email_validated'))

    def test_api_account_post_creation(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_account_post_creation
        '''
        url = reverse('account:account_creation')
        email = 'drigox90rih@gmail.com'  # test@xstock.new
        response = self.client.post(
            url,
            json.dumps({
                'email': email,
                'first_name': 'Rod',
                'last_name': 'Gar',
                'password': 'pass_valid',
                'user_type': USER_TYPES[1][0],
                'gender': GENDER_OPTIONS[1][0],
            }),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(201, response.status_code)
        self.assertEquals(email, data.get('username'))
        self.assertEquals(email, data.get('email'))
        self.assertEquals('Rod', data.get('first_name'))
        self.assertEquals('Gar', data.get('last_name'))
        self.assertEquals(USER_TYPES[1][0], data.get('user_type'))
        self.assertEquals(GENDER_OPTIONS[1][0], data.get('gender'))
        user = User.objects.get(email='drigox90rih@gmail.com')
        roles = [g.name for g in user.groups.all()]
        self.assertIn('xstock_publico', roles)

    def test_api_account_post_recovery(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_account_post_recovery
        '''
        url = reverse('account:account_recovery_request')
        response = self.client.post(
            url,
            json.dumps({
                'email': self.user1.email,
                'origin': settings.VISOR_APP,
                'recaptchaToken': RECAPTCHA_TEST
            }),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(self.user1.email, data.get('email'))
        self.assertEquals(True, data.get('recovery_request'))

    def test_api_account_put_recovery(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_account_put_recovery
        '''

        url = reverse('account:account_recovery', kwargs={
            'pk': self.user1.pk,
            'token': self.user1.token_recovery
        })
        response = self.client.put(
            url,
            json.dumps({
                'password': '123454321',
                'recaptchaToken': RECAPTCHA_TEST
            }),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals('drigox90rih@gmail.com', data.get('username'))
