import requests
from logging import error
import uuid
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
from schema.InternationalCompanyData import CompanyList, CompanyBaseInfo
from time import sleep
from fake_useragent import UserAgent


ua = UserAgent()


STOCK_ANALYSIS_ENDPOINT = os.environ.get("STOCK_ANALYSIS_ENDPOINT")


def get_company_list():
    """
    Gets the list of companies to be scrapped - using google cache
    """

    req = Request('http://webcache.googleusercontent.com/search?q=cache:https://stockanalysis.com/stocks/',
                  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})

    html = urlopen(req).read()
    soup = BeautifulSoup(html, "lxml")

    tmp_list = soup.find_all("a")

    company_list_tmp = []

    for item in tmp_list:
        company_list_tmp.append(item.text)

    company_list = []
    for company in company_list_tmp[23: len(company_list_tmp)-25]:

        newCompany = CompanyList(
            company_code=company.split("-", 1)[0].strip(),
            company_name=company.split("-", 1)[1].strip()
        )

        company_list.append(newCompany.company_list_data())

    CompanyList.parse_to_csv(company_list)

    return None


def get_company_base_data(base_list):
    """
    get company based overview data
    @param url: generated search url
    @return: company object
    """

    for company in base_list:
        try:
            company_code = company['company_code'].lower()

            # Reinitialize variables
            market_capitalization, revenue, net_income, shares_outstanding, earnings_per_share, price_equity_ration, forward_price_equity, dividend, dividend_yield, company_description, country, year_founded, ipo_date, industry, sector, employees, ceo_name, address, phone, website, exchange, fiscal_year, reporting_currency, cik_code, cusip_number, isin_number, employer_id = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""

            print(company_code)

            # Create proxy host
            proxy_host = f"http://105.112.8.53:3128"
            # Use Cache because the data is typically static
            req = Request(f'https://stockanalysis.com/stocks/{company_code}/',
                          headers={'User-Agent': ua.random})

            # req.set_proxy(proxy_host, 'https')
            html = urlopen(req).read()
            soup = BeautifulSoup(html, "lxml")

            # Summary Info
            summary_info = soup.find_all("div", attrs={'class': 'info'})

            # Company info
            req = Request(f'https://stockanalysis.com/stocks/{company_code}/company/', headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})

            html = urlopen(req).read()
            soup = BeautifulSoup(html, "lxml")

            # Description
            description = soup.find_all("div", attrs={'class': 'description'})
            for item in description:
                description = item.text

            # Company
            company_info = soup.find_all("div", attrs={'class': 'swrap'})

            # Table 1
            for i in company_info[1].find_all("td"):
                if i.text.strip() == "Country":
                    country = company_info[1].find_all(
                        "td")[company_info[1].find_all("td").index(i) + 1].text

                if i.text.strip() == "Founded":
                    year_founded = company_info[1].find_all(
                        "td")[company_info[1].find_all("td").index(i) + 1].text

                if i.text.strip() == "IPO Date":
                    ipo_date = company_info[1].find_all(
                        "td")[company_info[1].find_all("td").index(i) + 1].text

                if i.text.strip() == "Industry":
                    industry = company_info[1].find_all(
                        "td")[company_info[1].find_all("td").index(i) + 1].text

                if i.text.strip() == "Sector":
                    sector = company_info[1].find_all(
                        "td")[company_info[1].find_all("td").index(i) + 1].text

                if i.text.strip() == "Employees":
                    employees = company_info[1].find_all(
                        "td")[company_info[1].find_all("td").index(i) + 1].text

                if i.text.strip() == "CEO":
                    ceo_name = company_info[1].find_all(
                        "td")[company_info[1].find_all("td").index(i) + 1].text

            # Table 2
            for i in company_info[2].find_all("td"):
                if i.text.strip() == "Website":
                    website = company_info[2].find_all(
                        "td")[company_info[2].find_all("td").index(i) + 1].text

            for i in company_info[2].find_all("td"):
                if i.text.strip() == "Phone":
                    phone = company_info[2].find_all(
                        "td")[company_info[2].find_all("td").index(i) + 1].text

            for i in company_info[2].find_all("td"):
                if i.text.strip().startswith("Address"):
                    address = company_info[2].find_all(
                        "td")[company_info[2].find_all("td").index(i)].text.replace("Address:", "")

            # Table 3
            for i in company_info[3].find_all("td"):
                if i.text.strip() == "Exchange":
                    exchange = company_info[3].find_all(
                        "td")[company_info[3].find_all("td").index(i) + 1].text

            for i in company_info[3].find_all("td"):
                if i.text.strip() == "Fiscal Year":
                    fiscal_year = company_info[3].find_all(
                        "td")[company_info[3].find_all("td").index(i) + 1].text

            for i in company_info[3].find_all("td"):
                if i.text.strip() == "Reporting Currency":
                    reporting_currency = company_info[3].find_all(
                        "td")[company_info[3].find_all("td").index(i) + 1].text

            for i in company_info[3].find_all("td"):
                if i.text.strip() == "CIK Code":
                    cik_code = company_info[3].find_all(
                        "td")[company_info[3].find_all("td").index(i) + 1].text

            for i in company_info[3].find_all("td"):
                if i.text.strip() == "CUSIP Number":
                    cusip_number = company_info[3].find_all(
                        "td")[company_info[3].find_all("td").index(i) + 1].text

            for i in company_info[3].find_all("td"):
                if i.text.strip() == "ISIN Number":
                    isin_number = company_info[3].find_all(
                        "td")[company_info[3].find_all("td").index(i) + 1].text

            for i in company_info[3].find_all("td"):
                if i.text.strip() == "Employer ID":
                    employer_id = company_info[3].find_all(
                        "td")[company_info[3].find_all("td").index(i) + 1].text

            for data in summary_info:
                newBaseData = CompanyBaseInfo(
                    company_code=company_code,
                    company_name=company["company_name"],
                    market_capitalization=data.find_all("td")[1].text,
                    revenue=data.find_all("td")[3].text,
                    net_income=data.find_all("td")[5].text,
                    shares_outstanding=data.find_all("td")[7].text,
                    earnings_per_share=data.find_all("td")[9].text,
                    price_equity_ration=data.find_all("td")[11].text,
                    forward_price_equity=data.find_all("td")[13].text,
                    dividend=data.find_all("td")[15].text,
                    dividend_yield=data.find_all("td")[17].text,
                    company_description=description,
                    country=country,
                    year_founded=year_founded,
                    ipo_date=ipo_date,
                    industry=industry,
                    sector=sector,
                    employees=employees,
                    ceo_name=ceo_name,
                    address=address,
                    phone=phone,
                    website=website,
                    exchange=exchange,
                    fiscal_year=fiscal_year,
                    reporting_currency=reporting_currency,
                    cik_code=cik_code,
                    cusip_number=cusip_number,
                    isin_number=isin_number,
                    employer_id=employer_id)

                CompanyBaseInfo.parse_to_csv(
                    [newBaseData.company_data_summary()])

        except:
            pass

    return None


