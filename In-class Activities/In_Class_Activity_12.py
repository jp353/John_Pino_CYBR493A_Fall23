import requests
from lxml import html

def get_total_pages(initial_url):
    response = requests.get(initial_url)
    if response.status_code == 200:
        tree = html.fromstring(response.content)
        total_pages_element = tree.xpath("//div[@class='pagination']/a[last()-1]/text()")
        if total_pages_element:
            return int(total_pages_element[0])
    return None

def generate_url(base_url, page_number):
    return f"{base_url}&start={(page_number - 1) * 75}"

def make_request(url):
    response = requests.get(url)
    return response

def extract_bug_data():

    pass

def Generate_Pages(initial_url):

    currentPage = 1


    totalPages = get_total_pages(initial_url)

    if totalPages is None:
        print("Failed to retrieve the total number of pages.")
        return


    while currentPage <= totalPages:

        currentUrl = generate_url(initial_url, currentPage)


        print(f"Page {currentPage}: {currentUrl}")


        urlResponse = make_request(currentUrl)

        if urlResponse.status_code == 200:

            extract_bug_data(urlResponse.content)


            currentPage += 1
        else:

            print(f"Failed to fetch data from {currentUrl}")
            break

# Example usage:
initial_link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&orderby=-importance&start=0"
Generate_Pages(initial_link)
