from flask import Flask, request, jsonify
from flask_cors import CORS
from config import db, SECRET_KEY
from os import path, getcwd, environ
from dotenv import load_dotenv
from models.user import User
from models.personal_details import PersonalDetails
from models.projects import Projects
from models.experiences import Experiences
from models.education import Education
from models.skills import Skills
from models.certificates import Certificates

load_dotenv(path.join(getcwd(),'.env'))


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.secret_key = SECRET_KEY
    
    
    db.init_app(app)
    print("DB Initialized successfully")

    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()
    
        return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)