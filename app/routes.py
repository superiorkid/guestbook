from app import app, db, fake
from flask import render_template, request, redirect, url_for
from .forms import GuestForm
from bson.objectid import ObjectId


@app.route('/', methods=['POST', 'GET'])
def guestbook():
  forms = GuestForm()
  
  if forms.validate_on_submit():    
    name = forms.name.data
    email = forms.email.data
    message = forms.message.data
    
    db.guestbook.insert_one({
      'name': name,
      'email': email,
      'message': message
    })
    
    return redirect(request.url)
  
  forms.name.data = fake.name()
  forms.email.data = fake.email()
  forms.message.data = fake.text()
    
  comment = db.guestbook.find()
  
  return render_template('index.html', forms=forms, comment=comment)

@app.route('/delete/<guestId>')
def delete(guestId):
  db.guestbook.delete_one({'_id': ObjectId(guestId)})
  return redirect(url_for('guestbook'))