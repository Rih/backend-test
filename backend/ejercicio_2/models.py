from django.db import models
from api.models import Apimodel
# Create your models here.


class Company(Apimodel):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10)
    dv = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    year_constitution = models.CharField(max_length=4)
    address = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=30)

    def get_full_rut(self):
        return str(self.rut) + '-' + str(self.dv)
