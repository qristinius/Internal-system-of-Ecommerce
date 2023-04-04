import random, time
from datetime import date
import datetime

names = [
"Anri","Theo","Christina","George","Leo","Ruso",
"Arthur","Archie","Alfie","Niniko","Oscar","Henry",
"Harry","Jack","Teddy","Finley","Arlo","Luca","Jacob","Tommy",
"Lucas","Theodore","Max","Isaac","Albie","James","Mason","Rory",
"Thomas","Rueben","Roman","Logan","Harrison","William" ,"Elijah"
]


surnames = [
"Tvalabeishvili","Johnson","Dzneladze","Brown","Jones","Kvesitadze","Miller",
"Davis","Rodriguez","Kvesitadze","Hernandez","Lopez","Gonzales",
"Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin",
"Lee","Perez","Thompson","White","Harris","Sanchez","Clark",
"Ramirez","Lewis","Robinson","Walker","Young","Allen","King","Wright"
]

number_prefix = ["555","557","595", "599", "597", "571"]

cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi","Tbilisi"]

districts = ["Gldani","Didube","Vake", "Isani", "Krwanisi", "Mtathminda", "Nadzaladevi","Saburtalo", "Samgori"]

fullnames = [f"{name} {surname}" for name,surname in zip(names,surnames)]

mails = [f"{name}.{surname}@gmail.com" for name,surname in zip(names,surnames)]

mobile_numbers = [f"{random.choice(number_prefix )}{random.randint(1e5,9e5)}" for i in range(50)]


def create_users_registration_data(fullnames,mails ):


    data = []

    count = 0


    for fullname, mail in zip(fullnames,mails):

        if count< 2:
            user = {
                "full_name" : fullname,
                "email": mail,
                "role": 1,
                "password": mail,
                "registration_date": datetime.date(random.randint(2019,2022), random.randint(1,12), random.randint(1,26))
            }

        elif count< 5:

            user = {
                "full_name" : fullname,
                "email": mail,
                "role": 2,
                "password": mail,
                "registration_date": datetime.date(random.randint(2019,2022), random.randint(1,12), random.randint(1,26))
            }
        elif count<9:
                user = {
                "full_name" : fullname,
                "email": mail,
                "role": 3,
                "password": mail,
                "registration_date":  datetime.date(random.randint(2019,2022), random.randint(1,12), random.randint(1,26))
            }
        else:
            user = {
                "full_name" : fullname,
                "email": mail,
                "role": 4,
                "password": mail,
                "registration_date": datetime.date(random.randint(2019,2022), random.randint(1,12), random.randint(1,26))
            }

        count += 1 

        data.append(user)


    return data


def create_user_address(cities,districts,mobile_numbers,fullnames ):
    data = []
    for number in mobile_numbers:
        letters = "ABC"
        city = random.choice(cities)
        district = "N/A"
        building_address = f"{city}, bilbo baggins's {random.randint(1,50)}{random.choice(letters)}"
        if city == "Tbilisi":
            district = random.choice(districts)
            building_address = f"Tbilisi, {district}, middle earth's {random.randint(1,50)}{random.choice(letters)}"

        adress = {
            "full_name": random.choice(fullnames[9:]) ,
            "number":  number,
            "country": 2,
            "city":city,
            "State_Province_Region":district,
            "building_address":building_address,
            "Zip_code": random.randint(100,500)
        }

        data.append(adress)

    return data


def create_user_cards(fullnames):
    data = []

    initial_numbers = [2,3,4,5]

    for i in range(70):
        card_number = f"{random.choice(initial_numbers)}{random.randint(1e14,8e14)}"
        card_exp_date = datetime.date(random.randint(2019,2026), random.randint(1,12), random.randint(1,26))
        conf_number = random.randint(101,999)
        holder_name = random.choice(fullnames)

        card = {
            "user_full_name": holder_name,
            "card_number":card_number,
            "card_exp_date": card_exp_date,
            "conf_number":conf_number,
            "holder_name": holder_name.upper(),
        }

        data.append(card)

    return data




users_registration_data = create_users_registration_data(fullnames,mails)    # სულ არის 50 სხვადასხვა იუზერი

users_adress_data = create_user_address(cities,districts, mobile_numbers, fullnames)   # ერთ იუზერს შეუძლია რამდენიმე მისამართი ქონდეს და იქ გაგზავნოს ნივთი, ამიტომ სულ 70 მისამართი დავაგენერირე

user_cards_data = create_user_cards(fullnames)  # ერთ იუზერს შეუძლია რამდენიმე ბარათი ქონდეს, ამიტომ სულ 100 ბარათი დავაგენერირე


for i in user_cards_data:
    print(i)