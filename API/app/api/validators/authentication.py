from email_validator import validate_email


def validate_name(name):
    def check_name(user_name):
        full_name = ""
        for i in range(len(user_name)):
            if user_name[i].isalpha():
                full_name += user_name[i]
            else:
                return False
        return full_name

    try:
        name = name.split(" ")

        if check_name(name) and len(check_name(name)) >= 4:
            return True
    except:
        return False


def validate_password(password):
    if len(password) > 6:
        return True


def mail_validator(email):
    try:
        email_object = validate_email(email)
        return email_object
    except:
        return False


def user_exist_check(email, user_table):
    if bool(user_table.query.filter_by(email=modify_mail(email)).first()):
        return True


def modify_mail(email):
    email = email.lower().split("@")

    prefix = email[0].replace('.', '')
    suffix = email[1]

    return f"{prefix}@{suffix}"


def validate_registration_data(data, user_table):
    if not validate_name(data["full_name"]):
        return "Invalid name"

    if not mail_validator(data["email"]):
        return "Invalid mail"

    if not validate_password(data["password"]):
        return "Invalid password"

    if data["password"] != data["conf_password"]:
        return "Invalid conf_password"

    if user_exist_check(data["email"], user_table):
        return "This mail is already registered"



