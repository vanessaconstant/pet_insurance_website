from ast import Return
from crypt import methods
from flask_app import app
from flask_app.models import pet
from flask import render_template, redirect, request, flash, session


@app.route('/newPet')
def newPet():
    return render_template('pet.html')


@app.route('/createPet', methods=['POST'])
def createPet():

    data = {
        'pet_name': request.form['pet_name'],
        'birthday': request.form['birthday'],
        'breed': request.form['breed'],
        'user_id': session['user_id']
    }

    if not pet.Pet.createPet(data):
        return redirect('/newPet')

    return redirect('/dashboard')
