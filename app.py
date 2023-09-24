from flask import Flask, request
from waitress import serve

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    name = request.args.get('name')
    if name is None:
        name = 'Recruto!'
    message = request.args.get('message')
    if message is None:
        message = 'Давай дружить!'
    return f'Hello, {name} \n {message}'


if __name__ == '__main__':
    app.run(debug= True, host = '192.168.0.26', port=80)
