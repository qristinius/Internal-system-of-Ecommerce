from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
from app.models.user_info import Card
from app.api.validators.address import validate_address_data


class AddressApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("full_name", required=True, type=str)
    parser.add_argument("mobile_number", required=True, type=str)
    parser.add_argument("country_id", required=True, type=str)
    parser.add_argument("city", required=True, type=str)
    parser.add_argument("state_province_region", required=True, type=str)
    parser.add_argument("building_address", required=True, type=str)
    parser.add_argument("zip_code", required=True, type=str)

    @jwt_required()
    def post(self):

        return "Success", 200

    @jwt_required()
    def get(self):

        return "Success", 200

    @jwt_required()
    def put(self):

        return "Success", 200

    @jwt_required()
    def delete(self):

        return "Success", 200
