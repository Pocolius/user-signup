from flask import Flask, render_template
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup_form.html')

app.run()