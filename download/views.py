from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils.read_file import read_excel_file
from .utils.utility import service_classifier, fraud_detector, \
                            convert_lists_to_dict


class MyUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        fields = ['client_name', 'client_org', 'number', 'sum', 'service']

        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']
        elements = read_excel_file(f)
        data = convert_lists_to_dict(fields, elements)
        print(data)
        # print(elements)
        # print(fields)
        breakpoint()
        mymodel.my_file_field.save(f.name, f, save=True)
        return Response(status=status.HTTP_201_CREATED)
