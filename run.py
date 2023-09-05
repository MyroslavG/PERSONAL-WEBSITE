import os
from flask import Flask, render_template, url_for, redirect, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime

app = Flask(__name__)
load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')    

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Message('{self.username}', '{self.email}', '{self.message}')"

class ContactForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Name"})
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "Email"})                  
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"placeholder": "Content"})
    submit = SubmitField('SEND')

@app.route("/contact", methods=['GET', 'POST'])
def contact():    
    form = ContactForm()
    if form.validate_on_submit():
        message = Message(username=form.username.data, email=form.email.data, message=form.content.data)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('contact'))
    return render_template('contact.html', title='Contact', form=form, legend='Contact')

