from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils.read_file import read_excel_file


class MyUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']

        print(read_excel_file(f))
        breakpoint()
        mymodel.my_file_field.save(f.name, f, save=True)
        return Response(status=status.HTTP_201_CREATED)
