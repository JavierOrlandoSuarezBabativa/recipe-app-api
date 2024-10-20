# Sample tests

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    
    def test_add_numbers(self):
        
        res = calc.add(7,7)
        self.assertEqual(res, 14)
        
    def test_substract_numbers(self):
        
        res = calc.substract(7,6)
        self.assertEqual(res, 1)
        
    