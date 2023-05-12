from flask_restful import reqparse, Resource, inputs
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.purchase import Purchase
from app.models.users import User


class PurchaseApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("product_id", required=True, type=int)
    parser.add_argument("address_id", required=True, type=int)
    parser.add_argument("product_quantity", required=True, type=int)
    parser.add_argument("comment", required=False, type=str)
    parser.add_argument("purchase_date", required=True, type=inputs.datetime_from_iso8601)


    @jwt_required()
    def post(self):
        args = self.parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        purchase = Purchase(user_id=user.id,
                            product_id=args["product_id"],
                            address_id=args["address_id"],
                            product_quantity=args["product_quantity"],
                            user_price=args["user_price"],
                            comment=args["comment"],
                            status=args["status"],
                            purchase_date=args["purchase_date"],
                            delivery_date=args["delivery_date"]
                            )
        purchase.create()
        purchase.save()

        return "success", 200

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        user_purchase = Purchase.query.filtered_by(user_id=user.id).all()

        data = []

        for purchase in user_purchase:
            purchase = {
                "product_id": purchase.product_id,
                "address_id": purchase.address_id,
                "product_quantity": purchase.product_quantity,
                "user_price": purchase.user_price,
                "comment": purchase.comment,
                "status": purchase.status,
                "purchase_date": purchase.purchase_date,
                "delivery_date": purchase.delivery_date

            }

            data.append(purchase)

        return data, 200

    @jwt_required()
    def put(self):
        self.parser.add_argument("purchase_id", required=True, type=int)
        args = self.parser.parse_args()

        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        user_purchase = Purchase.query.filter_by(id=args["purchase_id"]).first()

        if not user_purchase:
            return "Bad request", 400

        user_purchase.product_id = args["product_id"],
        user_purchase.address_id = args["address_id"],
        user_purchase.product_quantity = args["product_quantity"],
        user_purchase.user_price = args["user_price"],
        user_purchase.comment = args["comment"],
        user_purchase.status = args["status"],
        user_purchase.purchase_date = args["purchase_date"],
        user_purchase.delivery_date = args["delivery_date"]

        user_purchase.save()

        return "Success", 200

    @jwt_required
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("purchase_id", required=True, type=int)

        args = parser.parse_args()
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        result = Purchase.query.filter_by(id=args["purchase_id"]).first()

        if not result:
            return "Bad request", 400

        result.delete()
        result.save()
        return "Success", 200
