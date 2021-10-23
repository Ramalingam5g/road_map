from rest_framework import serializers
from . models import RoadType,RoadProperties

class RoadTypeSerializers(serializers.ModelSerializer):
    class Meta :
        #import pdb;pdb.set_trace()
        model = RoadType
        fields = '__all__'

class RoadPropertiesSerializer(serializers.ModelSerializer):
   class Meta:
       #import pdb;pdb.set_trace()
       model = RoadProperties
       fields = '__all__'