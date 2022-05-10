from crypt import methods
from urllib import response
from flask_app import app
from flask_app.models import provider
from flask_app import api_key

import requests

from flask import render_template, redirect, request, flash, session


@app.route('/providers')
def loadAllproviders():

    return render_template('providers.html')


@app.route('/search', methods=['POST'])
def search():
    base_url = "https://api.yelp.com/v3/businesses/search"
    key = api_key.key

    headers = {
        "Authorization": "Bearer " + key
    }
    params = {
        "term": "veterinarian",
        "location": request.form['location']

    }

    response = requests.get(base_url, headers=headers, params=params)

    all_providers = response.json()['businesses']

    return render_template('providers.html', all_providers=all_providers)
