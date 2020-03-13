from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LogInForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1187e1018f98604604e74ed3f89349fe'

posts = [
    {
        'author': 'Michael Garlotte',
        'title': 'Blog Post 1',
        'content': 'First post content...',
        'date_posted': 'March 12th, 2020'
    },
    {
        'author': 'Danielle Brown',
        'title': 'Blog Post 2',
        'content': 'Second post content...',
        'date_posted': 'March 11th, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
