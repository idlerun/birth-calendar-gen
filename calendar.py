import json, math
from pprint import pprint

YEAR=2019
tree=set(["schmill","schmob"])

#https://stackoverflow.com/a/20007730/460976
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

with open('dates.json') as f:
  data = json.load(f)

for month in range(1,13):
  for day in range(1,32):
    date = "%02d-%02d" % (month, day)
    for p in data['people']:
      if len(tree.intersection(set(p['tree']))) == 0:
        continue
      if p['birth'].endswith(date):
        if 'death' in p:
          print("%s = Birth: %s in %s" % (p['birth'], p['name'], p['birth']))
        else:
          year = int(p['birth'][:4])
          if year == 0:
            age = "???"
          else:
            age = "%d" % (YEAR - year)
          print("%s = Birth: %s turns %s" % (p['birth'], p['name'],age))
      if 'death' in p and p['death'].endswith(date):
        year = p['death'][0:4]
        print("%s = Death: %s passed in %s" % (p['death'], p['name'], year))
    for p in data['weddings']:
      if len(tree.intersection(set(p['tree']))) == 0:
        continue
      if p['date'].endswith(date):
        age = YEAR - int(p['date'][:4])
        print("%s = Anniversary: %s & %s's %s anniversary" % (p['date'], p['husband'],p['wife'],ordinal(age)))

#pprint(data)