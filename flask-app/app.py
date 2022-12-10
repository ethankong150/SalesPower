###
# Main application interface
###

# import the create app function 
# that lives in src/__init__.py
from src import create_app
from flask import Flask, jsonify
from flask import request
from src.__init__ import db

# create the app object
app = create_app()

db.init_app(app)

@app.route("/test", methods = ['GET'])
def post_form():
    cur=db.get_db().cursor()
    cur.execute('select * from products')
    col_headers=[x[0] for x in cur.description]
    json_data=[]
    the_data=cur.fetchall()
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)    



@app.route("/")
def hello_world():
    return f'<h1>Hello From the Flask-MySQL Connection Tutorial</h1>'    

if __name__ == '__main__':
    # we want to run in debug mode (for hot reloading) 
    # this app will be bound to port 4000. 
    # Take a look at the docker-compose.yml to see 
    # what port this might be mapped to... 
    app.run(debug = True, host = '0.0.0.0', port = 4000)