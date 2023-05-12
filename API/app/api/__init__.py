from flask_restful import Api
from app.api.authentication import RegistrationApi, AuthorizationApi, ResetPasswordApi
from app.api.address import AddressApi
from app.api.card import CardsApi
from app.api.comment import ProductCommentApi
from app.api.mailconfirmation import ReceiveKeyApi, ConfirmEmailApi
from app.api.score import ScoreApi
from app.api.messages import MessageApi

api = Api()
api.add_resource(RegistrationApi, "/Registration")
api.add_resource(AuthorizationApi, "/Authorization")
api.add_resource(AddressApi, "/Address")
api.add_resource(CardsApi, "/Cards")
api.add_resource(ResetPasswordApi, "/ResetPassword")
api.add_resource(ProductCommentApi, "/ProductComment")
api.add_resource(ReceiveKeyApi, "/ReceiveKey")
api.add_resource(ConfirmEmailApi,"/ConfirmEmail")
api.add_resource(ScoreApi, "/Score")
api.add_resource(MessageApi, "/Message")

