from flask import Flask, render_template,request
from mysql_model import Person
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:p%40ssw0rd1@localhost:3307/test_mysql?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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

@app.route('/_request')
def test_request():
	return f'test_request:{request.args.get("dummy")}'

@app.route('/exercise_request/<aaa>')
def exercise_request(aaa):
	return f'test_request:{aaa}'

@app.route('/person_search')
def person_search():
    return render_template('./person_search.html')


@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)
