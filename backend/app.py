from flask import Flask, request, jsonify
import string, random
import flask_cors
import DataAccess
import models

# from backend.models.admin import Admin
# import backend.models.admin

logged_in_session = {}


def generate_key():
    # Define the pool of characters: uppercase, lowercase, and digits
    characters = string.ascii_letters + string.digits  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    # Randomly select 10 characters from the pool
    api_key = ''.join(random.choices(characters, k=10))
    return api_key


def generate_api_key():
    tmp = generate_key()
    while tmp in logged_in_session:
        tmp = generate_key()
    return tmp


app = Flask(__name__)
flask_cors.CORS(app)


def validate_input(data, required_fields):
    if not data:
        return {"error": "Invalid input. No data provided.", "status": 400}
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return {"error": f"Missing fields: {', '.join(missing_fields)}", "status": 400}
    return None


@app.route('/')
def hello_world():  # put application's code here
    return jsonify('Hello World! iguvhihihihiononhoi'), 201


@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        data = request.get_json()
        validation_error = validate_input(data, ['email', 'password'])
        if validation_error:
            return jsonify({"error": validation_error["error"]}), validation_error["status"]

        email = data['email']
        password = data['password']
        user = DataAccess.login_user(email=email, password=password)

        if not user:
            return jsonify({"error": "Invalid email or password."}), 401

        new_api_key = generate_api_key()
        session_type = 'admin' if user['AccountType'] == 'ADMIN' else 'user'
        logged_in_session[new_api_key] = {"type": session_type, **user, 'account_type': 'ADMIN',
                                          'AccountId': user['idAccount']}

        return jsonify({"message": "Logged in successfully!", "api_key": new_api_key}), 200

    except Exception as e:
        print(e)
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
        if DataAccess.add_user_or_admin(email=email, name=username, password=password,
                                        account_type=account_type,
                                        role="product manger" if str(account_type).upper() == 'ADMIN' else None):

            return jsonify({"message": "User registered successfully!"}), 201
        else:
            return jsonify({"error": "User registration failed!"}), 401
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

        if DataAccess.add_product_with_admin_id(admin_id=logged_in_session[api_key]['AccountId'], name=data['name'],
                                                price=data['price'], description='good product'):
            return jsonify({"message": "Product added successfully!"}), 201
        else:
            return jsonify({"error": "Product addition failed!"}), 401

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
def get_all_invoice():
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
