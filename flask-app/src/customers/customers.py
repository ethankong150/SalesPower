from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


customers = Blueprint('customers', __name__)

#log in authenticator
@customers.route('/login', methods=['GET'])
def login():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    password = request.form['password']
    email = request.form['email']
    query = f'select * from customers where pass = \'{password}\' && email = \'{email}\''
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    if json_data == []:
        raise Exception("Supplied data not found")
    return "Success!"    

#[
# {
#   "successful": "1"
# }    
#]

# Get all customers from the DB
@customers.route('/customers', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    word = 'lakers'
    em = 'lebronjames@gmail.com'
    cursor.execute('select * from customers where pass = \'lakers\' && email = \'lebronjames@gmail.com\'')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    if json_data == []:
        return "Failure."
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for customer with particular userID
@customers.route('/customers/<userID>', methods=['GET'])
def get_customer(userID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from customers where customerID = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response