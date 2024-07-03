import json
import requests
import pandas as pd

from connectaida import conect_aida

def main(): 
    token = conect_aida()
    format_request = 'application/json'

    api_url = 'https://app-prd-ty49.azurewebsites.net/aida/v1/service/dt0000_prd_itsm_consumo_vw_itsm_bdgc_cat_aplic'

    size_page = 100
    from_page = 1

    count = 0

    df = pd.DataFrame()

    while ((count == 0 ) or count > (size_page*(from_page - 1))):

        head = {'Authorization': 'Bearer '+ token['accessToken']}

        current_url = api_url + '?$format=' + format_request + '&$count=true&$top=' + str(size_page) + '&$skip=' + str(size_page*(from_page-1))

        print(current_url)
        from_page = from_page + 1
        jsonStr = requests.get(current_url, headers = head).json()

        if (count == 0):
            count = jsonStr['@odata.count'];

        df = pd.concat([df, pd.read_json(json.dumps(jsonStr['value']), orient='records')], ignore_index=True)

    with open('catalogo.txt', 'at') as volumes_file:
        print(df.info(), file=volumes_file)

if __name__ == "__main__":
    main()