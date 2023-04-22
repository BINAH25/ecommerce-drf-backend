from django.contrib.auth.models import User
from rest_framework import serializers
from . models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['_id','username','email','name','isAdmin']
        
        
    def get__id(self,obj):
        return obj.id
        
    def get_isAdmin(self,obj):
        return obj.is_staff
        
    def get_name(self,obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name
        
    