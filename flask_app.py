from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')



@app.route('/login', methods=['GET', 'POST'])
def student_login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'student' or request.form['password'] != 'student':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('student_page'))
    return render_template('login.html', error=error)



@app.route('/login_teacher', methods=['GET', 'POST'])
def login_teacher():
    error = None
    if request.method == 'POST':
        if request.form['name'] != 'teacher' and request.form['password'] != 'teacher':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/teacher_page'))
    return render_template('login.html', error=error)



@app.route('/login_parent', methods=['GET', 'POST'])
def login_parent():
    error = None
    if request.method == 'POST':
        if request.form['name'] != 'parent' and request.form['password'] != 'parent':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/parent_page'))
    return render_template('login.html', error=error)


@app.route('/login_admin')
def login_admin():
    error = None
    if request.method == 'POST':
        if request.form['name'] != 'admin' and request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/admin_page'))
    return render_template('login.html', error = error)