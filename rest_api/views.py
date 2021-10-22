from django.shortcuts import render
from .models import RoadProperties,Road
from .serializers import RoadPropertiesSerializer,RoadSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#import pdb;pdb.set_trace()
class RoadDetail(APIView):

    def get(self, request ):
        #import pdb;pdb.set_trace()
        snippets = RoadProperties.objects.all()
        serializers = RoadPropertiesSerializer(snippets)
        return Response(serializers.data)

    def post(self, request):
        #import pdb;pdb.set_trace()
        serializer = RoadPropertiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# Create your views here.
