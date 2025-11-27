__author__ = "Nathan Natoza"
__version__ = "1.1.4"
__credits__ = ""

import unittest 
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount
# python -m unittest tests/test_investment_account.py

class TestInvestmentAccount(unittest.TestCase):
    """
    Testing class for the investment account file.
    """
    def setUp(self):
        self.investment = InvestmentAccount(777, 320, 10000.00,
                                            date(2024, 12, 12), 2.00)
        
        self.old_date = date.today() - timedelta(days = 11 * 365.25)
        self.exactly_ten = date.today() - timedelta(days = 10 * 365.25)
        self.new_date = date.today() - timedelta(days = 9 * 365.25)

    def test_init_valid_arguments_attributes_set(self):
        self.assertEqual(date(2024, 12, 12), self.investment._date_created)
        self.assertEqual(2.00, 
                    self.investment._InvestmentAccount__management_fee)

    def test_init_invalid_management_fee_datatype(self):
        investment_account = InvestmentAccount(777, 320, 10000.00,
                                            date(2024, 12, 12), "non")
        self.assertEqual(
            investment_account._InvestmentAccount__management_fee, 2.55)

    def test_get_service_charge_creation_date_more_than_10YRS_limit_balance(self):
        investment_account = InvestmentAccount(777, 320, 10000.00,
                                            self.old_date, 2.00)
        self.assertEqual(investment_account.get_service_charges(), 0.50)

    def test_get_service_charge_creation_date_equal_than_10YRS_limit_balance(self):
        investment_account = InvestmentAccount(777, 320, 10000.00,
                                            self.exactly_ten, 2.00)
        self.assertEqual(investment_account.get_service_charges(), 2.5)

    def test_get_service_charge_creation_date_less_than_10YRS_limit_balance(self):
        investment_account = InvestmentAccount(777, 320, 10000.00,
                                            self.new_date, 2.00)
        self.assertEqual(investment_account.get_service_charges(), 2.5)

    def test_str_display_management_fee_within_more_then_10YRS_return(self):
        investment_account = InvestmentAccount(777, 320, 10000.00,
                                            date(2015, 2, 1), 2.00)
        expected = (f"Account Number: 777 Balance: $10,000.00\n"\
                    f"Date Created: 2015-02-01 Management Fee: Waived "\
                    f"Account Type: Investment.")
        self.assertEqual(expected, str(investment_account)) 
    
    def test_str_display_management_fee_within_less_then_10YRS_return(self):
        investment_account = InvestmentAccount(777, 320, 10000.00,
                                            date(2024, 12, 12), 2.00)
        expected = (f"Account Number: 777 Balance: $10,000.00\n" \
                    f"Date Created: 2024-12-12 Management Fee: $2.00 "\
                    f"Account Type: Investment.")
        self.assertEqual(expected, str(investment_account)) 