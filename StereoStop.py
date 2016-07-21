from flask import Flask, render_template, url_for

app = Flask(__name__)

Marvin = {
  'pic': 'https://d1qb2nb5cznatu.cloudfront.net/users/1280780-large?1433430580',
  'name': "Nate"
}

pics = [ 'main-qimg-81ed258627de52b9eaaec07423435aff-c.jpg', 'dina.jpg', 'ballet.jpg', '160310_arabs.jpg' ]

@app.route ('/')
def home():
	return render_template('home.html')


@app.route('/signup')
def signup():
	return render_template ('signup.html')


@app.route('/news')
def newsfeed():
	return render_template ('news.html')





@app.route('/profile')
def profile():
	return render_template('profile.html', user = Marvin, pics = pics)



@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
		app.run(debug=True)