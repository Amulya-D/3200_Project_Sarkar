from flask import Blueprint, request, jsonify
from db import db_connection

orderdetails_bp = Blueprint('orderdetails_bp', __name__)

# Karen Story 5

@orderdetails_bp.route('/OrderDetails', methods=['PUT'])
def update_payment_method():
    data = request.json
    order_id = data.get('order_id')
    payment_method = data.get('payment_method')

    if payment_method not in ['cash', 'card']:
        return jsonify({'error': 'Invalid payment method. Choose "cash" or "card".'}), 400

    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE OrderDetails SET payment_method = %s WHERE order_id = %s", (payment_method, order_id))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'message': f'Payment method updated to {payment_method}'})


