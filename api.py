#load the modules
import os
import threading
from flask import Flask, render_template
from pyngrok import ngrok
from deep_forest import deep_forest

os.environ['FLASK_ENV'] = 'development'
app = Flask(__name__)
port = 5000
# kill -9 "$(pgrep ngrok)"
# ngrok.set_auth_token('2Md5DkdvkhXqk0OcQBTWaUNp2fD_5na9nhxEwhuJWZFcx891f')
# public_url = ngrok.connect(port).public_url
# print(public_url)
# app.config['BASE_URL'] = public_url

@app.route('/')
def index():
    data = deep_forest()
    print(data)
    return render_template('index.html', image = f"<img src='data:image/png;base64,{data}'/>")

if __name__ == '__main__':
    # run application on the local development server
    app.run()