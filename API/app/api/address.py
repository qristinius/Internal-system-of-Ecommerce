from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
from app.api.validators.address import validate_address_data

class AddaddressApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("country", required=True, type=str)
    parser.add_argument("full_name", required=True, type=str)
    parser.add_argument("City", required=True, type=str)
    parser.add_argument("number", required=True, type=str)
    parser.add_argument("State_Province_Region", required=True, type=str)
    parser.add_argument("building_address", required=True, type=str)
    parser.add_argument("Zip_Code", required=True, type=str)

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        data = self.parser.parse_args()

        validation = validate_address_data(data)

        if validation:
            return validation, 400



        # user = User(
        #     full_name=data["full_name"],
        #     email=data["email"],
        # )                             # ამათ მაგივრად უნდა ჩავამტო მონაცემთა ბაზაში იუზერის დამატებული მისამართი

        # user.create()
        # user.save()



    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()


        # უკან გავაგზავნო ამ მომხმარებლის ყველა დამატებული მისამართი