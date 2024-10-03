"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """Test the clac module."""

    def test_add_module(self):
        """test the add function."""
        res = calc.add(5, 6, 7)

        self.assertEqual(res, 18)
