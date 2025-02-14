from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
    return jsonify(users)

@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Laptop", "price": 999.99},
        {"id": 2, "name": "Smartphone", "price": 599.99},
        {"id": 3, "name": "Headphones", "price": 149.99}
    ]
    return jsonify(products)

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = [
        {"id": 1, "user_id": 1, "product_id": 2, "quantity": 1},
        {"id": 2, "user_id": 2, "product_id": 1, "quantity": 1},
        {"id": 3, "user_id": 3, "product_id": 3, "quantity": 2}
    ]
    return jsonify(orders)

if __name__ == '__main__':
    app.run(debug=True)
