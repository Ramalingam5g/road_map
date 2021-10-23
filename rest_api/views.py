from django.shortcuts import render
from .models import RoadProperties,RoadType
from .serializers import RoadPropertiesSerializer,RoadTypeSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#import pdb;pdb.set_trace()
class RoadTypeView(APIView):

    def get(self,request,format=None):
        import pdb;pdb.set_trace()
        snippet = RoadType.objects.all()
        serializer = RoadTypeSerializers(snippet,many=True)
        return Response(serializer.data)
class RoadPropertyView(APIView):
    import pdb;pdb.set_trace()

    def get(self,request,road_type=None):
        import pdb;pdb.set_trace()
        roadproperty = RoadProperties.objects.filter(road_type__road_type=request.GET['road_type'])
        serializer = RoadPropertiesSerializer(roadproperty,many=True)
        return Response(serializer.data)

class RoadList(APIView):
    # #import pdb;pdb.set_trace()
   

    def post(self, request):
        import pdb;pdb.set_trace()
        
        if request.method == 'POST':
            data = request.data
            road_type = {'road_type':request.data['road_type']}
            name = data.pop('road_type')
            serializer = RoadTypeSerializers(data=road_type)
            if serializer.is_valid():
                roadtype = serializer.save()
            data['road_type'] = roadtype.id
            roadproperties = RoadPropertiesSerializer(data=data)
            if roadproperties.is_valid():
                properties = roadproperties.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        import pdb;pdb.set_trace()
        road = RoadType.objects.get(id=id)
        road_data = {'road_type':request.data['road_type']}
        serializer = RoadTypeSerializers(road, data=road_data)
        if serializer.is_valid():
            serializer.save()
        property_data = request.data
        #remove_key = ('id','road_type')
        #list(map(property_data.__delitem__, filter(property_data.__contains__,remove_key)))
        #property_data.pop('road_type')
        property_data['road_type'] = id
        road_property = RoadProperties.objects.get(road_type_id = id)
        serializer = RoadPropertiesSerializer(data=property_data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, id=None):
        import pdb;pdb.set_trace()
        road = RoadType.objects.get(id=id)
        road.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #serializer = RoadPropertiesSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors)

class RoadDetail(APIView):
    def get_object(self, pk):
        try:
            return RoadProperties.objects.get(pk=pk)
        except RoadProperties.DoesNotExist:
            raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = RoadPropertiesSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = RoadPropertiesSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)