from models.stock_analysis_scrapper import get_company_base_data, get_company_list, get_employee_data, get_financial_data
from schema.InternationalCompanyData import CompanyList, CompanyBaseInfo
from time import sleep
from models.csi_markets_scrapper import get_company_customers_suppliers


# Get Base List or Create New
try:
    base_list = CompanyList.read_company_list()
except:
    get_company_list()
    base_list = CompanyList.read_company_list()


iterator = 0
while iterator < len(base_list):
    get_company_base_data(base_list[iterator: iterator + 30])

    print("Sleeping.....")
    sleep(15)
    iterator += 30


# Using S&P 500 List

base_list = CompanyList.read_sp_company_list()
iterator = 0
while iterator < len(base_list):
    print(iterator)
    get_employee_data(base_list[iterator: iterator + 15])

    print("Sleeping.....")

    sleep(15)

    iterator += 15

base_list = CompanyList.read_sp_company_list()
iterator = 0
while iterator < len(base_list):
    print(iterator)
    get_financial_data(base_list[iterator: iterator + 15])

    print("Sleeping.....")

    sleep(15)

    iterator += 15

base_list = CompanyList.read_sp_company_list()
iterator = 0
while iterator < len(base_list):
    print(iterator)
    get_company_customers_suppliers(base_list[iterator: iterator + 15])

    print("Sleeping.....")

    sleep(15)

    iterator += 15
