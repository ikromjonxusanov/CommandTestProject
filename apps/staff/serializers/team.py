from rest_framework import serializers

from apps.staff.models import Team, TeamStaff
from apps.staff.serializers.staff import StaffShortSerializer


class TeamSerializer(serializers.ModelSerializer):
    staff = StaffShortSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'


class TeamShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']


class TeamStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamStaff
        fields = '__all__'
