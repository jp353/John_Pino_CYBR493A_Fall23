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
