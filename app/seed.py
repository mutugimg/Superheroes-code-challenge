from faker import Faker
import random
from models import Hero, Power, HeroPower,db
from app import app 

fake = Faker()

with app.app_context():
    db.session.query(Hero).delete()
    db.session.query(Power).delete()
    db.session.query(HeroPower).delete()

    
    powers = []
    for _ in range(6):
        pwr = Power(
            name=fake.word(),
            description='Power not available at the moment'
            
        )
        powers.append(pwr)

    db.session.add_all(powers)
    db.session.commit()

    heroes = []
    for _ in range(12):  
        hero = Hero(
            name=fake.name(),
            super_name=fake.word()
        )
        heroes.append(hero)

    db.session.add_all(heroes)
    db.session.commit()


    hero_powers = []
    elements=['Strong', 'Weak', 'Average']
    for _ in range(15):
        hero_power = HeroPower(
            strength=random.choice(elements),
            hero_id=random.choice(heroes).id,
            power_id=random.choice(powers).id
            )
        hero_powers.append(hero_power)



    db.session.add_all(hero_powers)
    db.session.commit()