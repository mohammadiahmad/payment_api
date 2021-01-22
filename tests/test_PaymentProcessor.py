from PaymentProcessor import PaymentProcessor
import unittest


class TestPaymentProcessor(unittest.TestCase):

    def test_cheap_payment(self):


        payment_processor = PaymentProcessor()
        result = payment_processor.payment_process({
            "card_holder": "Saman",
            "expiration_date": "2021-09",
            "credit_card_number": "4539148803436467",
            "security_code": "222",
            "amount": 15
        })
        self.assertEqual(result, True)

    def test_expensive_payment(self):


        payment_processor = PaymentProcessor()
        result = payment_processor.payment_process({
            "card_holder": "Saman",
            "expiration_date": "2021-09",
            "credit_card_number": "4539148803436467",
            "security_code": "222",
            "amount": 25
        })
        self.assertEqual(result, True)

    def test_premium_payment(self):


        payment_processor = PaymentProcessor()
        result = payment_processor.payment_process({
            "card_holder": "Saman",
            "expiration_date": "2021-09",
            "credit_card_number": "4539148803436467",
            "security_code": "222",
            "amount": 560
        })
        self.assertEqual(result, True)
