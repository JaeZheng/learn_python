import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee("Jae", 10000)
        self.sale_give_default = 15000
        self.sale_give_custom = 16000

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.sale_give_default, self.my_employee.sale)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(6000)
        self.assertEqual(self.sale_give_custom, self.my_employee.sale)


if __name__ == '__main__':
    unittest.main()

