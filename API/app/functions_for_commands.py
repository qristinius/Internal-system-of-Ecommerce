import datetime, click, random, json, os


# populating roles table
def create_roles_table(role_class):
    click.echo("Populating roles table \n")

    role = role_class(name="Admin", can_create_role=True, can_send_message=True)
    role.create()
    role = role_class(name="Category Manager", can_create_product=True, can_create_sales=True, can_see_stats=True,
                      can_send_message=True)
    role.create()
    role = role_class(name="Moderator", can_create_product=True, can_create_sales=True, can_send_message=True)
    role.create()
    role = role_class(name="Delivery", can_deliver_items=True, can_send_message=True)
    role.create()
    role = role_class(name="User", can_modify_profile=True, can_buy_product=True)
    role.create()
    role.save()


# populating country table
def create_country_table(country_class):
    click.echo("populating country table \n")

    file = open('Data/Countries.txt', 'r')
    countries = file.read().split("\n")
    for country in countries:
        country_ = country_class(name=country)
        country_.create()
        country_.save()


# populating User, Card, Address table
def create_users_table(user_class, user_role_class, card_class, address_class, quantity=-1):
    click.echo("populating: user, address and card tables \n")
    file = open('Data/Users.txt', 'r')
    data = file.read().split(";\n")

    for all_user_info in data[0:quantity]:
        user_data = json.loads(all_user_info)

        user_info = user_data["user"]
        user_ = user_class(full_name=user_info.get("full_name"),
                           email=user_info.get("email"),
                           password=user_info.get("password"),
                           registration_date=user_info.get("registration_date"))
        user_.create()
        user_.save()

        user_role_ = user_role_class(
            user_id=user_.id, role_id=user_info.get("role_id"))
        user_role_.create()
        user_role_.save()

        try:
            for user_card in user_data["user_card"]:

                if datetime.datetime.fromisoformat(user_card.get("card_exp_date")) > datetime.datetime.today():
                    card_ = card_class(user_id=user_.id,
                                       card_number=user_card.get("card_number"),
                                       expiration_date=user_card.get(
                                           "card_exp_date"),
                                       holder_name=user_card.get("holder_name"),
                                       brand=user_card.get("brand"))
                else:
                    card_ = card_class(user_id=user_.id,
                                       card_number=user_card.get("card_number"),
                                       expiration_date=user_card.get(
                                           "card_exp_date"),
                                       holder_name=user_card.get("holder_name"),
                                       usable=False,
                                       brand=user_card.get("brand"))

                card_.create()

                card_.save()

            for user_address in user_data["user_address"]:
                address_ = address_class(user_id=user_.id,
                                         full_name=user_address.get("full_name"),
                                         mobile_number=user_address.get(
                                             "mobile_number"),
                                         country_id=user_address.get("country_id"),
                                         city=user_address.get("city"),
                                         state_province_region=user_address.get(
                                             "State_Province_Region"),
                                         zip_code=user_address.get("Zip_code"),
                                         building_address=user_address.get("building_address"))
                address_.create()

                address_.save()

        except:

            continue


# populating category table
def create_category_table(category_table):
    click.echo("populating category table \n")

    file = open('Data/Category.txt', 'r')
    content = json.loads(file.read())
    main_category = list(content.keys())

    for main_category_name in main_category:
        main_category_data = (content[main_category_name])

        main = category_table(name=main_category_name)
        main.create()
        main.save()

        if dict == type(main_category_data):
            secondary_categories = list(main_category_data.keys())

            for second_category_name in secondary_categories:
                third_categories = main_category_data[second_category_name]

                secondary = category_table(name=second_category_name, parent_id=main.id)
                secondary.create()
                secondary.save()

                for third_category_name in third_categories:
                    # main_category_name
                    # second_category_name
                    # third_category_name

                    third = category_table(name=third_category_name, parent_id=secondary.id)
                    third.create()
                    third.save()
        else:

            for second_category_name in main_category_data:
                secondary = category_table(name=second_category_name, parent_id=main.id)
                secondary.create()
                secondary.save()


# populating Attribute table
def create_attribute_table(attribute_table, category_table):
    click.echo("populating Attribute table \n")

    file = open('Data/Attributes.txt', 'r')
    content = json.loads(file.read())
    category_names = list(content.keys())
    for category_name in category_names:
        category = category_table.query.filter_by(name=category_name).first()
        attributes = content[category_name]
        for attribute in attributes:
            if attribute != "price":
                main = attribute_table(name=attribute, category_id=category.id)
                main.create()
                main.save()

        main = attribute_table(name="online_img", category_id=category.id)
        main.create()
        main = attribute_table(name="img", category_id=category.id)

        main.create()
        main.save()


