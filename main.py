import csv
import requests
from bs4 import BeautifulSoup

#___basic syntax to set up the target website by using requests and BeautifulSoup___

def fetch_html():
    html=requests.get("https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html").text
    return html

# ___Navigate and Store data inside the list of dictionary___

def fetch_data(web):
    soup=BeautifulSoup(web,"lxml")
    books=soup.find_all('article', class_="product_pod")
    books_data=[]
    for b,book in enumerate(books):
        price_and_stock=book.find('div', class_='product_price')
        price=price_and_stock.find('p', class_='price_color').text
        stock=price_and_stock.find('p', class_='instock availability').get_text(strip=True)
        link=book.h3.a['href'].replace('../../../', '')
        title=book.h3.a['title']
        price_value=float(price[2:])
        if price_value<=45.00:
            books_info={"book_no"  :len(books_data)+1,
                        "title"    :title,
                        "stock"    :stock,
                        "price"    :price_value,
                        "more_info":link}
            books_data.append(books_info)
    return books_data

# ___Printed the results inside the terminal___

def print_data(books):
    for book in books:
        for key,value in book.items():
            print(f"{key}: {value}")
        print()

# ___Made a csv file and store the scraped data in it___

def store_data(books):
    with open("books.csv", "w", newline="", encoding="utf-8" ) as file:
        writer=csv.writer(file)
        writer.writerow([
                "Book_no",
                "Title"  ,
                "Stock"  ,
                "Price"  ,
                "More"   
        ])
        for book in books:
            writer.writerow([
            book["book_no"]  ,
            book["title"]    ,
            book["stock"]    ,
            book["price"]    ,
            book["more_info"]
            ]
            )
            
def main():
    web=fetch_html()
    books=fetch_data(web)
    print_data(books)
    store_data(books)
if __name__=="__main__":
    main()