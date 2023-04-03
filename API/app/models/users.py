from app.extensions import db
from app.models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel):
    __tablename__ = "registered_users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, unique=True, nullable=False)
    personal_id = db.Column(db.String, unique=True, nullable=False) # ეს ამოვიღოთ არაფერში არ გამოვიყენებთ მაინც
    mobile_number = db.Column(db.String, unique=True, nullable=False)  # ნომერი აქედან ამოვიღოთ და მისამართში ჩავამატოთ
    email = db.Column(db.String, unique=True, nullable=False)
    adress_id = db.Column(db.Integer, db.ForeignKey("user_adresses.id"))
    _password = db.Column("password", db.String, nullable=False)
    reset_password = db.Column(db.Boolean)
    registration_date = db.Column(db.Date)
    cards_id = db.Column(db.Integer, db.ForeignKey("user_card_info.id"))

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    def _check_password(self, password):
        return check_password_hash(self.password, password)

    password = db.synonym("_password", descriptor=property(
        _get_password, _set_password))


class Adress(BaseModel):
    __tablename__ = "user_adresses"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String)
    distrinct = db.Column(db.String)
    specific_adress = db.Column(db.String)
    user = db.relationship("User", backref="user_adress", uselist=False)


class Card(BaseModel):
    __tablename__ = "user_card_info"

    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String)
    card_exp_date = db.Column(db.Date)
    conf_number = db.Column(db.Integer)  # what is that?
    holder_name = db.Column(db.String, )
    user = db.relationship("User", backref="user_card", uselist=False)
