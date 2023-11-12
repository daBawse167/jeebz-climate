from flask import Flask, jsonify, send_file, request
from base64 import encodebytes
from PIL import Image

import io
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'

@app.route("/response", methods=["GET", "POST"])
def home(country, feature):
    country = request.args.get("country", None)
    feature = request.args.get("feature", None)
    
    df = pd.read_csv("World Energy Consumption.csv")
    country_data = df[df["country"] == country]
    
    plt.plot(country_data["year"], country_data[feature])
    plt.xlabel("year")
    plt.ylabel(feature)
    plt.title(feature+" in "+country)
    
    plt.savefig("graph.png")
    
    return send_file("graph.png", mimetype='image/png')

if __name__=="__main__":
    app.run(debug=True)
