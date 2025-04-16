from flask import Blueprint, request, jsonify
from db import db_connection  # assuming you have this helper

order_bp = Blueprint('order_bp', __name__)

# Karen Story 1 
@order_bp.route('/Orders/<int:order_id>/<string:treatment>', methods=['PUT'])
def update_order_treatment(order_id, treatment):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE Orders SET treatment = %s WHERE order_id = %s", (treatment, order_id))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'message': f'Order {order_id} updated with treatment: {treatment}'})

# Karen Story 6 
@order_bp.route('/Orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Orders WHERE order_id = %s", (order_id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if not result:
        return jsonify({'message': 'Order not found'}), 404

    return jsonify(result)
