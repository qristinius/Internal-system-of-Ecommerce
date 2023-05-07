from flask_restful import Api
from app.api.authentication import RegistrationApi, AuthorizationApi
from app.api.address import AddressApi
from app.api.card import CardsApi
from app.api.cart import CartsApi

api = Api()
api.add_resource(RegistrationApi, "/Registration")
api.add_resource(AuthorizationApi, "/Authorization")
api.add_resource(AddressApi, "/Address")
api.add_resource(CardsApi, "/Cards")
api.add_resource(CartsApi, "/Carts")
