from . import db
from flask_login import UserMixin
#from alembic import create_engine, Base

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

#engine = create_engine('sqlite:///db.sqlite')
#Base.metadata.create_all(engine)