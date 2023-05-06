from app.extensions import db
from app.models.base import BaseModel

class Purchase(BaseModel):
    __tablename__ = "purchases"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    address_id = db.Column(db.Integer, db.ForeignKey("user_addresses.id"))

    product_quantity_ = db.Column(db.Integer)
    user_price = db.Column(db.Integer)
    comment = db.Column(db.String)
    status = db.Column(db.String)
    purchase_date = db.Column(db.Date)
    delivery_date = db.Column(db.Date)

    user = db.relationship("User", backref = "purchase", uselist = False)
    product = db.relationship("Product", secondary = "product_and_purchase", backref = "purchase")
