from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = [{"id": 1, "user_id": 1, "product": "Book"}, {"id": 2, "user_id": 2, "product": "Laptop"}]
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
