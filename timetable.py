class component:
    def __init__(self, courseCode, instructor, days, hour):
        self.courseCode = courseCode
        self.instructor = instructor
        self.days = days
        self.hour = hour

class timeTable:
    def __init__(self):
        self.table = [[]]

    def addComponent(self, component):
        for day in component.days:
            self.table[day][component.hour] = (component.courseCode, component.instructor) 