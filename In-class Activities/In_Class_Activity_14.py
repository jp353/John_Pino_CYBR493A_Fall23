import requests
from lxml import html
import re

def get_web_tree(link):
    page = requests.get(link)
    page_tree = html.fromstring(page.content)
    return page_tree

link = "https://cwe.mitre.org/data/definitions/888.html"
main_tree = get_web_tree(link)

# Print the text content of each matching element
primaries = main_tree.xpath('//*[@class="group"]//text()')
for primary in primaries:
    # Use regular expression to find text within parentheses
    matches = re.findall(r'\((.*?)\)', primary)

    # Print the matches
    for match in matches:
        print(match.strip())
