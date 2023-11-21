import Web_Scraping as wb


def main():
    """
    Main screen for the web scrapping file
    :return:
    """

print("Here's a bunch of texts from the WVU website:")

main_tree = wb.get_web_tree("https://www.wvu.edu")


financial_aid = main_tree.xpath('/html/body/main/div[1]/div[1]/div/h1/span/text()')
print(financial_aid)

guide = main_tree.xpath('/html/body/main/div[3]/div/div[1]/h2/text()')
print(guide)

wheres_my_refund = main_tree.xpath('/html/body/main/div[4]/div/div[2]/ul/li[13]/a/text()')
print(wheres_my_refund)

admitted_students = main_tree.xpath('/html/body/main/div[3]/div/div[3]/div[2]/div/h3/text()')
print(admitted_students)

wvu_help = main_tree.xpath('/html/body/main/div[3]/div/div[2]/p[2]/text()')
print(wvu_help)



if __name__ == "__main__":
    main()
