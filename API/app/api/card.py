from flask_restful import Resource, reqparse, inputs
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
from app.models.user_info import Card
from app.api.validators.card import validate_card_data, check_card_existence


class CardsApi(Resource):

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("card_number", required=True, type=str)
        parser.add_argument("holder_name", required=True, type=str)
        parser.add_argument("cvv", required=True, type=str)
        parser.add_argument("expiration_date", required=True, type=inputs.datetime_from_iso8601)

        args = parser.parse_args()
        current_user = get_jwt_identity()
        validation = validate_card_data(args)

        if validation:
            return validation, 400

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_modify_profile"):
            return "Bad request", 400

        # if not bank_accept:
        #     return "bad request", 400

        for card in user.cards:
            if check_card_existence(card, args):
                if not card.deleted:
                    return "this card is already added", 200

                card.deleted = False
                card.save()
                return "Success", 200

        new_card = Card(user_id=user.id,
                        card_number=args["card_number"],
                        holder_name=args["holder_name"].upper(),
                        expiration_date=args["expiration_date"],
                        )

        new_card.create()
        new_card.save()
        return "Success", 200

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_modify_profile"):
            return "Bad request", 400

        data = []
        for card in user.cards:
            if not card.deleted:
                user_card = {
                    "card_number": card.encrypt_card_number(),
                    "holder_name": card.holder_name,
                    "expiration_date": card.expiration_date,
                    "expired": not card.usable
                }

                data.append(user_card)

        return data, 200

    @jwt_required()
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("card_number", required=True, type=str)
        parser.add_argument("holder_name", required=True, type=str)
        parser.add_argument("expiration_date", required=True, type=inputs.datetime_from_iso8601)

        args = parser.parse_args()
        current_user = get_jwt_identity()

        user = User.query.filter_by(email=current_user).first()

        if not user.check_permission("can_modify_profile"):
            return "Bad request", 400

        for card in user.cards:

            if check_card_existence(card, args):
                if card.deleted:
                    return "bad request", 400
                card.deleted = True
                card.save()
                return "Success", 200

        return "bad request", 400
