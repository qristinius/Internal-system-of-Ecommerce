from flask_restful import Resource, reqparse, inputs
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, Purchase
from datetime import datetime


class DeliveryApi(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("status", required=True, type=str)
    parser.add_argument("purchase_id", required=True, type=int)

    @jwt_required()
    def put(self):
        args = self.parser.parse_args()
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()

        purchase = Purchase.query.filter_by(id=args["purchase_id"]).first()

        if not user.check_permission("can_deliver_items"):
            return "Bad request", 200
        
        purchase.status = args["status"]
        purchase.save()

        if purchase.status == "Delivered":
            purchase.delivery_date = datetime.now()
            purchase.save()

        return "Success",200



