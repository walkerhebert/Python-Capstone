import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    
    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'
    
    @classmethod
    def create(cls, email, password):
         

       return cls(email=email, password=password)
   


class Item(db.Model):
    __tablename__ = "items"

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_name = db.Column(db.String)
    description = db.Column(db.Text)
    price = db.Column(db.String)
    image_path = db.Column(db.String)
    
    def __repr__(self):
        return f"<Item item_id={self.item_id} item_name={self.item_name}>"
    
    
    
    
class CartItem(db.Model):
    __tablename__ = "carts"
    
    cart_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    quantity = db.Column(db.Integer)
    item_id = db.Column(db.Integer,db.ForeignKey("items.item_id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.user_id"))

    
    user = db.relationship("User", backref="carts")
    item = db.relationship("Item", backref="carts")
   
    
        
        
    def __repr__(self):
        return f"<CartItem cart_id={self.cart_id} item_id={self.item_id} user_id={self.user_id} quantity_id={self.quantity_id}>"
    
    
    
    
class Coupon(db.Model):
    __tablename__ = "coupons"
    
    coupon_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    coupon_code = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    
    user = db.relationship("User", backref="coupons")
    
    
    
    def __repr__(self):
        return f"<Coupon coupon_id={self.coupon_id} coupon_name={self.coupon_code}>"
    
    
    
    
def connect_to_db(flask_app, db_uri=os.environ["POSTGRES_URI"], echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    
    connect_to_db(app, echo=False)