import unittest
from decorators import dynamic_programming


class test_dynamic_programming(unittest.TestCase):
    def setUp(self):
        self.call_count = 0

    def tearDown(self):
        pass

    def test_dynamic(self):
        @dynamic_programming
        def fib(n):
            self.call_count += 1
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fib(n - 1) + fib(n - 2)

        self.assertEqual(fib(8), 21)

        # TODO: Sort out a better way to check this. Mocks?
        self.assertEqual(self.call_count, 9)