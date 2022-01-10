from rest_framework import serializers
from .models import employe

# you need to create a serializers class for convert your all data in serializer that can user use the data
class employese(serializers.ModelSerializer):
    class Meta:
        model = employe
        fields = '__all__'        
        
