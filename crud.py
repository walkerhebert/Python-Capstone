from model import db, User, Coupon, Item, CartItem, connect_to_db


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




 ##--##  ##--##  ##--##  ##--##


def create_coupon(user,coupon_code):
    coupon = Coupon(
        user=user,
        coupon_code=coupon_code,
        )
    return coupon

def get_coupons():
    return Coupon.query.all()


def get_coupon_by_id(coupon_id):

    return Coupon.query.get(coupon_id)
   
   
    
  ##--##  ##--##  ##--##  ##--##
  
  
def create_cart_item(user_id,item_id,quantity):
    cart = CartItem(
        user_id=user_id,
        item_id=item_id,
        quantity=quantity,
    )
    return cart
  
def get_cart_items_by_user_id(user_id):
    return CartItem.query.filter(CartItem.user_id == user_id).all()

def delete_cart_by_cart_id(cart_id):
    cart_session = CartItem.query.get(cart_id)
    
    return cart_session

    
  
if __name__ == '__main__':
    from server import app
    connect_to_db(app)