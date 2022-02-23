import requests

import json


def initialize_dataset(url):

    fileobj = requests.get(url)

    json_fileobj = fileobj.json()
    json_li = json_fileobj['result']['records']

    result_string = json.dumps(json_li)


    with open('overdose_data.json', 'w') as outfile:
        outfile.write(result_string)


    print('done')


def create_url(resource_id, limit):
    return 'https://data.wprdc.org/api/3/action/datastore_search?resource_id=' + resource_id + '&' + str(limit)



if __name__ == "__main__":
    
    url = create_url('1c59b26a-1684-4bfb-92f7-205b947530cf', 10000)
    
    initialize_dataset(url)