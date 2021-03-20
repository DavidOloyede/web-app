import unittest
from fuelQuoteForm import Order

class testOrder(unittest.TestCase):
    #testing input of whole number of gallons and correct date input
    def testOrder1(self):
        order1= Order(10, "01/10/1000")
        self.assertEqual(order1.totalAmount(), 100)

    #testing input of fractional number of gallons requested and correct date 
    def testOrder2(self):
        order2= Order(10.7, "01/10/1000")
        self.assertEqual(order2.totalAmount(), 110)

    #testing whole number gallons and no date provided 
    def testOrder3(self):
        order3= Order(10, "")
        self.assertEqual(order3.totalAmount(), "Date is required")
    
    #testing whole number of gallons and incorrect date provided 
    def testOrder4(self):
        order4= Order(10,"02/31/2021")
        self.assertEqual(order4.totalAmount(), "Date is in the wrong format: dd/mm/yyyy")
    
    #testing fractional number of gallons provided and no date is provided
    def testOrder5(self):
        order5= Order(10.7, "")
        self.assertEqual(order5.totalAmount(), "Date is required")

    #testing fractional number of gallons and incorrect date provided 
    def testOrder6(self):
        order6= Order(10.7,"02/31/2021")
        self.assertEqual(order6.totalAmount(), "Date is in the wrong format: dd/mm/yyyy")
    
    #testing no gallons or no date provided 
    def testOrder7(self):
        order7= Order("","")
        self.assertEqual(order7.totalAmount(), "Date is required")
    
    #Testing a negative number of gallons
    def testOrder8(self):
        order8= Order(-20, "01/10/2021")
        self.assertEqual(order8.totalAmount(), "Number of gallons requested cant be negative")

    #Testing no number of gallons given
    def testOrder9(self):
        order9= Order("", "01/10/2021")
        self.assertEqual(order9.totalAmount(), "Need number of gallons")

    #testing if more than 100 gallons are requested
    def testOrder10(self):
        order10=Order(101, "01/10/2021")
        self.assertEqual(order10.totalAmount(), "Cant request more than 100 gallons")
#if __name__== '__main__':
   # unittest.main()