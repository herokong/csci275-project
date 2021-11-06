from flask.helpers import flash, url_for
from Classes.Account.Student import Student
from Classes.Account.Professor import Professor
from Domain.utils.DataGateway import DataGateway
from flask import Blueprint, request, redirect
from flask.templating import render_template

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    s = DataGateway.get_data('User', email)
  return render_template('index.html')

@auth.route('/logout')
def logout():
  print("Hello")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    role = request.form.get('user_role')
    if role == "Student":
      try:
        Student(first_name, last_name, password, email)
      except ValueError:
        flash(ValueError)
    elif role == "Professor":
      try:
        Professor(first_name, last_name, password, email)
      except ValueError:
        flash(ValueError)
    return render_template('index.html')
  return render_template('signup.html')