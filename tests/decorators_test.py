import unittest
from decorators import dynamic_programming


class test_dynamic_programming(unittest.TestCase):
    def setUp(self):
        # Init call counter
        self.call_count = 0

        # Define fib to check decorator
        @dynamic_programming
        def fib(n):
            self.call_count += 1
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fib(n - 1) + fib(n - 2)

        self.fib = fib

        # Set up dummy function for various tests.
        @dynamic_programming
        def dummy(parm1):
            return parm1

        self.dummy = dummy

    def tearDown(self):
        pass

    def test_dynamic_fib(self):
        # Make sure we get the correct answer
        self.assertEqual(self.fib(8), 21)

        # Check fib only recurses the correct number of times.
        # More than this indicates an issues with the cacheing.
        # TODO: Sort out a better way to check this. Mocks?
        self.assertEqual(self.call_count, 9)

    def test_complex_params(self):
        params = [
            "string",
            ['list', 'of', 'strings'],
            [1, 2, 3],
            {
                'key': 'value'
            },
            {
                1: 234
            },
            self.dummy,
        ]
        for param in params:
            try:
                self.dummy(param)
            except:
                self.fail(
                    f"Param failed to index. Type: {type(param)}, Value: {param}"
                )
