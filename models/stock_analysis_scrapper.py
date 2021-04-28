import requests
from logging import error
import uuid
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
from schema.InternationalCompanyData import CompanyList, CompanyBaseInfo, EmployeeData, CompanyNews, TradingData, FinancialRatios, FinancialStatement
from time import sleep
from fake_useragent import UserAgent


ua = UserAgent()


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


def get_employee_data(base_list):

    # Company info
    for company in base_list:

        company_code = company['company_code'].lower()
        print(company_code)

        req = Request(f'https://stockanalysis.com/stocks/{company_code}/company/', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})

        html = urlopen(req).read()
        soup = BeautifulSoup(html, "lxml")

        # Executives
        executives = soup.find_all("div", attrs={'class': 'executives'})

        executives_list = []
        for item in executives:
            table_data = item.find_all("td")
            for data in table_data:
                executives_list.append(data.text)

        iterator = 0
        while iterator < len(executives_list):
            newEmployeeItem = EmployeeData(
                company_code=company_code,
                employee_name=executives_list[iterator],
                employee_role=executives_list[iterator+1]
            )
            newEmployeeItem.parse_to_csv(
                [newEmployeeItem.key_employees_summary()])
            iterator += 2

    return None


def get_company_news_data(base_list):

    # Company info
    for company in base_list:
        company_code = company['company_code'].lower()
        print(company_code)

        req = Request(f'https://stockanalysis.com/stocks/{company_code}/',
                      headers={'User-Agent': ua.random})

        html = urlopen(req).read()
        soup = BeautifulSoup(html, "lxml")

        # Executives
        news = soup.find_all("div", attrs={'class': 'news-article'})
        for article in news:
            newCompanyNews = CompanyNews(
                company_code=company_code,
                news_title=article.find("h3").text,
                news_text=article.find("p").text,
                news_link=article.find("a", href=True)['href']
            )

            newCompanyNews.parse_to_csv(
                [newCompanyNews.company_news_summary()])

    return None


def get_company_trading_data(base_list):

    for company in base_list:
        # Reinitialize

        trading_date, current_stock_price, previous_closing_stock_price, stock_price_change, percentage_stock_price_change, opening_stock_price, stocks_day_range, day_trading_volume, fifty_two_week_range, analysts_forecast = "", "", "", "", "", "", "", "", "", ""

        company_code = company['company_code'].lower()
        print(company_code)

        req = Request(f'https://stockanalysis.com/stocks/{company_code}/',
                      headers={'User-Agent': ua.random})

        html = urlopen(req).read()
        soup = BeautifulSoup(html, "lxml")

        # Overview Data 1 Table
        summary_info_1 = soup.find_all("div", attrs={'class': 'quote'})

        for data in summary_info_1:
            trading_date = data.find_all("td")[1].text

            current_stock_price = data.find_all("td")[3].text

            previous_closing_stock_price = data.find_all("td")[5].text

            stock_price_change = data.find_all("td")[7].text

            percentage_stock_price_change = data.find_all("td")[9].text

            opening_stock_price = data.find_all("td")[11].text

            stocks_day_range = data.find_all("td")[13].text

            day_trading_volume = data.find_all("td")[15].text

            fifty_two_week_range = data.find_all("td")[17].text

        try:
            analysts_info = soup.find_all(
                "div", attrs={'class': 'sidew wintro'})[1]

            analysts_forecast = analysts_info.find("p").text
        except IndexError:
            pass

        newTradingData = TradingData(
            company_code=company_code,
            trading_date=trading_date,
            current_stock_price=current_stock_price,
            previous_closing_stock_price=previous_closing_stock_price,
            stock_price_change=stock_price_change,
            percentage_stock_price_change=percentage_stock_price_change,
            opening_stock_price=opening_stock_price,
            stocks_day_range=stocks_day_range,
            day_trading_volume=day_trading_volume,
            fifty_two_week_range=fifty_two_week_range,
            analysts_forecast=analysts_forecast
        )
        newTradingData.parse_to_csv([newTradingData.trading_data_summary()])
    return None


