import Web_Scraping as wb
import requests
from lxml import html
import re

def get_web_tree(link):
    page = requests.get(link)
    page_tree = html.fromstring(page.content)
    return page_tree

def generate_pages(start_link, page_number):
    bugs_per_page = 75
    current_start = int(start_link.split('&start=')[-1])
    next_start = current_start + bugs_per_page
    new_link = f"{start_link.split('&start=')[0]}&start={next_start}"
    return new_link

if __name__ == "__main__":
    initial_link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&start=0"

    initial_page_tree = get_web_tree(initial_link)

    total_bugs_raw = initial_page_tree.xpath('//*[@id="bugs-table-listing"]//text()')
    total_bugs = 0


    '''Not sure if I have to cite sources or not, but I had to consult ChatGPT to help
    me figure out how to extract the total pages from the xpath and to help with 
    some of the code in the generate_pages method'''

    # Define a regex pattern for a 6-digit number
    six_digit_pattern = re.compile(r'\b(\d{6})\b')


    for item in total_bugs_raw:
        match = six_digit_pattern.search(item)
        if match:
            total_bugs = int(match.group(1))
            break

    print("Total Bugs:", total_bugs)

    bugs_per_page = 75
    total_pages = (total_bugs // bugs_per_page)

    # Generate and print links to access each bug page
    for page_number in range(1, total_pages + 1):
        page_link = generate_pages(initial_link, page_number)
        print(f"Link to Page {page_number}: {page_link}")

        # Get the tree for the current page
        current_page_tree = get_web_tree(page_link)
