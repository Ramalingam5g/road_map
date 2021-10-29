""" Views for road details in rest_framework using APIView """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RoadProperties, RoadType
from .serializers import RoadPropertiesSerializer, RoadTypeSerializers
import geopy.distance
from math import sin, cos, sqrt, atan2, radians


class RoadTypeView(APIView):
    """ View for get type of road """

    def get(self, request):
        """Function for get road type with its id"""
        # pylint: disable=no-member
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

    def get(self, request, id=None):
        snippet = RoadProperties.objects.get(id=id)
        serializer = RoadPropertiesSerializer(snippet)
        return Response(serializer.data)

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


class calculate_distance(APIView):
    

    def get(self, request):
        import pdb;pdb.set_trace()
        R = 6373.0

        lat1_value = float(request.GET["latitude"])
        lat1 = radians(lat1_value)
        lon1_value = float(request.GET["longitude"])
        lon1 = radians(lon1_value)
        lat2_value = float(request.GET["latitude_a"])
        lat2 = radians(lat2_value)
        lon2_value = float(request.GET["longitude_a"])
        lon2 = radians(lon2_value)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        coords_1 = (lat1_value, lon1_value)
        coords_2 = (lat2_value, lon2_value)

        context = (geopy.distance.geodesic(coords_1, coords_2).km)
        return Response(context)

        # a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        # c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # distance = R * c

        # print("Result:", distance)
        # print("Should be:", distance, "km")
        # road_names = RoadProperties.objects.filter(distance__range=[0, distance])
        # list_value = road_names.values_list("name")
        # context = {"road_name": list_value}
        # return Response(context)

        # coords_1 = (52.2296756, 21.0122287)
        # coords_2 = (52.406374, 16.9251681)

        # print (geopy.distance.vincenty(coords_1, coords_2).km )