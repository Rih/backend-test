from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from account.managers import UserManager
from django.core.mail import send_mail
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(_('username'), unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(
        _('first name'),
        max_length=50,
        blank=False,
        null=False,
        default='nombre'
    )
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is staff'), default=False)
    is_superuser = models.BooleanField(_('is superuser'), default=False)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        # 'first_name',
        # 'email'
    ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Company(models.Model):
    rut = models.IntegerField()
    dv = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    year_constitution = models.CharField(max_length=4)
    address = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=30)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_full_rut(self):
        return str(self.rut) + '-' + str(self.dv)
