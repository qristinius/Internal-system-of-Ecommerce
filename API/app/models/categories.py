from app.extensions import db
from app.models.base import BaseModel


class ProductAttribute(BaseModel):
    __tablename__ = "product_attributes"

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    attribute_id = db.Column(db.Integer, db.ForeignKey("attributes.id"))
    value = db.Column(db.String)


class Category(BaseModel):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    name = db.Column(db.String)

    product = db.relationship("Product", backref="category")


class Attribute(BaseModel):
    __tablename__ = "attributes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    product = db.relationship("Product", secondary="product_attributes", backref="attributes")
