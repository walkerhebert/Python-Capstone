from model import db, User, Item, connect_to_db

def create_user(email, password):
    
    user = User(email=email, password=password)
    return user

def get_users():
    
    return User.query.all()

def get_user_by_id(user_id):

    return User.query.get(user_id)

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()



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


if __name__ == '__main__':
    from server import app
    connect_to_db(app)