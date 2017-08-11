#!/usr/bin/env python

from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index():
    return 'index.htm'

@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/user/<username>')
def show_user_profile(username):
    #show the user profile for that user
    return 'User %s' % username 

@app.route('/post/<int:post_id>')
def show(post_id):
    #show the post with give id, the id is an int
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show the subpath after /path/
    return 'Subpath %s' % subpath

