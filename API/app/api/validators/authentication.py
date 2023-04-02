from email_validator import validate_email


def validate_name(name):

    try: 
        name = name.split(" ")

        if name[0].isalpha() and name[1].isalpha() and len(name[0] + name[1]) >= 4:
            return True
    except:
        return False
    

def validate_password(password):
    if len(password) > 6:
        return True


def mail_validator(email):
    try:
        emailObject = validate_email(email)
        return True
    except:
        return False


def user_exist_check(email,number, User):
    if bool(User.query.filter_by(email=email).first()):
        return "This mail is already redgistered"

    if bool(User.query.filter_by(mobile_number=number).first()):
        return "This number is already redgistered"



def validate_registration_data(data, User):

    if not validate_name(data["full_name"]):
        return "Invalid name"

    if not mail_validator(data["email"]):
        return "Invalid mail"

    if not validate_password(data["password"]):
        return "Invalid password"

    if data["password"] != data["conf_password"]:
        return "Invalid conf_password"

    exist_user = user_exist_check(data["email"], data["number"], User)

    if exist_user:
        return exist_user
