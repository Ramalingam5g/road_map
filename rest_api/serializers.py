from rest_framework import serializers
from . models import Road,RoadProperties

class RoadSerializers(serializers.ModelSerializer):
    class Meta :
        #import pdb;pdb.set_trace()
        model = Road
        fields = '__all__'

class RoadPropertiesSerializer(serializers.ModelSerializer):
   class Meta:
       #import pdb;pdb.set_trace()
       model = RoadProperties
       fields = '__all__'