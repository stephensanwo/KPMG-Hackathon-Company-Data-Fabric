from models.nse_scrapper import parse_company_base_info
from schema.CompanyData import Company
import os
from dotenv import load_dotenv
from redislite import Redis
import csv


# Init redis storage local caching
redis_connection = Redis('./tmp/test.db')


# Environment
load_dotenv()
LISTED_COMPANIES_ENDPOINT = os.environ.get("LISTED_COMPANIES_ENDPOINT")


# Get Company Base information
res = parse_company_base_info(url=LISTED_COMPANIES_ENDPOINT)
print(res)

company_base_data = []
for data in res:
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


fieldNames = list(Company.__dict__['__annotations__'].keys())


with open('./tmp/company_base_data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(company_base_data)
