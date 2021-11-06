from Classes.Account.Student import Student
from flask import Flask, redirect, url_for, render_template, request, flash
import uuid

from Domain.utils.DataGateway import DataGateway

# app = Flask(__name__)
# def create_user(first_name, last_name, password, email):
#   AdminGateway.create_account(first_name, last_name, password, email)

# def delete_user(password, email):
#   AdminGateway.delete_account(email, password)

# @app.route("/")
# def hello_world():
#   # create_user('Hero', 'Kong', '123', 'hkong@gmail.com')
#   delete_user('123', 'hkong@gmail.com')
#   return render_template("index.html")

if __name__ == "__main__":
#   app.run(debug=True)
  s = DataGateway.get_data('User', 'hk@gmail.com')
  print(s)