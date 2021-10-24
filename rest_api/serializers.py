from rest_framework import serializers
from . models import RoadType,RoadProperties

class RoadTypeSerializers(serializers.ModelSerializer):
    class Meta :
        model = RoadType
        fields = '__all__'

class RoadPropertiesSerializer(serializers.ModelSerializer):
   class Meta:
       model = RoadProperties
       fields = '__all__'