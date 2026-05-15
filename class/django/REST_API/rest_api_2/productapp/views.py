from rest_framework.views import APIView
from rest_framework.response import Response


class ProductView(APIView):
    def get(self, request):
        return Response({"message": "GET calling"})
    
    def post(self, request):
        return Response({"message": "POST calling"})


class ProductDetailView(APIView):
    def get(self, request, id):
        return Response({"message": "GET detail calling", "id": id})

    def put(self, request, id):
        return Response({"message": "PUT calling", "id": id})
    
    def delete(self, request, id):
        return Response({"message": "DELETE calling", "id": id})