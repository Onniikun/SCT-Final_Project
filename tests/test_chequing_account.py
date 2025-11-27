__author__ = "Nathan Natoza"
__version__ = "1.1.4"
__credits__ = ""

import unittest 
from datetime import date
from bank_account.chequing_account import ChequingAccount
# python -m unittest tests/test_chequing_account.py

class TestChequingAccount(unittest.TestCase):
    """
    Testing class for the chequing account file.
    """
    def setUp(self):
        self.chequing = ChequingAccount(777, 320, 10000.00,
                                    date(2024, 12, 12), 120.00, 0.10)
    
    def test_init_valid_arguments_attributes_set(self):
        self.assertEqual(date(2024, 12, 12), 
                    self.chequing._date_created)
        self.assertEqual(120.00, 
                    self.chequing._ChequingAccount__overdraft_limit)
        self.assertEqual(0.10, 
                    self.chequing._ChequingAccount__overdraft_rate)

    def test_init_invalid_overdraft_limit_attribute_valueerror(self):
        chequing = ChequingAccount(777, 320, 10000.00,
                                    date(2024, 12, 12), "non", 0.10)
        self.assertEqual(chequing._ChequingAccount__overdraft_limit,
                          -100.00)

    def test_init_invalid_overdraft_rate_attribute_valueerror(self):
        chequing = ChequingAccount(777, 320, 10000.00,
                                    date(2024, 12, 12), 120.00, "non")
        self.assertEqual(chequing._ChequingAccount__overdraft_rate, 
                         0.05)
    
    def test_init_invalid_date_created_attribute_valueerror(self):
        chequing = ChequingAccount(777, 320, 10000.00,
                                      "non", 120.00, 0.10)
        self.assertEqual(chequing._date_created, date.today())
                         
    def test_get_service_charge_greater_overdraft_limit_balance(self):
        chequing = ChequingAccount(777, 320, 10000.00,
                                    date(2024, 12, 12), 120.00, 0.10)
        self.assertEqual(chequing.get_service_charges(), 
                        0.5)

    def test_get_service_charge_less_than_overdraft_limit_balance(self):
        chequing = ChequingAccount(777, 320, 100.00,
                                        date(2024, 12, 12), 120.00, 0.10)
        self.assertEqual(chequing.get_service_charges(), 
                         3.0)

    def test_get_service_charge_equal_overdraft_limit_balance(self):
        chequing = ChequingAccount(777, 320, 120.00,
                                        date(2024, 12, 12), 120.00, 0.10)
        self.assertEqual(chequing.get_service_charges(), 
                         0.5)

    def test_str_valid_inputs_formatted_string_return(self):
        expected = (f"Account Number: 777 Balance: $10,000.00\n" \
                    f"Overdraft limit: $120.00 Overdraft rate: 10.00% " \
                    f"Account Type: Chequing.")
        self.assertEqual(expected, str(self.chequing)) 



            
    