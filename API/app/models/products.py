from app.extensions import db
from app.models.base import BaseModel


class Cart(BaseModel):
    __tablename__  = "cart"

    id = db.Column(db.Integer, primary_key = True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))


class Product(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"))
    model = db.Column(db.String)
    qunatity = db.Column(db.Integer)
    description = db.Column(db.String)
    official_link = db.Column(db.String)
    user = db.relationship("User", secondary = "cart", backref = "product_cart")


class Price(BaseModel):
    __tablename__ = "prices"
    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    product = db.relationship("Product", backref="product_price")

    purchhase_price = db.Column(db.Integer)
    selling_price = db.Column(db.Integer)
    sale_price = db.Column(db.Integer)
    sale = db.Column(db.Boolean)
    sale_start_date = db.Column(db.Date)
    sale_end_date = db.Column(db.Date)


class Brand(BaseModel):
    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String)
    product = db.relationship("Product", backref="product_brand")
