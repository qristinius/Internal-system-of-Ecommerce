import datetime, random

Names = ["Zura", "Niniko"]
Lastname = ["Dzneladze", "Kvesitazde"]


Emails = [f"{name}.{lastname}@gmail.com" for name, lastname in zip(Names, Lastname)]
Full_names = [f"{name} {lastname}" for name, lastname in zip(Names, Lastname)]

Roles = {"Administrator":1, "Category Manaager":2, "Moderator":3, "User":4, "User":4}

Number_prefix = ["555","557","595", "599", "597", "571"]
Cities = ["Tbilisi", "Tbilisi", "Batumi", "Kutaisi", "Rustavi"]
Districts = ["Gldani","Didube","Vake", "Isani", "Krwanisi", "Mtathminda", "Nadzaladevi","Saburtalo", "Samgori"]









def create_workers_data():
    data = []

    Names = ["Anri", "Ruso", "Christine"]
    Lastname = ["Tvalabeishvili", "Kvesitazde", "Dzneladze"]
    Emails = [f"{name}.{lastname}@gmail.com" for name, lastname in zip(Names, Lastname)]
    Full_names = [f"{name} {lastname}" for name, lastname in zip(Names, Lastname)]
    Roles = [1, 2, 3]

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
                    "full_name": full_name,
                    "email": email,
                    "role_id": 4,
                    "password": email,
                    "registration_date": datetime.date(2022, 12, 25)
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

            for i in range(random.randint(1,3)):

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

complete_admin_populate_data  =  create_workers_data()
complete_user_populate_data =  user_populate_data(Full_names, Emails, Number_prefix, Cities, Districts)



