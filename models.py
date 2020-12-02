from flask import url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Fruit(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String,
        index=True
    )

    description = db.Column(
        db.Text
    )

    @property
    def url(self):
        return url_for("get_fruit", id=self.id)
