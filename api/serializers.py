from rest_framework import serializers
from .models import Members, Squad, Power

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        exclude = ('id', )

class MembersSerializer(serializers.ModelSerializer):
    powers = PowerSerializer(many=True)
    class Meta:
        model = Members
        exclude = ('id', )

class SquadSerializer(serializers.ModelSerializer):
    members = MembersSerializer()
    class Meta:
        model = Squad
        fields = '__all__'