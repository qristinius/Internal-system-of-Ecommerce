from flask import render_template
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from datetime import datetime
from app.models.users import User, UserRole
from app.api.validators.authentication import validate_registration_data
from app.api.validators.mail import create_key, send_email


class RegistrationApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("full_name", required=True, type=str)
    parser.add_argument("email", required=True, type=str)
    parser.add_argument("password", required=True, type=str)
    parser.add_argument("conf_password", required=True, type=str)

    def post(self):
        data = self.parser.parse_args()
        validation = validate_registration_data(data, User)

        if validation:
            return validation, 400

        user = User(full_name=data["full_name"],
                    email=data["email"].lower().replace('.', ''),
                    password=data["password"],
                    registration_date=datetime.today().isoformat()
                    )
        user.create()

        user_role = UserRole(user_id=user.id, role_id=4)
        user_role.create()

        user.save()
        user_role.save()

        key = create_key(data["email"])
        html = render_template('_activation_massage.html', key=key)

        send_email(subject="Confirm your account", html=html, recipients=data["email"])

        return "Success", 200


class AuthorizationApi(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("email", required=True, type=str)
    parser.add_argument("password", required=True, type=str)

    def post(self):

        data = self.parser.parse_args()

        user = User.query.filter_by(email=data["email"].lower().replace('.', '')).first()

        if user and user.check_password(data["password"]):
            access_token = create_access_token(identity=user.email)
            response = {'access token': access_token}
            return response, 200

        else:

            return "Password or mail is incorrect", 400