def get_financial_data(base_list):
    for company in base_list:
        # Reinitialize
        current_ratio, quick_ratio, debt_equity, debt_ebitda, debt_free_cash_flow, return_on_equity, return_on_assets, return_on_capital, revenue_per_employee, profits_per_employee, asset_turnover, inventory_turnover, gross_margin, operating_margin, profit_margin = "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""

        revenue, gross_profit, operating_income, pre_tax_income, net_income, ebitda, ebit, eps, cash_equivalents, total_debt, net_cash, book_value, working_capital, operating_cashflow, capital_expenditures, free_cash_flow, income_tax, = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""

        company_code = company['company_code'].lower()
        print(company_code)

        req = Request(
            f'https://stockanalysis.com/stocks/{company_code}/statistics/', headers={'User-Agent': ua.random})

        html = urlopen(req).read()
        soup = BeautifulSoup(html, "lxml")

        # Overview Data 1 Table
        financial_ratios = soup.find_all("td")
        for data in financial_ratios:
            if data.text == "Current Ratio":
                index = int(financial_ratios.index(data))
                current_ratio = financial_ratios[index+1].text

            if data.text == "Quick Ratio":
                index = int(financial_ratios.index(data))
                quick_ratio = financial_ratios[index+1].text

            if data.text == "Debt / Equity":
                index = int(financial_ratios.index(data))
                debt_equity = financial_ratios[index+1].text

            if data.text == "Debt / EBITDA":
                index = int(financial_ratios.index(data))
                debt_ebitda = financial_ratios[index+1].text

            if data.text == "Debt / FCF":
                index = int(financial_ratios.index(data))
                debt_free_cash_flow = financial_ratios[index+1].text

            if data.text == "Return on Equity (ROE)":
                index = int(financial_ratios.index(data))
                return_on_equity = financial_ratios[index+1].text

            if data.text == "Return on Assets (ROA)":
                index = int(financial_ratios.index(data))
                return_on_assets = financial_ratios[index+1].text

            if data.text == "Return on Capital (ROIC)":
                index = int(financial_ratios.index(data))
                return_on_capital = financial_ratios[index+1].text

            if data.text == "Revenue Per Employee":
                index = int(financial_ratios.index(data))
                revenue_per_employee = financial_ratios[index+1].text

            if data.text == "Profits Per Employee":
                index = int(financial_ratios.index(data))
                profits_per_employee = financial_ratios[index+1].text

            if data.text == "Asset Turnover":
                index = int(financial_ratios.index(data))
                asset_turnover = financial_ratios[index+1].text

            if data.text == "Inventory Turnover":
                index = int(financial_ratios.index(data))
                inventory_turnover = financial_ratios[index+1].text

            if data.text == "Gross Margin":
                index = int(financial_ratios.index(data))
                gross_margin = financial_ratios[index+1].text

            if data.text == "Operating Margin":
                index = int(financial_ratios.index(data))
                operating_margin = financial_ratios[index+1].text

            if data.text == "Profit Margin":
                index = int(financial_ratios.index(data))
                profit_margin = financial_ratios[index+1].text

        newFinancialRatio = FinancialRatios(
            company_code=company_code,
            current_ratio=current_ratio,
            quick_ratio=quick_ratio,
            debt_equity=debt_equity,
            debt_ebitda=debt_ebitda,
            debt_free_cash_flow=debt_free_cash_flow,
            return_on_equity=return_on_equity,
            return_on_assets=return_on_assets,
            return_on_capital=return_on_capital,
            revenue_per_employee=revenue_per_employee,
            profits_per_employee=profits_per_employee,
            inventory_turnover=inventory_turnover,
            asset_turnover=asset_turnover,
            gross_margin=gross_margin,
            profit_margin=profit_margin,
            operating_margin=operating_margin
        )

        newFinancialRatio.parse_to_csv(
            [newFinancialRatio.financial_ratio_summary()])

        # Table 2
        for data in financial_ratios:
            if data.text == "Revenue":
                index = int(financial_ratios.index(data))
                revenue = financial_ratios[index+1].text

            if data.text == "Gross Profit":
                index = int(financial_ratios.index(data))
                gross_profit = financial_ratios[index+1].text

            if data.text == "Operating Income":
                index = int(financial_ratios.index(data))
                operating_income = financial_ratios[index+1].text

            if data.text == "Pretax Income":
                index = int(financial_ratios.index(data))
                pre_tax_income = financial_ratios[index+1].text

            if data.text == "Net Income":
                index = int(financial_ratios.index(data))
                net_income = financial_ratios[index+1].text

            if data.text == "EBITDA":
                index = int(financial_ratios.index(data))
                ebitda = financial_ratios[index+1].text

            if data.text == "EBIT":
                index = int(financial_ratios.index(data))
                ebit = financial_ratios[index+1].text

            if data.text == "Earnings Per Share (EPS)":
                index = int(financial_ratios.index(data))
                eps = financial_ratios[index+1].text

            if data.text == "Cash & Cash Equivalents":
                index = int(financial_ratios.index(data))
                cash_equivalents = financial_ratios[index+1].text

            if data.text == "Total Debt":
                index = int(financial_ratios.index(data))
                total_debt = financial_ratios[index+1].text

            if data.text == "Net Cash":
                index = int(financial_ratios.index(data))
                net_cash = financial_ratios[index+1].text

            if data.text == "Book Value":
                index = int(financial_ratios.index(data))
                book_value = financial_ratios[index+1].text

            if data.text == "Working Capital":
                index = int(financial_ratios.index(data))
                working_capital = financial_ratios[index+1].text

            if data.text == "Operating Cash Flow":
                index = int(financial_ratios.index(data))
                operating_cashflow = financial_ratios[index+1].text

            if data.text == "Capital Expenditures":
                index = int(financial_ratios.index(data))
                capital_expenditures = financial_ratios[index+1].text

            if data.text == "Free Cash Flow":
                index = int(financial_ratios.index(data))
                free_cash_flow = financial_ratios[index+1].text

            if data.text == "Income Tax":
                index = int(financial_ratios.index(data))
                income_tax = financial_ratios[index+1].text

        newFinancialStatement = FinancialStatement(
            company_code=company_code,
            revenue=revenue,
            gross_profit=gross_profit,
            operating_income=operating_income,
            pre_tax_income=pre_tax_income,
            net_income=net_income,
            ebitda=ebitda,
            ebit=ebit,
            eps=eps,
            cash_equivalents=cash_equivalents,
            total_debt=total_debt,
            net_cash=net_cash,
            book_value=book_value,
            working_capital=working_capital,
            operating_cashflow=operating_cashflow,
            capital_expenditures=capital_expenditures,
            free_cash_flow=free_cash_flow,
            income_tax=income_tax
        )

        newFinancialStatement.parse_to_csv(
            [newFinancialStatement.financial_data_summary()])
    return None


if __name__ == "__main__":

    try:
        base_list = CompanyList.read_company_list()
    except:
        get_company_list()
        base_list = CompanyList.read_company_list()

    iterator = 3948
    while iterator < len(base_list):
        get_company_base_data(base_list[iterator: iterator + 30])

        print("Sleeping.....")
        sleep(15)

        iterator += 30
