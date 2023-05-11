from flask.cli import with_appcontext
from app.extensions import db
from app.models import Role, User, UserRole, Address, Country, Card, Category, Attribute
from app.models import ProductAttribute, Purchase, Brand, Product, Price
from app.functions_for_commands import *


@click.command("test")
@with_appcontext
def test():
    click.echo("nothing")


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating Database")


@click.command("populate_test_db")
@with_appcontext
def populate_test_db():
    click.echo("\n")

    create_roles_table(Role)
    create_country_table(Country)
    create_users_table(User, UserRole, Card, Address, quantity=7)
    create_category_table(Category)
    create_attribute_table(Attribute, Category)
    create_brand_table(Brand)
    create_product_table(Product, Category, Attribute, Brand, Price, ProductAttribute, quantity=3)
    create_purchase_table(Purchase, User, Product, 5)

    click.echo("Done all")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("\n")

    create_roles_table(Role)
    create_country_table(Country)
    create_users_table(User, UserRole, Card, Address)
    create_category_table(Category)
    create_attribute_table(Attribute, Category)
    create_brand_table(Brand)
    create_product_table(Product, Category, Attribute, Brand, Price, ProductAttribute)
    create_purchase_table(Purchase, User, Product, 3e4)
    click.echo("Done all")
