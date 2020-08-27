from flask import Flask, request, jsonify, make_response, render_template
from flask_cors import CORS, cross_origin
#import pandas as pd

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
cors = CORS(app)

@app.route('/')
def home():
    return render_template('index.html') 

    

if __name__ == "__main__":
    app.run()        