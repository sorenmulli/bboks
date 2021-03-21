import os

import requests
from bs4 import BeautifulSoup

COLLECT_LINK = "https://kalliope.org/da/work/oehlenschlaeger/1819"
OUT = "local_data/oehlenschlager1819"

def get_links() -> list[str]:
    class_data = r"jsx-531762627 block"
    page = BeautifulSoup(requests.get(COLLECT_LINK).content, "html.parser")
    return page.find_all("div", class_=class_data)

if __name__ == '__main__':
    print(
        get_links()
    )
