from cov.utils import my_sum
from unittest import TestCase


class MyTest(TestCase):
    def test_sum(self):
        a = 1
        b = 2
        self.assertEqual(my_sum(a, b), a + b)