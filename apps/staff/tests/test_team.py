from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.staff.models import Team, TeamStaff, Staff


class TeamTest(TestCase):

    def setUp(self):
        self.staff = Team.objects.create(
            name="Team 1"
        )

    def test_team_str(self):
        self.assertEqual(str(self.staff), "Team 1")

    def test_team_name(self):
        self.assertEqual(self.staff.name, "Team 1")

    def test_team_count(self):
        team_count = Team.objects.count()
        self.assertEqual(team_count, 1)

    def test_unique_name(self):
        with self.assertRaises(Exception):
            Team.objects.create(name="Team 1")

    def test_team_staff(self):
        team_staff = Team.objects.get(name="Team 1")
        self.assertEqual(team_staff.staff.count(), 0)
        staff = Staff.objects.create(
            first_name="Ikromjon",
            last_name="Xusanov",
            email="ikromjonkhusanov06@gmail.com"
        )
        TeamStaff.objects.create(staff=staff, team=team_staff)
        self.assertEqual(team_staff.staff.count(), 1)


class TeamAPITest(APITestCase):

    def setUp(self):
        self.team = Team.objects.create(
            name="Team 1"
        )

    def test_check_team_list(self):
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_team_retrieve(self):
        response = self.client.get(reverse('team-detail', args=[self.team.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "Team 1")
        self.assertEqual(response.data['staff'], [])

        staff = self.client.post(reverse('staff-list'), {
            "first_name": "Ikromjon",
            "last_name": "Xusanov",
            "email": "ikromjonkhusanov06@gmail.com"
        })

        staff_short = [{"email": "ikromjonkhusanov06@gmail.com",
                        "first_name": "Ikromjon",
                        "id": staff.data['id'],
                        "last_name": "Xusanov"}]

        self.client.post(reverse('team-staff-list'), {'staff': staff.data['id'], 'team': self.team.id})

        response = self.client.get(reverse('team-detail', args=[self.team.id]))

        self.assertEqual(response.data['staff'], staff_short)

    def test_team_create(self):
        data = {
            "name": "Human Resources",
        }
        response = self.client.post(reverse('team-list'), data)
        self.assertEqual(response.status_code, 201)

    def test_staff_update(self):
        data = {
            "name": "development"
        }
        response = self.client.put(reverse('team-detail', args=[self.team.id]), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "development")

    def test_team_delete(self):
        response = self.client.delete(reverse('team-detail', args=[self.team.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Staff.objects.count(), 0)
