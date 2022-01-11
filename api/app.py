# Add this to app.py
from flask import Flask

app = Flask(__name__)

@app.route('/temperature/select')
def select():
        return {
                "data": []
        }

if __name__ == "__main__":
        app.run(host="0.0.0.0",port=4000)
