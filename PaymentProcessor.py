from PaymentGatway import PremiumPaymentGateway, CheapPaymentGateway, ExpensivePaymentGateway


def payment_process(parameters):
    if parameters['amount'] <= 20:
        cheap_gateway = CheapPaymentGateway()
        if cheap_gateway.is_available:
            return cheap_gateway.pay(parameters)
        else:
            print("Cheap payment gateway is not available.")
    elif 20 < parameters['amount'] <= 500:
        expensive_gateway = ExpensivePaymentGateway()
        if expensive_gateway.is_available:
            return expensive_gateway.pay(parameters)
        else:
            print("Expensive payment gateway is not available, try to pay using cheap payment gateway.")
            cheap_gateway = CheapPaymentGateway()
            if cheap_gateway.is_available:
                return cheap_gateway.pay(parameters)
            else:
                print("Cheap payment gateway is not available.")

    elif parameters['amount'] > 500:
        premium_gateway = PremiumPaymentGateway()
        if premium_gateway.is_available:
            return premium_gateway.pay(parameters)
        else:
            print("Premium payment gateway is not available, trying to pay again")
            for _ in range(3):
                if premium_gateway.is_available:
                    return premium_gateway.pay(parameters)
                else:
                    print("Premium payment gateway is not available, trying to pay again")
