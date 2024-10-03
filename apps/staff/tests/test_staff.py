from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.staff.models import Staff


class StaffTest(TestCase):

    def setUp(self):
        self.staff = Staff.objects.create(
            first_name="Ikromjon",
            last_name="Xusanov",
            email="ikromjonkhusanov06@gmail.com"
        )

    def test_staff_str(self):
        self.assertEqual(str(self.staff), "Ikromjon Xusanov")

    def test_staff_email(self):
        self.assertEqual(self.staff.email, "ikromjonkhusanov06@gmail.com")

    def test_staff_count(self):
        staff_count = Staff.objects.count()
        self.assertEqual(staff_count, 1)

    def test_unique_email(self):
        with self.assertRaises(Exception):
            Staff.objects.create(first_name="Ikromjon", last_name="Khusanov", email="ikromjonkhusanov06@gmail.com")


class StaffAPITest(APITestCase):


    def test_check_staff_list(self):
        response = self.client.get(reverse('staff-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_staff_retrieve(self):
        response = self.client.get(reverse('staff-detail', args=[self.staff.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['first_name'], "Ikromjon")
        self.assertEqual(response.data['last_name'], "Xusanov")
        self.assertEqual(response.data['email'], "ikromjonkhusanov06@gmail.com")

    def test_staff_create(self):
        data = {
            "first_name": "Abduhamid",
            "last_name": "Abdusamatov",
            "email": "abduhamid@gmail.com"
        }
        response = self.client.post(reverse('staff-list'), data)
        self.assertEqual(response.status_code, 201)

    def test_staff_update(self):
        data = {
            "first_name": "Ikrom",
            "last_name": "Khusanov",
            "email": "ikromjonkhusanov06@gmail.com"
        }
        response = self.client.put(reverse('staff-detail', args=[self.staff.id]), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['first_name'], "Ikrom")

    def test_staff_partial_update(self):
        data = {
            "first_name": "Ikromjohn"
        }
        response = self.client.patch(reverse('staff-detail', args=[self.staff.id]), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['first_name'], "Ikromjohn")

    def test_staff_delete(self):
        response = self.client.delete(reverse('staff-detail', args=[self.staff.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Staff.objects.count(), 0)
