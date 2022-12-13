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
@coupons.route('/remove', methods=['DELETE'])
def remove_coup():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    couponID = request.form['couponID']
    query = f'DELETE FROM coupon WHERE couponID = \'{couponID}\''
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"


# Get all coupons from the DB
@coupons.route('/coupCust', methods=['GET'])
def get_cust_coup():
    cursor = db.get_db().cursor()
    cursor.execute('select terms as \'Terms:\', endDate as \'End Date:\' from coupon')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

    # Get all coupons from the DB
@coupons.route('/coupRetail', methods=['GET'])
def retail_coup():
    cursor = db.get_db().cursor()
    cursor.execute('select couponID as \'Coupon ID:\', terms as \'Terms:\', endDate as \'End Date:\' from coupon')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response