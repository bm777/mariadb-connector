# Add this to app.py
from flask import Flask
from operation import *

app = Flask(__name__)

@app.route('/temp/select')
def select():
    conn = con()
    temperatures = execute(conn, "SELECT * FROM sensor.temperature;")
    dump = [int(t) for t in temperatures]
    return {
        "data": dump
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000)
