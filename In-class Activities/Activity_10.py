# Import necessary libraries
import requests
from lxml import html
import psycopg2


url = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=75&start=0"


response = requests.get(url)
page_content = response.text

tree = html.fromstring(page_content)


bugs = tree.xpath("//div[contains(@class, 'bug')]")


conn = psycopg2.connect(
    database="your_database_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cursor = conn.cursor()


for bug in bugs:
    bug_number = int(bug.xpath(".//div[contains(@class, 'id')]/text()")[0])
    status = bug.xpath(".//div[contains(@class, 'status')]/text()")[0]
    heat = int(bug.xpath(".//div[contains(@class, 'heat')]/text()")[0])
    title = bug.xpath(".//a[contains(@class, 'bugtitle')]/text()")[0]

    cursor.execute("INSERT INTO Activity10_John_Pino (bug_number, status, heat, title) VALUES (%s, %s, %s, %s)", (bug_number, status, heat, title))


conn.commit()
conn.close()

print("Bug data extracted and added to the PostgreSQL database.")
