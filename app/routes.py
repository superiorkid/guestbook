from email.policy import default
from app import app, db, fake
from flask import render_template, request, redirect, url_for, jsonify
from .forms import GuestForm
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_args
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
  
  # paginate
  collection = db.guestbook
  total = collection.count_documents({})
  page, per_page, offset = get_page_args(page_parameter="p", per_page_parameter="pp", pp=5)
  if per_page:
    cursor = collection.find().sort('_id', pymongo.DESCENDING).limit(5)
  else:
    cursor = collection.find().sort('_id', pymongo.DESCENDING)
    
  
  _guestbook = cursor
  
  pagination = get_pagination(
    page=page,
    per_page=per_page,
    total=total,
    record_name="GuestBook",
    format_total=True,
    format_number=True,
    page_parameter="p",
    page_per_parameter="pp"
    )
  
  return render_template(
    'index.html',
    forms=forms,
    pagination=pagination,
    _guestbook=_guestbook
    )
  
@app.route('/message', defaults={'page': 1}, methods=['POST', 'GET'])
@app.route('/message/page/<int:page>', methods=['POST', 'GET'])
def messages(page):
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
  
  # paginate
  collection = db.guestbook
  total = collection.count_documents({})
  page, per_page, offset = get_page_args(per_page_parameter="pp", pp=5)
  if per_page:
    cursor = collection.find().sort('_id', pymongo.DESCENDING).limit(5)
  else:
    cursor = collection.find().sort('_id', pymongo.DESCENDING)
    
  
  _guestbook = cursor
  
  pagination = get_pagination(
    page=page,
    per_page=per_page,
    total=total,
    record_name="_guestbook",
    format_total=True,
    format_number=True,
    page_parameter="p",
    page_per_parameter="pp"
    )
  
  return render_template(
    'index.html',
    forms=forms,
    pagination=pagination,
    _guestbook=_guestbook,
    active_url='_guestbook-page-url',
    )

    
@app.route('/delete/<guestId>')
def delete(guestId):
  # Deleting a document from the database.
  db.guestbook.delete_one({'_id': ObjectId(guestId)})
  return redirect(url_for('guestbook'))




def get_pagination(**kwargs):
  # The above code is creating a Pagination object with the following attributes:
  #     - page
  #     - per_page
  #     - total_count
  #     - items
  #     - pages
  #     - has_prev
  #     - has_next
  #     - prev_num
  #     - next_num
  #     - iter_pages
  #     - record_name
  kwargs.setdefault("record_name", "records")
  return Pagination(**kwargs)