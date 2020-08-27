import pickle, re

class component:
    pass

def load_obj(name):
    with open(name + ".pkl", "rb") as f:
        return pickle.load(f)

objects = load_obj("objects")
cdc = load_obj("cdc")
yearWise = {}

for i in range(1,8):
    yearWise[i] = {}

for tup in objects:
    courseCode = tup[0]
    code = re.split(r"\s", courseCode)
    try:
        if code[1][0] == "F":
            yearWise[int(code[1][1])][tup] = objects[tup]
    except:
        pass

# print(yearWise[3])     

for course in yearWise[1]:
    print(course)
    for componentType in yearWise[1][course]:
        print(componentType, [(obj.days, obj.hours) for obj in yearWise[1][course][componentType]])
    print("\n")

# print(cdc)