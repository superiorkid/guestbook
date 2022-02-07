from app import app, db
from flask import render_template

@app.route('/')
def guestbook():
  msg = 'Hello'
  return render_template('index.html', msg=msg)