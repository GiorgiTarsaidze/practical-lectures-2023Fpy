from bs4 import BeautifulSoup
import requests
# pip install "მოდულის სახელი"

url = "https://realpython.com/python-web-scraping-practical-introduction/"

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


parsed_info = soup.find_all("a")

for i in parsed_info:
    print(i.text)
