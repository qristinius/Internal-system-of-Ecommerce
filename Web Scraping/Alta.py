from bs4 import BeautifulSoup
from PIL import Image
import requests, time, json, os, random, string
from Links import *

letters = string.ascii_lowercase + string.ascii_uppercase + string.digits


def product_quantity(link):
    html_text = requests.get(link + "?sl=en").text
    soup = BeautifulSoup(html_text, "lxml")

    data = soup.find('div', class_="count-cp").text.replace(" Products", "")

    return data


def product_links(link, quantity):
    html_text = requests.get(link + f"?items_per_page={quantity}" + "?sl=en").text
    soup = BeautifulSoup(html_text, "lxml")

    big_data = soup.find_all('a', class_="product-title", href=True)

    data = []
    for item in big_data:
        data.append(str(item["href"]))

    return data


def product_information(link, filename):
    html_text = requests.get(link + "?sl=en").text
    soup = BeautifulSoup(html_text, "lxml")

    name = soup.find('div', class_="nj_custom_product_title_product_page").text
    price = soup.find("div", class_="ty-product-block__price-actual").text.replace(" ₾", "").replace("\n", "")
    descriptions = soup.find_all('div', class_="ty-product-feature")
    img_urls = soup.find_all("a", class_="cm-image-previewer", href=True)
    category_name = link.split("/")[-1][:-5]

    data = {
        "name": name,
        "price": price,
        "category_name": filename,
    }

    count = 0
    for i in img_urls:
        count += 1
        img = Image.open(requests.get(i['href'], stream=True).raw)

        img_name = ''.join(random.choice(letters) for i in range(30))

        exist = os.path.exists(f'Alta Data/Photos/{filename}')
        if not exist:
            os.makedirs(f'Alta Data/Photos/{filename}')

        try:

            img.save(f'Alta Data/Photos/{filename}/{img_name}.png')
            data[f"img{count}"] = f'Alta Data/Photos/{filename}/{img_name}.png'
            data[f"online_img{count}"] = i['href']
        except:
            try:
                img.save(f'Alta Data/Photos/{filename}/{img_name}.jpg')
                data[f"img{count}"] = f'Alta Data/Photos/{filename}/{img_name}.jpg'
                data[f"online_img{count}"] = i['href']
            except:
                continue

    for i in descriptions:
        data[i.find("span").text.replace(":", "")] = i.find("div").text

    return data


def miner(links, category):
    for product_link in links:
        item_quantity = product_quantity(product_link)
        item_links = product_links(product_link, item_quantity)

        filename = product_link.split("/")[-1][:-5]
        exist = os.path.exists(f'Alta Data/Products/{category}')
        if not exist:
            os.makedirs(f'Alta Data/Products/{category}')
        file = open(f'Alta Data/Products/{category}/{filename}.txt', 'w')

        print(f"start {filename} mining ...")
        count = 0
        for item_link in item_links:
            count += 1
            time.sleep(5)
            file.write(json.dumps(product_information(item_link, filename)) + ";" + "\n")
            current = str(round((count / int(item_quantity) * 100), 2))
            print(f"progress {current} %")

        file.close()
        print(f"Done {filename} mining ... \n")
        time.sleep(10)
    time.sleep(10)


#miner(links_for_pc_components[1:], links_for_pc_components[0])
# miner(links_for_monitors_projectors[1:], links_for_monitors_projectors[0])
# miner(links_for_tablets_accessories[1:], links_for_tablets_accessories[0])
# miner(links_for_computer_accessories[1:], links_for_computer_accessories[0])
# miner(links_for_printers_scanners_supplies[1:], links_for_printers_scanners_supplies[0])
# miner(links_for_notebooks_accessories[1:], links_for_notebooks_accessories[0])
# miner(links_for_phones_communications[1:], links_for_phones_communications[0])
# miner(links_for_tV_photo_video_audio_game_consoles[1:], links_for_tV_photo_video_audio_game_consoles[0])
# miner(links_for_home_appliances[1:], links_for_home_appliances[0])
# miner(links_for_kitchen_appliances[1:], links_for_kitchen_appliances[0])
# miner(links_for_house[1:], links_for_house[0])

