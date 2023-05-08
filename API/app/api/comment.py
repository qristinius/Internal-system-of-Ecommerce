from flask_restful import Resource, reqparse,inputs
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
from app.models.products import ProductComment
from app.models.purchase import Purchase


class ProductCommentApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("product_id", required = True, type=int)
    parser.add_argument("comment", required = True, type=str)
    parser.add_argument("picture_path",required = True, type=str)
    parser.add_argument("comment_date", required = True, type=inputs.datetime_from_iso8601)



    @jwt_required()
    def post(self):
        parser=self.parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()
        permission = Purchase.query.filter_by(user_id = user.id, product_id=parser["product_id"]).first()

        if not permission:
            return "Bad Request", 400
        
        
        comment = ProductComment(user_id = user.id,
                                product_id = parser["product_id"],
                                comment = parser["comment"],
                                picture_path = parser["picture_path"],
                                comment_date = parser["comment_date"]  
                                )
        comment.create()
        comment.save()

        return "success", 200
    
    @jwt_required()
    def post(self):
        self.parser.add_argument("comment_id", required=True, type=str)
        
        parser=self.parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()
        user_purchase = Purchase.query.filter_by(user_id = user.id).first()

        if not user_purchase:
            return "Bad Request", 400
        
        selected_comment = ProductComment.query.filter_by(id=parser["comment_id"])

        if not selected_comment:
            return "Bad Request", 400
        
        selected_comment.product_id = parser["product_id"]
        selected_comment.comment = parser["comment"]
        selected_comment.picture_path = parser["picture_path"]
        selected_comment.comment_date = parser["comment_date"]
        selected_comment.save()

        return "success", 200
    

    
        



        

        

