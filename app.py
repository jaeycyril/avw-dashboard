from flask import Flask, request, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/2/')
def index2():
	return render_template('index2.html')


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True )