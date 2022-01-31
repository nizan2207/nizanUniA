class Clock:
    """
    bulding the object it gets hours and optional minutes
    """
    def __init__(self, hours, minutes=0):
        self.hours = hours
        self.minutes = minutes
    """
    printing the object Clock
    """    
    def __repr__(self):
        if self.hours<10 and self.minutes<10: # setting the right amount of number to be if it is less tha 2 numbers we put the number zero infront of the number 
            return "0"+str(self.hours) + ":0" + str(self.minutes)
        if self.minutes<10:
            return str(self.hours) + ":0" + str(self.minutes)
        if self.hours<10:
            return "0"+str(self.hours) + ":" + str(self.minutes)
        return str(self.hours) + ":" + str(self.minutes)
    """
    oparator that add clock to onther object or int or clock
    """
    def __add__(self,other):
        if isinstance(other,int):
            other = Clock(other)
        if self.minutes + other.minutes > 59:
            return Clock(self.hours + other.hours + 1,(self.minutes + other.minutes)-60)
        else:    
            return Clock(self.hours + other.hours,self.minutes + other.minutes)
    """
    oparator that add clock to onther object or int or clock
    """
    def __radd__(self,other):
        return self + other
    """
    operator that check if clocks are equal to one onther
    """
    def __eq__(self,other):
        return self.hours == other.hours and self.minutes == other.minutes
    """
    operator the checks if the clock of the right side is or equal or smaller than the object from the left
    """
    def __lt__(self,other):
        if self.hours == other.hours:
            return self.minutes<other.minutes
        return self.hours<other.hours
    """
    operator the checks if the clock of the right side is or equal or bigger than the object from the left
    """
    def __le__(self,other):
        if self.hours == other.hours:
            return self.minutes<=other.minutes
        if self==other:
            return True
        return self.hours<=other.hours
    """
    operator the checks if the clock of the right side is bigger than the object from the left
    """
    def __gt__(self,other):
        if self.hours == other.hours:
            return self.minutes>other.minutes
        return self.hours>other.hours
    """
    operator the checks if the clock of the right side is or smaller than the object from the left
    """
    def __ge__(self,other):
        if self.hours == other.hours:
            return self.minutes>=other.minutes
        if self==other:
            return True
        return self.hours>=other.hours
    """
    operator that sub betwween clocks
    """
    def __sub__(self,other):
        if self < other:
            raise ValueError("Right side clock is greater than left side")
        else:
            if self.minutes - other.minutes<0:
                return Clock(self.hours-other.hours-1,self.minutes-other.minutes+60)
            return Clock(self.hours-other.hours,self.minutes-other.minutes)


