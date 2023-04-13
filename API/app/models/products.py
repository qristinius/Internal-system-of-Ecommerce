from app.extensions import db
from app.models.base import BaseModel


class Cart(BaseModel):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))


class PurchaseProduct(BaseModel):
    __tablename__ = "product_and_purchase"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    purchase_id = db.Column(db.Integer, db.ForeignKey("purchases.id"))

class ProductComment(BaseModel):
    __tablename__ = "product_comments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))

    comment = db.Column(db.Text)
    picture_comment = db.Column(db.String) #this is photopath 
    comment = db.relationship("Product", backref = "comments")


class Product(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    price_id = db.Column(db.Integer, db.ForeignKey("prices.id"))
    brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id")) 

    name = db.Column(db.String)
    model = db.Column(db.String)
    quantity = db.Column(db.Integer)
    official_link = db.Column(db.String)
    photo_path = db.Column(db.String)
    score = db.Column(db.Float)
    
    user = db.relationship("User", secondary="cart", backref="product_cart")

class Price(BaseModel):
    __tablename__ = "prices"
    id = db.Column(db.Integer, primary_key=True)

    product = db.relationship("Product", backref="price", uselist=False)

    original_price = db.Column(db.Integer)
    selling_price = db.Column(db.Integer)
    sale_price = db.Column(db.Integer)
    sale = db.Column(db.Boolean)
    sale_start_date = db.Column(db.Date)
    sale_end_date = db.Column(db.Date)




class Brand(BaseModel):
    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String)
    product = db.relationship("Product", backref="brand")
