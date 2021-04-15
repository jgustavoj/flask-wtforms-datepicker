from flask import Flask, redirect, render_template, url_for, request, session
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField
from models import db, Todo

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '\x14B~^\x07\xe1\x197\xda\x18\xa6[[\x05\x03QVg\xce%\xb2<\x80\xa4\x00'
app.config['DEBUG'] = True

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db.init_app(app)

class InfoForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['startdate'] = form.startdate.data
        session['enddate'] = form.enddate.data
        return redirect('date')
    return render_template('index.html', form=form)

@app.route('/date', methods=['GET', 'POST'])
def date():
    startdate = session['startdate']
    enddate = session['enddate']
    return render_template('date.html')


if __name__ == "__main__":
    app.run(port=3000)
