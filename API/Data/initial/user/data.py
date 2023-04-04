import datetime, random


Names = ["Anri", "Ruso", "Christine", "Zura", "Niniko"]
Lastname = ["Tvalabeishvili", "Kvesitazde", "Dzneladze", "Dzneladze", "Kvesitazde"]
Emails = [f"{name}.{lastname}@gmail.com" for name, lastname in zip(Names, Lastname)]
Full_names = [f"{name} {lastname}" for name, lastname in zip(Names, Lastname)]

Roles = ["Administrator", "Category Manaager", "Moderator", "User", "User"]
Roles = [1, 2, 3, 4, 4]



Number_prefix = ["555","557","595", "599", "597", "571"]
Mobile_numbers = [f"{random.choice(Number_prefix )}{random.randint(1e5,9e5)}" for i in range(5)]


Cities = ["Tbilisi", "Tbilisi", "Batumi", "Kutaisi", "Rustavi"]
Districts = ["Gldani","Didube","Vake", "Isani", "Krwanisi", "Mtathminda", "Nadzaladevi","Saburtalo", "Samgori"]



def user_populate_data(Full_names,Emails,Roles):
    data = []
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


def address_populate_data(Full_names,Mobile_numbers,Cities,Districts):
    data = []
    for i in range(2):
        for full_name, mobile_number,  in zip(Full_names[-2:],Mobile_numbers):
            
            city = random.choice(Cities)

            if city == "Tbilisi":
                district = random.choice(Districts)
                address = {
                    "full_name": full_name ,
                    "number":  mobile_number,
                    "country": 2,
                    "city":city,
                    "State_Province_Region":district,
                    "building_address":f"{city}, {district}, middle earth {random.randint(10,25)}",
                    "Zip_code": random.randint(100,500)
                }
            else:
                address = {
                    "full_name": full_name ,
                    "number":  mobile_number,
                    "country": 2,
                    "city":city,
                    "State_Province_Region":"N/A",
                    "building_address":f"{city}, bilbo baggins's {random.randint(10,25)}",
                    "Zip_code": random.randint(100,500)
                }

            data.append(address)
    return data


def card_populate_data(Full_names):

    data = []
    Full_names = Full_names[-2:]


    initial_numbers = [2,3,4,5]

    for i in range(5):
        card_number = f"{random.choice(initial_numbers)}{random.randint(1e14,8e14)}"
        card_exp_date = datetime.date(random.randint(2019,2026), random.randint(1,12), random.randint(1,26))
        conf_number = random.randint(101,999)

        user_name = random.choice(Full_names)
        
        card = {
            "user_full_name": user_name,
            "card_number":card_number,
            "card_exp_date": card_exp_date,
            "conf_number":conf_number,
            "holder_name": user_name.upper(),
        }

        data.append(card)
    return data




user_data = user_populate_data(Full_names,Emails,Roles)
address_data = address_populate_data(Full_names,Mobile_numbers,Cities,Districts)
card_data = card_populate_data(Full_names)


