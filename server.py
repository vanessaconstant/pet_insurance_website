
from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import claims
from flask_app.controllers import pets
from flask_app.controllers import providers

if (__name__) == "__main__":
    app.run(debug=True)
