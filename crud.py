from model import db, User, Quantity, Coupon, Item, CartItem, connect_to_db

def create_user(email, password):
    
    user = User(email=email, password=password)
    return user

def get_users():
    
    return User.query.all()

def get_user_by_id(user_id):

    return User.query.get(user_id)

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()


 ##--##  ##--##  ##--##  ##--##


def create_item(item_name, description, price, image_path):
    item = Item(
        item_name=item_name,
        description=description,
        price=price,
        image_path=image_path,
    )
    return item

def get_items():
    return Item.query.all()


def get_item_by_id(item_id):

    return Item.query.get(item_id)


 ##--##  ##--##  ##--##  ##--##


def create_quantity(user,item,amount):
    quantity = Quantity(
        user=user,
        item=item,
        amount=amount,
        )
    return quantity

def update_quantity(quantity_id, new_amount):

    quantity = Quantity.query.get(quantity_id)
    quantity.amount = new_amount


 ##--##  ##--##  ##--##  ##--##


def create_coupon(user,item):
    coupon = Coupon(
        user=user,
        item=item,
        )
    return coupon

def get_coupons():
    return Coupon.query.all()


def get_coupon_by_id(coupon_id):

    return Coupon.query.get(coupon_id)
   
   
    
  ##--##  ##--##  ##--##  ##--##
  
  
# def create_cart_item(user,item,quantity):
#     cart_item = CartItem(
#         user=user,
#         item=item,
#         quantity=quantity,
#         )
#     return cart_item
    
# def get_cart_items():
#     return CartItem.query.all()

# def get_cart_item_by_id(cart_item_id):

#     return CartItem.query.get(cart_item_id)
    
    
  
if __name__ == '__main__':
    from server import app
    connect_to_db(app)