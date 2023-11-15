from Web_Scraping import get_web_tree

url = "https://www.wvu.edu"

web_tree = get_web_tree(url)

def extract_text(tree, num_texts):
    texts = tree.xpath('//text()')
    return texts[:num_texts]

if web_tree is not None:
    texts = extract_text(web_tree, num_texts=5)  # Add a comma to separate the arguments

    for text in texts:
        print(text)

html_content = '''
<html>
  <body>
    <h2 class="header-margin">Let us be your guide</h2>
  </body>
</html>
'''

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract text from the element with class "header-margin"
header_text = tree.xpath('//h2[@class="header-margin"]/text()')[0]  # Get the first matching element

# Print the extracted text
print("Header Text:", header_text)