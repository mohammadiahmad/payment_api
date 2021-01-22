from Setting import PaymentGatewayStatus

class CheapPaymentGateway:
    def __init__(self):
        self.is_available = PaymentGatewayStatus.CheapPaymentGateway

    def set_staus(self, status):
        self.is_available = status

    def pay(self, parameters):
        if self.is_available:
            print("Payment processed successfully")
            return True
        else:
            print("Payment processed failed!")
            return False


class ExpensivePaymentGateway:
    def __init__(self):
        self.is_available = PaymentGatewayStatus.ExpensivePaymentGateway

    def set_staus(self, status):
        self.is_available = status

    def pay(self, parameters):
        if self.is_available:
            print("Payment processed successfully")
            return True
        else:
            print("Payment processed failed!")
            return False


class PremiumPaymentGateway:
    def __init__(self):
        self.is_available = PaymentGatewayStatus.PremiumPaymentGateway

    def set_staus(self, status):
        self.is_available = status

    def pay(self, parameters):
        if self.is_available:
            print("Payment processed successfully")
            return True
        else:
            print("Payment processed failed!")
            return False
