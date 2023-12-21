from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string)
    super_name = db.Column(db.string)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    hero_powers=db.relationship("HeroPower")

    def __repr__(self):
        return f"{self.name}'s super power name is {self.super_name}"

    

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string)
    description = db.Column(db.string)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    # hero_powers=db.relationship("HeroPower")

    def __repr__(self):
        return f"{self.name} power is: {self.description}"


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.string)
    hero_id = db.Column(db.DateTime, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.DateTime, db.ForeignKey("powers.id"))
    created_at = db.Column(db.DateTime, onupdate = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        return f"Super hero of ID: {self.hero_id} with power ID {self.power_id} strength is {self.strength}"
    



    



