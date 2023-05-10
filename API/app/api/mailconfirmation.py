from flask_restful import Resource, reqparse
from flask import render_template
from app.models.users import User
from app.api.validators.mail import create_key, send_email, confirm_key


class ReceiveKeyApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", required=True, type=str)

    def post(self):
        parser = self.parser.parse_args()
        user = User.query.filter_by(email=parser["email"]).first()

        if not user:
            return "Bad Request", 400 
        if not user.check_permission("can_modify_profile"):
            return "Bad Request", 400
        
        if user and not user.confirmation:
            key = create_key(parser["email"])
            html = render_template('auth/_activation_massage.html', key=key)

            send_email(subject="Confirm your account",
                       html=html, recipients=parser["email"])
            return "Success", 200
        return "invalid mail"


class ConfirmEmailApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("key", required=True, type=str)

    def post(self):
        parser = self.parser.parse_args()
        email = confirm_key(parser["key"])
        user = User.query.filter_by(email=email).first()
        if user and not user.confirmation:
            user.confirmation = True
            user.save()
            return "Success"
        else:
            return "Wrong secret key or expired, or already confirmed"