def get_company_trading_data(base_list):
    """
    get company based overview data
    @param url: generated search url
    @return: company object
    """

    for company in base_list:
        company_code = company['company_code'].lower()
        print(company_code)

        # Use Cache because the data is typically static
        req = Request(f'https://stockanalysis.com/stocks/{company_code}/company/',
                      headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})

        html = urlopen(req).read()
        soup = BeautifulSoup(html, "lxml")

        # Description
        description = soup.find_all("div", attrs={'class': 'description'})
        for item in description:
            description = item.text
            pass

        # Company
        company_info = soup.find_all("div", attrs={'class': 'swrap'})

        # Table 1
        print(company_info[2].find_all("td"))
        for i in company_info[2].find_all("td"):
            if i.text.strip() == "Website":
                website = company_info[2].find_all(
                    "td")[company_info[2].find_all("td").index(i) + 1].text

        for i in company_info[2].find_all("td"):
            if i.text.strip() == "Phone":
                phone = company_info[2].find_all(
                    "td")[company_info[2].find_all("td").index(i) + 1].text

        for i in company_info[2].find_all("td"):
            if i.text.strip().startswith("Address"):
                address = company_info[2].find_all(
                    "td")[company_info[2].find_all("td").index(i)].text.replace("Address:", "")

        print(website)
        print(phone)
        print(address)

        # country = company_info[1].find_all("td")[3].text
        # year_founded = company_info[1].find_all("td")[5].text
        # ipo_date = company_info[1].find_all("td")[7].text
        # industry = company_info[1].find_all("td")[9].text
        # sector = company_info[1].find_all("td")[11].text
        # employees = company_info[1].find_all("td")[13].text

        # print(company_info[1].find_all("td")[14].text)

        # address = company_info[2].find_all("td")[0].text
        # phone = company_info[2].find_all("td")[2].text
        # website = company_info[2].find_all("td")[4].text

        # exchange = company_info[3].find_all("td")[3].text
        # fiscal_year = company_info[3].find_all("td")[5].text
        # reporting_currency = company_info[3].find_all("td")[7].text
        # cik_code = company_info[3].find_all("td")[9].text
        # cusip_number = company_info[3].find_all("td")[11].text
        # isin_number = company_info[3].find_all("td")[13].text
        # employer_id = company_info[3].find_all("td")[15].text

        # # Executives
        # executives = soup.find_all("div", attrs={'class': 'executives'})

        # executives_list = []
        # for item in executives:
        #     table_data = item.find_all("td")
        #     for data in table_data:
        #         executives_list.append(data.text)

        # for data in company_info:
        #     print(data.find_all("td"))

    # Overview Data 1 Table
    # summary_info_1 = soup.find_all("div", attrs={'class': 'quote'})
    # for data in summary_info_1:
    #     tmp_data["trading_date"] = data.find_all("td")[1].text
    #     tmp_data["current_stock_price"] = data.find_all("td")[3].text
    #     tmp_data["previous_closing_stock_price"] = data.find_all("td")[5].text
    #     tmp_data["stock_price_change"] = data.find_all("td")[7].text
    #     tmp_data["percentage_stock_price_change"] = data.find_all("td")[9].text
    #     tmp_data["opening_stock_price"] = data.find_all("td")[11].text
    #     tmp_data["stocks_day_range"] = data.find_all("td")[13].text
    #     tmp_data["day_trading_volume"] = data.find_all("td")[15].text

    return None


if __name__ == "__main__":

    try:
        base_list = CompanyList.read_company_list()
    except:
        get_company_base_data()
        base_list = CompanyList.read_company_list()

    iterator = 3948
    while iterator < len(base_list):
        get_company_base_data(base_list[iterator: iterator + 30])

        print("Sleeping.....")
        sleep(15)

        iterator += 30
