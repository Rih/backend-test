from ejercicio_2.models import Company
from rest_framework import serializers


class CompanyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class CompanyEditModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = [
            'name',
            'rut',
            'dv',
            'year_constitution',
            'contact_phone',
            'address'
        ]


class CompanyDeletionModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'rut',
            'dv',
            'estado',
        ]
