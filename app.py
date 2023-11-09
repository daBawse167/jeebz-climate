from base64 import encodebytes
from PIL import Image

import io
import os
import numpy as np
import plotly as px
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'

@app.route("/response", methods=["GET", "POST"])
def home(country="China", feature="population"):
    df = pd.read_csv("World Energy Consumption.csv")
    country_data = df[df["country"] == country]

    #plt.plot(country_data["year"], country_data[feature])
    #plt.savefig("graph.png")

    pil_img = Image.open("graph.png", mode="r")
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format="PNG")
    encoded_image = encodebytes(byte_arr.getvalue()).decode("ascii")

    response = { 'Status' : 'Success', 'message': 'message', 'ImageBytes': encoded_image}
    print(response)
    return jsonify(response)

if __name__=="__main__":
    app.run(debug=True)
