from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
from app.models.user_info import Address, Country
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
        args = self.parser.parse_args()
        current_user = get_jwt_identity()
        validation = validate_address_data(args, Country)

        if validation:
            return validation, 400

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_modify_profile"):
            return "Bad request", 400

        address = Address(user_id=user.id,
                          full_name=args["full_name"],
                          mobile_number=args["mobile_number"],
                          country_id=args["country_id"],
                          city=args["city"],
                          state_province_region=args["state_province_region"],
                          building_address=args["building_address"],
                          zip_code=args["zip_code"]
                          )

        address.create()
        address.save()

        return "Success", 200

    @jwt_required()
    def get(self):
        
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_modify_profile"):
            return "Bad request", 400

        if not user.address:
            return [], 200

        data = []
        for address in user.address:
            if not address.deleted:
                country = Country.query.filter_by(id=address.country_id).first()
                user_address = {
                    "address_id": address.id,
                    "full_name": address.full_name,
                    "mobile_number": address.mobile_number,
                    "country": country.name,
                    "city": address.city,
                    "state_province_region": address.state_province_region,
                    "building_address": address.building_address,
                    "zip_code": address.zip_code,
                }
                data.append(user_address)

        return data, 200

    @jwt_required()
    def put(self):
        self.parser.add_argument("address_id", required=True, type=str)

        args = self.parser.parse_args()
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_modify_profile"):
            return "Bad request", 400

        result = Address.query.filter_by(id=args["address_id"]).first()

        if not result:
            return "Bad request", 400

        result.full_name = args["full_name"]
        result.mobile_number = args["mobile_number"]
        result.country_id = args["country_id"]
        result.city = args["city"]
        result.state_province_region = args["state_province_region"]
        result.building_address = args["building_address"]
        result.zip_code = args["zip_code"]
        result.save()

        return "Success", 200

    @jwt_required()
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("address_id", required=True, type=int)

        args = parser.parse_args()
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_modify_profile"):
            return "Bad request", 400

        result = Address.query.filter_by(id=args["address_id"]).first()

        if not result:
            return "Bad request", 400

        result.deleted = True
        result.save()

        return "Success", 200
