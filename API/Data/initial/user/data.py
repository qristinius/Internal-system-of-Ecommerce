import random
from datetime import date, datetime
from app.api.validators.authentication import modify_mail

Names = ["Zura", "Niniko"]
Lastname = ["Dzneladze", "Kvesitazde"]

Emails = [f"{name}.{lastname}@gmail.com" for name, lastname in zip(Names, Lastname)]
Full_names = [f"{name} {lastname}" for name, lastname in zip(Names, Lastname)]

Roles = {"Administrator": 1, "Category Manager": 2, "Moderator": 3, "User": 4}

Number_prefix = ["555", "557", "595", "599", "597", "571"]
Cities = ["Tbilisi", "Tbilisi", "Batumi", "Kutaisi", "Rustavi"]
Districts = ["Gldani", "Didube", "Vake", "Isani", "Krwanisi", "Mtathminda", "Nadzaladevi", "Saburtalo", "Samgori"]


def create_workers_data():
    data = []

    names = ["Anri", "Ruso", "Christine"]
    lastname = ["Tvalabeishvili", "Kvesitazde", "Dzneladze"]
    emails = [f"{name}.{lastname}@gmail.com" for name, lastname in zip(names, lastname)]
    full_names = [f"{name} {lastname}" for name, lastname in zip(names, lastname)]
    roles = [1, 2, 3]

    for full_name, email, role in zip(full_names, emails, roles):
        user = {
            "full_name": full_name,
            "email": modify_mail(email),
            "role_id": role,
            "password": "Admin",
            "registration_date": datetime(random.randint(2019, 2022), random.randint(1, 12),
                                          random.randint(1, 26), random.randint(1, 12),
                                          random.randint(1, 59), random.randint(1, 59)).isoformat()
        }

        data.append(user)

    return data


def user_populate_data(full_names, emails, number_prefix, cities, districts):
    data = []

    for full_name, email in zip(full_names, emails):

        def create_user():

            user = {
                "full_name": full_name,
                "email": modify_mail(email),
                "role_id": 4,
                "password": "Admin",
                "registration_date": datetime(random.randint(2019, 2022), random.randint(1, 12),
                                              random.randint(1, 26), random.randint(1, 12),
                                              random.randint(1, 59), random.randint(1, 59)).isoformat()
            }

            return user

        def create_card():
            cards = []
            for i in range(random.randint(1, 3)):
                card_number = f"{random.randint(2, 5)}{random.randint(int(1e14), int(8e14))}"
                card_exp_date = date(random.randint(2019, 2026), random.randint(1, 12), random.randint(1, 26))
                cvv = random.randint(101, 999)

                card = {
                    "holder_name": full_name.upper(),
                    "card_number": card_number,
                    "cvv": cvv,
                    "card_exp_date": card_exp_date,
                }

                cards.append(card)

            return cards

        def create_address():
            addresses = []

            for i in range(random.randint(1, 3)):

                mobile_number = f"{random.choice(number_prefix)}{random.randint(int(1e5), int(9e5))}"
                city = random.choice(cities)

                if city == "Tbilisi":
                    district = random.choice(districts)
                    address = {
                        "full_name": full_name,
                        "mobile_number": mobile_number,
                        "country_id": 2,
                        "city": city,
                        "State_Province_Region": district,
                        "building_address": f"{city}, {district}, middle earth {random.randint(10, 25)}",
                        "Zip_code": random.randint(100, 500)
                    }
                else:
                    address = {
                        "full_name": full_name,
                        "mobile_number": mobile_number,
                        "country_id": 2,
                        "city": city,
                        "State_Province_Region": "N/A",
                        "building_address": f"{city}, bilbo baggins's {random.randint(10, 25)}",
                        "Zip_code": random.randint(100, 500)
                    }

                addresses.append(address)

            return addresses

        data.append([create_user(), create_card(), create_address()])

    return data


# [{}, [{},{} ....], [{},{} .....]]     this is template of data

complete_admin_populate_data = create_workers_data()
complete_user_populate_data = user_populate_data(Full_names, Emails, Number_prefix, Cities, Districts)
