from models.stock_analysis_scrapper import get_company_news_data, get_company_list, get_company_trading_data
from schema.InternationalCompanyData import CompanyList, CompanyBaseInfo
from time import sleep

# Get Base List or Create New
try:
    base_list = CompanyList.read_company_list()
except:
    get_company_list()
    base_list = CompanyList.read_company_list()


base_list = CompanyList.read_sp_company_list()
# Get Company News Data

iterator = 0
while iterator < len(base_list):
    print(iterator)
    get_company_news_data(base_list[iterator: iterator + 15])
    print("Sleeping.....")

    sleep(15)

    iterator += 15

# Get Trading Data
iterator = 0
while iterator < len(base_list):
    print(iterator)
    get_company_trading_data(base_list[iterator: iterator + 15])
    print("Sleeping.....")

    sleep(15)
    iterator += 15
