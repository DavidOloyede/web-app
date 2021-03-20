import unittest
from login import email, password

class Testlog(unittest.TestCase):
    def testemail1(self):
        self.assertEqual(email('bob@123.com'), True)

    def testemail2(self):
        self.assertEqual(email('bob.com'), False)

    def testemail3(self):
        self.assertEqual(email('bob@y.com'), True)

    def testemail4(self):
        self.assertEqual(email('bobbyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy@123.com'), False)

    def testpassword1(self):
        self.assertEqual(password('11111111111111111111111111111'), False)

    def testpassword2(self):
        self.assertEqual(password('password'), False)

    def testpassword3(self):
        self.assertEqual(password('password%'), True)

    def testpassword4(self):
        self.assertEqual(password('a'), False)


#if name== 'main':
#    unittest.main()
