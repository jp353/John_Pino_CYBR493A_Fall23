import requests
from lxml import html
import re

def get_web_tree(link):
    page = requests.get(link)
    page_tree = html.fromstring(page.content)
    return page_tree

link = "https://cwe.mitre.org/data/definitions/888.html"
main_tree = get_web_tree(link)


primaries = main_tree.xpath('//*[@class="group"]//text()')
primaries_raw = main_tree.xpath('//*[@class="group"]//text()')
pattern = re.compile(r'(.+?),(.+?) - \((\d+)\)')

for primary in primaries:
    # Find patter
    match = pattern.search(primary)

    # Check if the pattern is found
    if match:

        # Get and print matches
        string1 = match.group(1).strip()
        string2 = match.group(2).strip()
        number = match.group(3).strip()

        print(f"String 1: {string1}\nString 2: {string2}\nNumber: {number}\n")
    else:
        print(primaries_raw)
