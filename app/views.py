from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes

from app.models import *

from app.serializers import *

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def Emp(request):
    empdata=Employee.objects.all()
    empJSONdata=EmpModelSerializer(empdata,many=True)
    return Response(empJSONdata.data)
