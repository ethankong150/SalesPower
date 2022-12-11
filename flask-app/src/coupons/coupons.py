from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


coupons = Blueprint('coupons', __name__)

#add a coupon
@coupons.route('/addCoup', methods=['POST'])
def add_coup():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    couponID = request.form['couponID']
    terms = request.form['terms']
    endDate = request.form['endDate']
    query = f'INSERT INTO coupon(couponID, terms, endDate) VALUES(\"{couponID}\", \"{terms}\", \"{endDate}\")'
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"

#remove a coupon
@coupons.route('/removeCoup', methods=['POST'])
def remove_coup():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    couponID = request.form['couponID']
    query = f'DELETE FROM coupon WHERE couponID = \'{couponID}\''
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"


# Get all coupons from the DB
@coupons.route('/coupons', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('select * from coupon')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for customer with particular userID
@coupons.route('/coupons/<coupID>', methods=['GET'])
def get_coupons(userID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from coupon where couponID = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response