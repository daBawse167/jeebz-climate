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
def home():
    country = request.args.get("country", None)
    feature = request.args.get("feature", None)
    
    country_data = pd.read_csv("https://raw.githubusercontent.com/daBawse167/jeebz-climate-data/main/"+country+"%20data.csv").drop([
    'Unnamed: 0'], axis=1)
    
    feature_column = country_data[feature].dropna()
    idx = feature_column.index
    year_column = country_data["Year"][idx]
    
    fig = go.Figure(
        go.Scatter(
            x=year_column,
            y=feature_column
        )
    )
    fig.update_layout(title=feature+" in " + country, xaxis_title="year", yaxis_title=feature)
    fig.write_image("graph.png", format="png", engine="kaleido")
    
    return send_file("graph.png", mimetype='image/png')

if __name__=="__main__":
    app.run(debug=True)
