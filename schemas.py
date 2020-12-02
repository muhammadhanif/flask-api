from flask_marshmallow import Marshmallow
from models import Fruit

ma = Marshmallow()


class FruitSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        model = Fruit


fruit_schema = FruitSchema()
fruits_schema = FruitSchema(many=True)
