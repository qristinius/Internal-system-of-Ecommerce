from app.extensions import db
from app.models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


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

    user = db.relationship("User", backref="address")
    purchase = db.relationship("Purchase", backref="purchase_address")


class Country(BaseModel):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    adress = db.relationship("Address", backref="country", uselist=False)


class Card(BaseModel):
    __tablename__ = "user_card_info"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))

    _card_number = db.Column("card_number", db.String, nullable=False)
    _cvv = db.Column("cvv", db.Integer, nullable=False)
    holder_name = db.Column(db.String, nullable=False)
    usable = db.Column(db.Boolean, default=True)
    expiration_date = db.Column(db.Date, nullable=False)

    user = db.relationship("User", backref="cards")

    def _get_card_number(self):
        return self._card_number

    def _get_cvv(self):
        return self._cvv

    def _set_card_number(self, card_number):
        self._card_number = generate_password_hash(str(card_number))

    def _set_cvv(self, cvv):
        self._cvv = generate_password_hash(str(cvv))

    def _check_card_number(self, card_number):
        return check_password_hash(self.card_number, card_number)

    def _check_cvv(self, cvv):
        return check_password_hash(self.cvv, cvv)

    card_number = db.synonym("_card_number", descriptor=property(
        _get_card_number, _set_card_number))

    cvv = db.synonym("_cvv", descriptor=property(
        _get_cvv, _set_cvv))
