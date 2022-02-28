from email.policy import default
from re import search

from click import get_os_args
from app import app, db, fake
from flask import render_template, request, redirect, url_for, jsonify
from .forms import GuestForm
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_parameter
from flask_pymongo import pymongo


@app.route('/', methods=['POST', 'GET'])
def guestbook():  
  forms = GuestForm()

  if forms.validate_on_submit():    
    name = forms.name.data
    email = forms.email.data
    message = forms.message.data
    
    db.guestbook.insert_one ({
      'name': name,
      'email': email,
      'message': message
    })
    
    return redirect(request.url)
  
  forms.name.data = fake.name()
  forms.email.data = fake.email()
  forms.message.data = fake.text()
  
  search = False
  
  q = request.args.get('q')
  
  if q:
    search = True
  
  # paginate
  page = request.args.get(get_page_parameter(), type=int, default=1)
  per_page = 5
  collection = db.guestbook
  total = collection.count_documents({})
  all_guest = collection.find().skip((page - 1) * per_page).limit(per_page)
  pagination = Pagination(page=page, per_page=per_page, total=total, search=search, record_name="allguest")
  
  return render_template(
    'index.html',
    forms=forms,
    posts=all_guest,
    pagination=pagination
    )
  
