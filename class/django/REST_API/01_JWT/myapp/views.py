from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display(request):

    data = {
        "message": "Display API Calling",
        "user": str(request.user)
    }

    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def create(request):

    data = {
        "message": "Create API Calling",
        "user": str(request.user)
    }

    return Response(data)