import Clock
class Shift:
    """
    bulding the object it gets a start time that is a clock object
    """
    def __init__(self, start, finish=None):
        exeption = False
        try:
            self.duration = finish-start
        except:
            exeption = True
        finally:
            if exeption:
                self.duration = start
        
    """
    print the object shift
    """
    def __repr__(self):
        return str(self.duration)
    
    """
    add shifts to one onther 
    """
    def __add__(self,other):
        if self.duration.minutes + other.duration.minutes > 59:
            return Shift(Clock.Clock(self.duration.hours + other.duration.hours + 1,self.duration.minutes + other.duration.minutes - 60))
        return Shift(Clock.Clock(self.duration.hours + other.duration.hours,self.duration.minutes + other.duration.minutes))
