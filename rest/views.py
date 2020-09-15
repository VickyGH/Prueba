from django.shortcuts import render
import json
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import * 
from rest_framework.response import Response

from account.models import Client
from rest.serializers import ClientSerializer, ListClientSerializer


class CreateClient(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer
    queryset = Client.objects.all().order_by('id')


class UpdateClient(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AllowAny]
    serializer_class = ClientSerializer
    queryset = Client.objects.all().order_by('id')
    #filter_backends = [, ]


class DeleteClient(generics.DestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer
    queryset = Client.objects.all().order_by('id')


class ListClient(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AllowAny]
    serializer_class = ListClientSerializer
    queryset = Client.objects.all().order_by('id')
    #pagination_class = None


class GetClient(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes =  [AllowAny]
    serializer_class = ListClientSerializer
    queryset = Client.objects.all()
