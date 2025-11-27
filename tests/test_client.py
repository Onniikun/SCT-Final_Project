"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
__author__ = "ACE Faculty"
__version__ = "1.4.0"
__credits__ = "Nathan Natoza"

import unittest
from client.client import Client


class TestClient(unittest.TestCase):
    """
    Testing class for the client flie
    """
    def setUp(self):
        self.client = Client(404, "Nathan", "Natoza", "NatNat@email.ca")

    def test_init_valid_arguments_attributes_set(self):

        client = Client(404, "Nathan", "Natoza", "NatNat@email.ca")

        self.assertEqual(404, client._Client__client_number)
        self.assertEqual("Nathan", client._Client__first_name)
        self.assertEqual("Natoza", client._Client__last_name)
        self.assertEqual("NatNat@email.ca", client._Client__email_address)

    def test_init_empty_client_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            client = Client("", "Nathan", "Natoza", "NatNat@email.ca")
    
    def test_init_empty_first_name_raises_valueerror(self):
        with self.assertRaises(ValueError):
            client = Client(404, "", "Natoza", "NatNat@email.ca")

    def test_init_empty_last_name_raises_valueerror(self):
        with self.assertRaises(ValueError):
            client = Client(404, "Nathan", "", "NatNat@email.ca")
    
    def test_init_invalid_email_return_default_email_return(self):
        # Arrange
        invalid_email = "NatNat@emailca"
        # Act 
        client = Client(404, "Nathan", "Natoza", invalid_email)    
        # Assert
        self.assertEqual(self.client.email_address, "NatNat@email.ca")

#--PEP8-Standards-Line--------------------------------------------------------

    def test_client_number_accessor_valid_return(self):
        self.assertEqual(404, self.client.client_number)

    def test_first_name_accessor_valid_return(self):
        self.assertEqual("Nathan", self.client.first_name)

    def test_last_name_accessor_valid_return(self):
        self.assertEqual("Natoza", self.client.last_name)

    def test_email_address_accessor_valid_return(self):
        self.assertEqual("NatNat@email.ca", self.client.email_address)

    def test_str_valid_inputs_formatted_string_return(self):
        expected = ("Nathan, Natoza, [404] - NatNat@email.ca")

        self.assertEqual(expected, str(self.client))
    

    
