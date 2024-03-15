from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        dob = datetime.strptime(request.form['dob'], '%Y-%m-%d').date()
        
        user = User(name=name, email=email, age=age, dob=dob)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/data')
def data():
    users = User.query.all()
    return render_template('data.html', users=users)
