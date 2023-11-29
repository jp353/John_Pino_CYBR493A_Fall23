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
pattern = re.compile(r'(\s*.+\s*)(\s*-\s* +\(\d{3}\))')


for primary in primaries:
    # Find pattern
    match = pattern.search(primary)

    # Check if the pattern is found
    if match:
        # Print the matched components directly
        print(f"CWE Title: {match.group(1).strip()}\nThree-digit number: {match.group(2).strip()}")
