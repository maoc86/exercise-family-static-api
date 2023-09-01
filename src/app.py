"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

array = [
    {
        "id":1,
        "age": 33,
        "first_name": "John",
        "last_name": "Jakson",
        "lucky_numbers": [7, 13,22]
    },
    {
        "id":2,
        "age": 35,
        "first_name": "Jane",
        "last_name": "Jakson",
        "lucky_numbers": [10, 14,3]
    },
    {
        "id":3,
        "age": 5,
        "first_name": "Jimmy",
        "last_name": "Jakson",
        "lucky_numbers": [1]
    }
]

# Create the jackson family object
jackson_family = FamilyStructure("Jackson", array)

@app.route('/members', methods=['GET'])
def handle_hello():
    members = jackson_family.get_all_members()
    response_body = members


    return jsonify(response_body), 200

# Family member
@app.route('/member', methods=['POST'])
def handle_member():
    
    family_member = request.json

    # Verify data:
    if 'id' not in family_member:
        id = jackson_family._generateId()
    else:
        id= family_member["id"]
    first_name = family_member["first_name"] if 'first_name' in family_member else None
    last_name = family_member["last_name"] if 'last_name' in family_member else jackson_family.last_name
    age = family_member["age"] if 'age' in family_member else None
    lucky_numbers= family_member["lucky_numbers"] if 'lucky_numbers' in family_member else None
    
    # Data type
    if id == None:
        id = jackson_family._generateId()
    elif first_name == None or type(first_name) != str:
        return jsonify("Nombre no puede estar vacio"),400
    elif age == None or not isinstance(age,int):
        return jsonify("Edad no puede estar vacio"),400 
    elif lucky_numbers == None:   
        return jsonify("Numero de la Suerte no puede estar vacio"),400

    # New family member
    jackson_family._members.append(family_member)
    # All list
    return jsonify()


# Get one member
@app.route('/member/<int:id>', methods=['GET'])
def handle_one_member(id):
    one_member =jackson_family.get_member(id)
    if one_member is None:
        return jsonify('Not found'),404
    return jsonify(one_member),200

# Delete one member
@app.route('/member/<int:id>', methods=['DELETE'])
def handle_two_member(id):
    one_member = jackson_family.delete_member(id)
    if one_member is True:
        return jsonify({"done": True}), 200
    else:
        return jsonify(), 400


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
