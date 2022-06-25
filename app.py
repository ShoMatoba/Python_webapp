from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def inex():
	return 'Response Data'

@app.route('/another')
def another():
	return 'another respon'

@app.route('/_request')
def test_request():
	return f'test_request:{request.args.get("dummy")}'

@app.route('/exercise_request/<aaa>')
def exercise_request(aaa):
	return f'test_request:{aaa}'
