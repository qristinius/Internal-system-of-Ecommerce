import random, time
from datetime import date
import datetime

names = [
"Noah","Theo","Oliver","George","Leo","Freddie",
"Arthur","Archie","Alfie","Charlie","Oscar","Henry",
"Harry","Jack","Teddy","Finley","Arlo","Luca","Jacob","Tommy",
"Lucas","Theodore","Max","Isaac","Albie","James","Mason","Rory",
"Thomas","Rueben","Roman","Logan","Harrison","William" ,"Elijah",
"Ethan","Joshua","Hudson","Jude","Louie","Jaxon","Reggie","Oakley",
"Hunter","Alexander","Toby","Adam","Sebastian","Daniel", "Oscar"
]



surnames = [
"Smith","Johnson","Williams","Brown","Jones","Garcia","Miller",
"Davis","Rodriguez","Martinez","Hernandez","Lopez","Gonzales",
"Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin",
"Lee","Perez","Thompson","White","Harris","Sanchez","Clark",
"Ramirez","Lewis","Robinson","Walker","Young","Allen","King","Wright",
"Scott","Torres","Nguyen","Hill","Flores","Green","Adams","Nelson",
"Baker","Hall","Rivera","Campbell","Mitchell","Carter","Roberts"
]

number_prefix = ["555","557","595", "599", "597", "571"]

cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi","Tbilisi"]

districts = ["Gldani","Didube","Vake", "Isani", "Krwanisi", "Mtathminda", "Nadzaladevi","Saburtalo", "Samgori"]

fullnames = [f"{name} {surname}" for name,surname in zip(names,surnames)]

mails = [f"{name}.{surname}@gmail.com" for name,surname in zip(names,surnames)]

mobile_numbers = [f"{random.choice(number_prefix )}{random.randint(1e5,9e5)}" for i in range(70)]


def create_users_registration_data(fullnames,mails ):


    data = []

    count = 0


    for fullname, mail in zip(fullnames,mails):

        if count< 5:
            user = {
                "full_name" : fullname,
                "email": mail,
                "role": 1,
                "password": mail,
                "registration_date": datetime.date(2022, 12, 25)
            }

        elif count< 10:

            user = {
                "full_name" : fullname,
                "email": mail,
                "role": 2,
                "password": mail,
                "registration_date": datetime.date(2022, 12, 25)
            }
        elif count<15:
                user = {
                "full_name" : fullname,
                "email": mail,
                "role": 3,
                "password": mail,
                "registration_date": datetime.date(2022, 12, 25)
            }
        else:
            user = {
                "full_name" : fullname,
                "email": mail,
                "role": 4,
                "password": mail,
                "registration_date": datetime.date(2022, 12, 25)
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
        specific_adress = f"netasaqmemoqndes kucha {random.randint(1,50)}{random.choice(letters)}"
        if city == "Tbilisi":
            district = random.choice(districts)
            specific_adress = f"{district} imasknishvilis kucha {random.randint(1,50)}{random.choice(letters)}"

        print(type(number))
        adress = {
            "full_name": random.choice(fullnames) ,
            "number":  number,
            "country": 2,
            "city":city,
            "State_Province_Region":district,
            "building_address":specific_adress,
            "Zip_code": random.randint(100,500)
        }


        data.append(adress)

    return data


def create_user_cards(fullnames):
    data = []

    initial_numbers = [2,3,4,5]

    for i in range(100):
        card_number = f"{random.choice(initial_numbers)}{random.randint(1e14,8e14)}"
        card_exp_date = datetime.date(random.randint(2019,2023), random.randint(1,12), random.randint(1,26))
        conf_number = random.randint(101,999)
        holder_name = random.choice(fullnames)

        card = {
            "card_number":card_number,
            "card_exp_date": card_exp_date,
            "conf_number":conf_number,
            "holder_name": holder_name,
        }

        data.append(card)

    return data




users_registration_data = create_users_registration_data(fullnames,mails)    # სულ არის 50 სხვადასხვა იუზერი

users_adress_data = create_user_address(cities,districts, mobile_numbers, fullnames)   # ერთ იუზერს შეუძლია რამდენიმე მისამართი ქონდეს და იქ გაგზავნოს ნივთი, ამიტომ სულ 70 მისამართი დავაგენერირე

User_cards_data = create_user_cards(fullnames)  # ერთ იუზერს შეუძლია რამდენიმე ბარათი ქონდეს, ამიტომ სულ 100 ბარათი დავაგენერირე

