from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'

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

class ContactForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "Email"})                  
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"placeholder": "Content"})
    submit = SubmitField('Send')

@app.route("/contact", methods=['GET', 'POST'])
def contact():    
    form = ContactForm()
    if form.validate_on_submit():
        flash('You contacted me successfully!', 'success')
        return redirect(url_for('contact'))
    elif request.method == 'GET':
        form.email.data = ''
        form.content.data = ''
    return render_template('contact.html', title='Contact', form=form, legend='Contact')

