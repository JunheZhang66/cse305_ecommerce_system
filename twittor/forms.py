from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField\
,TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from twittor.models import User

class LoginForm(FlaskForm):
    class Meta:
        csrf = False
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Password Repeat", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")
    #check username exist
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username exist! please use different username')
    def validate_email(self,email): 
        em = User.query.filter_by(email=email.data).first()
        if em is not None:
            raise ValidationError('E-mail is used! please use different E-mail address')
# class EditProfileForm(FlaskForm):
#     about_me = TextAreaField('About me', validators=[Length(min=0,max=120)])
#     submit = SubmitField('Save')
class EditProfileForm(FlaskForm):
    about_me = TextAreaField('About me', validators=[Length(min=0, max=120)])
    submit = SubmitField('Save')