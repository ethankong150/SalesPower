from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


brands = Blueprint('brands', __name__)

#log in authenticator
@brands.route('/login', methods=['GET'])
def login():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    password = request.form['password']
    employeeID = request.form['employeeID']
    query = f'Select * from brandemployee where pass = \'{password}\' && employeeID = \'{employeeID}\''
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    if json_data == []:
        raise Exception("Supplied data not found")
    return "Success!"  

# Get all brand data from the DB
@brands.route('/brandData', methods=['GET'])
def get_brand_data():
    cursor = db.get_db().cursor()
    cursor.execute('select * from brands')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
