from ejercicio_2.serializers import (
    CompanyModelSerializer,
    CompanyEditModelSerializer,
    CompanyDeletionModelSerializer,
)
from ejercicio_2.models import Company
from ejercicio_2.factories import CompanyFactory
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import viewsets, generics
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.views import APIView
from django.conf import settings

# Create your views here.


class CompanyFakerView(generics.ListCreateAPIView):
    serializer_class = CompanyModelSerializer
    queryset = Company.objects.all()

    def post(self, request, **kwargs):
        batchs = CompanyFactory.create_batch(
            size=request.data.get('batch_number', 1)
        )
        serializer = CompanyModelSerializer(batchs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


company_faker_view = CompanyFakerView.as_view()


class CompanyView(generics.ListCreateAPIView):
    serializer_class = CompanyModelSerializer
    queryset = Company.objects.filter(estado=Company.ACTIVE)

    def get(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = CompanyModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        data = request.data
        serializer = CompanyModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        company = Company.objects.get(pk=kwargs.get('pk'))
        data = request.data
        serializer = CompanyEditModelSerializer(company, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        company = Company.objects.get(pk=kwargs.get('pk'))
        data = request.data
        serializer = CompanyEditModelSerializer(
            company,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_206_PARTIAL_CONTENT
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        try:
            company = Company.objects.get(pk=kwargs.get('pk'))
        except Company.DoesNotExist:
            return Response(
                {'id': ['Registro no encontrado']},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {'estado': Company.DELETE}
        serializer = CompanyDeletionModelSerializer(
            company,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


company_view = CompanyView.as_view()
