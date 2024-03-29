# Add this to app.py
from flask import Flask
from operation import *

app = Flask(__name__)

@app.route('/temp/')
def select():
    conn = con()
    temperatures = execute(conn, "SELECT * FROM sensor.temperature;")
    dump = [int(t) for t in temperatures]
    return {
        "data": dump
    }

@app.route('/temp/add/<value>')
def add(value):
    conn = con()
    create_(conn, "insert into sensor.temperature (value) values ({});".format(value))
    return {
        "data": "ok"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000)
