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

    def value_to_convert_test_01(self):
        assert my_main.final_result > 0
        print("more then 0")

    def result_is_valid_test_02(self):
        assert my_main.final_result != ""
        print("is not string")

    def file_content_is_valid_test_03(self):
        assert my_main.print_final_results() == []
        print("is list")

    @classmethod
    def tearDownClass(self):
        print('bye')
