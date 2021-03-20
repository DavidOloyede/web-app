import unittest
from profile import fullname
from profile import address
from profile import city
from profile import zipcode


class TestName(unittest.TestCase):
    def test_twoNames(self):
        self.assertTrue(fullname("bob rob"))
        self.assertFalse(fullname(25))
        self.assertFalse(fullname('25'))

class TestAddress(unittest.TestCase):
    def test_address(self):
        self.assertTrue(address("3488 calhoun st"))
        self.assertFalse(address("this aint adresss"))
        self.assertFalse(address("122sgbasdrhbrsdhg"))
        self.assertFalse(address("4245324"))
        self.assertFalse(address(552))

class TestCity(unittest.TestCase):
    def test_city(self):
        self.assertFalse((city(25)))
        self.assertTrue(city("houston"))
        self.assertTrue(city("salt lake"))
        self.assertFalse(city("houston713"))

class TestZip(unittest.TestCase):
    def test_zipcode(self):
        self.assertFalse(zipcode("bob rob"))
        self.assertTrue(zipcode(77004))
        self.assertTrue(zipcode('77005'))
        self.assertFalse(zipcode(770055))
        self.assertFalse(zipcode(770))

































# class TestFibonacci(unittest.TestCase):
#     def test_fibonacci_1(self):
#         self.assertEqual(fibonacci(1), 1)

#     def test_fibonacci_10(self):
#         self.assertEqual(fibonacci(10), 89)

#     def test_fibonacci_30(self):
#         self.assertEqual(fibonacci(30), 1346269)

# class TestFActorial(unittest.TestCase):
#     def test_factorial_1(self):
#         self.assertEqual(factorial(1), 1)



# if __name__ == '__main__':
#     unittest.main()