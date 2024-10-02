# create category's serializers

"""
this is not efficient as we need to declare all the fields we want to serialize;

from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True) # read_only=True indicates this is not user input, only read record from data 
    name = serializers.CharField(
        required=True,
        max_length=150, # communicate serializer about the constraint to do the validation of the input
        )
    type = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self,instance, validated_data):
        instance.name = validated_data('name', instance.name) # dictionary get function: dict_name("field", default_value) -> find field in dictionary, if there is none return default value
        instance.type = validated_data('type', instance.type)
        instance.save()
        return instance
        
"""

from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "pk",
            "name",
            "type",
        )
        # fields =  "__all__" # include all
        # exclude = (
        #     "created_at" # instead of adding included field, we can exclude field 
        # )