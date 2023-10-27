import requests
from lxml import html
import Web_Scraping

url = "https://www.wvu.edu"  # Make sure to include the protocol (https://) in the URL

response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page using lxml
    tree = html.fromstring(response.content)

    # Use your extract_text function from Web_Scraping.py to extract 5 different texts
    texts = extract_text(tree, 5)

    # Print all the extracted text
    for text in texts:
        print(text)

    # Commit and push your changes to your version control system (e.g., Git)
    # This step depends on the version control system you are using
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
