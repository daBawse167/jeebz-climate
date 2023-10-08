import os
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'

@app.route("/response", methods=["GET"])
def response():
    return ["hello"]

if __name__=="__main__":
    app.run(debug=True)