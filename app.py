from flask import Flask, jsonify, send_file
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
def home(country="China", feature="population"):
    df = pd.read_csv("World Energy Consumption.csv")
    country_data = df[df["country"] == country]
    
    fig = go.Figure(
        go.Scatter(
            x=country_data["year"], 
            y=country_data[feature]
        )
    )
    fig.update_layout(title=feature+" in " + country, xaxis_title="year", yaxis_title=feature)
    fig.write_image("graph.png", format="png", engine="kaleido")
    
    return send_file("graph.png", mimetype='image/png')

if __name__=="__main__":
    app.run(debug=True)
