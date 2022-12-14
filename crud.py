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



def get_item_by_item_id(item_id):
    item = Item.query.get(item_id())
    return item
   
   
    
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

def get_cart_by_cart_id(cart_id):
    cart_session = CartItem.query.get(cart_id)
    return cart_session

def delete_cart_item(item_id):
    cart_item = CartItem.query.get(item_id)
    db.session.delete(cart_item)
    db.session.commit()
    


    
  
if __name__ == '__main__':
    from server import app
    connect_to_db(app)