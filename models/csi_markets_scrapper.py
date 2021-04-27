import requests
from logging import error
import uuid
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os


tmp_data = {
    "company_description_detailed": "",
}



def get_company_base_data():
    """
    get company based overview data
    @param url: generated search url
    @return: company object
    """

    req = Request('http://webcache.googleusercontent.com/search?q=cache:https://csimarket.com/stocks/AMZN-Business-Description.html',
                  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})

    html = urlopen(req).read()
    soup = BeautifulSoup(html, "lxml")

    summary_info = soup.find_all("div", attrs={'class': 'raz2'})

    description = []
    for data in summary_info:
        i = 0
        while i < len(data):
            tmp_description = data.find_all("p")[i].text
            description.append(tmp_description)
            i += 1
    tmp_data['company_description_detailed'] = ', '.join(description)

    print(tmp_data)
    return None


if __name__ == "__main__":
    get_company_base_data()
