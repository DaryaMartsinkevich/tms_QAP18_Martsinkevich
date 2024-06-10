import os
from bs4 import BeautifulSoup

def check_html(direct, check, tags):
    for dirs, root, files in os.walk(direct):
        for file in files:
            if file.endswith(".html"):
                path_file = os.path.join(dirs, file)
                with open(path_file, "r", encoding="utf-8") as f:
                    hashtag = f.readlines()
                    for number, hashtag in enumerate(hashtag, start=1):
                        for x in tags:
                            if x in hashtag:
                                soup = BeautifulSoup(hashtag, 'html.parser')
                                for elem in soup.find_all(x):
                                    if not elem.has_attr(check):
                                        print(
                                            f'Tag {x} not contain {check} in file {os.path.join(dirs, file)} at hashtag {number}: {elem}'
                                        )



check_tags = ("p", "button", "h2", "h")
check_html('/Users/48574/qap18/tms_QAP18_Martsinkevich/test-i18n/app','i18n', check_tags)

