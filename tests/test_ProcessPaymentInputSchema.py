import unittest
from ProcessPaymentInputSchema import ProcessPaymentInputSchema


class TestPaymentProcessor(unittest.TestCase):

    def test_credit_card_number(self):
        payment_process_schema = ProcessPaymentInputSchema()

        '''When credit card is valid'''
        data = {
            "card_holder": "Saman",
            "expiration_date": "2021-09",
            "credit_card_number": "4539148803436467",
            "security_code": "222",
            "amount": 550
        }
        errors = payment_process_schema.validate(data)
        self.assertEqual(errors, {})

        '''When credit card is not valid'''
        data = {
            "card_holder": "Saman",
            "expiration_date": "2021-09",
            "credit_card_number": "4539148803436877",
            "security_code": "222",
            "amount": 550
        }
        errors = payment_process_schema.validate(data)
        self.assertNotEqual(errors, {})

    def test_security_code(self):
        payment_process_schema = ProcessPaymentInputSchema()

        '''When security code is valid'''
        data = {
            "card_holder": "Saman",
            "expiration_date": "2021-09",
            "credit_card_number": "4539148803436467",
            "security_code": "222",
            "amount": 550
        }
        errors = payment_process_schema.validate(data)
        self.assertEqual(errors, {})

        '''When security code is not valid'''
        data = {
            "card_holder": "Saman",
            "expiration_date": "2021-09",
            "credit_card_number": "4539148803436467",
            "security_code": "22g",
            "amount": 550
        }
        errors = payment_process_schema.validate(data)
        self.assertNotEqual(errors, {}, "Security code is not valid")

    def test_expiration_date(self):
        payment_process_schema = ProcessPaymentInputSchema()

        '''When expiration date is valid'''
        data = {
            "card_holder": "Saman",
            "expiration_date": "2021-09",
            "credit_card_number": "4539148803436467",
            "security_code": "222",
            "amount": 550
        }
        errors = payment_process_schema.validate(data)
        self.assertEqual(errors, {})

        '''When expiration date is not valid'''
        data = {
            "card_holder": "Saman",
            "expiration_date": "2018-09",
            "credit_card_number": "4539148803436467",
            "security_code": "22g",
            "amount": 550
        }
        errors = payment_process_schema.validate(data)
        self.assertNotEqual(errors, {}, "Expiration code is not valid")

    def test_amount_value(self):
        payment_process_schema = ProcessPaymentInputSchema()

        '''When amount value is valid'''
        data = {
            "card_holder": "Saman",
            "expiration_date": "2021-09",
            "credit_card_number": "4539148803436467",
            "security_code": "222",
            "amount": 56
        }
        errors = payment_process_schema.validate(data)
        self.assertEqual(errors, {})

        '''When amount value is not valid'''
        data = {
            "card_holder": "Saman",
            "expiration_date": "2018-09",
            "credit_card_number": "4539148803436467",
            "security_code": "22g",
            "amount": -10
        }
        errors = payment_process_schema.validate(data)
        self.assertNotEqual(errors, {}, "Amount value is not valid")
