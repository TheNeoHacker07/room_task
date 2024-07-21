from rest_framework.serializers import  ModelSerializer
from .models import ApartmentModel, MyRentsModel

class AparmentSerializer(ModelSerializer):
    class Meta:
        model = ApartmentModel
        fields = '__all__'


class MyRentSerializer(ModelSerializer):
    class Meta:
        model = MyRentsModel
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        instance = self.Meta.model.objects.create(**validated_data)
        return instance
    