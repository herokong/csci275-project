from Domain.utils.DataGateway import DataGateway
from Classes.Classroom import Classroom, PrivateClassroom, PublicClassroom
from Classes.Account import Student, Professor
from Classes.Announcement import Announcement
from flask import Flask, render_template, url_for, redirect, request, session
from flask.helpers import flash
from forms import RegistrationForm, LoginForm, CreatClassroom_JoinClassroom, AnnouncementForm
import jsonpickle
app = Flask(__name__)

app.config['SECRET_KEY']='2c4ea20438c3372acc6869f8e70fc460'

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    form = CreatClassroom_JoinClassroom()
    classname = ''
    if 'User' in session:
            USER = DataGateway.get_data('User', jsonpickle.decode(session['User']).get_email())
            classrooms = USER.get_class_list()
    else:
        return redirect(url_for('login'))

    if(request.method == 'POST'):
        try:
            if (request.form.get('submit')):
                    classname = form.ClassName.data
                    if request.form['Type'] == 'Private':
                        classroom = PrivateClassroom.PrivateClassroom(form.ClassName.data, form.ClassDiscriptio.data, form.NumberOfStudents.data, USER)
                        flash(f'Please store this class code in a safe place {classroom.get_code()}', 'success')
                    elif request.form['Type'] == 'Open':
                        PublicClassroom.PrublicClassroom(form.ClassName.data, form.ClassDiscriptio.data, form.NumberOfStudents.data, USER)
                        flash(f'Successfully Created!', 'success')
            elif (request.form.get('Jsubmit')):
                classname = form.JClassName.data
                Classroom.Classroom.join_classroom(form.JClassName.data, form.Jpassword.data, USER)
                flash(f'Successfully Join!', 'success')
            return redirect(url_for('classroom', className=classname))
        except ValueError as e:
            flash(f'{e}', 'danger')
    return render_template("home.html",form = form, user=session.get('User'), classes=classrooms)


@app.route('/logout')
def logout():
    session.pop('User', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            if (form.role.data == 'Student'):
                USER = Student.Student(form.Fname.data, form.Lname.data, form.password.data, form.email.data)
            elif (form.role.data == 'Professor'):
                USER = Professor.Professor(form.Fname.data, form.Lname.data, form.password.data, form.email.data)
            session['User'] = jsonpickle.encode(USER)
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
            user = DataGateway.get_data('User', form.email.data)
            user.verify_pw(form.password.data)
            username = user.get_name_string()
            flash(f'Logged in as {username}!', 'success')
            session['User'] = jsonpickle.encode(user)
            return redirect(url_for('home'))
        except:
            flash(f'Login Unsuccessful. please check username and password', 'danger')
    return render_template('login.html', title = 'LogIn', form = form)

@app.route('/classroom/<className>', methods=['GET', 'POST'])
def classroom(className):
    try:
        form = AnnouncementForm()
        CLASSROOM = DataGateway.get_data('Classroom', className)

        # Create new annoucement
        if (request.method == 'POST'):
            if (request.form.get('Submit')):
                Announcement.Announcement(form.Title.data, form.Content.data, CLASSROOM)
            return redirect(url_for('classroom', className=className))

        # get creator of the classroom if the account is still existed
        if DataGateway.get_data('User', CLASSROOM.get_creator()):
            creator = DataGateway.get_data('User', CLASSROOM.get_creator()).get_name_string()
        else:
            creator = CLASSROOM.get_creator()

        students = []
        for student in CLASSROOM.get_student_list():
            students.append(DataGateway.get_data('User', student).get_name_string())

        announcements = []
        for announcement in CLASSROOM.get_announcements():
            announcements.insert(0, DataGateway.get_data('Announcement', announcement))

    except ValueError as e:
        flash(f'There is an error: {e}')
    return render_template('classroom.html', s_list=students, user=session.get('User'), classroom=CLASSROOM, creator=creator, form=form, announcements=announcements)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    USER = DataGateway.get_data('User', jsonpickle.decode(session['User']).get_email())
    return render_template('profile.html', user_name=USER.get_name_string(), user=USER)

@app.route('/profile/delete', methods=['GET'])
def delete():
    try:
        USER = DataGateway.get_data('User', jsonpickle.decode(session['User']).get_email())
        if len(USER.get_class_list()) > 0:
            for classroom in USER.get_class_list():
                classroom_obj = DataGateway.get_data('Classroom', classroom)
                if classroom_obj.is_creator(USER.get_email()):
                    classroom_obj.set_creator("Account Deleted")
                else:
                    classroom_obj.remove_student(USER.get_email())
                DataGateway.save_data('Classroom', classroom, classroom_obj)
        DataGateway.delete_data('User', USER.get_email())
    except ValueError as e:
        flash(f"There is an error: {e}")
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True) 
