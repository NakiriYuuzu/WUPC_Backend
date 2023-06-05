import requests
from bs4 import BeautifulSoup
import pymysql

# 連接到 MySQL 資料庫
db = pymysql.connect(host="192.168.31.74", user="yuuzu", password="qwer", database="pcbuilder")
cursor = db.cursor()

# 請求網站並解析 HTML
url = "https://www.coolpc.com.tw"
url_pattern = "/eachview.php?IGrp="

count = 0

for i in range(1, 18):
    response = requests.get(url + url_pattern + str(i))
    soup = BeautifulSoup(response.text, "html.parser")

    product_list = []

    for span in soup.find_all('span', {'onclick': 'Show(this)'}):
        img = span.find('img')['src']
        product_name = span.find('div', {'class': 't'}).text
        price = span.find('div', {'class': 'x'}).text.split('：')[1].split(' ')[0]

        product_list.append({
            'image': img,
            'product_name': product_name,
            'price': price[2:],
        })

    for product in product_list:
        count += 1
        print("Image:", product['image'])
        print("Product Name:", product['product_name'])
        print("Price:", product['price'])
        print(f'{count}---', i)

        sql = "INSERT INTO `wupc_part` (`part_name`, `part_description`, `part_price`, `part_image`, `category_id`) VALUES (%s, NULL, %s, %s, %s);"
        cursor.execute(sql, (product['product_name'], product['price'], product['image'], i))
        db.commit()


# 關閉資料庫連接
cursor.close()
db.close()
