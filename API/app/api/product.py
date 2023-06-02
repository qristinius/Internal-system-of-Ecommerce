from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Product
from app.models import Category


class ProductsApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("category_id", required=True, type=int)

    def get(self):
        args = self.parser.parse_args()
        category_id = args["category_id"]

        categories = [category.id for category in Category.query.filter_by(parent_id=category_id).all()]

        if not categories:
            data = []
            products = Product.query.filter_by(category_id=category_id).all()

            for product in products:
                data.append(
                    {
                        "name": product.name,
                        #"score": product.score,
                        "old_price": product.price.selling_price,
                        "new_price": product.price.get_price(),
                    }
                )

            return data, 200

        data = []

        for category in categories:
            products = Product.query.filter_by(category_id=category).all()

            for product in products:
                data.append(
                    {
                        "name": product.name,
                        #"score": product.score,
                        "old_price": product.price.selling_price,
                        "new_price": product.price.get_price(),
                    }
                )

        return data, 200
