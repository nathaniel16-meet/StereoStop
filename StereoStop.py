from flask import Flask, render_template

app = Flask(__name__)


@app.route ('/')
def home():
	return render_template('home.html')

#@app.route('/profile/<name>')
#def profile(name):
#	return render_template('profile.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
		app.run(debug=True)