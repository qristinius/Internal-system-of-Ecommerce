from flask.cli import with_appcontext
from app.extensions import db
import datetime
from app.models import Role, User, UserRole, Address, Country, Card
from Data.initial.user.data import complete_admin_populate_data, complete_user_populate_data
import click


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating Database")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("\n")

    # populating roles table
    def create_roles_table(Role):
        click.echo("Populating roles table")

        role_ = Role(name="Admin", can_create_role=True,
                     can_create_product=False, can_create_sales=False)
        role_.create()
        role_ = Role(name="Category Manager", can_create_role=False,
                     can_create_product=True, can_create_sales=True)
        role_.create()
        role_ = Role(name="Moderator", can_create_role=False,
                     can_create_product=True, can_create_sales=False)
        role_.create()
        role_ = Role(name="User", can_create_role=False,
                     can_create_product=False, can_create_sales=False)
        role_.create()
        role_.save()

        click.echo("finished creating roles table\n")

    # populating country table
    def create_country_table(Country):
        click.echo("populating country table")

        countries = ["USA", "Georgia", "Germany"]
        for country in countries:
            country_ = Country(name=country)
            country_.create()
        country_.save()

        click.echo("done populating country tables \n")

    # function for populating [users, address, card] tables
    def create_users_table(User, UserRole, Card, Address):

        click.echo("populating employees and employee's role tables")
        for worker in complete_admin_populate_data:
            worker_ = User(full_name=worker.get("full_name"),
                           email=worker.get("email"),
                           password=worker.get("password"),
                           registration_date=worker.get("registration_date"))
            worker_.create()
            worker_.save()

            worker_role_ = UserRole(user_id=worker_.id, role_id=worker.get("role_id"))
            worker_role_.create()
            worker_role_.save()
        click.echo("done populating employees and employee's role tables \n")

        click.echo("populating: user, address and card tables")
        for all_user_info in complete_user_populate_data:

            user_info = all_user_info[0]
            user_ = User(full_name=user_info.get("full_name"),
                         email=user_info.get("email"),
                         password=user_info.get("password"),
                         registration_date=user_info.get("registration_date"))
            user_.create()
            user_.save()

            user_role_ = UserRole(user_id=user_.id, role_id=user_info.get("role_id"))
            user_role_.create()
            user_role_.save()

            for user_card in all_user_info[1]:

                if user_card.get("card_exp_date") > datetime.date.today():
                    card_ = Card(user_id=user_.id,
                                 card_number=user_card.get("card_number"),
                                 expiration_date=user_card.get("card_exp_date"),
                                 cvv=user_card.get("cvv"),
                                 holder_name=user_card.get("holder_name"))
                else:
                    card_ = Card(user_id=user_.id,
                                 card_number=user_card.get("card_number"),
                                 expiration_date=user_card.get("card_exp_date"),
                                 cvv=user_card.get("cvv"),
                                 holder_name=user_card.get("holder_name"),
                                 usable=False)
                card_.create()

            card_.save()

            for user_address in all_user_info[2]:
                address_ = Address(user_id=user_.id,
                                   full_name=user_address.get("full_name"),
                                   mobile_number=user_address.get("mobile_number"),
                                   country_id=user_address.get("country_id"),
                                   city=user_address.get("city"),
                                   state_province_region=user_address.get("State_Province_Region"),
                                   zip_code=user_address.get("Zip_code"),
                                   building_address=user_address.get("building_address"))
                address_.create()

            address_.save()
        click.echo("done populating: user, address and card tables \n")

    # populating users table
    create_roles_table(Role)
    create_country_table(Country)
    create_users_table(User, UserRole, Card, Address)

    click.echo("Done all")
