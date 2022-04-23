import requests

URL = "http://127.0.0.1:5000/users/"
SAMPLE_USER = {
    "first_name": "John",
    "last_name": "Doe",
    "hobbies": "Playing golf",
    "color": "red",
    "license_plate": "1234",
    "v_type": "Truck",
}

def create_user (first_name, last_name, hobbies, color, license_plate, v_type):
    user_data = SAMPLE_USER
    user_data["first_name"] = first_name
    user_data["last_name"] = last_name
    user_data["hobbies"] = hobbies
    user_data["color"] = color
    user_data["license_plate"] = license_plate
    user_data["v_type"] = v_type 

    response = requests.post(URL, json=user_data)
    if response.status_code == 204:
        print("Successfully created a new user.")
    else: 
        print("Something went wrong while trying to create a user.")    

if __name__ == "__main__":
    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")
    hobbies = input("Enter hobbies: ") 
    color = input("Enter vehicle color: ")
    license_plate = input("Enter license plate: ")
    v_type = input("Enter vehicle_type: ")

    create_user(first_name, last_name, hobbies, color, license_plate, v_type)       