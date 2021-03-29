from django.test import SimpleTestCase

# Create your tests here.
class TestTestCase(SimpleTestCase):
    def test_nothing(self):
        self.assertEqual("moby dock", "moby dock")
