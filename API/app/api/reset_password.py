from flask_restful import Resource, reqparse
from flask import render_template
from app.models.users import User
from app.api.validators.mail import create_key, send_email, confirm_key





class ForgotPasswordApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", required=True, type=str)

    def post(self):
        parser = self.parser.parse_args()
        user = User.query.filter_by(email = parser["email"]).first()
        if user:
            user.reset_password = True
            reset_key = create_key(parser["email"])
            html = render_template("auth/_reset_message.html", key=reset_key)
            send_email(subject ="reset your password", html=html, recipients=parser["email"])
            return "Success", 200
        return "Invalid mail"
    

class ResetPasswordApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("password", required=True, type=str)
    parser.add_argument("key", required=True, type=str )

    def post(self):
        parser = self.parser.parse_args()
        email = confirm_key(parser["key"])
        user = User.query.filter_by(email=email).first()

        if user:
            user.password = parser["password"]
            user.reset_password = False
            user.save()
            return "Password changed successfully"
        return "Wrong secret key or expired, or already reset"

            





     
