
from crypt import methods
from flask_app import app
from flask_app.models import user
from flask_app.models import pet
from flask_app.models import claim
from flask import render_template, redirect, request, flash, session


@app.route('/newClaim')
def newClaimPage():
    all_pets = pet.Pet.get_all_pets(session['user_id'])

    return render_template('claim.html', all_pets=all_pets)


@app.route('/createClaim', methods=['POST'])
def createClaim():

    data = {
        'date_service': request.form['date_service'],
        'service_type': request.form['service_type'],
        'charge': request.form['charge'],
        'vet_name': request.form['vet_name'],
        'description': request.form['description'],
        'pet_id': request.form['pet_id'],
        'user_id': session['user_id'],

    }

    if not claim.Claim.createClaim(data):
        return redirect('/newClaim')

    return redirect('/dashboard')


@app.route('/viewClaim/<id>')
def viewClaim(id):
    claim_info = claim.Claim.viewClaim(id)

    return render_template('view.html', claim_info=claim_info)


@app.route('/editClaim/<id>')
def getClaimtoEdit(id):

    if not session:
        return redirect('/loginPage')

    claim_info = claim.Claim.get_claim_to_edit(id)
    print(claim_info)

    return render_template("edit.html", claim_info=claim_info)


@app.route('/editClaim', methods=['POST'])
def editClaim():

    data = {

        "id": request.form['id'],
        "date_service": request.form['date_service'],
        "service_type": request.form['service_type'],
        "charge": request.form['charge'],
        "vet_name": request.form['vet_name'],
        "description": request.form['description'],

    }

    claim.Claim.editClaim(data)

    return redirect('/dashboard')


@app.route('/delete/<id>')
def deleteClaim(id):

    if not session:
        return redirect('/loginPage')

    claim.Claim.deleteClaim(id)

    return redirect('/dashboard')
