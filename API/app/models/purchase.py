from app.extensions import db
from app.models.base import BaseModel

class PurchaseAddress(BaseModel):
    __tablename__ = "adresses_of_purchases"
    id = db.Column(db.Integer, primary_key = True)
    address_id = db.Column(db.Integer, db.ForeignKey("user_addresses.id"))
    purchase_id = db.Column(db.Integer, db.ForeignKey("purchases.id"))


class Purchase(BaseModel):
    __tablename__ = "purchases"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))

    purchased_product_quantity_= db.Column(db.Integer)
    user_price = db.Column(db.Integer)
    comment = db.Column(db.String)
    status = db.Column(db.String)
    purhcase_date  = db.Column(db.Date)
    delivery_date = db.Column(db.Date)
    user = db.relationship("User", backref = "purchase", uselist = False)
    product = db.relationship("Product", secondary = "product_and_purchase", backref = "purchase")
    adress = db.relationship("Address", secondary = "adresses_of_purchases", backref = "address_purchase")
