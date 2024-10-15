import pyodbc
from util.property_util import PropertyUtil

class DBConnection:
    @staticmethod
    def getConnection():
        try:
            conn_string = PropertyUtil.getConnectionString()
            connection = pyodbc.connect(conn_string)
            print("Connection established successfully.")
            return connection
        except Exception as e:
            print(f"Connection failed: {e}")
            return None
