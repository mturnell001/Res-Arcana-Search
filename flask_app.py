from flask import Flask, json, render_template, url_for
import os

app = Flask(__name__)




@app.route('/')
def home():
    """
    This renders the home page/base route
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    url_for('static/data', filename='RA.json')