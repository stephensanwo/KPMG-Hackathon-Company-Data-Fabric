import requests


def parse_company_base_info(*args, **kwargs):
    """
    @Desc: Scrape base url for company data
    @param: Base URL
    @return: Company object
    """

    print(f"Fetching base data from {kwargs['url']}")
    # Define the response object

    req = requests.get(kwargs['url'])
    print(f"Connection to API Status {req}")

    res = req.json()

    return res
