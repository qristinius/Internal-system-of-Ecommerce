from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
from app.models.purchase import Purchase
from app.models.products import Score
from app.api.validators.score import validate_score_range


class ScoreApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("product_id", required=True, type=int)
    parser.add_argument("score", required=True, type=int)

    @jwt_required()
    def post(self):
        args = self.parser.parse_args()
        current_user = get_jwt_identity()
        validation = validate_score_range(args["score"])

        if validation:
            return validation, 400

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        purchased = Purchase.query.filter_by(user_id=user.id, product_id=args["product_id"]).first()
        

        if not purchased:
            return "Bad Request", 400
        
        

        score = Score(user_id=user.id,
                      product_id=args["product_id"],
                      score=args["score"]
                      )
        score.create()
        score.save()

        return "Success", 200

    @jwt_required()
    def put(self):
        args = self.parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        selected_score = Score.query.filter_by(user_id=user.id, product_id=args["product_id"]).first()

        if not selected_score:
            return "Bad Request", 400

        selected_score.product_id = args["product_id"]
        selected_score.score = args["score"]
        selected_score.save()

        return "Success", 200


    @jwt_required()
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("product_id", required=True, type=int)

        args = parser.parse_args()
        current_user = get_jwt_identity()
        user=User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400
        
        selected_score = Score.query.filter_by(user_id=user.id, product_id=args["product_id"]).first()

        if not selected_score:
            return "Bad Request", 400
        
        selected_score.delete()
        selected_score.save()

        return "Success", 200
        
