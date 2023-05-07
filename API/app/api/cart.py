from flask_restful import Resource, reqparse, inputs
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
from app.models.products import Cart, Product
from app.models.categories import ProductAttribute, Attribute


class CartsApi(Resource):

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("product_id", required=True, type=int)
        parser.add_argument("quantity", required=True, type=int)

        args = parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()
        product = Product.query.filter_by(id=args["product_id"]).first()

        if not product:
            return "Bad request", 400

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        existed_product = Cart.query.filter_by(product_id=product.id, user_id=user.id).first()

        if existed_product:
            existed_product.quantity = existed_product.quantity + args["quantity"]
            existed_product.save()
            return "Success", 200

        new_card = Cart(user_id=user.id,
                        product_id=product.id,
                        quantity=args["quantity"]
                        )

        new_card.create()
        new_card.save()

        return "Success", 200

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        data = []

        for product in user.product_cart:
            item = Cart.query.filter_by(product_id=product.id, user_id=user.id).first()
            img = ProductAttribute.query.filter_by(product_id=product.id,
                                                   attribute_id=Attribute.query.filter_by(name="img",
                                                                                          category_id=product.category_id).first().id).first().value
            online_img = ProductAttribute.query.filter_by(product_id=product.id,
                                                          attribute_id=Attribute.query.filter_by(name="online_img",
                                                                                                 category_id=product.category_id).first().id).first().value
            data.append(
                {
                    "cart_id": item.id,
                    "product_id": product.id,
                    "product_name": product.name,
                    "quantity": item.quantity,
                    "price": product.price.get_price(),
                    "img": img,
                    "online_img": online_img
                }
            )

        return data, 200

    @jwt_required()
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("cart_id", required=True, type=int)
        parser.add_argument("quantity", required=True, type=int)

        args = parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        item = Cart.query.filter_by(id=args["cart_id"]).first()

        if not item:
            return "Bad request", 400

        item.quantity = args["quantity"]
        item.save()

        return "Success", 200

    @jwt_required()
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("cart_id", required=True, type=int)

        args = parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        item = Cart.query.filter_by(id=args["cart_id"]).first()

        if not item:
            return "Bad request", 400

        item.delete()
        item.save()

        return "Success", 200
