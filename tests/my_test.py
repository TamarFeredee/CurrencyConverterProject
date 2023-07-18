import my_main
import unittest


# Write a Pytest test for your calculator with the following 3 tests:
# • Entering a value to convert
# • Asserting Result is valid
# • Checking the content of the results file.


class MyTest(unittest.TestCase, my_main):
    @classmethod
    def setUpClass(self):
        print('hello')

    def value_to_convert_55(self):
        assert my_main.final_result == 15.400000000000002
        print("correct result when entering 55 Shekels")

    @classmethod
    def tearDownClass(self):
        print('bye')
