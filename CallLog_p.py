def getDistinctValues(arr): 
    result = [] 
    for i in arr: 
        if i not in result: 
            result.append(i) 
    return result

def getFreePlan(arr): 
    result = [] 
    for i in arr: 
        seconds = int(i['duration'].split(':')[2])
        hrs = int(i['duration'].split(':')[0])
        mins = int(i['duration'].split(':')[1])
        if hrs == 0 and mins == 0 and seconds <= 59: 
            result.append(i['number']) 
    return result

callLogs = [
    "9898989898, 8989898989, 00:05:23", 
    "1898989898, 9989898989, 01:00:23", 
    "2898989898, 7989898989, 00:00:21",
    "2898989898, 6989898989, 00:00:23",
    "4898989898, 5989898989, 00:01:23",
    "5898989898, 4989898989, 00:05:55",
    "5898989898, 3989898989, 00:00:23",
    "7898989898, 2989898989, 00:02:23",
    "8898989898, 1189898989, 00:05:20",
    "1098989898, 8459898989, 00:00:23",
    "1898989898, 8967898989, 00:00:40",
    "2898989898, 8989898989, 00:05:23"
]
fromArray = []
fromArrayWithDuration = []
for x in callLogs:
    fromArray.append(x.split(',')[0])
    fromArrayWithDuration.append({'number': x.split(',')[0], 'duration': x.split(',')[2]})

distinctFromValues = getDistinctValues(fromArray)

freePlanNumbers = getFreePlan(fromArrayWithDuration)
distinctfreePlanNumbers = getDistinctValues(freePlanNumbers)
print("Distinct From Numbers for a day",distinctFromValues)
print("Distinct From Numbers who used the Free Plan" , distinctfreePlanNumbers)
