from marshmallow import Schema, fields, validates, ValidationError
from marshmallow.validate import Length, Range
from datetime import datetime


class ProcessPaymentInputSchema(Schema):
    """ /process-payment - POST

    Parameters:
     - credit_card_number (str)
     - card_holder (str)
     - expiration_date (date)
     - security_code (string)
     - amount (int)
    """
    # the 'required' argument ensures the field exists
    credit_card_number = fields.Str(required=True)
    card_holder = fields.Str(required=True)
    expiration_date = fields.Date(required=True,format='%Y-%m')
    security_code = fields.Str(required=True, validate=Length(min=3, max=3))
    amount = fields.Int(required=True, validate=Range(min=1))

    @validates('expiration_date')
    def is_not_in_past(schema,value):
        """'value' is the date parsed from expiration_date by marshmallow"""
        now = datetime.today().date()
        if value < now:
            raise ValidationError("Expiration date  in not valid.!")

    @validates('security_code')
    def is_digit(schema,value):

        if not value.isdigit():
            raise ValidationError("Security code  in not valid.!")

    @validates('credit_card_number')
    def is_valid_credit_card_number(schema, value):
        card_number=list(value.strip(' '))

        check_digit = card_number.pop()

        # Reverse the order of the remaining numbers
        card_number.reverse()

        processed_digits = []

        for index, digit in enumerate(card_number):
            if index % 2 == 0:
                doubled_digit = int(digit) * 2

                # Subtract 9 from any results that are greater than 9
                if doubled_digit > 9:
                    doubled_digit = doubled_digit - 9

                processed_digits.append(doubled_digit)
            else:
                processed_digits.append(int(digit))

        total = int(check_digit) + sum(processed_digits)

        # Verify that the sum of the digits is divisible by 10
        if total % 10 != 0:
            raise ValidationError("Credit card number  in not valid.!")
