from django.test import TestCase
from restaurant import models

# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = models.Menu.objects.create(name="IceCream", price=80)
        self.assertEqual(str(item), "IceCream: 80")
