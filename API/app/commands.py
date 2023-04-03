from flask.cli import with_appcontext
from app.extensions import db
from app.models import Role, User, UserRole, Address, Country
from Data.user_data import users_registration_data, users_adress_data
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
    # populating roles table
    def create_roles_table(Role):
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

    click.echo("Populating roles table")
    create_roles_table(Role)
    click.echo("finished creating roles table\n")

    # populating country table
    def create_country_table(Country):
        countries = ["USA", "Georgia", "Germany"]
        for country in countries:
            counries_ = Country(name=country)
            counries_.create()
        counries_.save()

    click.echo("populating country table")
    create_country_table(Country)
    click.echo("done populating user and userrole tables \n")

    # populating users table
    def create_users_table(User, UserRole):
        for user in users_registration_data:
            user_ = User(full_name=user.get("full_name"), email=user.get(
                "email"), password=user.get("password"), registration_date=user.get("registration_date"))
            user_.create()
            user_.save()
            userrole_ = UserRole(user_id=user_.id, role_id=user.get("role"))
            userrole_.create()
            userrole_.save()

    click.echo("populating user and userrole tables")
    create_users_table(User, UserRole)
    click.echo("done populating user and userrole tables \n")

   # populating adresses
    def create_adress_table(User, Address):
        for user_address in users_adress_data:
            user = User.query.filter_by(
                full_name=user_address.get("full_name"))
            user_address_ = Address(user_id=user.id, full_name=user_address.get("full_name"), mobile_number=user_address.get("mobile_number"), country_id=user_address.get("country"), city=user_address.get(
                "city"), state_provincce_region=user_address.get("State_Province_Region"), zip_code=user_address.get("Zip_code"), building_address=user_address.get("building_address"))
            user_address_.create()
        user_address_.save()
    
    click.echo("creating user adresss table")
    create_adress_table(User, Address)
    click.echo("done populating user adress tables \n")
    click.echo("nothing")
