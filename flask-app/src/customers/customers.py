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

# Get specified customer from the DB
@customers.route('/customers', methods=['GET'])
def get_customers():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    cursor.execute('select * from customers')
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

@customers.route('/fName', methods=['POST'])
def update_fname():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    customerID = request.form['customerID']
    fName = request.form['fname']
    query = f'update customers set f_name = \'{fName}\' where customerID = \'{customerID}\''
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"

@customers.route('/lName', methods=['POST'])
def update_lname():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    customerID = request.form['customerID']
    lName = request.form['lname']
    query = f'update customers set l_name = \'{lName}\' where customerID = \'{customerID}\''
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"    

@customers.route('/email', methods=['POST'])
def update_email():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    customerID = request.form['customerID']
    email = request.form['email']
    query = f'update customers set email = \'{email}\' where customerID = \'{customerID}\''
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"    

@customers.route('/password', methods=['POST'])
def update_password():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    customerID = request.form['customerID']
    password = request.form['password']
    query = f'update customers set pass = \'{password}\' where customerID = \'{customerID}\''
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"

@customers.route('/address', methods=['POST'])
def update_address():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    customerID = request.form['customerID']
    address = request.form['address']
    query = f'update customers set street_address = \'{address}\' where customerID = \'{customerID}\''
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"    

@customers.route('/city', methods=['POST'])
def update_city():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    customerID = request.form['customerID']
    city = request.form['city']
    query = f'update customers set city = \'{city}\' where customerID = \'{customerID}\''
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"    

@customers.route('/state', methods=['POST'])
def update_state():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    customerID = request.form['customerID']
    state = request.form['state']
    query = f'update customers set state = \'{state}\' where customerID = \'{customerID}\''
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"   

@customers.route('/zipcode', methods=['POST'])
def update_zipcode():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    customerID = request.form['customerID']
    zipcode = request.form['zipcode']
    query = f'update customers set postal_code = \'{zipcode}\' where customerID = \'{customerID}\''
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"     