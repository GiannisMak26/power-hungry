from unittest import TestCase

from solar_panel_maintenance import get_maximum_string_output


class TestMaximumStringOutput(TestCase):
    """ Example test cases for testing """

    def test_zeroes(self):
        self.assertEqual(get_maximum_string_output([2, 0, 2, 2, 0]), '8')

    def test_negative_output(self):
        self.assertEqual(get_maximum_string_output([-2, -3, 4, -5]), '60')
