from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/chat',methods=['GET'])
def test():
    return "heste hest"