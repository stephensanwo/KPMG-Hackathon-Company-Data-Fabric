from dataclasses import dataclass
from models.nse_scrapper import parse_company_base_info


@dataclass
class Company():
    id: str
    internationalSecNumber: str
    symbol: str
    marketCap: str
    sharesOutstanding: str
    sector: str
    subSector: str
    companyName: str
    marketClassification: str
    dateListed: str
    dateOfIncorporation	: str
    website:	str
    natureofBusiness: str
    companyAddress: str
    telephone:	str
    fax: str
    email: str
    companySecretary: str
    auditor	: str
    registrars: str
    boardOfDirectors: str

    def get_company_base_data(self) -> object:
        res = parse_company_base_info()

        return self.unit_price * self.quantity_on_hand

    def company_data_summary(self):
        data = {
            "id": self.id,
            "internationalSecNumber": self.internationalSecNumber,
            "symbol": self.symbol,
            "marketCap": self.marketCap,
            "sharesOutstanding": self.sharesOutstanding,
            "sector": self.sector,
            "subSector": self.subSector,
            "companyName": self.companyName,
            "marketClassification": self.marketClassification,
            "dateListed": self.dateListed,
            "dateOfIncorporation"	: self.dateOfIncorporation,
            "website":	self.website,
            "natureofBusiness": self.natureofBusiness,
            "companyAddress": self.companyAddress,
            "telephone": self.telephone,
            "fax": self.fax,
            "email": self.email,
            "companySecretary": self.companySecretary,
            "auditor": self.auditor,
            "registrars": self.registrars,
            "boardOfDirectors": self.boardOfDirectors

        }
        return data


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
