from Todo import app
from flask import render_template


@app.route('/')
def hello():
    return 'Hello World!'

