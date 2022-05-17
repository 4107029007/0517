from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port=5050, debug=True)