""" Views for road details in rest_framework using APIView """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RoadProperties, RoadType
from .serializers import RoadPropertiesSerializer, RoadTypeSerializers



class RoadTypeView(APIView):
    """ View for get type of road """
    def get(self, request):
        '''Function for get road type with its id'''
        # pylint: disable=no-member
        get_roadtype = RoadType.objects.all()
        serializer = RoadTypeSerializers(get_roadtype, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        """ Method for create a new road """
        if request.method == "POST":
            data = request.data
            road_type = {"road_type": request.data["road_type"]}
            serializer = RoadTypeSerializers(data=road_type)
            if serializer.is_valid():
                roadtype = serializer.save()
            data["road_type"] = roadtype.id
            roadproperties = RoadPropertiesSerializer(data=data)
            if roadproperties.is_valid():
                roadproperties.save()
            return Response(roadproperties.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self, request):
    #     import pdb;pdb.set_trace()
    #     '''Function for get a attribute of a road type'''
    #     # pylint: disable=no-member
    #     if request.GET["road_type"] != " ":
    #         get_roadproperty = RoadProperties.objects.filter(
    #             road_type__road_type=request.GET["road_type"]
    #         )
    #         serializer = RoadPropertiesSerializer(get_roadproperty, many=True)
    #         return Response(serializer.data)
    #     elif request.GET["latitude"] and request.GET["longitude"] and request.GET["distance"] != "":
    #         roadproperty = RoadProperties.objects.filter(
    #             latitude=request.GET["latitude"],
    #             longitude=request.GET["longitude"],
    #             distance=request.GET["distance"],
    #         )
    #         list_value = roadproperty.values_list("name", "road_type__road_type")
    #         context = {"road_names": list_value}
    #         return Response(context)

        


    # def get(self, request):
    #     import pdb;pdb.set_trace()
    #     """
    #     Function for get a road name and road type
    #     using their latitude and longitude with their distance
    #     """
    #     # pylint: disable=no-member
    #     if road_type == " ":
    #         get_roadproperty = RoadProperties.objects.filter(
    #             road_type__road_type=request.GET["road_type"]
    #         )
    #         serializer = RoadPropertiesSerializer(get_roadproperty, many=True)
    #         return Response(serializer.data)

        # else:
        #     roadproperty = RoadProperties.objects.filter(
        #         latitude=request.GET["latitude"],
        #         longitude=request.GET["longitude"],
        #         distance=request.GET["distance"],
        #     )
        #     list_value = roadproperty.values_list("name", "road_type__road_type")
        #     context = {"road_names": list_value}
        #     return Response(context)



class RoadView(APIView):
    import pdb;pdb.set_trace()
    """ View for CRUD(add,edit,delete) method """

    def get(self, request, id=None):
        snippet = RoadProperties.objects.get(id=id)
        serializer = RoadPropertiesSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id=None):
        '''Method for update a road using their id'''
        properties = RoadProperties.objects.get(id=id)
        serializer = RoadPropertiesSerializer(properties, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id=None):
        '''Method for delete a road using id'''
        # pylint: disable=no-member
        road = RoadType.objects.get(id=id)
        road.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def get(self, request):
    #     import pdb;pdb.set_trace()
    #     '''Function for get a attribute of a road type'''
    #     # pylint: disable=no-member
    #     get_roadproperty = RoadProperties.objects.filter(
    #         road_type__road_type=request.GET["road_type"]
    #     )
    #     serializer = RoadPropertiesSerializer(get_roadproperty, many=True)
    #     return Response(serializer.data)

    
    

    # class RoadListView(APIView):
#     """View for get list of road type and name
#     using latitude and longitude with distance """
    # def get(self, request):
    #     """
    #     Function for get a road name and road type
    #     using their latitude and longitude with their distance
    #     """
    #     # pylint: disable=no-member
    #     roadproperty = RoadProperties.objects.filter(
    #         latitude=request.GET["latitude"],
    #         longitude=request.GET["longitude"],
    #         distance=request.GET["distance"],
    #     )
    #     list_value = roadproperty.values_list("name", "road_type__road_type")
    #     context = {"road_names": list_value}
    #     return Response(context)

