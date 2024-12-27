from datetime import date
import mysql
from mysql.connector import connect


def get_db_connection():
    return connect(
        host="localhost",
        user="mostafa",
        password="12345678",
        database="mydb"
    )


def add_user_or_admin(name: str, email: str, password: str, account_type: str, balance=0, role: str = None) -> bool:
    try:

        connection = get_db_connection()  # create connection with database
        cursor = connection.cursor()

        account_query = "INSERT INTO account (Name, Email, Password, Balance,AccountType) VALUES (%s, %s, %s, %s,%s)"
        account_values = (name, email, password, balance, account_type)
        cursor.execute(account_query, account_values)
        account_id = cursor.lastrowid  # get the last inserted id

        if role is None:  # Add to User table
            user_query = "INSERT INTO user (Account_AccountId) VALUES (%s)"
            cursor.execute(user_query, (account_id,))
        else:  # Add to Admin table
            admin_query = "INSERT INTO admin (Role, Account_AccountId) VALUES (%s, %s)"
            cursor.execute(admin_query, (role, account_id))

        connection.commit()  # apply changes to database
        return True

    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
        return False

    finally:
        cursor.close()
        connection.close()


def login_user(email: str, password: str) -> dict:
    query = "SELECT * FROM account WHERE Email = %s AND Password = %s"
    values = (email, password)

    try:
        Connection = get_db_connection()
        cursor = Connection.cursor(dictionary=True)
        cursor.execute(query, values)
        user = cursor.fetchone()
        return user if user else None
    except Exception as e:
        print(f"Error: {e}")
        return None  # Return None if an error occurs
    finally:
        cursor.close()
        Connection.close()


def search_product(name: str = "", min_price: float = 0, max_price: float = 10000) -> list:
    query = """
    SELECT * FROM product
    WHERE name LIKE %s AND price BETWEEN %s AND %s
    """
    values = (f"%name%", min_price, max_price)

    try:
        Connection = get_db_connection()
        cursor = Connection.cursor(dictionary=True)
        cursor.execute(query, values)
        glasses = cursor.fetchall()
        return glasses if glasses else None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        Connection.close()


def get_product_data(product_id):
    query = "SELECT * FROM product WHERE idProduct = %s"
    values = (product_id,)
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, values)
        product = cursor.fetchone()
        return product
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return None


def get_all_products():
    query = "SELECT * FROM product"
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        products = cursor.fetchall()
        return products
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return None


def update_account_balance(account_id, new_balance):
    query = "UPDATE account SET Balance = %s WHERE idAccount = %s"
    values = (new_balance, account_id)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False


def fetch_user_products(account_id: int) -> list:
    query = """SELECT * FROM user_products where IdAccount = %s"""

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (account_id,))
        invoices = cursor.fetchall()
        return invoices if invoices else []
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        cursor.close()
        connection.close()


def add_product_with_admin_id(name: str, price: int, description: str, admin_id: int, image_src) -> bool:
    query = "INSERT INTO product (Name, price, description, Admin_idAdmin,ImageSrc) VALUES (%s, %s, %s, %s,%s)"
    values = (name, price, description, admin_id, image_src)

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        connection.close()


def get_user_data(account_id):
    query = "SELECT * FROM account WHERE idAccount = %s"
    values = (account_id,)
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, values)
        user = cursor.fetchone()
        return user

    finally:
        cursor.close()
        connection.close()
    return None


def buy_product(account_id: int, product_id: int) -> bool:
    try:
        product = get_product_data(product_id)
        if not product:
            print("Product not found!")
            return False

        total_price = product['price']
        user = get_user_data(account_id)

        if not user:
            print("User not found!")
            return False

        if user['Balance'] < total_price:
            print("Insufficient balance!")
            return False

        new_balance = user['Balance'] - total_price
        update_account_balance(account_id, new_balance)

        query = "INSERT INTO user_products (IdAccount, IdProduct) VALUES (%s, %s);"
        values = (account_id, product_id)
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, values)
        connection.commit()
        tmp = cursor.fetchone()
        print(tmp)
    except Exception as e:
        print(e)
        return False
    return True


if __name__ == '__main__':
    buy_product(1, 1)
