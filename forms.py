from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
<<<<<<< HEAD
from wtforms import  BooleanField, StringField, IntegerField
from wtforms import DateField
from wtforms import PasswordField
=======
from wtforms.fields.core import  BooleanField, StringField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.fields.simple import PasswordField
>>>>>>> 7c4eafe82126345dbcb09c088da453df0bbd1030
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    Fname= StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)] )
    Lname= StringField('Last Name', validators=[Length(min=2, max=20)] )
    email=StringField('Email',validators=[DataRequired(), Email() ])
    password= PasswordField('Password' , validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password' , validators=[DataRequired(), EqualTo('password')])
<<<<<<< HEAD
    role= SelectField("Role", choices=[('Professor'),('Student')] )
    submit= SubmitField('Register')
class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(), Email() ])
    password= PasswordField('Password' , validators=[DataRequired()])
    remember= BooleanField('Remember Me')
    submit= SubmitField('Sign In')

=======
    role= SelectField("Role", choices=[('Professor'),('Student'),( 'Admin')] )
    submit= SubmitField('Register')
class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(), 
       Email() ])
    password= PasswordField('Password' , validators=[DataRequired()])
    remember= BooleanField('Remember Me')
    submit= SubmitField('Sign In')
  
>>>>>>> 7c4eafe82126345dbcb09c088da453df0bbd1030
class CreatClassroom_JoinClassroom(FlaskForm):
    ClassName= StringField('Class Name', validators=[DataRequired(), Length(min=2, max=20)] )
    ClassDiscriptio=StringField('Class Discription', validators=[DataRequired(), Length(min=10, max=20)] )
    Type= SelectField("Class Type", choices=[('Private'),('Open')] )
    NumberOfStudents=IntegerField('Size of the Class')
    password= PasswordField('Password' , validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password' , validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField('Create Classroom')
    JClassName=StringField('Class Name', validators=[DataRequired(), Length(min=2, max=20)] )
    Jpassword= PasswordField('Password' , validators=[])
    Jsubmit= SubmitField('Join Classroom')

