import unittest
from kalkulator import *

class TestMyMethods ( unittest.TestCase ):
    
    def test_pusty_string_zwraca_zero ( self ):
        self.assertEqual(add(""), 0)
    
    def test_1_liczby ( self ):
         self.assertEqual(add("3"), 3)
         self.assertEqual(add("6"), 6)
         self.assertEqual(add("2"), 2)

    def test_dodawania_2_liczb ( self ):
        self.assertEqual(add("4,6"), 10)
        self.assertNotEqual(add("4,6"), 46)
    
    def test_wprowadzanie_wielu_liczb(self):
        self.assertEqual(add("1,2,3,4,5"), 15)
    #def znak_w_funkcji(self):
    #    with self.assertRaises(ValueError):
    #        add("ada")

    

unittest.main()
