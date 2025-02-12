import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)
rhtml = r.text
soup = BeautifulSoup(rhtml,"html.parser")
for val in soup.find_all("h2"):
    print(val.text)
