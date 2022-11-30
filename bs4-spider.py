import requests
from bs4 import BeautifulSoup

URL = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C26&q=netpyne&btnG="
resp = requests.get(URL)
soup = BeautifulSoup(resp.text, features="lxml")

gs_fls = soup.find_all('div', {'class': 'gs_fl'})#every other one
