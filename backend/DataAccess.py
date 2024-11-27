def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="xx",
        database="mydb"
    )



def register_user(name: str, email: str, password: str) -> bool:
   
    query = "INSERT INTO User (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)

    try:
        Connection = get_db_connection()
        cursor = Connection.cursor()
        cursor.execute(query, values)
        Connection.commit()
        return True  
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        Connection.close()



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


def search_glasses(name: str = "", min_price: float = 0, max_price: float = 10000) -> list:
    
    query = """
    SELECT * FROM Glasses
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