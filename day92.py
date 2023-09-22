import requests
timezone = "GMT"
latitude = 52.2906
longitude = -1.5427

#----------WMO CODE LOOKUP--------
codes = requests.get("http://codes.wmo.int/wmdr/DataFormat/csv")
coderead = codes.text

f = open('codes.csv', 'r')

codelist = []
while True:
  line = f.readline()[4:]
  codelist.append(line)
  if line == "":
    break

f.close()

#---READ IN LOCATION AND WEATHER---

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()["daily"]

weathercode = result.json()["daily"]["weathercode"][-1]
weatherdesc=codelist[weathercode]
mintemp = result.json()["daily"]["temperature_2m_max"][-1]
maxtemp = result.json()["daily"]["temperature_2m_min"][-1]

print(weatherdesc)
print("Max: "+str(maxtemp)+"    Min:"+str(mintemp))