from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
import search

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return 
    return render_template('search.html', 
                           title='Search',
                           form=form)