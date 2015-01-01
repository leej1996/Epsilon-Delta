from flask import Flask

app = Flask(__name__)
#================================
from flask import render_template, request, url_for
from run_delta_ep import proof
import jinja2

@app.template_filter('proofs')
def proofs(limit, fx):
    x = int(limit)
    return proof(x, fx)
app.jinja_env.filters['proofs'] = proofs


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    q1 = request.form['limit']
    q2 = request.form['fx']
    return render_template('answer.html')


if __name__ == "__main__":
    app.run(debug=True)
