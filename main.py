import requests
from bs4 import BeautifulSoup
html=requests.get("https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html").text
soup=BeautifulSoup(html,"lxml")
books=soup.find_all('article', class_="product_pod")
books_data=[]
for b,book in enumerate(books):
    price_and_stock=book.find('div', class_='product_price')
    price=price_and_stock.find('p', class_='price_color').text
    stock=price_and_stock.find('p', class_='instock availability').get_text(strip=True)
    link=book.h3.a['href']
    title=book.h3.a['title']
    price_value=float(price[2:])
    if price_value<=45.00:
        books_info={"book_no"  :len(books_data)+1,
                    "title"    :title,
                    "stock"    :stock,
                    "price": f"£{price_value}",
                    "more_info":link}
        books_data.append(books_info)
    
for book in books_data:
    for key,value in book.items():
        print(f"{key}: {value}")
    print()
        
