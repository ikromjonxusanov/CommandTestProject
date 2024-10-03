from rest_framework.viewsets import ModelViewSet

from apps.staff.models import Staff
from apps.staff.serializers.staff import StaffSerializer


class StaffViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
