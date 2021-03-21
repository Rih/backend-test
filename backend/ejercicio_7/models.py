from django.db import models
# Create your models here.


class Continents(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    anual_adjustment = models.IntegerField(default=0)

    class Meta:
        db_table = 'continents'


class Countries(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    continent = models.ForeignKey(Continents, on_delete=models.CASCADE)

    class Meta:
        db_table = 'countries'


class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    salary = models.IntegerField(default=0)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employees'
