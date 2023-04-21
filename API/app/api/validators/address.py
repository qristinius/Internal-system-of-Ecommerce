from app.api.validators.authentication import validate_name


def validate_country_id(user_country_id, country_table):
    ids = [country.id for country in country_table.query.all()]

    if int(user_country_id) in ids:
        return True


def validate_address_data(data, country_table):
    if not validate_name(data["full_name"]):
        return "Invalid name"

    if not validate_country_id(data["country_id"], country_table):
        return "Invalid country_id"
