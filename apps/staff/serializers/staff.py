from rest_framework import serializers
from apps.staff.models import Staff


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'


class StaffShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'first_name', 'last_name', 'email']
