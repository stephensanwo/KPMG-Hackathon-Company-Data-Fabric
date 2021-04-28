import requests
from logging import error
import uuid
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
from fake_useragent import UserAgent
from schema.InternationalCompanyData import SuppliersCustomers

ua = UserAgent()


def get_company_customers_suppliers(base_list):
    """
    get company based overview data
    @param url: generated search url
    @return: company object
    """

    for company in base_list:
        company_code = company['company_code'].lower()
        print(company_code)

        # Suppliers
        req = Request(f'https://csimarket.com/stocks/competitionNO4.php?supply&code={company_code}',
                      headers={'User-Agent': ua.random})

        html = urlopen(req).read()
        soup = BeautifulSoup(html, "lxml")

        summary_info = soup.find_all(
            "table", attrs={'class': 'osnovna_tablica_bez_gifa'})

        for item in summary_info:
            tr = item.find_all("td")
            # skip headers and bottom
            iterator = 10
            while iterator < len(tr) - 5:
                newSC = SuppliersCustomers(
                    company_code=company_code,
                    name=tr[iterator].text,
                    code=tr[iterator+1].text,
                    category="Supplier"
                )
                newSC.parse_to_csv([newSC.sc_summary()])
                iterator += 5

        # Customers
        req = Request(f'https://csimarket.com/stocks/competitionNO4.php?markets&code={company_code}',
                      headers={'User-Agent': ua.random})

        html = urlopen(req).read()
        soup = BeautifulSoup(html, "lxml")

        summary_info_1 = soup.find_all(
            "table", attrs={'class': 'osnovna_tablica_bez_gifa'})

        for item in summary_info:
            tr = item.find_all("td")
            # skip headers and bottom
            iterator = 10
            while iterator < len(tr) - 5:
                newSC = SuppliersCustomers(
                    company_code=company_code,
                    name=tr[iterator].text,
                    code=tr[iterator+1].text,
                    category="Customer"
                )
                newSC.parse_to_csv([newSC.sc_summary()])
                iterator += 5

    return None
