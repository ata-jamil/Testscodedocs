import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Ataul', 'Jamil', 50000)
        self.emp_2 = Employee('Fabian', 'Fagerholm', 60000)

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Ataul.Jamil@email.com')
        self.assertEqual(self.emp_2.email, 'Fabian.Fagerholm@email.com')

        self.emp_1.first = 'Mikko'
        self.emp_2.first = 'Jari'

        self.assertEqual(self.emp_1.email, 'Mikko.Jamil@email.com')
        self.assertEqual(self.emp_2.email, 'Jari.Fagerholm@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Ataul Jamil')
        self.assertEqual(self.emp_2.fullname, 'Fabian Fagerholm')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Jamil')
        self.assertEqual(self.emp_2.fullname, 'Jane Fagerholm')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
