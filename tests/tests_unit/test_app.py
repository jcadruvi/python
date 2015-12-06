import unittest
from mock import Mock


class TestApp(unittest.TestCase):
    def setUp(self):
        self.test_var = 1

    def test_var(self):
        self.assertEqual(1, self.test_var)