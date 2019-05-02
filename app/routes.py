from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
	user = {'username': 'Thomas'}
	posts = [
		{
			'author' : {'username': 'John' },
			'body' : 'Beautiful Day in Belfast'
		},
		{
			'author' : {'username': 'Susan'},
			'body': 'Avengers Endgame was so cool'
		}
		]
	return render_template('index.html', title="Home", user=user, posts=posts)
