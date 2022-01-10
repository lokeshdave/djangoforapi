from re import search
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import pagination, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response, responses
from .models import employe
from .serializers import employese
from django.views.decorators.csrf import csrf_exempt
from rest_framework.filters import SearchFilter,OrderingFilter
from .page import limit

# for all data you write def employe1(request):'
# emp = employe.objects.all()
# emps = employese(emp,many = True)
class employelist(ListAPIView):
    queryset = employe.objects.all()
    serializer_class = employese
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['first_name','last_name']
    pagination_class = limit
    


# Create your views here.



@api_view(['GET','POST','PUT','PATCH','DELETE'])
def employe1_all(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            emp = employe.objects.get(id=id)
            emps = employese(emp)
            return Response(emps.data)
        emp = employe.objects.all()
        emps = employese(emp,many=True)
        return Response(emps.data)            

    if request.method == 'POST':
        se = employese(data=request.data)
        if se.is_valid():
            se.save()
            return Response({'msg':201},status=status.HTTP_201_CREATED)
        return Response(se.save())
           
    if request.method == 'PUT':
        id = pk
        em = employe.objects.get(pk=id)
        se = employese(em,data=request.data,partial=True)
        if se.is_valid():
           se.save()
           return Response({'msg': 201},status=status.HTTP_200_OK)
        return Response(se.save())
       
    if request.method == 'PATCH':
        id = pk
        em = employe.objects.get(pk=id)
        se = employese(em,data=request.data,partial=True)
        if se.is_valid():
           se.save()
           return Response({'msg': 'PATCHDATA'},status=status.HTTP_200_OK)
        return Response(se.save())           
           
    if request.method == 'DELETE':
        id = pk
        em = employe.objects.get(pk=id) 
        em.delete()
        return Response({'msg': 201},status=status.HTTP_200_OK) 
    

