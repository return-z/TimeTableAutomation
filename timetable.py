import pickle, re, json
import pandas as pd

class component:
    pass

def load_obj(name):
    with open(name + ".pkl", "rb") as f:
        return pickle.load(f)

objects = load_obj("objects")
cdc = load_obj("cdc")

stream = "B2"
year, sem = 1, 1
days, hours = 6, 12

courses = cdc[stream][(year, sem)]
print(courses)
dayToNum = {'M' : 1, 'T' : 2, 'W' : 3, 'Th' : 4, 'F' : 5, 'S' : 6}
timeTable = {}
for day in range(1,7):
    timeTable[day] = {}
    for hour in range(1,13):
        timeTable[day][hour] = []

def checkFree(timetable, dayarray, hourarray):
    for day in dayarray:
        for hour in hourarray:
            if timetable[dayToNum[day]][hour]:
                return False
    return True

def dayCanBeLoaded(timetable, dayarray):
    for day in dayarray:
        day = dayToNum[day]
        count = 0
        for slot in range(1,13):
            if timeTable[day][slot]:
                count += 1
        if (count > 5):
            return False
    return True

for course in courses:
    for tup in objects:
        if tup[0] == course:
            for courseType in objects[tup]:
                print(tup, courseType)
                if objects[tup][courseType]:
                    for obj in objects[tup][courseType]:
                        dayArr = obj.days
                        hourArr = obj.hours
                        if checkFree(timeTable, dayArr, hourArr) and 1 not in hourArr and dayCanBeLoaded(timeTable, dayArr):
                            for day in dayArr:
                                for hour in hourArr:
                                    timeTable[dayToNum[day]][hour].append(f"{tup[0]} {courseType[0]}")
                            break
                        else:
                            print(f"clash @ {tup[0]}")
# for day in timeTable:
#     print(timeTable[day]) 
with open('timetable.json', 'w', encoding='utf-8') as f:
    json.dump(timeTable, f, ensure_ascii=False, indent=4)


