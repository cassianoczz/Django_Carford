from carford_app.models import Owner, Car
from carford_app import views
from django.test import TestCase, RequestFactory



class CarTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.owner = Owner.objects.create(
            id=1,
            name='Cassiano'
        )
        return super().setUp()

class TestListOwners(CarTestCase):

    def test_list_owner_without_car_get_200(self):
        request = self.factory.get('/')
        response = views.OwnerList.as_view()(request)
        self.assertEqual(response.status_code, 200)
