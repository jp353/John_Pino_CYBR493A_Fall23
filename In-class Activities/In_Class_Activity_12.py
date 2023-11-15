import Web_Scraping as wb
import lxml
import requests



def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    main_tree = wb.get_web_tree("https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=0&start=0")
    print(main_tree.xpath)

    get_url = main_tree.xpath('/html/body/div[2]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div[3]/div/div[1]/div[2]/div[1]/a')
    print(uni_name)

    all_divs = main_tree.xpath('//*[@id="yui_3_10_3_1_1700016780175_557"]')
    print(str(len(all_divs)))
    # Interact with the first div
    first_div = all_divs[0]
    # This will get the number of sections (divs) under the first div.
    print(str(len(first_div)))


if __name__ == "__main__":
    main()