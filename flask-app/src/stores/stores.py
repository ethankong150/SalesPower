from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


stores = Blueprint('stores', __name__)

#log in authenticator
@stores.route('/login', methods=['GET'])
def login():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    password = request.form['password']
    employeeID = request.form['employeeID']
    query = f'select * from outletemployee where pass = \'{password}\' && employeeID = \'{employeeID}\''
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
@stores.route('/storeData', methods=['GET'])
def get_store_data():
    cursor = db.get_db().cursor()
    cursor.execute('select * from retailoutlets')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
   