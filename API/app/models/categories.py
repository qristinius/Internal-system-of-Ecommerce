from app.extensions import db
from app.models.base import BaseModel

class Category(BaseModel):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    parent_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

class SubCategory(BaseModel):
    __tablename__ = "sub_category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    parent_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    attributes = db.relationship("ProductCharacteristic", backref = "type")

class ProductCharacteristic(BaseModel):
    __tablename__ = "characteristic"
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    product_type_id = db.Column(db.Integer, db.ForeignKey("sub_category.id"))


