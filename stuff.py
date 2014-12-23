from flask import Flask
import run_delta_ep

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello worls'


if __name__ == '__main__':
    app.run()
