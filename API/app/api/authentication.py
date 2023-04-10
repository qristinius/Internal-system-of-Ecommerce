from flask import render_template
from flask_restful import Resource, reqparse, inputs
from flask_jwt_extended import create_access_token
from app.models.users import User

# from app.models.roles import UserRole       დასამატებელი აქვს ქრისტინეს
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

        user = User(
            full_name=data["full_name"],
            email=data["email"],
            password=data["password"],
            # აქ რეგისტრაციის თარიღი მაქ დასამატებელი
            personal_id="N/A",  # შესაცველელია
            adress_id=5
            # აქ იცი როგორ მინდა user.address რო პირდაპირ მისამართს მიბრუნებდეს არ ვიცი ახლა მასეა თუ არა გაკეთებული
        )

        user.create()
        user.save()

        # user_role = UserRole(user_id=user.id, role_id=1)           # ეს მალე დამიმატო იქნება

        # user_role.create()
        # user_role.save()

        key = create_key(data["email"])
        html = render_template('_activation_massage.html', key=key)

        send_email(subject="Confirm your account", html=html, recipients=data["mail"])

        return "Success", 200


class AuthorizationApi(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("email", required=True, type=str)
    parser.add_argument("password", required=True, type=str)

    def post(self):

        data = self.parser.parse_args()

        user = User.query.filter_by(email=data["email"]).first()

        if user and user._check_password(data["password"]):
            access_token = create_access_token(identity=user.email)
            response = {'access token': access_token}
            return response, 200

        else:

            return "Password or mail is incorrect", 400
