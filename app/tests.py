from django.test import TestCase

class GeneralTest(TestCase):
    
    def test_first(self):
        self.assertEqual(1, 1)
    
    def test_second(self):
        self.assertEqual(2, 2)

    def test_third(self):
        self.assertEqual(3, 4)

    def test_fourth(self):
        self.assertEqual(4, 4)
