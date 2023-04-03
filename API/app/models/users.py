from app.extensions import db
from app.models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


class UserRole(BaseModel):
    __tablename__ = "user_roles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))


class User(BaseModel):
    __tablename__ = "registered_users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password = db.Column("password", db.String, nullable=False)
    reset_password = db.Column(db.Boolean, default=False)
    registration_date = db.Column(db.Date)
    confirmation = db.Column(db.Boolean, default=False)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    def _check_password(self, password):
        return check_password_hash(self.password, password)

    password = db.synonym("_password", descriptor=property(
        _get_password, _set_password))


class Role(BaseModel):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    can_create_role = db.Column(db.Boolean)
    can_create_product = db.Column(db.Boolean)
    can_create_sales = db.Column(db.Boolean)
    user = db.relationship("User", secondary="user_roles", backref="role")


class Address(BaseModel):
    __tablename__ = "user_addresses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    
    full_name = db.Column(db.String, nullable = False)
    mobile_number = db.Column(db.String, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"))
    city = db.Column(db.String, nullable=False)
    state_provincce_region = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)
    building_address = db.Column(db.String, nullable=False)
    user = db.relationship("User", backref="address")


class Country(BaseModel):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    adress = db.relationship("Address", backref="country")


class Card(BaseModel):
    __tablename__ = "user_card_info"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))

    card_number = db.Column(db.String, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    unique_number = db.Column(db.Integer, nullable=False)
    holder_name = db.Column(db.String, nullable=False)
    usable  = db.Column(db.Boolean, default = True)
    user = db.relationship("User", backref="cards")
