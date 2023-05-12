from flask_restful import Resource, reqparse, inputs
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
from app.models.products import ProductComment
from app.models.purchase import Purchase


class ProductCommentApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("product_id", required=True, type=int)
    parser.add_argument("comment", required=True, type=str)
    parser.add_argument("picture_path", required=False, type=str)
    parser.add_argument("comment_date", required=True, type=inputs.datetime_from_iso8601)

    @jwt_required()
    def post(self):
        args = self.parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        user_purchase = Purchase.query.filter_by(user_id=user.id, product_id=args["product_id"]).first()

        if not user_purchase:
            return "Bad Request", 400

        comment = ProductComment(user_id=user.id,
                                 product_id=args["product_id"],
                                 comment=args["comment"],
                                 picture_path=args["picture_path"],
                                 comment_date=args["comment_date"]
                                 )
        comment.create()
        comment.save()

        return "success", 200

    @jwt_required()
    def put(self):
        args = self.parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        selected_comment = ProductComment.query.filter_by(user_id=user.id, product_id=args["product_id"], comment_date=str(args["comment_date"])).first()
    

        if not selected_comment:
            return "Bad Request", 400

        selected_comment.product_id = args["product_id"]
        selected_comment.comment = args["comment"]
        selected_comment.picture_path = args["picture_path"]
        selected_comment.comment_date = args["comment_date"]
        selected_comment.save()

        return "success", 200

    @jwt_required() 
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("product_id", required=True, type=int)
        parser.add_argument("comment_date", required=True, type=inputs.datetime_from_iso8601)


        args = parser.parse_args()
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_buy_product"):
            return "Bad request", 400

        selected_comment = ProductComment.query.filter_by(user_id=user.id, product_id=args["product_id"], comment_date=str(args["comment_date"])).first()
    

        if not selected_comment:
            return "Bad Request", 400
    
        selected_comment.delete()
        selected_comment.save()
        return "Success", 200
