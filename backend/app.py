from flask import Flask, request, jsonify
import string, random
import flask_cors
import DataAccess

logged_in_session = {}


def generate_random_string():
    # Generate a random string
    characters = string.ascii_letters + string.digits
    api_key = ''.join(random.choices(characters, k=10))
    return api_key


def generate_api_key():
    # Generate a random unique api key
    tmp = generate_random_string()
    while tmp in logged_in_session:
        tmp = generate_random_string()
    return tmp


app = Flask(__name__)
flask_cors.CORS(app)


# def update_api_key(api_key):
#     return DataAccess.get_user_data(logged_in_session[api_key]['AccountId'])


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


@app.route('/account/data', methods=['GET', 'POST'])
def get_user_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input. No data provided."}), 400

    validation_error = validate_input(data, ['api_key'])
    try:
        account_id=logged_in_session[data['api_key']]['AccountId'] # get Account id from session

        tmp = DataAccess.get_user_data(account_id) # get updated data from data access layer

        return jsonify(tmp), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500
    if validation_error:
        return jsonify({"error": validation_error["error"]}), validation_error["status"]
    return jsonify(logged_in_session[data['api_key']]), 200


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

        return jsonify({"message": "Logged in successfully!", "api_key": new_api_key,
                        "account_type": session_type
                        }), 200

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
        if missing_fields: # check missing fields
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
        required_fields = ['api_key', 'name', 'price', 'image', 'quantity']

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        api_key = data['api_key']
        if api_key not in logged_in_session:
            return jsonify({"error": f"API key {api_key} not found."}), 401

        if logged_in_session[api_key]['account_type'] != 'ADMIN':
            return jsonify({"error": f"API key {api_key} not Admin."}), 401
        if DataAccess.add_product_with_admin_id(admin_id=logged_in_session[api_key]['AccountId'], name=data['name'],
                                                price=data['price'], description='good product',
                                                image_src=data['image']):
            return jsonify({"message": "Product added successfully!"}), 201
        else:
            print("data acess error")
            return jsonify({"error": "Product addition failed!"}), 401

    except Exception as e:
        print(e)
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/products', methods=['GET'])
def get_products():
    data = DataAccess.get_all_products()
    return jsonify(data), 200


@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    productInfo = DataAccess.get_product_data(product_id)
    if productInfo == None:
        return jsonify({"error": "Product not found."}), 404
    return jsonify(productInfo), 200


@app.route('/payment/deposit', methods=['POST', 'GET'])
def deposit():
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
        if api_key not in logged_in_session:
            return jsonify({"error": f"API key {api_key} not found."}), 401
        user_data = logged_in_session[api_key]

        if DataAccess.update_account_balance(account_id=user_data['AccountId'],
                                             new_balance=user_data['Balance'] + amount):
            user_data['Balance'] += amount
            return jsonify({"message": "Deposit successful!"}), 201
        else:
            raise Exception("Failed to update account balance.")
    except Exception as e:
        print(e)
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/payment/withdraw', methods=['POST', 'GET'])
def withdraw():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key', 'amount']

        api_key = data['api_key']
        amount = data['amount']
        if api_key not in logged_in_session:
            return jsonify({"error": f"API key {api_key} not found."}), 401
        user_data = logged_in_session[api_key]
        if user_data['Balance'] < amount:
            return jsonify({"error": "Insufficient balance!"}), 400
        if DataAccess.update_account_balance(account_id=user_data['AccountId'],
                                             new_balance=user_data['Balance'] - amount):
            user_data['Balance'] -= amount
            return jsonify({"message": "Withdraw successful!"}), 201
        else:
            raise Exception("Failed to update account balance.")
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/user/checkout_product', methods=['POST'])
def checkout():
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

        user_data = logged_in_session[api_key]
        if DataAccess.buy_product(product_id=data['product_id'], account_id=user_data['AccountId']):
            return jsonify({"message": "Product bought successfully!"}), 201
        else:
            return jsonify({"error": "Failed to buy product!"}), 401
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


@app.route('/user/products', methods=['GET', 'POST'])
def get_user_products():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. No data provided."}), 400
        required_fields = ['api_key']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        api_key = data['api_key']
        if logged_in_session[api_key]['AccountType'] != 'USER':
            return jsonify({"error": f"API key {api_key} not user."}), 401
        # TODO get all user invoice from database
        tmp = DataAccess.fetch_user_products(logged_in_session[api_key]['AccountId'])
        return jsonify(tmp), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == '__main__':
    print("asdfghjkl")
    app.run(host='0.0.0.0', debug=True)
