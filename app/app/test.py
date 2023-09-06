""""
Simmple Tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the Calc Module."""

    def test_add_numbers(self):
        """test adding numbers together."""
        res = calc.add(5,6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """test subtracting numbers together."""
        res  = calc.subtract(12,21)
        self.assertEqual(res, 9)