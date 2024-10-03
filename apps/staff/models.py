from django.db import models

from apps.common.models import BaseModel


class Staff(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Team(BaseModel):
    name = models.CharField(max_length=255)
    staff = models.ManyToManyField(Staff, through='TeamStaff')

    def __str__(self):
        return self.name


class TeamStaff(BaseModel):
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff} - {self.team} - {self.joined_date}"
