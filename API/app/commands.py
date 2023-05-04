from flask.cli import with_appcontext
from app.extensions import db
from datetime import datetime
import json
from app.models import Role, User, UserRole, Address, Country, Card, Category, Attribute
import click


# global functions

# populating roles table
def create_roles_table(role_class):
    click.echo("Populating roles table \n")

    role = role_class(name="Admin", can_create_role=True, can_send_message=True)
    role.create()
    role = role_class(name="Category Manager", can_create_product=True, can_create_sales=True, can_see_stats=True,
                      can_send_message=True)
    role.create()
    role = role_class(name="Moderator", can_create_product=True, can_create_sales=True, can_send_message=True)
    role.create()
    role = role_class(name="Delivery", can_deliver_items=True, can_send_message=True)
    role.create()
    role = role_class(name="User", can_modify_profile=True, can_write_comment=True, can_rate_product=True,
                      can_buy_product=True)
    role.create()
    role.save()


# populating country table
def create_country_table(country_class):
    click.echo("populating country table \n")

    file = open('Data/Countries.txt', 'r')
    content = file.read().split("\n")
    for item in content:
        country = country_class(name=item)
        country.create()
        country.save()


# populating User, Card, Address table
def create_users_table(size, user_class, user_role_class, card_class, address_class):
    click.echo("populating: user, address and card tables \n")
    file = open('Data/Users.txt', 'r')
    data = file.read().split(";\n")

    for all_user_info in data[size[0]:size[1]]:
        user_data = json.loads(all_user_info)

        user_info = user_data["user"]
        user_ = user_class(full_name=user_info.get("full_name"),
                           email=user_info.get("email"),
                           password=user_info.get("password"),
                           registration_date=user_info.get("registration_date"))
        user_.create()
        user_.save()

        user_role_ = user_role_class(
            user_id=user_.id, role_id=user_info.get("role_id"))
        user_role_.create()
        user_role_.save()

        try:
            for user_card in user_data["user_card"]:

                if datetime.fromisoformat(user_card.get("card_exp_date")) > datetime.now():
                    card_ = card_class(user_id=user_.id,
                                       card_number=user_card.get("card_number"),
                                       expiration_date=user_card.get(
                                           "card_exp_date"),
                                       holder_name=user_card.get("holder_name"),
                                       brand=user_card.get("brand"))
                else:
                    card_ = card_class(user_id=user_.id,
                                       card_number=user_card.get("card_number"),
                                       expiration_date=user_card.get(
                                           "card_exp_date"),
                                       holder_name=user_card.get("holder_name"),
                                       usable=False,
                                       brand=user_card.get("brand"))

                card_.create()

                card_.save()

            for user_address in user_data["user_address"]:
                address_ = address_class(user_id=user_.id,
                                         full_name=user_address.get("full_name"),
                                         mobile_number=user_address.get(
                                             "mobile_number"),
                                         country_id=user_address.get("country_id"),
                                         city=user_address.get("city"),
                                         state_province_region=user_address.get(
                                             "State_Province_Region"),
                                         zip_code=user_address.get("Zip_code"),
                                         building_address=user_address.get("building_address"))
                address_.create()

                address_.save()

        except:

            continue


# populating category table
def create_category_table(category_table):
    click.echo("populating category table \n")

    file = open('Data/Category.txt', 'r')
    content = json.loads(file.read())
    main_category = list(content.keys())

    for main_category_name in main_category:
        main_category_data = (content[main_category_name])

        main = category_table(name=main_category_name)
        main.create()
        main.save()

        if dict == type(main_category_data):
            secondary_categories = list(main_category_data.keys())

            for second_category_name in secondary_categories:
                third_categories = main_category_data[second_category_name]

                secondary = category_table(name=second_category_name, parent_id=main.id)
                secondary.create()
                secondary.save()

                for third_category_name in third_categories:
                    # main_category_name
                    # second_category_name
                    # third_category_name

                    third = category_table(name=third_category_name, parent_id=secondary.id)
                    third.create()
                    third.save()
        else:

            for second_category_name in main_category_data:
                secondary = category_table(name=second_category_name, parent_id=main.id)
                secondary.create()
                secondary.save()


# populating Attribute tables
def create_attribute_table(attribute_table, category_table):
    click.echo("populating Attribute table \n")

    file = open('Data/Attributes.txt', 'r')
    content = json.loads(file.read())
    category_names = list(content.keys())

    for category_name in category_names:
        category = category_table.query.filter_by(name=category_name).first()
        attributes = content[category_name]
        for attribute in attributes:
            main = attribute_table(name=attribute, category_id=category.id)
            main.create()
            main.save()


@click.command("test")
@with_appcontext
def test():
    print("True")


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
    create_users_table([0, 7], User, UserRole, Card, Address)
    create_category_table(Category)
    create_attribute_table(Attribute, Category)
    click.echo("Done all")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("\n")

    create_roles_table(Role)
    create_country_table(Country)
    create_users_table([0, -1], User, UserRole, Card, Address)
    create_category_table(Category)
    create_attribute_table(Attribute, Category)

    click.echo("Done all")
