from flask import render_template
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from datetime import datetime
from app.models.users import User, UserRole
from app.api.validators.authentication import validate_registration_data, modify_mail
from app.api.validators.mail import create_key, send_email, confirm_key


class RegistrationApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("full_name", required=True, type=str)
    parser.add_argument("email", required=True, type=str)
    parser.add_argument("password", required=True, type=str)
    parser.add_argument("conf_password", required=True, type=str)

    def post(self):
        args = self.parser.parse_args()
        validation = validate_registration_data(args, User)

        if validation:
            return validation, 400

        user = User(full_name=args["full_name"],
                    email=modify_mail(args["email"]),
                    password=args["password"],
                    registration_date=datetime.today().isoformat()
                    )
        user.create()

        user_role = UserRole(user_id=user.id, role_id=4)
        user_role.create()

        user.save()
        user_role.save()

        key = create_key(modify_mail(args["email"]))
        html = render_template('auth/_activation_massage.html', key=key)

        send_email(subject="Confirm your account", html=html, recipients=args["email"])

        return "Success", 200


class AuthorizationApi(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("email", required=True, type=str)
    parser.add_argument("password", required=True, type=str)

    def post(self):

        args = self.parser.parse_args()

        user = User.query.filter_by(email=modify_mail(args["email"])).first()

        if user and user.check_password(args["password"]):
            access_token = create_access_token(identity=user.email)
            response = {'token': access_token}
            return response, 200

        else:

            return "Password or mail is incorrect", 400


class ResetPasswordApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", required=False, type=str)
    parser.add_argument("password", required=False, type=str)
    parser.add_argument("key", required=False, type=str)

    def post(self):
        args = self.parser.parse_args()
        if args["email"]:
            user = User.query.filter_by(email=args["email"]).first()
            if not user:
                return "Bad Request", 400
            if not user.check_permission("can_modify_profile"):
                return "Bad Request", 400

            user.reset_password = True
            reset_key = create_key(args["email"])
            html = render_template("auth/_reset_message.html", key=reset_key)
            send_email(subject="reset your password", html=html, recipients=args["email"])
            return "Success", 200
        
        elif args["key"] and args["password"]:
            email = confirm_key(args["key"])
            user = User.query.filter_by(email=email).first()

            if user:
                user.password = args["password"]
                user.reset_password = False
                user.save()
                return "Password changed successfully"
            return "Wrong secret key or expired, or already reset"
        
        else:
            return "Bad request", 400

