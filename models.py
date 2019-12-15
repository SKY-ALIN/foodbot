import sqlalchemy as db
from datetime import datetime

from base import Base

class People(Base):
	__tablename__ = 'people'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
    dishes = db.relationship('Dishes', lazy=True, backref='person')

	def __init__(self, name):
		self.name = name

class Dishes(Base):
    __tablename__ = 'dishes'
	id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    count = db.Column(db.Integer, default=1)
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    def __init__(self, name):
		self.name = name
