import os
import json
from random import choice, randint

import string
import random
import crud
import model
import server
from model import Coupon, connect_to_db, db

os.system("dropdb waka")
os.system('createdb waka')

model.connect_to_db(server.app)
model.db.create_all()

with open("data/items.json") as f:
    item_data = json.loads(f.read())
    
items_in_db = []
for item in item_data:
    item_name, description, price, image_path = (
        item["item_name"],
        item["description"],
        item["price"],
        item["image_path"],
    )

    db_item = crud.create_item(item_name, description, price, image_path)
    items_in_db.append(db_item)
    
model.db.session.add_all(items_in_db)
model.db.session.commit()

 ##--##  ##--##  ##--##  ##--##


user_count = 10

for n in range(user_count):
    email = f"user{n}@test.com"
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)
    
    
##--##  ##--##  ##--##  ##--##
    
    
    for k in range(10):
        random_item = choice(items_in_db)
        amount = randint(1, 11)

        quantity = crud.create_cart_item(user.user_id, random_item.item_id, amount)
        model.db.session.add(quantity)

model.db.session.commit()


##--##  ##--##  ##--##  ##--##





# coupon_code = string.ascii_letters + string.digits

# def coupon_generator(code_length=20):
#     return "".join([ random.choice(coupon_code) for _ in range(code_length) ])


# new_coupon = crud.create_coupon(user, coupon_generator())
# model.db.session.add(new_coupon)
# model.db.session.commit()

# print(coupon_generator())





