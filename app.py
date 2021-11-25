from Domain.utils.DataGateway import DataGateway
from Classes.Classroom import Classroom, PrivateClassroom, PublicClassroom
from Classes.Account import Student, Professor
from flask import Flask, render_template, url_for, redirect, request
from flask.helpers import flash
from forms import RegistrationForm, LoginForm, CreatClassroom_JoinClassroom
app = Flask(__name__)

app.config['SECRET_KEY']='2c4ea20438c3372acc6869f8e70fc460'

# HERO
# INFO: this will be later move to session
# For now will store user with the global variable
USER = None

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    form = CreatClassroom_JoinClassroom()
    if(request.method == 'POST'):
        try:
            if USER:
                if (request.form.get('submit')):
                        if request.form['Type'] == 'Private':
                            classroom = PrivateClassroom.PrivateClassroom(form.ClassName.data, form.ClassDiscriptio.data, form.NumberOfStudents.data, USER.get_email())
                            flash(f'Please store this class code in a safe place {classroom.get_code()}', 'success')
                        elif request.form['Type'] == 'Open':
                            PublicClassroom.PrublicClassroom(form.ClassName.data, form.ClassDiscriptio.data, form.NumberOfStudents.data, USER.get_email())
                            flash(f'Successfully Created!', 'success')
                elif (request.form.get('Jsubmit')):
                    Classroom.Classroom.join_classroom(form.JClassName.data, USER.get_email(), USER.get_role())
                    flash(f'Successfully Join!', 'success')
            else:
                flash(f'You need to login before joining a class!', 'danger')
        except ValueError as e:
            flash(f'{e}', 'danger')
    return render_template("home.html",form = form, user=USER)


@app.route('/about')
def about():
    return render_template("about.html", title="About", user=USER)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            if (form.role.data == 'Student'):
                Student.Student(form.Fname.data, form.Lname.data, form.password.data, form.email.data)
            elif (form.role.data == 'Professor'):
                Professor.Professor(form.Fname.data, form.Lname.data, form.password.data, form.email.data)
        except:
            flash(f'The email is already used!', 'danger')
            return render_template('register.html', title = 'Register', form = form)
        flash(f'Account created for {form.Fname.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            global USER
            USER = DataGateway.get_data('User', form.email.data)    # in the next version we will save user in the cookie session
            USER.verify_pw(form.password.data)
            username = USER.get_name_string()
            flash(f'Logged in as {username}!', 'success')
            return redirect(url_for('home'))
        except:
            flash(f'Login Unsuccessful. please check username and password', 'danger')
    return render_template('login.html', title = 'LogIn', form = form)


if __name__ == "__main__":
    app.run(debug=True) 
