import requests
from lxml import html
import Web_Scraping

url = "https://www.wvu.edu"

response = requests.get(url)

if response.status_code == 200:

    tree = html.fromstring(response.content)


    texts = extract_text(tree, 5)

    for text in texts:
        print(text)


else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
