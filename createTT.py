import pickle, re, json

class CustomUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        if name == 'component':
            from component_class import component
            return component
        return super().find_class(module, name)


def load_obj(name):
    name = "/home/returnz/TimeTableAutomation/objects.pkl"
    with open(name, "rb") as f:
        return pickle.load(f)



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

dayToNum = {'M' : 1, 'T' : 2, 'W' : 3, 'Th' : 4, 'F' : 5, 'S' : 6}
timeTable = {}

def returnData(stream,year,sem):

    objects = CustomUnpickler(open('/home/returnz/TimeTableAutomation/objects.pkl', 'rb')).load()
    cdc = CustomUnpickler(open('/home/returnz/TimeTableAutomation/cdc.pkl', 'rb')).load()

    days, hours = 6, 12

    courses = cdc[stream][(year, sem)]
    #print(courses)


    for day in range(1,7):
        timeTable[day] = {}
        for hour in range(1,13):
            timeTable[day][hour] = []

    for course in courses:
        for tup in objects:
            if tup[0] == course:
                for courseType in objects[tup]:
                    #print(tup, courseType)
                    if objects[tup][courseType]:
                        for obj in objects[tup][courseType]:
                            dayArr = obj.days
                            hourArr = obj.hours
                            if checkFree(timeTable, dayArr, hourArr) and 1 not in hourArr and dayCanBeLoaded(timeTable, dayArr):
                                for day in dayArr:
                                    for hour in hourArr:
                                        timeTable[dayToNum[day]][hour].append(f"{tup[0]} {courseType[0]}")
                                break
                            #else:
                                #print(f"clash @ {tup[0]}")
    return timeTable
# for day in timeTable:
#     print(timeTable[day])
#with open('timetable.json', 'w', encoding='utf-8') as f:
#    json.dump(timeTable, f, ensure_ascii=False, indent=4)
