from django.shortcuts import render
from productapp.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from productapp.serializer import *
# Create your views here.


class productview(APIView):
    def get(self,request):
        products = Product.objects.all()
        ser = Productserializer(products,many=True)
        return Response({"data":ser.data})
    
    def post(self,request):
        ser = Productserializer(data=self.request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"Somthing Went Wrong !!"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data inserted Successfullt !!"})


class productviewRetrive(APIView):
    def put(self,request,id):
        product = Product.objects.get(id=id)
        ser = Productserializer(product,request.data,partial=True)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"Somthing Went Wrong !!"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data Update Successfullt !!"})
    
    def delete(self,request,id):
        product = Product.objects.get(id=id)
        product.delete()
        return Response({"message":"Product data is successfullt delete"})



class categoryview(APIView):
    def get(self,request):
        category = Category.objects.all()
        ser = Categoryserializer(category,many=True)
        return Response({"data":ser.data})
    
    def post(self,request):
        ser = Categoryserializer(data=self.request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"Somthing Went Wrong !!"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data inserted Successfullt !!"})


class categoryviewRetrive(APIView):
    def put(self,request,id):
        category = Category.objects.get(id=id)
        ser = Categoryserializer(category,request.data,partial=True)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"Somthing Went Wrong !!"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data Update Successfullt !!"})
    
    def delete(self,request,id):
        category = Category.objects.get(id=id)
        category.delete()
        return Response({"message":"category data is successfullt delete"})


@api_view(['GET'])
def product_by_category(request,id):
    category = Category.objects.get(pk=id)
    products = Product.objects.filter(category=category)
    ser = Productserializer(products,many=True)
    return Response({"data":ser.data})