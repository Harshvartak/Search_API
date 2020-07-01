import pandas as pd

from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
import requests
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework import filters


from .serializers import *

'''
For adding the csv to the database this function was created
Not it is of no use

def datafill(request):
    df=pd.read_csv("bank_branches.csv")
    for a,i in df.iterrows():
        bank = Bank()
        bank.ifsc = i['ifsc']
        bank.bank_id = i['bank_id']
        bank.bank_name = i['bank_name']
        bank.branch = i['branch']
        bank.address = i['address']
        bank.city = i['city']
        bank.district = i['district']
        bank.state = i['state']
        bank.save()

    return render(request, "Data/datafill.html")

'''

'''
@api_view(['POST'])
def ifsc_search(request):
    if request.method == 'POST':
        ifsc = JSONParser().parse(request)
        print(ifsc)
        if ifsc:
            match=Bank.objects.filter(Q(ifsc_icontains=ifsc))
            if match:
                serializer = IfscSearchSerializer(data=match)
                return Response(serializer.data)
            else:
                return Response("Not found")

'''

'''This is the working part of the first part of the assignment'''
class IfscAPIView(generics.ListCreateAPIView):
    search_fields = ['ifsc']
    filter_backends = (filters.SearchFilter,)
    queryset = Bank.objects.all()
    serializer_class = IfscSearchSerializer



'''
class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


'''


'''This is the second part of the assignment, there is a bug, will fix later'''
class Part2APIView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = IfscSearchSerializer
    search_fields = ['bank_name','city']
    filter_backends = [filters.SearchFilter,]
