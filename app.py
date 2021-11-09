from flask import Flask, render_template, url_for, redirect
from flask.helpers import flash
from forms import RegistrationForm, LoginForm, CreatClassroom_JoinClassroom
app = Flask(__name__)

app.config['SECRET_KEY']='2c4ea20438c3372acc6869f8e70fc460'



@app.route('/home', methods=['GET', 'POST'])
@app.route('/')
def home():
    form = CreatClassroom_JoinClassroom()
    return render_template("home.html",form = form)


@app.route('/about')
def about():
    return render_template("about.html", title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.Fname.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Logged in as {form.Fname.data}!', 'success')
        return redirect(url_for('home'))
    else:
        flash(f'Login Unsuccessful. please check username and password', 'danger')
    return render_template('login.html', title = 'LogIn', form = form)


# if __name__ == "__main__":
#     app.run(debug=True) 