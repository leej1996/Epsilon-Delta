import flask, flask.views
import run_delta_ep
import delta_ep

app = flask.Flask(__name__)
app.secret_key = "delta"

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')

    def post(self):
        limit =  eval(flask.request.form['expression'])
        fx = eval(flask.request.form['equation'])
        flask.flash(limit)
        flask.flash(fx)
        if '**' in fx:
            q = run_delta_ep.Quadratic(fx, limit)
        else:
            q = run_delta_ep.Linear(fx, limit)
        return self.get()

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])


app.debug = True
app.run()
