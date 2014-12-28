from flask import Flask

app = Flask(__name__)
#================================
from flask import render_template, request
from run_delta_ep import proof
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz_answers', methods=['POST'])
def quiz_answers():
    q1 = request.form['limit']
    q2 = request.form['fx']

    return proof(q1, q2)
if __name__ == "__main__":
    app.run(debug=True)
