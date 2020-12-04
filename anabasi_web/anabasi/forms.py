from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, validators

from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
        username = StringField('e-mail', validators=[DataRequired(), Email()])
        password = PasswordField('Password', validators=[DataRequired(message="qualcosa non va")])
        remember_me = BooleanField('Ricordami')
        submit = SubmitField('Login')



class NewUser(FlaskForm):
    nome= StringField('Nome', validators=[DataRequired()])
    username = StringField('e-mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

#validators.Regexp('^\w+$', message="Username must contain only letters numbers or underscore")
