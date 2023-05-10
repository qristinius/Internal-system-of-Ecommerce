from flask_restful import Resource, reqparse,inputs
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
from app.models.purchase import Purchase
from app.models.products import Score



class ScoreApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("product_id", required = True, type=int)
    parser.add_argument("score", required = True, type=int)

    @jwt_required()
    def post(self):
        args=self.parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400 
        
        permission = Purchase.query.filter_by(user_id = user.id, product_id=args["product_id"]).first()

        if not permission:
            return "Bad Request", 400
        
        score = Score(user_id = user.id,
                      product_id = args["product_id"],
                      score = args["score"]
                      )
        score.create()
        score.save()

        return"success", 200
    

    @jwt_required()
    def put(self):
        self.parser.add_argument("score_id", required=True, type=str)
        
        args=self.parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()
        user_purchase = Purchase.query.filter_by(user_id = user.id, product_id=args["product_id"]).first()
        
        if not user_purchase:
            return "Bad Request", 400
        
        selected_score = Score.query.filter_by(id=args["score_id"]).first()
        

        if not selected_score:
            return "Bad Request", 400
        
        selected_score.product_id = args["product_id"]
        selected_score.score = args["score"]
        selected_score.save()

        return "success", 200
        
    



