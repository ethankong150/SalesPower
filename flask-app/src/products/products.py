from flask import Blueprint, request, jsonify, make_response
import json
from src import db


products = Blueprint('products', __name__)

# get the top 5 products from the database
@products.route('/byPopularity')
def get_most_pop_products():
    cursor = db.get_db().cursor()
    query = '''
        SELECT p.productID as \'Product ID:\', productName as \'Product Name:\', count(*) as \'Total Orders:\'
        FROM products p JOIN orders od on p.productID = od.productID
        GROUP BY p.productID, productName
        ORDER BY \'Total Orders:\' DESC;
    '''
    cursor.execute(query)
       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)