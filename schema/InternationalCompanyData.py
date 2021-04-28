from dataclasses import dataclass
import csv
import os


@dataclass
class CompanyList():
    company_code: str
    company_name: str

    def company_list_data(self):
        return {"company_code": self.company_code, "company_name": self.company_name}
    # Parse to csv

    @staticmethod
    def parse_to_csv(data: list):
        fieldNames = list(CompanyList.__dict__['__annotations__'].keys())
        with open('./tmp/international_company_data/companies_base_list.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def read_company_list() -> list:
        with open('./tmp/international_company_data/companies_base_list.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = []
            for row in csv_reader:
                tmp_data = {}
                tmp_data['company_code'] = row["company_code"]
                tmp_data['company_name'] = row["company_name"]
                data.append(tmp_data)

    @staticmethod
    def read_sp_company_list() -> list:
        with open('./tmp/international_company_data/SP_500_base_list.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = []
            for row in csv_reader:

                tmp_data = {}
                tmp_data['company_code'] = row["\ufeffcompany_code"]
                tmp_data['company_name'] = row["company_name"]
                data.append(tmp_data)

        return data


@dataclass
class CompanyBaseInfo():
    company_code: str
    company_name: str
    market_capitalization: str
    revenue: str
    net_income: str
    shares_outstanding: str
    earnings_per_share: str
    price_equity_ration: str
    forward_price_equity: str
    dividend: str
    dividend_yield: str
    company_description: str
    country: str
    year_founded: str
    ipo_date: str
    industry: str
    sector: str
    employees: str
    ceo_name: str
    address: str
    phone: str
    website: str
    exchange: str
    fiscal_year: str
    reporting_currency: str
    cik_code: str
    cusip_number: str
    isin_number: str
    employer_id: str

    def company_data_summary(self):
        data = {
            "company_code": self.company_code,
            "company_name": self.company_name,
            "market_capitalization": self.market_capitalization,
            "revenue": self.revenue,
            "net_income": self.net_income,
            "shares_outstanding": self.shares_outstanding,
            "earnings_per_share": self.earnings_per_share,
            "price_equity_ration": self.price_equity_ration,
            "forward_price_equity": self.forward_price_equity,
            "dividend": self.dividend,
            "dividend_yield": self.dividend_yield,
            "company_description": self.company_description,
            "country": self.country,
            "year_founded": self.year_founded,
            "ipo_date": self.ipo_date,
            "industry": self.industry,
            "sector": self.sector,
            "employees": self.employees,
            "ceo_name": self.ceo_name,
            "address": self.address,
            "phone": self.phone,
            "website": self.website,
            "exchange": self.exchange,
            "fiscal_year": self.fiscal_year,
            "reporting_currency": self.reporting_currency,
            "cik_code": self.cik_code,
            "cusip_number": self.cusip_number,
            "isin_number": self.isin_number,
            "employer_id": self.employer_id


        }
        return data

    @staticmethod
    def parse_to_csv(data):
        fileName = './tmp/international_company_data/companies_base_data.csv'
        create_header = os.path.exists(fileName)
        fieldNames = list(CompanyBaseInfo.__dict__['__annotations__'].keys())
        with open(fileName, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

            if create_header == False:
                writer.writeheader()

            writer.writerows(data)


@dataclass
class EmployeeData():
    company_code: str
    employee_name: str
    employee_role: str

    def key_employees_summary(self):
        data = {
            "company_code": self.company_code,
            "employee_name": self.employee_name,
            "employee_role": self.employee_role,

        }
        return data

    @staticmethod
    def parse_to_csv(data):
        fileName = './tmp/international_company_data/key_employees_data.csv'
        create_header = os.path.exists(fileName)
        fieldNames = list(EmployeeData.__dict__['__annotations__'].keys())
        with open(fileName, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

            if create_header == False:
                writer.writeheader()

            writer.writerows(data)


@dataclass
class CompanyNews():
    company_code: str
    news_title: str
    news_text: str
    news_link: str

    def company_news_summary(self):
        data = {
            "company_code": self.company_code,
            "news_title": self.news_title,
            "news_text": self.news_text,
            "news_link": self.news_link,

        }
        return data

    @staticmethod
    def parse_to_csv(data):
        fileName = './tmp/international_company_data/company_news_data.csv'
        create_header = os.path.exists(fileName)
        fieldNames = list(CompanyNews.__dict__['__annotations__'].keys())
        with open(fileName, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

            if create_header == False:
                writer.writeheader()

            writer.writerows(data)


@dataclass
class TradingData():
    company_code: str
    trading_date: str
    current_stock_price: str
    previous_closing_stock_price: str
    stock_price_change: str
    percentage_stock_price_change: str
    opening_stock_price: str
    stocks_day_range: str
    day_trading_volume: str
    fifty_two_week_range: str
    analysts_forecast: str

    def trading_data_summary(self):
        data = {
            "company_code": self.company_code,
            "trading_date": self.trading_date,
            "current_stock_price": self.current_stock_price,
            "previous_closing_stock_price": self.previous_closing_stock_price,
            "stock_price_change": self.stock_price_change,
            "percentage_stock_price_change": self.percentage_stock_price_change,
            "opening_stock_price": self.opening_stock_price,
            "stocks_day_range": self.stocks_day_range,
            "day_trading_volume": self.day_trading_volume,
            "fifty_two_week_range": self.fifty_two_week_range,
            "analysts_forecast": self.analysts_forecast,


        }
        return data

    @staticmethod
    def parse_to_csv(data):
        fileName = './tmp/international_company_data/company_trading_data.csv'
        create_header = os.path.exists(fileName)
        fieldNames = list(TradingData.__dict__['__annotations__'].keys())
        with open(fileName, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

            if create_header == False:
                writer.writeheader()

            writer.writerows(data)


@dataclass
class FinancialRatios():
    company_code: str
    current_ratio: str
    quick_ratio: str
    debt_equity: str
    debt_ebitda: str
    debt_free_cash_flow: str
    return_on_equity: str
    return_on_assets: str
    return_on_capital: str
    revenue_per_employee: str
    profits_per_employee: str
    inventory_turnover: str
    asset_turnover: str
    gross_margin: str
    operating_margin: str
    profit_margin: str

    def financial_ratio_summary(self):
        data = {
            "company_code": self.company_code,
            "current_ratio": self.current_ratio,
            "quick_ratio": self.quick_ratio,
            "debt_equity": self.debt_equity,
            "debt_ebitda": self.debt_ebitda,
            "debt_free_cash_flow": self.debt_free_cash_flow,
            "return_on_equity": self.return_on_equity,
            "return_on_assets": self.return_on_assets,
            "return_on_capital": self.return_on_capital,
            "revenue_per_employee": self.revenue_per_employee,
            "profits_per_employee": self.profits_per_employee,
            "asset_turnover": self.asset_turnover,
            "inventory_turnover": self.inventory_turnover,
            "gross_margin": self.gross_margin,
            "operating_margin": self.operating_margin,
            "profit_margin": self.profit_margin
        }
        return data

    @staticmethod
    def parse_to_csv(data):
        fileName = './tmp/international_company_data/company_financial_ratios.csv'
        create_header = os.path.exists(fileName)
        fieldNames = list(FinancialRatios.__dict__['__annotations__'].keys())
        with open(fileName, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

            if create_header == False:
                writer.writeheader()

            writer.writerows(data)


@dataclass
class FinancialStatement():
    company_code: str
    revenue: str
    gross_profit: str
    operating_income: str
    pre_tax_income: str
    net_income: str
    ebitda: str
    ebit: str
    eps: str
    cash_equivalents: str
    total_debt: str
    net_cash: str
    book_value: str
    working_capital: str
    operating_cashflow: str
    capital_expenditures: str
    free_cash_flow: str
    income_tax: str

    def financial_data_summary(self):
        data = {
            "company_code": self.company_code,
            "revenue": self.revenue,
            "gross_profit": self.gross_profit,
            "operating_income": self.operating_income,
            "pre_tax_income": self.pre_tax_income,
            "net_income": self.net_income,
            "ebitda": self.ebitda,
            "ebit": self.ebit,
            "eps": self.eps,
            "cash_equivalents": self.cash_equivalents,
            "total_debt": self.total_debt,
            "net_cash": self.net_cash,
            "book_value": self.book_value,
            "working_capital": self.working_capital,
            "operating_cashflow": self.operating_cashflow,
            "capital_expenditures": self.capital_expenditures,
            "free_cash_flow": self.free_cash_flow,
            "income_tax": self.income_tax
        }
        return data

    @staticmethod
    def parse_to_csv(data):
        fileName = './tmp/international_company_data/company_financial_statements.csv'
        create_header = os.path.exists(fileName)
        fieldNames = list(FinancialStatement.__dict__[
                          '__annotations__'].keys())
        with open(fileName, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

            if create_header == False:
                writer.writeheader()

            writer.writerows(data)


@dataclass
class SuppliersCustomers():
    company_code: str
    name: str
    code: str
    category: str

    def sc_summary(self):
        data = {
            "company_code": self.company_code,
            "name": self.name,
            "code": self.code,
            "category": self.category
        }
        return data

    @staticmethod
    def parse_to_csv(data):
        fileName = './tmp/international_company_data/company_suppliers_and_customers.csv'
        create_header = os.path.exists(fileName)
        fieldNames = list(SuppliersCustomers.__dict__[
                          '__annotations__'].keys())
        with open(fileName, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

            if create_header == False:
                writer.writeheader()

            writer.writerows(data)
