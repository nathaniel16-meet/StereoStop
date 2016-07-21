from flask import Flask, render_template

app = Flask(__name__)

Marvin = {
  'pic': 'https://d1qb2nb5cznatu.cloudfront.net/users/1280780-large?1433430580',
  'name': "Nate"
}

@app.route ('/')
def home():
	return render_template('base.html')

@app.route('/profile')
def profile():
  return render_template('profile.html', user = Marvin)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
		app.run(debug=True)