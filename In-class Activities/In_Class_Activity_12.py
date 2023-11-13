from lxml import lxml
import requests
import Web_Scraping as wb


page = requests.get("https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&orderby=-importance&start=0")

tree = html.fromstring(page.content)


data = tree.xpath("/html/body/div[2]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div[3]/div/div[1]/div[2]/div[1]/a")

print(data)

