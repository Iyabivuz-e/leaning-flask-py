# Here, we are going to create our routes
from flask import request, jsonfy
from config import app, db
from models import Contact




if __name__ == '__main__':
    with app.app_context():
        app.create_all() #This is going to connect and call the database by building all the tables there. "Signup to the db"
    app.run(debug=True) #This is going to run our flask app