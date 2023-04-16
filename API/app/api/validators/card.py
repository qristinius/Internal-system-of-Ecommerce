from app.api.validators.authentication import validate_name
from datetime import datetime


def validate_card_number(card_number):
    if card_number[0] == "3" and len(card_number) == 15:
        return True
    elif card_number[0] in ["4", "5", "6"] and len(card_number) == 16:
        return True


def validate_card_expiration_date(expiration_date):
    if datetime.now() < expiration_date:
        return True


def validate_card_data(data):
    if not validate_name(data["holder_name"]):
        return "Invalid name"

    if not validate_card_number(data["card_number"]):
        return "Invalid card number"

    if not validate_card_expiration_date(data["expiration_date"]):
        return "card is expired"


def check_card_existence(card, args):
    check_expiration_date = str(card.expiration_date) == str(args["expiration_date"])
    check_holder_name = card.holder_name == args["holder_name"].upper()
    check_card_number = card.encrypt_card_number() == args["card_number"][-4:]

    if check_expiration_date and check_holder_name and check_card_number:
        return True
