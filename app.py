from flask import Flask, request, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/help')
def help():
	return render_template('help.html')

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True )