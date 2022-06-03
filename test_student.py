import unittest
from student import Student
from datetime import timedelta

class TestStudent(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_apply_extension(self):
        print("test_apply_extension")
        old_date = self.student.end_date
        new_date = self.student.apply_extension(20)
        self.assertTrue(old_date == self.student.end_date - timedelta(days=20))

        

if __name__ == "__main__":
    unittest.main()