import mysql.connector
from util.dbproperty import get_property_string

def get_connection():
    props = get_property_string("db.properties")
    return mysql.connector.connect(
        host=props["host"],
        user=props["user"],
        password=props["password"],
        database=props["database"],
        port=int(props["port"])
    )
