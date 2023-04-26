from app.extensions import db
from app.models.base import BaseModel


class Category(BaseModel):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    name = db.Column(db.String)

    product = db.relationship("Product", backref="category")


class SubCategory(BaseModel):
    __tablename__ = "sub_category"
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    name = db.Column(db.String)

    characteristics = db.relationship("ProductCharacteristic", backref="type")


class ProductCharacteristic(BaseModel):
    __tablename__ = "characteristic"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    subcategory_id = db.Column(db.Integer, db.ForeignKey("sub_category.id"))
