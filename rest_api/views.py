""" Views for road details in rest_framework using APIView """
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import geopy.distance
from .models import RoadProperties, RoadType
from .serializers import RoadPropertiesSerializer, RoadTypeSerializers

class RoadTypeView(APIView):
    """ View for get type of road """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Function for get road type with its id"""
        import pdb;pdb.set_trace()
        if request.GET.get("road_type"):
            get_roadproperty = RoadProperties.objects.filter(
                road_type__road_type=request.GET["road_type"]
            )
            all_fields = RoadProperties._meta.get_fields()
            print(all_fields)
            fields = {"field_name":all_fields}
            serializer = RoadPropertiesSerializer(get_roadproperty, many=True)
            return Response(serializer.data)
            # serializer = RoadPropertiesSerializer(get_roadproperty, many=True)
            # return Response(serializer.data)

        if (request.GET.get("latitude_1")
            and request.GET.get("longitude_1")
            and request.GET.get("latitude_2")
            and request.GET.get("longitude_2")):
            lat1_value = float(request.GET["latitude_1"])
            lon1_value = float(request.GET["longitude_1"])
            lat2_value = float(request.GET["latitude_2"])
            lon2_value = float(request.GET["longitude_2"])
            coords_1 = (lat1_value, lon1_value)
            coords_2 = (lat2_value, lon2_value)
            calculate_distance = geopy.distance.geodesic(coords_1, coords_2).km
            print("Distance:",calculate_distance)
            road_names = RoadProperties.objects.filter(distance__range=[0, calculate_distance])
            list_value = road_names.values_list("name")
            context = {"road_name": list_value}
            return Response(context)

        else:
            get_roadtype = RoadType.objects.all()
            serializer = RoadTypeSerializers(get_roadtype, many=True)
            return Response(serializer.data)

    def post(self, request):
        import pdb;pdb.set_trace()
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



class RoadView(APIView):

    """ View for CRUD(add,edit,delete) method """

    def put(self, request, id=None):
        """Method for update a road using their id"""
        properties = RoadProperties.objects.get(id=id)
        serializer = RoadPropertiesSerializer(properties, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        """Method for delete a road using id"""
        # pylint: disable=no-member
        road = RoadType.objects.get(id=id)
        road.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

