def validate_name(name):
    try:
        name = name.split(" ")

        if name[0].isalpha() and name[1].isalpha() and len(name[0] + name[1]) >= 4:
            return True
    except:
        return False


def validate_number(number):
    number_prefix = ["568", "571", "574", "579", "592", "597", "500", "550", "555",
                     "593", "514", "557", "558", "544", "511", "522", "533", "505",
                     "575", "585", "551", "591", "595", "596", "598", "599"]

    if number.isdecimal() and len(number) == 9 and str(number)[:3] in number_prefix:
        return True


def validate_address_data(data):
    if not validate_name(data["full_name"]):
        return "Invalid name"

    if not validate_number(data["number"]):
        return "Invalid number"
