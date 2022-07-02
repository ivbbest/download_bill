from rest_framework import serializers
from .models import Client, Organization, Bill


class ClientSerializer(serializers.ModelSerializer):
    """
    Сериализатор для сериализации данных таблицы Client
    """
    class Meta:
        model = Client
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для сериализации данных таблицы Organization
    """

    class Meta:
        model = Organization
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    """
    Сериализатор для сериализации данных таблицы Bill
    """
    class Meta:
        model = Bill
        fields = '__all__'
