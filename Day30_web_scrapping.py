import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

# Step 1: Web Scraping
url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding = 'utf-8'   # Fix encoding issue
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

names = []
prices = []

for book in books:
    name = book.h3.a["title"]
    
    # Get raw price text 
    price_text = book.find("p", class_="price_color").text
    # Extract numeric value using regex (fix for Â£ issue)
    price = float(re.findall(r'\d+\.\d+', price_text)[0])
    
    names.append(name)
    prices.append(price)

# Step 2: Store Data in Table
df = pd.DataFrame({
    "Book Name": names,
    "Price": prices
})

print("\n📊 Table Data:\n")
print(df.head())

# Save to CSV
df.to_csv("books_data.csv", index=False)
print("\n✅ CSV file 'books_data.csv' created successfully!")

# Step 3: Data Visualization
plt.figure()
plt.bar(names[:10], prices[:10])   # Top 10 books
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Book Prices (Top 10)")
plt.subplots_adjust(bottom=0.3)#plt.tight_layout()
plt.show()




# IMPORT REQUIRED LIBRARIES

import pandas as pd
import requests
from bs4 import BeautifulSoup


# WEBSITE URL

URL = "https://timely-sunshine-e821b3.netlify.app/"


# LOAD WEB PAGE USING REQUESTS

page = requests.get(URL)


# CHECK STATUS CODE

print("Status Code :", page.status_code)


# EXTRACT HTML CONTENT

html_code = page.text

# CREATE BEAUTIFULSOUP OBJECT

soup = BeautifulSoup(html_code, "html.parser")


# DISPLAY PAGE TITLE

if soup.title:
    print("Page Title :", soup.title.text.strip())
else:
    print("No Title Found")


# EXTRACT FIRST PRODUCT NAME

first_name = soup.find("div", class_="name")

if first_name:
    print("First Product Name :", first_name.text.strip())
else:
    print("Product Name Not Found")


# EXTRACT FIRST PRODUCT PRICE

first_price = soup.find("div", class_="price")

if first_price:
    print("First Product Price :", first_price.text.strip())
else:
    print("Product Price Not Found")


# EXTRACT FIRST PRODUCT IMAGE

first_image = soup.find("div", class_="image")

if first_image:
    img_tag = first_image.find("img")

    if img_tag:
        print("First Product Image :", img_tag.get("src"))
    else:
        print("Image Tag Not Found")
else:
    print("Image Div Not Found")


# EXTRACT ALL PRODUCTS

items = soup.find_all("div", class_="a")


# EMPTY LISTS TO STORE DATA

product_names = []
product_prices = []
product_images = []


# LOOP THROUGH EACH PRODUCT

for item in items:


    name_tag = item.find("div", class_="name")

    if name_tag:
        name = name_tag.text.strip()
    else:
        name = "No Name"


    price_tag = item.find("div", class_="price")

    if price_tag:
        price = price_tag.text.strip()
    else:
        price = "No Price"


    image_div = item.find("div", class_="image")

    if image_div:
        image_tag = image_div.find("img")

        if image_tag:
            image_src = image_tag.get("src")
        else:
            image_src = "No Image"
    else:
        image_src = "No Image"


    product_names.append(name)
    product_prices.append(price)
    product_images.append(image_src)


# DISPLAY EXTRACTED DATA

print("\nProduct Names :", product_names)
print("\nProduct Prices :", product_prices)
print("\nProduct Images :", product_images)


# CREATE DATAFRAME

df = pd.DataFrame({
    "Product_Name": product_names,
    "MRP": product_prices,
    "Image_SRC": product_images
})


# DISPLAY DATAFRAME

print("\nDataFrame:\n")
print(df)


# DATAFRAME DETAILS

print("\nShape of DataFrame :", df.shape)

print("\nFirst 5 Rows:\n")
print(df.head())


# SAVE DATAFRAME TO CSV FILE

df.to_csv("productdetails.csv", index=False)

print("\nCSV File Saved Successfully!")




