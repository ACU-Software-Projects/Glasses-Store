from flask import Flask, request, jsonify
import string, random
import flask_cors
from jinja2.utils import missing
import mysql.connector

logged_in_session = {}


def generate_api_key():
    while tmp := (''.join([random.choice(string.ascii_letters) for _ in range(8)])) in logged_in_session:
        pass
    return tmp


app = Flask(__name__)
flask_cors.CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return jsonify('Hello World! iguvhihihihiononhoi'), 201


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        # Parse JSON data from request
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400

        # Validate required fields
        required_fields = ['email', 'password']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        email = data['email']
        password = data['password']

        new_api_key = generate_api_key()

        # TODO Other data from database
        logged_in_session[new_api_key] = {'email': email, 'password': password}

        return jsonify({"message": "User registered successfully!", "api_key": new_api_key}), 201

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        # Parse JSON data from request
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400

        # Validate required fields
        required_fields = ['email', 'password', 'username', 'account_type']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        email = data['email']
        username = data['username']
        account_type = data['account_type']
        password = data['password']
        print(email, username, account_type, password)
        # TODO call database to add new account
        # TODO check if there user with same username or email

        return jsonify({"message": "User registered successfully!"}), 201

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400

        # Validate required fields
        required_fields = ['api_key']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        api_key = data['api_key']
        if api_key not in logged_in_session:
            return jsonify({"error": f"API key {api_key} not found."}), 401

        del logged_in_session[api_key]
        return jsonify({"message": "User logged out!"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/admin/product/add', methods=['GET', 'POST'])
def add_product():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key', 'name', 'price', 'quantity']

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        api_key = data['api_key']
        if api_key not in logged_in_session:
            return jsonify({"error": f"API key {api_key} not found."}), 401

        if logged_in_session[api_key]['account_type'] != 'ADMIN':
            return jsonify({"error": f"API key {api_key} not Admin."}), 401

        # TODO call database to add product

        return jsonify({"message": "Product added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


app.route('/product/', methods=['GET'])


def get_products():
    # TODO Retrieve all products from database in data var
    data = ""
    return jsonify(data), 200


app.route('/product/<int:product_id>', methods=['GET'])


def get_product(product_id):
    # TODO check product in database by id and get it's all data
    # if product_id not in ##DATABASE##:
    #   return error 404
    productInfo = ""
    return jsonify(productInfo), 200


app.route('/product/<int:product_id>', methods=['DELETE'])


def delete_product(product_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key', 'product_id']

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        api_key = data['api_key']
        if api_key not in logged_in_session:
            return jsonify({"error": f"API key {api_key} not found."}), 401

        if logged_in_session[api_key]['account_type'] != 'ADMIN':
            return jsonify({"error": f"API key {api_key} not Admin."}), 401

        # TODO send request to database to delete product using product_id and check if product exisit

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/payment/deposit', methods=['POST'])
def deposit():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key', 'amount']

        api_key = data['api_key']
        amount = data['amount']

        # TODO make deposit in database
        return jsonify({"message": "Deposit successful!"}), 201
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/payment/withdraw', methods=['POST'])
def withdraw():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key', 'amount']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        api_key = data['api_key']
        amount = data['amount']

        # TODO make withdraw in database

        return jsonify({"message": "withdraw successful!"}), 201
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/user/cart/add_product', methods=['POST'])
def add_cart():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key', 'product_id']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        # TODO add product to cart database

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


# TODO make function that create Invoice
@app.route('/user/cart/checkout', methods=['POST'])
def checkout():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key', 'cart_id']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        api_key = data['api_key']

        if api_key not in logged_in_session:
            return jsonify({"error": f"API key {api_key} not found."}), 401

        # TODO make invoice in the data base
        # get it's data
        # return it's data to the frontend

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/admin/invoice', methods=['GET', 'POST'])
def get_invoice():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        api_key = data['api_key']
        if logged_in_session[api_key]['account_type'] != 'ADMIN':
            return jsonify({"error": f"API key {api_key} not Admin."}), 401

        # TODO get all invoices from database

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/admin/invoice/<int:invoice_id>', methods=['GET'])
def get_invoice(invoice_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        api_key = data['api_key']
        if logged_in_session[api_key]['account_type'] != 'ADMIN':
            return jsonify({"error": f"API key {api_key} not Admin."}), 401
        # TODO get invoice from database
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/user/invoice/<int:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        api_key = data['api_key']
        if logged_in_session[api_key]['account_type'] != 'USER':
            return jsonify({"error": f"API key {api_key} not user."}), 401
        # TODO get invoice from database
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/user/invoice/', methods=['GET'])
def get_user_invoice():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        api_key = data['api_key']
        if logged_in_session[api_key]['account_type'] != 'USER':
            return jsonify({"error": f"API key {api_key} not user."}), 401
        # TODO get all user invoice from database
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
