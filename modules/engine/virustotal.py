import json
import urllib
import urllib.request

def main(domain):
    print("\n VirusTotal Module Loaded")
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    parameters = {'domain': domain, 'apikey': 'e3301e0c05ae13a4a3d85cc4c2fd3b59c0d8829bbc175f6f22d4c4d98c351948'}
    response = urllib.request.urlopen('%s?%s' % (url, urllib.parse.urlencode(parameters))).read()
    response_dict = json.loads(response)
    print(response_dict)
