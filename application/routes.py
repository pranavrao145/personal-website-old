from flask import render_template, url_for
from application import app

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title="Home")

@app.route('/about')
def about():
	return render_template('about.html', title="About")

@app.route('/contact')
def contact():
	return render_template('contact.html', title="Contact Me")

@app.route('/projects')
def projects():
	return render_template('projects.html', title="Projects")