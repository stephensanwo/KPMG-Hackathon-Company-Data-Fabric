import requests
import json
import xmltodict


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


def parse_financial_statement_xml(*args, **kwargs):
    """
    @Desc: Scrape base url for company data
    @param: Base URL
    @return: Company object
    """

    print(f"Fetching base data from {kwargs['url']}")
    # Define the response object

    req = requests.get(kwargs['url'])
    print(f"Connection to API Status {req}")

    res = req.text

    data_dict = xmltodict.parse(res)

    data_list = data_dict['feed']['entry']

    result = []
    try:
        for data in data_list:
            tmp_data = {}
            content = data['content']['m:properties']
            for key, value in content.items():
                if key == "d:Type_of_Submission":
                    tmp_data['type_of_submission'] = value

                if key == "d:URL":
                    tmp_data['url'] = value['d:Url']
                    tmp_data['description'] = value['d:Description']

                if key == "d:Modified":
                    tmp_data['modified'] = value['#text']

            result.append(tmp_data)

    except TypeError:
        tmp_data = {}
        content = data_list['content']['m:properties']
        print(content['d:URL'])
        for key, value in content.items():
            if key == "d:Type_of_Submission":
                tmp_data['type_of_submission'] = value

            if key == "d:URL":
                tmp_data['url'] = value['d:Url']
                tmp_data['description'] = value['d:Description']

            if key == "d:Modified":
                tmp_data['modified'] = value['#text']

            result.append(tmp_data)

    return result
