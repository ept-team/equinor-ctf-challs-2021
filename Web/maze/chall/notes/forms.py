from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, TextAreaField
from wtforms import validators
from wtforms.fields.simple import HiddenField
from wtforms.validators import DataRequired, InputRequired, Length

class LoginForm(FlaskForm):
    user_name  = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class NoteForm(FlaskForm):
    style={'style': 'font-size: 36px', 'readonly': False}
    title = StringField('Title', [validators.Length(min=1, max=- 1, message="You need to enter a title")], render_kw={"class":"form-control"})
    note  = TextAreaField('Note', [validators.Length(min=1, max=- 1, message="You need to enter a note")], render_kw={"class":"form-control"})
    id = HiddenField('id')
    submit = SubmitField('Save')
