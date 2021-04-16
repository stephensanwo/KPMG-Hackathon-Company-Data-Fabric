from models.nse_scrapper import parse_company_base_info, parse_financial_statement_xml
from schema.CompanyData import Company, TradingData, FinancialStatements
import os
from dotenv import load_dotenv
from redislite import Redis
import csv


# Init redis storage local caching
redis_connection = Redis('./tmp/test.db')


# Environment
load_dotenv()
LISTED_COMPANIES_ENDPOINT = os.environ.get("LISTED_COMPANIES_ENDPOINT")
TRADE_HISTORY_ENDPOINT = os.environ.get("TRADE_HISTORY_ENDPOINT")
FINANCIAL_STATEMENTS_ENDPOINT = os.environ.get("FINANCIAL_STATEMENTS_ENDPOINT")
CORPORATE_DISCLOSURES_ENDPOINT = os.environ.get(
    "CORPORATE_DISCLOSURES_ENDPOINT")


# Get Company Base information
base_data = parse_company_base_info(url=LISTED_COMPANIES_ENDPOINT)


company_base_data = []
for data in base_data:
    newCompany = Company(
        id=data["$id"],
        internationalSecNumber=data["InternationSecIN"],
        symbol=data["Symbol"],
        marketCap=data["MarketCap"],
        sharesOutstanding=data["SharesOutstanding"],
        sector=data["Sector"],
        subSector=data["SubSector"],
        companyName=data["CompanyName"],
        marketClassification=data["MarketClassification"],
        dateListed=data["DateListed"],
        dateOfIncorporation=data["DateOfIncorporation"],
        website=data["Website"],
        natureofBusiness=data["NatureofBusiness"],
        companyAddress=data["CompanyAddress"],
        telephone=data["Telephone"],
        fax=data["Fax"],
        email=data["Email"],
        companySecretary=data["CompanySecretary"],
        auditor=data['Auditor'],
        registrars=data["Registrars"],
        boardOfDirectors=data["BoardOfDirectors"]
    )

    company_base_data.append(newCompany.company_data_summary())

# # fieldNames = list(Company.__dict__['__annotations__'].keys())


# # # Parse to csv
# # with open('./tmp/company_base_data.csv', 'w') as csvfile:
# #     writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
# #     writer.writeheader()
# #     writer.writerows(company_base_data)

# trade_history = []
# for company in company_base_data:
#     search_id = company['internationalSecNumber']
#     url = f"{TRADE_HISTORY_ENDPOINT}/{search_id}"
#     print(url)
#     trading_history = parse_company_base_info(url=url)
#     for data in trading_history:
#         newTradingData = TradingData(
#             internationalSecNumber=search_id,
#             tradeId=data['Id'],
#             price=data['PRICE'],
#             indexDate=data['INDEX_DATE'],
#             indexTime=data['INDEX_TIME'],
#             volume=data['VOLUME']

#         )
#         trade_history.append(newTradingData.trading_data_summary())
# print(trade_history)


# # Parse to csv
# fieldNames = list(TradingData.__dict__['__annotations__'].keys())
# with open('./tmp/company_trading_history.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
#     writer.writeheader()
#     writer.writerows(trade_history)


financial_statements_data = []
for company in company_base_data:
    search_id = company['internationalSecNumber']
    url = f"{FINANCIAL_STATEMENTS_ENDPOINT} '{search_id}' and (Type_of_Submission eq 'Financial Statements' or Type_of_Submission eq 'EarningForcast')"

    financial_statements = parse_financial_statement_xml(url=url)
    for data in financial_statements:
        newFinancialStatement = FinancialStatements(
            internationalSecNumber=search_id,
            typeOfSubmission=data['type_of_submission'],
            description=data['description'],
            url=data['url'],
            dateModified=data['modified']

        )
        financial_statements_data.append(
            newFinancialStatement.financial_statements_summary())


# Parse to csv
fieldNames = list(FinancialStatements.__dict__['__annotations__'].keys())
print(fieldNames)
with open('./tmp/company_financial_statements.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(financial_statements_data)

# corporate_disclosures = parse_xml_data(
#     url=CORPORATE_DISCLOSURES_ENDPOINT)
