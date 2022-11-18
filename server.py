from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "walker-project-key"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")



@app.route("/landing")
def landing():
    """View landing."""
    
    return render_template("landing.html")


#####______######_______######_____#######


@app.route("/items")
def all_():
    """View all items."""

    items = crud.get_items()

    return render_template("all_items.html", items=items)


@app.route("/items/<item_id>")
def show_item(item_id):
    """Show details on a particular item."""

    item = crud.get_item_by_id(item_id)

    return render_template("item_details.html", item=item )


#####______######_______######_____#######


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")
    


# @app.route("/users/<user_id>")
# def show_user(user_id):
#     """Show details on a particular user."""

#     user = crud.get_user_by_id(user_id)

#     return render_template("user_details.html", user=user)

        
#####______######_______######_____#######   


@app.route("/login", methods=["GET","POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    
    
    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was not valid.")
    else:
        session["user_email"] = user.email
        flash(f"You're logged in as {user.email}!")

    return redirect("/")

@app.route("/logout", methods=["POST"])
def process_logout():
    """Process user logout."""

    logged_in_to_email = session.get("user_email")
    if logged_in_to_email is None:
        flash("You were already logged out!")
    else:
        del session["user_email"]
        flash("You're logged out!")

    return redirect("/")


#####______######_______######_____#######


@app.route("/update_quantity", methods=["POST"])
def update_quantity():
    quantity_id = request.json["quantity_id"]
    updated_amount = request.json["updated_amount"]
    crud.update_quantity(quantity_id, updated_amount)
    db.session.commit()

    return "Quantity Updated"


#####______######_______######_____#######


@app.route("/cart")
def cart():
    """Show items in cart."""
    
    
    get_user = crud.get_user_by_email(session.get("user_email"))
    
    cart_items = crud.get_cart_items_by_user_id(get_user.user_id)
    
    return render_template("cart.html", cart_items=cart_items)



@app.route("/items/<item_id>/carts", methods=["GET","POST"])
def create_cart_item(item_id):
    """Create a new cart item."""

    logged_in_email = session.get("user_email")
    quantity_amount = request.form.get("quantity")

    if logged_in_email is None:
        flash("Log in to update quantity!")
    elif not quantity_amount:
        flash("Error: you didn't select a quantity.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        item = crud.get_item_by_id(item_id)

        cart_item = crud.create_cart_item(user.user_id, item.item_id, int(quantity_amount))
        db.session.add(cart_item)
        db.session.commit()

        flash(f" {quantity_amount} of this item has been added to your cart.")

    return redirect(f"/items")
    # return render_template("cart.html", cart_items=cart_items)
    
    
    
# @app.route("/empty_cart")
# def empty_cart(cart_id):
#     delete_carts = crud.delete_cart_by_cart_id(cart_id)
#     db.session.delete(cart_id)
#     db.session.commit()
    
#     return render_template("empty_cart.html", delete_carts=delete_carts)
    
    

# @app.route("/carts/empty_cart", methods=["POST"])
# def empty_cart_method(cart_id):
#     """Empty cart."""
    
#     delete_carts = crud.delete_cart_by_cart_id(cart_id)
#     db.session.delete(cart_id)
#     db.session.commit()
    
#     return redirect("/empty_cart", delete_carts=delete_carts)




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
