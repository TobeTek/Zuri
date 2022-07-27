from django.test import TestCase
from django.contrib.auth import get_user_model 
import secrets
from links import models 

UserModel = get_user_model()

class LinkModelTestCase(TestCase):
    @classmethod 
    def setUpTestData(cls):
        # This function is executed before any test is run
        # Create a new user to use in tests
        cls.user = UserModel.objects.create_user(username="normaluser", email="normaluser@email.com", password=secrets.token_urlsafe(10))
            

    def test___str___representation(self):
        link = models.Link.objects.create(
            target_url = "http://httpbin.org",
            description = "An active link",
            identifier = "active-link-httpbin",
            author = self.user,
        )
        # str(Link) should be it's identifier
        self.assertEqual(str(link), f"{link.identifier}")
    
    def test_identifier_is_never_empty(self):
        # Identifier should be automatically created if left blank
        link = models.Link.objects.create(
            target_url = "http://httpbin.org",
            description = "An active link",
            author = self.user,
        )
        self.assertNotEqual(link.identifier, '') # is not blank

        # Custom identifier should not be overwritten when provided
        link = models.Link.objects.create(
            target_url = "http://httpbin.org",
            description = "An active link",
            identifier = "link-identifier",
            author = self.user,
        )
        self.assertEqual(link.identifier, "link-identifier") # is not overriden by our custom save logic