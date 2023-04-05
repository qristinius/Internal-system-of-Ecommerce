from app.extensions import db
from app.models.base import BaseModel

class Purchase(BaseModel):
    __tablename__ = "purchases"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    purchased_product_quantity_= db.Column(db.Integer)
    address_id = db.Column(db.Integer, db.ForeignKey("user_addresses.id"))
    user_price = db.Column(db.Integer)  #es raari?
    comment = db.Column(db.String)
    purhcase_date  = db.Column(db.Date)
    delivery_date = db.Column(db.Date)
    status = db.Column(db.String)
    user = db.relationship("User", backref = "purchase")

