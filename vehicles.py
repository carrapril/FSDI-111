from app.database import get_db

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


def inser(vehicles_dict):
    value_tuple = (
        vehicles_dict.get("color"),
        vehicles_dict.get("license_plate"),
        vehicles_dict.get("v_type"),
        vehicles_dict.get("owner_id"),
    )
    statement = """
        INSERT INTO vehicles (
            color, 
            license_plate,
            v-type,
            owner_id
        ) VALUES (?, ?, ?, ?)
    """

def scan():
    cursor = get_db().execute("SELECT * FROM vehicles WHERE active=1", ())
    vehicles = cursor.fetchall()
    cursor.close()
    return output_formatter(vehicles)

def select_by_id(pk):
    cursor = get_db().execute("SELECT * FROM vehicles WHERE id=?", (pk,))
    vehicles = cursor.fetchall()
    cursor.close()
    return output_formatter(vehicles)   

def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data.get("color"),
        vehicle_data.get("license_plate"),
        vehicle_data.get("v-type"),
        vehicle_data.get("owner_id"),
        pk
    ) 
    statement = """
        UPDATE vehicles
        SET color=?,
        license_plate=?,
        v-type=?,
        WHERE owner_id=?
    """   
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()         
    cursor.close()
