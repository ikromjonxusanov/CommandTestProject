from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet

from apps.staff.models import Team, TeamStaff, Staff
from apps.staff.serializers.team import TeamSerializer, TeamStaffSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.prefetch_related(
        Prefetch('staff', queryset=Staff.objects.only('id', 'first_name', 'last_name', 'email'))
    )
    serializer_class = TeamSerializer


class TeamStaffViewSet(ModelViewSet):
    queryset = TeamStaff.objects.all()
    serializer_class = TeamStaffSerializer
