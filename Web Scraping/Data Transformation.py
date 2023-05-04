import os, time
import json

path = f"{os.getcwd()}\\Alta Data\\Products"
dir_list = os.listdir(path)

files = {}
categories = []


def take_new_attributes(data):
    data = data.read()
    components = data.split(";\n")
    red_line = (len(components)-1) * 0.4

    all_keys = []

    for component in components[0:-1]:
        component_keys = list(eval(component).keys())
        all_keys += component_keys

    new_keys = [key for key in set(all_keys) if (all_keys.count(key) > red_line and "img" not in key)]

    return new_keys


def create_filtered_data(data, attributes, category, filename):
    data = data.read()
    components = data.split(";\n")

    exist = os.path.exists(f'Data/Products/{category}')
    if not exist:
        os.makedirs(f'Data/Products/{category}')

    new_file = open(f'Data/Products/{category}/{filename}', 'w')

    for component in components[0:-1]:

        component_keys = list(eval(component).keys())
        dict_component = eval(component)

        new_product_data = {}

        for key in component_keys:
            if key in attributes:
                new_product_data[key] = dict_component[key]
            elif "online_img" in key:
                new_product_data[key] = dict_component[key]
            elif "img" in key:
                new_product_data[key] = dict_component[key][5:]

        new_file.write(json.dumps(new_product_data) + ";" + "\n")

    new_file.close()


for category in dir_list:
    new_path = f"{path}\\{category}"
    dir_list = os.listdir(new_path)
    if category != "Photos":
        categories.append(category)
        files[category] = dir_list


attributes_file = open(f'Data/attributes.txt', 'w')
attributes_file_data = {}
category_file = open(f'Data/category.txt', 'w')
category_file_data = {}

for category in categories:
    file_names = files[category]
    category_file_data[category] = [i[0:-4] for i in file_names]

    for file_name in file_names:
        file = open(f"{path}\\{category}\\{file_name}", "r")
        new_attributes = take_new_attributes(file)
        attributes_file_data[file_name[0:-4]] = new_attributes

        file = open(f"{path}\\{category}\\{file_name}", "r")
        create_filtered_data(file, new_attributes, category, file_name)


attributes_file.write(json.dumps(attributes_file_data))
attributes_file.close()

category_file.write(json.dumps(category_file_data))
category_file.close()



