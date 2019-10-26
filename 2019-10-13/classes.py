class Time:
    hour = 0
    minute = 0
    second = 0

    # Байгуулагч функц
    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s

    def printTime(self):
        print("%d:%d:%d" % (self.hour,self.minute, self.second))

    def addSeconds(self, secondsToAdd):
        self.second = self.second + secondsToAdd
        s_mod = self.second % 60
        s_div = self.second // 60
        self.second = s_mod
        self.minute = self.minute + s_div
        m_mod = self.minute % 60
        m_div = self.minute // 60
        self.minute = m_mod
        self.hour = self.hour + m_div
        self.hour = self.hour % 24

    # Return Boolean
    # True - self < time2
    # False - self >= time2
    def isAfter(self, time2):
        if(self.hour < time2.hour):
            return True
        elif(self.hour == time2.hour and self.minute < time2.minute):
            return True
        elif(self.hour == time2.hour and self.minute == time2.minute and self.second < time2.second):
            return True

        return False


timeObject_1 = Time(17, 30, 00)
timeObject_1.addSeconds(40)
timeObject_1.printTime()

timeObject_2 = Time()
timeObject_2.printTime()

print(timeObject_2.isAfter(timeObject_1))