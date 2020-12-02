import sys
from flask import Flask, jsonify, request
from models import db, Fruit
from schemas import ma, fruit_schema, fruits_schema

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fruit.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ma.init_app(app)


@app.route("/fruits", methods=["GET"])
def get_fruits():
    """
    List existing fruits
    """

    fruits = Fruit.query.all()

    return fruits_schema.jsonify(fruits)


@app.route("/fruits/<int:id>", methods=["GET"])
def get_fruit(id):
    """
    Get detail of a fruit
    """

    fruit = Fruit.query.get_or_404(id)

    return fruit_schema.jsonify(fruit)


@app.route("/fruits", methods=["POST"])
def create_fruit():
    """
    Create a fruit
    """

    fruit = fruit_schema.load(request.form)

    db.session.add(fruit)
    db.session.commit()

    resp = jsonify(
        {
            "message": "created"
        }
    )
    resp.status_code = 201
    resp.headers["Location"] = fruit.url

    return resp


@app.route("/fruits/<int:id>", methods=["PUT"])
def update_fruit(id):
    """
    Update a fruit
    """

    fruit_data = Fruit.query.get_or_404(id)
    fruit = fruit_schema.load(request.form, instance=fruit_data)

    db.session.add(fruit)
    db.session.commit()

    resp = jsonify(
        {
            "message": "updated"
        }
    )

    return resp


@ app.route("/fruits/<int:id>", methods=["DELETE"])
def delete_fruit(id):
    """
    Delete a fruit
    """

    fruit = Fruit.query.filter(Fruit.id == id).first_or_404()

    db.session.delete(fruit)
    db.session.commit()

    return jsonify(
        {
            "message": "deleted"
        }
    )


@ app.errorhandler(404)
def page_not_found(error):
    """
    error handler for 404
    """

    resp = jsonify({"message": "resource is not found"})
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    if "create_db" in sys.argv:
        with app.app_context():
            db.create_all()

        print("Database created!")
    elif "seed_db" in sys.argv:
        with app.app_context():
            banana = Fruit(
                name="banana",
                description="banana lorem ipsum dolor sit amet"
            )

            db.session.add(banana)
            db.session.commit()

        print("Database seeded!")
    else:
        app.run(debug=True)
