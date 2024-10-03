from django.urls import path, include
from rest_framework import routers

from apps.staff.views import staff, team

router = routers.DefaultRouter()
router.register(r'staff', staff.StaffViewSet, basename='staff')
router.register(r'team', team.TeamViewSet, basename='team')
router.register(r'team-staff', team.TeamStaffViewSet, basename='team-staff')

urlpatterns = [
    path('', include(router.urls)),
]
