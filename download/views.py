from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from django.db.models import *


from .serializers import ClientSerializer, BillSerializer, \
                            OrganizationSerializer
from .utils.read_file import read_excel_file
from .utils.utility import service_classifier, fraud_detector, \
                            convert_lists_to_dict
from .models import Client, Organization, Bill


fields_client = ['name']
fields_org = ['client_name', 'name', 'address']
fields_bill = ['client_name', 'client_org', 'number', 'sum', 'date', 'service', 'fraud_score', 'service_class', 'service_name']
# fields_bill = ['client_name', 'client_org', 'number', 'sum', 'date', 'service']


class ClientOrgUploadView(APIView):
    """
    Обработка загрузки данных с файла client_org.xlsx
    """
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        file = request.data['file']
        client = read_excel_file(file, sheet_name='client')
        organization = read_excel_file(file, sheet_name='organization')
        data_client = convert_lists_to_dict(fields_client, client)
        data_org = convert_lists_to_dict(fields_org, organization)

        # передаем все на вход сериализатору
        serializer_client = ClientSerializer(data=data_client, many=True)
        serializer_org = OrganizationSerializer(data=data_org, many=True)

        # проверка валидации и сохранение в базу
        if serializer_client.is_valid(raise_exception=True):
            serializer_client.save()

            if serializer_org.is_valid(raise_exception=True):
                serializer_org.save()

                return Response({'status': 'OK'}, status=status.HTTP_201_CREATED)
            return Response(serializer_org.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer_client.errors, status=status.HTTP_400_BAD_REQUEST)


class BillUploadView(APIView):
    """
    Обработка загрузки данных с файла bills.xlsx
    """
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        file = request.data['file']
        bills = read_excel_file(file)
        bills_new = list()

        for elem in bills:
            print(elem)
            fraud_score = fraud_detector(str(elem[-1]))
            for service_class, service_name in service_classifier(str(elem[-1])).items():
                elem.extend([str(fraud_score), str(service_class), str(service_name)])
                bills_new.append(elem)
                print(elem)

        data = convert_lists_to_dict(fields_bill, bills_new)
        # передаем все на вход сериализатору
        serializer = BillSerializer(data=data, many=True)

        # проверка валидации и сохранение в базу
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({'status': 'OK'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientAPIList(APIView):
    """
    Эндпоинт со списком клиентов. Данные, которые нужно
    отдавать для каждого элемента списка:
     - Название клиента
     - Кол-во организаций
     - Приход (сумма по счетам всех организаций клиента)
    """
    def get(self, request, format=None):
        data = Bill.objects.values('client_name').\
            annotate(count_org=Count('client_org'), sum=Sum('sum'))
        return Response(data)