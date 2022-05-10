
from flask_app import app
from flask_app.models import user
from flask_app.models import pet
from flask_app.models import claim
from flask import render_template, redirect, request, flash, session


@app.route('/')
def mainPage():
    return render_template('index.html')


@app.route('/about')
def aboutPage():
    return render_template('about.html')


# @app.route('/providers')
# def providersPage():
#     return render_template('providers.html')


@app.route('/registrationPage')
def registrationPage():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'conf_password': request.form['conf_password']
    }

    if not user.User.createUser(data):
        return redirect('/registrationPage')

    return redirect('/loginPage')


@app.route('/loginPage')
def loginPage():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    if not user.User.loginUser(data):
        return redirect('/loginPage')

    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if not session:
        return redirect('/loginPage')
    user_info = user.User.get_user_by_id(session['user_id'])

    all_claims = claim.Claim.get_all_claims(session['user_id'])

    all_pets = pet.Pet.get_all_pets(session['user_id'])
    return render_template('dashboard.html', user_info=user_info, all_pets=all_pets, all_claims=all_claims)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
