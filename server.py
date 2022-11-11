from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/items")
def all_():
    """View all items."""

    items = crud.get_items()

    return render_template("all_items.html", items=items)


@app.route("/items/<item_id>")
def show_item(item_id):
    """Show details on a particular item."""

    item = crud.get_item_by_id(item_id)

    return render_template("item_details.html", item=item)


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


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was not valid.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"You're logged in as {user.email}!")

    return redirect("/")


@app.route("/update_quantity", methods=["POST"])
def update_quantity():
    quantity_id = request.json["quantity_id"]
    updated_amount = request.json["updated_amount"]
    crud.update_quantity(quantity_id, updated_amount)
    db.session.commit()

    return "Quantity Updated"


@app.route("/items/<item_id>/quantities", methods=["POST"])
def create_quantity(item_id):
    """Create a new quantity for the item."""

    logged_in_email = session.get("user_email")
    quantity_amount = request.form.get("quantity")

    if logged_in_email is None:
        flash("Log in to update quantity!")
    elif not quantity_amount:
        flash("Error: you didn't select a quantity.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        item = crud.get_item_by_id(item_id)

        quantity = crud.create_quantity(user, item, int(quantity_amount))
        db.session.add(quantity)
        db.session.commit()

        flash(f"You selected {quantity_amount} of this item.")

    return redirect(f"/items/{item_id}")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
