from flask import Flask

app = Flask(__name__)
#================================
from flask import render_template, request, url_for
from run_delta_ep import proof
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    q1 = request.form['limit']
    q2 = request.form['fx']
    w = proof(q1, q2)
    return str(w)
if __name__ == "__main__":
    app.run(debug=True)
