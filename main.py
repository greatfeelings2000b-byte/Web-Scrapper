import requests
from bs4 import BeautifulSoup
html=requests.get("https://www.mykhel.com/cricket/most-runs-in-odi-rs1/").text
print(html)
