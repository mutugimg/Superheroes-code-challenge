#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate

from models import db, Hero, HeroPower, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact=False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return "This is the home"

@app.route('/heroes', methods=['GET'])
def get_all():
    
    list_heroes=[hero.to_dict() for hero in Hero.query.all()]
    response=make_response(
        jsonify(list_heroes),
        200
        )
    
    return response

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    
    if request.method=='GET':
        hero=Hero.query.filter(Hero.id==id).first()
        
        if hero ==None:
            response=make_response(
                jsonify({
                    "error": "Hero not found"
                }),404)
            return response
        elif hero:    
            response=make_response(
                jsonify(hero.to_dict()),
                200)
            return response

@app.route('/powers/<int:id>', methods=['GET','PATCH'])
def get_power_by_id(id):
    
    if request.method=='GET':
        power=Power.query.filter(Power.id==id).first()
        
        if power ==None:
            response=make_response(
                jsonify({
                    "error": "Power not found"
                }),404)
            return response        
        elif power:    
            response=make_response(
                jsonify(power.to_dict()),
                200)
            return response
        
    elif request.method=='PATCH':
        update_power = Power.query.filter_by(id=id).first()

        if update_power ==None:
            response=make_response(
                jsonify({
                    "error": "Power not found"}),404)
            return response
        elif update_power:
            try:
                for attribute in request.get_json():
                    setattr(update_power, attribute, request.get_json()[attribute])
                db.session.add(update_power)
                db.session.commit()
                response_dict = update_power.to_dict()
                response = make_response(
                    jsonify(response_dict),
                    200)
                return response
            except:
                response=make_response(
                    jsonify({
                        "errors": ["validation errors"]
                    }),404)
                return response
            
@app.route('/hero_powers', methods=['POST'])
def create_new_hero_power():
    data = request.get_json()
    hero = Hero.query.get(data.get('hero_id'))
    power = Power.query.get(data.get('power_id'))

    if not (hero and power):
        return jsonify({"errors": [" Not available"]}), 404
    new_record = HeroPower(
        strength=data.get('strength'),
        power_id=data.get('power_id'),
        hero_id=data.get('hero_id'))

    try:
        db.session.add(new_record)
        db.session.commit()
        response_dict = new_record.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,)
        return response
    except:
        response=make_response(
                jsonify({
                "errors": ["validation errors"]
                }),404)
        return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
        

    

