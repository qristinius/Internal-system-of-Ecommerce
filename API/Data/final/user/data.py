import random, time
from datetime import date
import datetime



names = ["Theo","George","Leo","Arthur","Archie","Alfie","Oscar","Henry", "Harry","Jack","Teddy","Finley","Arlo","Luca","Jacob","Tommy","Lucas","Theodore","Max","Isaac","Albie","James","Mason","Rory","Thomas","Rueben","Roman","Logan","Harrison","William"]
surnames = ["Johnson","Brown","Jones","Miller","Davis","Rodriguez","Hernandez","Lopez","Gonzales","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin","Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson","Walker","Young","Allen","King"]

Number_prefix = ["568", "571", "574", "579", "592", "597", "500", "550", "555", "593", "514", "557", "558", "544", "511", "522", "533", "505", "575", "585", "551", "591", "595", "596", "598", "599"]

Cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi","Gori", "Samtredia", "Tbilisi", "Tbilisi" ]

Districts = ["Gldani","Didube","Vake", "Isani", "Krwanisi", "Mtathminda", "Nadzaladevi","Saburtalo", "Samgori"]

Full_names = [f"{name} {surname}" for name,surname in zip(names,surnames)]

Emails = [f"{name}.{surname}@gmail.com" for name,surname in zip(names,surnames)]








def create_workers_data():
    data = []

    Names = ["Anri", "Ruso", "Christine", "Zura", "Nino", "Dato"]
    Lastname = ["Tvalabeishvili", "Kvesitazde", "Dzneladze", "Dzneladze", "Kvesitazde", "Adeishvili"]
    Emails = [f"{name}.{lastname}@gmail.com" for name, lastname in zip(Names, Lastname)]
    Full_names = [f"{name} {lastname}" for name, lastname in zip(Names, Lastname)]
    Roles = [1, 1, 2, 2, 3, 3]

    for full_name, email, role in zip(Full_names,Emails,Roles):
        user = {
                "full_name" : full_name,
                "email": email,
                "role_id": role,
                "password": email,
                "registration_date": datetime.date(2022, 12, 25)
            }   
        data.append(user)

    return data


def user_populate_data(Full_names,Emails, Number_prefix, Cities, Districts):
    data = []
    
    

    for full_name, email in zip(Full_names,Emails):

        
        def create_user():

            user = {
                    "full_name" : full_name,
                    "email": email,
                    "role_id": 4,
                    "password": email,
                    "registration_date": datetime.date(random.randint(2019,2022), random.randint(1,12), random.randint(1,26))
                }  
            
            return user
        

        def create_card():
            cards = []
            for i in range(random.randint(1,3)):

                card_number = f"{random.randint(2,5)}{random.randint(1e14,8e14)}"
                card_exp_date = datetime.date(random.randint(2019,2026), random.randint(1,12), random.randint(1,26))
                cvv = random.randint(101,999)

                card = {
                    "holder_name": full_name.upper(),
                    "card_number":card_number,
                    "cvv":cvv,
                    "card_exp_date": card_exp_date,
                }

                cards.append(card)

            return cards
        

        def create_address():
            addresses = []

            for i in range(random.randint(1,2)):

                mobile_number = f"{random.choice(Number_prefix )}{random.randint(1e5,9e5)}"
                city = random.choice(Cities)



                if city == "Tbilisi":
                    district = random.choice(Districts)
                    address = {
                        "full_name": full_name ,
                        "mobile_number":  mobile_number,
                        "country_id": 2,
                        "city":city,
                        "State_Province_Region":district,
                        "building_address":f"{city}, {district}, middle earth {random.randint(10,25)}",
                        "Zip_code": random.randint(100,500)
                    }
                else:
                    address = {
                        "full_name": full_name ,
                        "mobile_number":  mobile_number,
                        "country_id": 2,
                        "city":city,
                        "State_Province_Region":"N/A",
                        "building_address":f"{city}, bilbo baggins's {random.randint(10,25)}",
                        "Zip_code": random.randint(100,500)
                    }

                addresses.append(address)

            return addresses


        data.append([create_user() , create_card(), create_address()])




    return data



#[{}, [{},{} ....], [{},{} .....]]     this is template of datga 

complete_admin_populate_data = create_workers_data()
complete_user_populate_data =  user_populate_data(Full_names, Emails, Number_prefix, Cities, Districts)




