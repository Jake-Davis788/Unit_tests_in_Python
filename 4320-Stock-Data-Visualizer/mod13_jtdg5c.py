import unittest
import re
from datetime import datetime

def is_valid_symbol(symbol):
    """Stock symbol must be 1-7 uppercase alpha characters."""
    return bool(re.fullmatch(r"[A-Z]{1,7}", symbol))

def is_valid_chart_type(chart):
    """Chart type must be '1' or '2'."""
    return chart in ['1', '2']

def is_valid_time_series(time):
    """Time series must be '1', '2', '3', or '4'."""
    return time in ['1', '2', '3', '4']

def is_valid_date(date_str):
    """Date must be in format YYYY-MM-DD and a valid date."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestInputValidations(unittest.TestCase):

    def test_symbol_valid(self):
        self.assertTrue(is_valid_symbol("AAPL"))
        self.assertTrue(is_valid_symbol("GOOG"))
        self.assertTrue(is_valid_symbol("T"))
        self.assertFalse(is_valid_symbol("aapl"))          
        self.assertFalse(is_valid_symbol("APPL123"))       
        self.assertFalse(is_valid_symbol("ABCDEFGHI"))    

    def test_chart_type_valid(self):
        self.assertTrue(is_valid_chart_type('1'))
        self.assertTrue(is_valid_chart_type('2'))
        self.assertFalse(is_valid_chart_type('0'))
        self.assertFalse(is_valid_chart_type('3'))
        self.assertFalse(is_valid_chart_type('a'))

    def test_time_series_valid(self):
        self.assertTrue(is_valid_time_series('1'))
        self.assertTrue(is_valid_time_series('2'))
        self.assertTrue(is_valid_time_series('3'))
        self.assertTrue(is_valid_time_series('4'))
        self.assertFalse(is_valid_time_series('5'))
        self.assertFalse(is_valid_time_series('0'))
        self.assertFalse(is_valid_time_series('a'))

    def test_date_format_valid(self):
        self.assertTrue(is_valid_date("2024-04-25"))
        self.assertTrue(is_valid_date("1999-01-01"))
        self.assertFalse(is_valid_date("2024/04/25"))      
        self.assertFalse(is_valid_date("2024-13-01"))      
        self.assertFalse(is_valid_date("2024-02-30"))      
        self.assertFalse(is_valid_date("01-01-2024"))      

if __name__ == '__main__':
    unittest.main()