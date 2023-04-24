from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Flowers

class PlantsyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )


        cls.flower = Flowers.objects.create(
            author=cls.user,
            title="A good title",
            image = "https://www.daysoftheyear.com/cdn-cgi/image/dpr=1%2Cf=auto%2Cfit=cover%2Cheight=650%2Cq=70%2Csharpen=1%2Cwidth=956/wp-content/uploads/colourful-rose-2022-09-16-02-50-50-utc-scaled.jpg",
            description ="Nice body content",
            price = 20.55,
            is_in_stock = True,
        )


    def test_post_model(self):
        self.assertEqual(self.flower.author.username, "testuser")
        self.assertEqual(self.flower.title, "A good title")
        self.assertEqual(self.flower.image, "https://www.daysoftheyear.com/cdn-cgi/image/dpr=1%2Cf=auto%2Cfit=cover%2Cheight=650%2Cq=70%2Csharpen=1%2Cwidth=956/wp-content/uploads/colourful-rose-2022-09-16-02-50-50-utc-scaled.jpg")
        self.assertEqual(self.flower.description, "Nice body content")
        self.assertEqual(self.flower.price, 20.55)
        self.assertEqual(self.flower.is_in_stock, True)
        self.assertEqual(str(self.flower), "A good title")
        

# Create your tests here.
