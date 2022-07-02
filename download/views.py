from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ClientSerializer, BillSerializer, \
                            OrganizationSerializer
from .utils.read_file import read_excel_file
from .utils.utility import service_classifier, fraud_detector, \
                            convert_lists_to_dict


fields_client = ['name']
fields_org = ['client_name', 'name', 'address']
fields_bill = ['client_name', 'client_org', 'number', 'sum', 'service', 'fraud_score', 'service_class', 'service_name']


class ClientOrgUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']
        client = read_excel_file(f, sheet_name='client')
        organization = read_excel_file(f, sheet_name='organization')
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


class BillOrgUploadView(APIView):
    parser_class = (FileUploadParser,)

    pass