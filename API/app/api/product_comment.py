from flask_restful import Resource, reqparse,inputs
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
from app.models.products import ProductComment


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
        
        if user:
            comment = ProductComment(
                user_id = user.id,
                product_id = parser["product_id"],
                comment = parser["comment"],
                picture_path = parser["picture path"],
               #comment_date = parser["comment_date"]  
            )
            comment.create()
            comment.save()

            return "success", 200

        

