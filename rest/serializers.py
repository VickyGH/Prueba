from rest_framework import serializers

from account.models import Client


# Additional
class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ListClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
