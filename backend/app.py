from flask import Flask, request, jsonify
import string, random

logged_in_session = {}


def generate_api_key():
    while tmp := (''.join([random.choice(string.ascii_letters) for _ in range(8)])) in logged_in_session:
        pass
    return tmp


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


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


if __name__ == '__main__':
    app.run()
