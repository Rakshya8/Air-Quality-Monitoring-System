from flask import Flask
from serial import Serial

import mysql.connector

# __name__ name of module
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    # 9600-->bud rate (how many bytes per second)
    with Serial('COM7', 9600) as ser:
        data=ser.readline()

    return "<h1>" + str(data) + "</h1>"

@app.route("/about")
def about_page():
    return "<h1>About Page</h1>"

if __name__=='__main__':
    app.run(debug=True)