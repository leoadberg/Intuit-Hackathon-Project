import urllib.request
import json
from numpy import genfromtxt
import locale
import sys
import io

api_key = "3d4047590356727bf89cab9124ab1340c179068c"

states = []
naics = []
minSalary = [0]
maxSalary = [100000000]
prediction = [10]

# Code to turn a state/county name into a FIPS code and back
locale.setlocale(locale.LC_ALL, 'en_US')
stateCodes = genfromtxt("codes/FIPS.txt", dtype="str", delimiter="	")
countyCodes = genfromtxt("codes/Counties.txt", dtype="str", delimiter="	")
industryCodes = genfromtxt("codes/NAICS.txt", dtype="str", delimiter="	")
def FIPSToCounty(state, county):
	for i in range(len(countyCodes)):
		if countyCodes[i][0] == state:
			if int(countyCodes[i][1]) == int(county):
				return countyCodes[i][2]
	#print("Could not get county "+county+" in state "+state)
	return "Unknown County"
def FIPSToState(fips):
	for i in range(len(stateCodes)):
		if stateCodes[i][0] == fips:
			return stateCodes[i][1]
def StateToFIPS(state):
	for i in range(len(stateCodes)):
		if stateCodes[i][1] == state:
			return stateCodes[i][0]
def NAICSToIndustry(NAICS):
	for i in range(len(industryCodes)):
		if industryCodes[i][0] == NAICS:
			return industryCodes[i][1]

# Parse arguments and put them into the right lists
currentSelected = None
for arg in sys.argv:
	if arg == "GetData.py":
		pass
	elif arg == "-state":
		currentSelected = states
	elif arg == "-NAICS":
		currentSelected = naics
	elif arg == "-minSalary":
		currentSelected = minSalary
	elif arg == "-maxSalary":
		currentSelected = maxSalary
	elif arg == "-prediction":
		currentSelected = prediction
	else:
		currentSelected.append(arg)
minSalary = int(minSalary[-1])
maxSalary = int(maxSalary[-1])
prediction = int(prediction[-1])


# Set up API query
#dataToGet = "PAYANN,ESTAB,EMP,NAICS2012_TTL,GEO_TTL"
#stateToSearch = "06" #California
#countyToSearch = "*" #Alameda
#NAICSToSearch = "54" #Professional, Scientific, and Technical Services
#URL = 'http://api.census.gov/data/2012/ewks?get='+dataToGet+'&for=county:'+countyToSearch+'&in=state:'+stateToSearch+'&NAICS2012='+NAICSToSearch+'&OPTAX=A&key='+api_key
#print(URL)
#request = urllib.request.Request(URL)
#response = urllib.request.urlopen(request)
#encoding = response.info().get_content_charset('utf8')
#output = json.loads(response.read().decode(encoding))

statesToSearch = [StateToFIPS(x) for x in states]
allData = {}
allData2002 = {}

for code in naics:
	with open('data/2012/'+code+".txt") as data_file:    
		data = json.load(data_file)
		allData[code] = data
	with open('data/2002/'+code+".txt") as data_file2:    
		data2 = json.load(data_file2)
		allData2002[code] = data2

#print(allData)
#0/0

finalData = []

PAYANN = list(allData.values())[0][0].index('PAYANN')
STATE = list(allData.values())[0][0].index('state')
COUNTY = list(allData.values())[0][0].index('county')
EMP = list(allData.values())[0][0].index('EMP')
NAICSYEAR = 3 #Kinda hardcoded in
for code in allData:
	for x in allData[code][1:]:
		#state = FIPSToState(x[output[0].index('state')])
		#print(x)
		if int(x[EMP]) == 0:
			averagePay = 0
		else:
			averagePay = int(x[PAYANN]) * 1000 / int(x[EMP])
		if averagePay >= minSalary and averagePay <= maxSalary:
			state = x[STATE]
			if FIPSToState(state) in states:
				thisEntry = []
				county = x[COUNTY]
				#Industry = x[allData[code][0].index('NAICS2012_TTL')]
				Industry = x[NAICSYEAR]
				employees = int(x[EMP])
				#print("In state: "+state)
				#print("In county: "+county)
				#print("Industry: "+Industry)
				#print("Average pay: $"+locale.format("%d", averagePay, grouping=True))
				thisEntry.append(state)
				thisEntry.append(county)
				thisEntry.append(Industry)
				thisEntry.append(employees)
				thisEntry.append(averagePay)
				finalData.append(thisEntry)

# Sort all entries by average pay
finalData = sorted(finalData, key = lambda x: -x[3])[0:20]

for entry in finalData:
	jobs = allData2002[entry[2]][1:]
	alreadyappended = False
	for x in jobs:
		if int(x[STATE]) == int(entry[0]) and int(x[COUNTY]) == int(entry[1]):
			if not alreadyappended:
				annual = int(x[PAYANN])
				employees = int(x[EMP])
			alreadyappended = True
	if not alreadyappended or employees == 0:
		entry.append(0)
		entry.append(0)
	else:
		entry.append(int(annual * 1000 / employees))
		entry.append(employees)




print(finalData)

for entry in finalData:
	print("In state: "+FIPSToState(entry[0]))
	print("In county: "+FIPSToCounty(entry[0], entry[1]))
	print("Industry: "+NAICSToIndustry(entry[2]))
	print("2002 Average Pay: $"+locale.format("%d", entry[5], grouping=True))
	print("2012 Average pay: $"+locale.format("%d", entry[4], grouping=True))
	print("Projected Avg. Pay in "+str(2016+prediction)+": $" + locale.format("%d", (entry[4] - entry[5]) / 10 * (2016 + prediction - 2012) + entry[4], grouping=True))
	if entry[6] == 0:
		print("Employee growth per year: Unknown")
	else:
		print("Employee growth per year: "+ str(((entry[3] - entry[6]) / entry[6] * 10)) + "%")

