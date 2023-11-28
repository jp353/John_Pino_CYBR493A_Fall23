import requests
from lxml import html

def get_web_tree(link):
    page = requests.get(link)
    page_tree = html.fromstring(page.content)
    return page_tree

link = "https://cwe.mitre.org/data/definitions/888.html"
main_tree = get_web_tree(link)

# Print the text content of each matching element
primaries = main_tree.xpath('//*[@class="group"]')
for primary in primaries:
    print(primary.text_content().strip())
