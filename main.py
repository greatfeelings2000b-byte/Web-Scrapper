import requests
from bs4 import BeautifulSoup
html=requests.get("https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html").text
soup=BeautifulSoup(html,"lxml")
book=soup.find('article', class_="product_pod")
# div=section.find_all('div')
# target_div=div[1]
# elements=target_div.find('ol')
# books=elements.find('li')
price_and_stock=book.find('div', class_='product_price')
price=price_and_stock.find('p', class_='price_color').text
stock=price_and_stock.find('p', class_='instock availability').get_text(strip=True)
link=book.h3.a['href']
print(f'this book is {stock} and its price is {price} for further information click on this {link}')