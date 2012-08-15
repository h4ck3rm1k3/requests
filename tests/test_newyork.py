import pprint
import requests
pp = pprint.PrettyPrinter(indent=4)

def debugresponse (r):
    statuscode= r.status_code
    print("Response status code: %s" % statuscode)
    print("Response status code: %d" % statuscode)
    print("Response url %s" % pp.pformat(r.url))            
    print("Response headers %s" % pp.pformat(r.headers))            



index =4212345984343434
url = ("http://open.nysenate.gov/legislation/search/"
       "?search=otype:bill&searchType=&format=xml"
       "&pageIdx=%d" % index)

r = requests.get(url)
print pp.pformat(url)
print pp.pformat(r)
debugresponse (r)


