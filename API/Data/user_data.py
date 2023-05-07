import random, json
from datetime import datetime
from app.api.validators.authentication import modify_mail
Roles = {"Administrator": 1, "Category Manager": 2, "Moderator": 3, "Delivery": 4, "User": 5}


Names = ["Theo", "George", "Leo", "Arthur", "Archie", "Alfie", "Oscar", "Henry", "Harry", "Jack",
         "Teddy", "Finley", "Arlo", "Luca", "Jacob", "Tommy", "Lucas", "Theodore", "Max", "Isaac", "Albie", "James",
         "Mason", "Rory", "Thomas", "Rueben", "Roman", "Logan", "Harrison", "William"]

Lastname = ["Johnson", "Brown", "Jones", "Miller", "Davis", "Rodriguez", "Hernandez",
            "Lopez", "Gonzales", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee",
            "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
            "Young", "Allen", "King"]

employees = ["Anri Tvalabeishvili", "Ruso Kvesitazde", "Christine Dzneladze", "Zura Dzneladze"]


def create_workers_data(employees_data):
    file = open(f"Users.txt", 'w')
    emails = [f"{employee.replace(' ', '.')}@gmail.com" for employee in employees_data]
    roles = [1, 2, 3, 4]

    for employee, email, role in zip(employees_data, emails, roles):
        user = {
            "full_name": employee,
            "email": modify_mail(email),
            "role_id": role,
            "password": "password",
            "registration_date": datetime(random.randint(2021, 2022), random.randint(1, 12),
                                          random.randint(1, 26), random.randint(1, 12),
                                          random.randint(1, 59), random.randint(1, 59)).isoformat()
        }

        data = {"user": user}
        file.write(json.dumps(data) + ";\n")
    file.close()
    return "Done"


def user_populate_data(names, lastname):
    file = open(f"Users.txt", 'a')
    cities = ["Tbilisi"]

    full_names = [f"{name} {lastname}" for name, lastname in zip(names, lastname)]
    emails = [f"{name}.{lastname}@gmail.com" for name, lastname in zip(names, lastname)]

    def create_user(user_name, user_email):

        user = {
            "full_name": user_name,
            "email": modify_mail(user_email),
            "role_id": 5,
            "password": "password",
            "registration_date": datetime(random.randint(2019, 2022), random.randint(1, 12),
                                          random.randint(1, 26), random.randint(1, 12),
                                          random.randint(1, 59), random.randint(1, 59)).isoformat()
        }

        return user

    def create_card():
        data = []
        for i in range(random.randint(1, 3)):
            card_number = f"{random.randint(3, 6)}{random.randint(int(1e14), int(8e14))}"
            card_exp_date = datetime(random.randint(2019, 2026), random.randint(1, 12),
                                     random.randint(1, 26)).isoformat()

            brands = {
                "3": "American Express",
                "4": "Visa",
                "5": "Mastercard",
                "6": "Discover"
            }

            card = {
                "holder_name": full_name.upper(),
                "card_number": card_number,
                "card_exp_date": card_exp_date,
                "brand": brands[card_number[0]],
            }

            data.append(card)

        return data

    def create_address():
        data = []
        countries_file = open('Countries.txt', 'r')
        cities_file = open('Cities.txt', 'r')
        countries = countries_file.read().split("\n")
        cities = cities_file.read().split("\n")

        for i in range(random.randint(1, 3)):
            mobile_number = f"+({random.randint(int(1), int(999))}) {random.randint(int(354), int(999))}{random.randint(int(1e5), int(9e5))}"
            city = random.choice(cities)
            country = random.choice(countries)

            address = {
                "full_name": full_name,
                "mobile_number": mobile_number,
                "country_id": countries.index(country) + 1,
                "city": city,
                "State_Province_Region": "N/A",
                "building_address": f"{country}, {city}, bilbo baggins's {random.randint(1, 125)}",
                "Zip_code": random.randint(1000, 9000)
            }

            data.append(address)

        return data

    for full_name, email in zip(full_names, emails):
        data = {
            "user": create_user(full_name, email),
            "user_card": create_card(),
            "user_address": create_address()
        }
        file.write(json.dumps(data) + ";\n")

    file.close()
    return "Done"


create_workers_data(employees)
user_populate_data(Names, Lastname)