# populating brand table
def create_brand_table(brand_table):
    click.echo("populating Brand table \n")
    file = open('Data/Brands.txt', 'r')
    content = file.read().split("\n")

    for brand in list(content):
        main = brand_table(brand_name=brand)
        main.create()
        main.save()


# populating product, price, ProductAttribute tables
def create_product_table(product_table, category_table, attribute_table, brand_table, price_table,
                         product_attribute_table, quantity=-1):
    path = f"{os.getcwd()}\\Data\\Products"
    dir_list = os.listdir(path)

    files = {}
    categories = []

    def price_generator(price, price_table):
        try:
            price = int(price)
            margin = random.randint(30, 50)
            sale_margin = random.randint(10, 30)
            original_price = price * (100 - margin) / 100
            sale_price = price * (100 - sale_margin) / 100

            if random.randint(1, 5) == 2:
                start_date = datetime.datetime.today().isoformat()
                end_date = (datetime.datetime.today() + datetime.timedelta(days=40)).isoformat()

                main = price_table(original_price=original_price, selling_price=price, sale_price=sale_price, sale=True,
                                   sale_start_date=start_date, sale_end_date=end_date, margin=sale_margin)
                main.create()
                main.save()
            else:
                main = price_table(original_price=original_price, selling_price=price, sale_price=sale_price,
                                   margin=margin)
                main.create()
                main.save()

            return main
        except:
            return False

    def img_generator(attributes):
        online_img = []
        img = []

        response = {
            "online_img": online_img,
            "img": img
        }

        for attribute in product_attributes:
            if "online_img" in attribute:
                online_img.append(product[attribute])
            elif "img" in attribute:
                img.append(product[attribute])

        return response

    for category in dir_list:
        new_path = f"{path}\\{category}"
        dir_list = os.listdir(new_path)

        categories.append(category)
        files[category] = dir_list

    for category in categories:
        file_names = files[category]
        for file_name in file_names:
            click.echo(f"        start {file_name} \n")
            file = open(f"{path}\\{category}\\{file_name}", "r")
            data = file.read()
            components = data.split(";\n")

            db_category = category_table.query.filter_by(name=file_name[0:-4]).first()

            for component in components[0:quantity]:
                product = eval(component)
                product_attributes = list(product.keys())
                if "Brand" not in product_attributes:
                    continue

                db_brand = brand_table.query.filter_by(brand_name=product["Brand"]).first()

                if not db_brand or not db_category:
                    continue

                price = price_generator(product["price"], price_table)

                if not price:
                    continue

                db_product = product_table(price_id=price.id, brand_id=db_brand.id, category_id=db_category.id,
                                           name=product["name"], quantity=random.randint(10, 30)
                                           )  # score=random.randint(70, 100) / 10
                db_product.create()
                db_product.save()

                product_attributes.remove('price')
                product_attributes.remove('Brand')
                product_attributes.remove('name')

                for attribute in product_attributes:
                    if "img" not in attribute:
                        db_attribute = attribute_table.query.filter_by(category_id=db_category.id,
                                                                       name=attribute).first()

                        db_product_attribute = product_attribute_table(product_id=db_product.id,
                                                                       attribute_id=db_attribute.id,
                                                                       value=product[attribute])
                        db_product_attribute.create()
                        db_product_attribute.save()

                data = img_generator(product_attributes)

                for attribute in ["online_img", "img"]:
                    db_attribute = attribute_table.query.filter_by(category_id=db_category.id,
                                                                   name=attribute).first()

                    db_product_attribute = product_attribute_table(product_id=db_product.id,
                                                                   attribute_id=db_attribute.id,
                                                                   value=str(data[attribute]))
                    db_product_attribute.create()
                    db_product_attribute.save()


# populating purchase table
def create_purchase_table(purchase_table, user_table, product_table, quantity):
    users = user_table.query.all()
    products = product_table.query.all()
    counter = 0
    while counter < quantity:
        user = random.choice(users)
        user_role = user.role[0]
        if user_role.name != "User":
            continue
        counter += 1
        product = random.choice(products)
        address = random.choice(user.address)
        price = product.price.selling_price

        purchase = purchase_table(user_id=user.id,
                                  address_id=address.id,
                                  product_id=product.id,
                                  product_quantity=1,
                                  user_price=price,
                                  purchase_date=datetime.datetime.today(),
                                  )
        purchase.create()
        purchase.save()
