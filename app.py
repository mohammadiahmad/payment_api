from flask import Flask, request, abort, jsonify

from ProcessPaymentInputSchema import ProcessPaymentInputSchema
from PaymentProcessor import PaymentProcessor



app = Flask(__name__)

payment_process_schema = ProcessPaymentInputSchema()
payment_processor=PaymentProcessor()

@app.route('/process-payment', methods=['POST'])
def process_payment():
    errors = payment_process_schema.validate(request.get_json())
    if errors:
        return jsonify(errors), 400

    validated_parameters = payment_process_schema.load(request.get_json())
    try:
        status = payment_processor.payment_process(validated_parameters)
        if status:
            return jsonify({"message": "payment procces success."}), 200
        else:
            return jsonify({"message": "payment gateway is not available."}), 500
    except:
        return jsonify({"message": "Unknown error"}), 500


if __name__ == '__main__':
    app.run()
