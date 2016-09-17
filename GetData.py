import urllib.request
import json

api_key = "3d4047590356727bf89cab9124ab1340c179068c"

dataToGet = "EMP,NAICS2012_TTL,OPTAX,GEO_TTL"
state = "02"
county = "016"
NAICS = "54" #Professional, Scientific, and Technical Services

#response = urllib2.urlopen('http://api.census.gov/data/2012/ewks?get=EMP,NAICS2012_TTL,OPTAX,GEO_TTL&for=county:016&in=state:02&NAICS2012=31-33')
URL = 'http://api.census.gov/data/2012/ewks?get='+dataToGet+'&for=county:'+county+'&in=state:'+state+'&NAICS2012='+NAICS+'&key='+api_key
#print(URL)
request = urllib.request.Request(URL)
response = urllib.request.urlopen(request)
encoding = response.info().get_content_charset('utf8')
output = json.loads(response.read().decode(encoding))


print(output)