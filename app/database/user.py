"""Database functions for user table"""
from app.database import get_db

def output_formatter(results):       #results will be a tuple of tuples
    out = []                         # empty list
    for result in results:           #For each loop.
        result_dict = {
            "id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "hobbies": result[3],
            "active": result[4]
        }
        out.append(result_dict)
    return out

def output_formatter(vehicles):
    out = []
    for results in vehicles:
        result_dict = {
            "id": results[0],
            "color": results[1],
            "license_plate": results[2],
            "v_type": results[3],
            "owner_id": results[4],
            "active": results[5]
        }  
        out.append(result_dict)
    return out  

def insert(user_dict):
    value_tuple = (
        user_dict.get("first_name"),
        user_dict.get("last_name"),
        user_dict.get("hobbies")
    )
    statement = """
        INSERT INTO user (
            first_name,
            last_name, 
            hobbies
        
        ) VALUES (?, ?, ?)

    """
def inser(vehicles_dict):
    value_tuple = (
        vehicles_dict.get("color"),
        vehicles_dict.get("license_plate"),
        vehicles_dict.get("v_type"),
        vehicles_dict.get("owner_id"),
    )
    statement = """
        INSERT INTO user (
            color, 
            license_plate,
            v-type,
            owner_id
        ) VALUES (?, ?, ?, ?)
    """


    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()     


def scan():
    cursor = get_db().execute("SELECT * FROM user WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id(pk):
    cursor = get_db().execute("SELECT * FROM user WHERE id=?", (pk,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def update(pk, user_data):
    value_tuple = (
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        pk
    )
    statement = """
        UPDATE user
        SET first_name=?,
        last_name=?,
        hobbies=?
        WHERE id=?
    """

def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data.get("color"),
        vehicle_data.get("license_plate"),
        vehicle_data.get("v-type"),
        vehicle_data.get("owner_id"),
        pk
    ) 
    statement = """
        UPDATE vehicle
        SET color=?,
        license_plate=?,
        v-type=?,
        WHERE owner_id=?
    """   

def deactivate(pk, user_data):
    cursor = get_db().execute("SELECT * FROM user WHERE id=?", (pk))  
    
    
    

    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()         
    cursor.close()