from app.extensions import db
from app.models.base import BaseModel
from cryptography.fernet import Fernet
from app.models.users import User


class Address(BaseModel):
    __tablename__ = "user_addresses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))

    full_name = db.Column(db.String, nullable=False)
    mobile_number = db.Column(db.String, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"))
    city = db.Column(db.String, nullable=False)
    state_province_region = db.Column(db.String, nullable=False)
    building_address = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)
    deleted = db.Column(db.Boolean, default=False)

    user = db.relationship("User", backref="address")
    purchase = db.relationship("Purchase", backref="purchase_address")


class Country(BaseModel):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.relationship("Address", backref="country", uselist=False)


class Card(BaseModel):
    __tablename__ = "user_card_info"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))

    _card_number = db.Column("card_number", db.String, nullable=False)
    holder_name = db.Column(db.String, nullable=False)
    expiration_date = db.Column(db.TEXT, nullable=False)
    brand = db.Column(db.String)  #ამას nullable ´false უნდა დაეწეროს მას მერე რაც დათა შეიცვლება 
    usable = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    user = db.relationship("User", backref="cards")

    def _get_card_number(self):
        return self._card_number

    def _set_card_number(self, card_number):
        user = User.query.filter_by(id=self.user_id).first()
        secret = Fernet(user.password[-43:] + "=")
        self._card_number = secret.encrypt(bytes(str(card_number), 'utf-8'))

    def check_card_number(self, card_number):
        user = User.query.filter_by(id=self.user_id).first()
        secret = Fernet(user.password[-43:] + "=")
        if self.card_number == secret.encrypt(bytes(str(card_number), 'utf-8')):
            return True

    def encrypt_card_number(self):
        user = User.query.filter_by(id=self.user_id).first()
        secret = Fernet(user.password[-43:] + "=")
        card_number = str(secret.decrypt(self.card_number))
        return card_number[-5:-1]

    card_number = db.synonym("_card_number", descriptor=property(
        _get_card_number, _set_card_number))
