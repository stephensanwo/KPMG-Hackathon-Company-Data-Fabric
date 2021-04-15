from models.nse_scrapper import parse_company_base_info
from schema.CompanyData import Company
import os
from dotenv import load_dotenv
import redis
from redislite import Redis


# Environment
load_dotenv()
LISTED_COMPANIES_ENDPOINT = os.environ.get("LISTED_COMPANIES_ENDPOINT")

# Caching
r = redis.Redis(
    host='localhost',
    port=6379)

# Get Company Base information
res = parse_company_base_info(url=LISTED_COMPANIES_ENDPOINT)
print(res)

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

    print(newCompany.company_data_summary())
