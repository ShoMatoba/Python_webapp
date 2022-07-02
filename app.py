from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def inex():
	return 'Response Data'

@app.route('/another')
def another():
	return 'another respon'

@app.route('/try_html')
def try_html():
	return render_template('try_html.html')

@app.route('/show_data', methods=["GET", "POST"])
def show_data():
	return render_template('try_html.html')