import Web_Scraping as wb
#import functions

"""
This will be our main screen
"""


def main():
    # Your code goes here.
    main_link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=0&start=0"
    links = generate_links(main_link)
    user_input = int(input('Which page would you like to view?'))
    display_bugs_info(links[user_input])


def generate_links(start_link):
    """
        This method generates ALL the links to all pages and stores them in a list
        :param start_link: The start link of the bug tracking system.
        :return: The list of all pages to all bugs. Each element in the list will refer to one page
    """
    # Get total number of pages
    #1. Get # of bugs / 75 (xpath)
    main_tree = wb.get_web_tree(start_link)
    bugs = main_tree.xpath('//*[@id="bugs-table-listing"]//text()')
    print(bugs)
    list_of_links = []
    index_of_75 = main_tree.index('75')
    print(index_of_75)

    # everytime you get a link to a new page, use list_of_links.append(new_page)

    return list_of_links
    list_of_links.append(newLink)
    # this will put all links to all of the pages inside user input
    #


def display_bugs_info(bugs_page):
    """
        This method displays the bugs info. for a specific page
        Display: Bug Number, Title, Importance, and Heat - in this order for each bug.
        :param bugs_page: The  link to the page
    """


if __name__ == "__main__":
    main()
