from datetime import date
import mysql


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="xx",
        database="mydb"
    )


def add_user_or_admin(name: str, email: str, password: str, account_type: str, balance=0, role: str = None) -> bool:
    try:

        connection = get_db_connection()
        cursor = connection.cursor()

        account_query = "INSERT INTO Account (Name, Email, Password, Balance,AccountType) VALUES (%s, %s, %s, %s,%s)"
        account_values = (name, email, password, balance, account_type)
        cursor.execute(account_query, account_values)
        account_id = cursor.lastrowid

        if role is None:  # Add to User table
            user_query = "INSERT INTO User (Account_AccountId) VALUES (%s)"
            cursor.execute(user_query, (account_id,))
        else:  # Add to Admin table
            admin_query = "INSERT INTO Admin (Role, Account_AccountId) VALUES (%s, %s)"
            cursor.execute(admin_query, (role, account_id))

        connection.commit()
        return True

    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
        return False

    finally:
        cursor.close()
        connection.close()


def login_user(email: str, password: str) -> dict:
    query = "SELECT * FROM User WHERE email = %s AND password = %s"
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
    SELECT * FROM Product
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


# def add_product(name: str, price: int, product_col: str, description: str, product_col1: str)


def insert_invoice(issuedate: date) -> bool:
    query = "INSERT INTO Invoice (IssueDate) VALUES (%s)"
    values = (issuedate,)

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.exectute(query, values)
        connection.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
        return False
    finally:
        cursor.close()
        connection.close()


def del_product(product_id: int) -> bool:
    query = "Delete FROM Product WHERE idProduct = %s"

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(query, (product_id,))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
        return False
    finally:
        cursor.close()
        connection.close()


def fetch_invoices() -> list:
    query = "Select * FROM Inovice"

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, )
        invoice = cursor.fetchall()
        return invoice if invoice else None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def fetch_invoice_by_id(invoice_id: int) -> dict:
    query = "SELECT * FROM Invoice WHERE idInvoice = %s"

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (invoice_id,))
        invoice = cursor.fetchone()
        return invoice if invoice else None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def get_product_data(product_id):
    query = "SELECT * FROM product WHERE ProductID = %s"
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


def update_account_balance(account_id, new_balance):
    query = "UPDATE account SET Balance = %s WHERE AccountID = %s"
    values = (new_balance, account_id)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def add_product_to_cart(cart_id, product_id, quantity):
    query = """
    INSERT INTO cart (CartID, ProductID, Quantity) 
    VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE 
    Quantity = Quantity + VALUES(Quantity)
    """
    values = (cart_id, product_id, quantity)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def delete_product_from_cart(cart_id, product_id):
    query = "DELETE FROM cart WHERE CartID = %s AND ProductID = %s"
    values = (cart_id, product_id)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
