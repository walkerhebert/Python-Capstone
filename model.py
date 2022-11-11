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
    
    def __repr__(self):
        return f"<Item item_id={self.item_id} item_name={self.item_name}>"
    
    
    
class Quantity(db.Model):
    __tablename__ = "quantities"
    
    quantity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    amount = db.Column(db.Integer)
    item_id = db.Column(db.Integer,db.ForeignKey("items.item_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    
    item = db.relationship("Item", backref="quantity")
    user = db.relationship("User", backref="quantity")
    
    def __repr__(self):
        return f"<Quantity quantity_id={self.quantity_id} amount={self.amount}>"
    
    
# class Coupon(db.Model):
#     __tablename__ = "coupons"
    
#     coupon_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     coupon_name = db.Column(db.Integer)
#     item = db.Column(db.Integer,db.ForeignKey("items.item_id"))
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
#     quantity_id = db.Column(db.Integer, db.ForeignKey("quantities.quantity_id"))
    
    
#     item = db.relationship("Item", backref="coupons")
#     user = db.relationship("User", backref="coupons")
#     quantity = db.relationship("Quantity", backref="coupons")
    
    def __repr__(self):
        return f"<Coupon coupon_id={self.coupon_id} coupon_name={self.coupon_name}>"
    
    
    
    
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