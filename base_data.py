from models.stock_analysis_scrapper import get_company_base_data, get_company_list
from schema.InternationalCompanyData import CompanyList, CompanyBaseInfo

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
