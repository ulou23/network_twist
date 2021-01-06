import json
import requests

raw_json=requests.get('https://api.nfz.gov.pl/app-itl-api/swagger/v1.3/swagger.json').text
parsed=json.loads(raw_json)
print(json.dumps(parsed,indent=4,sort_keys=True))
