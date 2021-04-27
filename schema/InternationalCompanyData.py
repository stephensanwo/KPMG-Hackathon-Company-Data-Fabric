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
class TradingData():
    internationalSecNumber: str
    tradeId: str
    price: str
    indexDate: str
    indexTime: str
    volume: str

    def trading_data_summary(self):
        data = {
            "internationalSecNumber": self.internationalSecNumber,
            "tradeId": self.tradeId,
            "price": self.price,
            "indexDate": self.indexDate,
            "indexTime": self.indexTime,
            "volume": self.volume,

        }
        return data


@dataclass
class FinancialStatements():
    internationalSecNumber: str
    typeOfSubmission: str
    description: str
    url: str
    dateModified: str

    def financial_statements_summary(self):
        data = {
            "internationalSecNumber": self.internationalSecNumber,
            "typeOfSubmission": self.typeOfSubmission,
            "description": self.description,
            "url": self.url,
            "dateModified": self.dateModified
        }
        return data


@dataclass
class CorporateDisclosures():
    internationalSecNumber: str
    typeOfSubmission: str
    description: str
    url: str
    dateModified: str

    def corporate_disclosures_summary(self):
        data = {
            "internationalSecNumber": self.internationalSecNumber,
            "typeOfSubmission": self.typeOfSubmission,
            "description": self.description,
            "url": self.url,
            "dateModified": self.dateModified
        }
        return data
