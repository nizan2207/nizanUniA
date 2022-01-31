import Shift
import Clock
import copy
class Employee:
    """
    bulding the object it gets name of the employee
    """
    def __init__(self,name):
        self.name = name
        self.__shifts =[]
    """
    print the object of Empolyee
    """
    def __repr__(self):
        return "Employee Name: "+ self.name + "\nEmployee Shifts: " + str(self.__shifts)
    """
    add to the property list of shifts onther shift for the empolyee
    """
    def add_shift(self, shift):
        self.__shifts.append(shift)
    """
    return the list of the sifts for the employee
    """
    def get_shifts(self):
        return copy.deepcopy(self.__shifts)
    
class Manager(Employee):
    """
    bulding the object it gets name the the salary he gets. it inheratace from employee
    """
    def __init__(self, name, salary):
        Employee.__init__(self,name)
        self.salary = salary
    """
    calculate the salary of the manager by the rules we were given
    """
    def calculate_salary(self):
        Sumshifts = Shift.Shift(Clock.Clock(0,0),Clock.Clock(0,0))
        for i in range(len(self.get_shifts())):
            Sumshifts += self.get_shifts()[i]
        if Sumshifts.duration.hours >= 80:
            return self.salary
        else:
            return int(((Sumshifts.duration.hours + (Sumshifts.duration.minutes / 60))/ 80) * self.salary)
    """
    print the object manager
    """
    def __repr__(self):
        res = Employee.__repr__(self)
        res += "\nSalary: " + str(self.calculate_salary()) + "\nPosition: Manager\n========================="
        return res

class Cashier(Employee):
    """
    bulding the object it gets name the the salary per an hour of work he gets. it inheratace from employee
    """
    def __init__(self, name, salary_per_hour):
        Employee.__init__(self,name)
        self.salary_per_hour = salary_per_hour
    """
    calculate the salary of a cashior by the rules we were given
    """
    def calculate_salary(self):
        SumSalary = 0
        for i in range(len(self.get_shifts())):
            temp = (self.get_shifts()[i].duration.hours + (self.get_shifts()[i].duration.minutes / 60))
            if temp>7.5:
                SumSalary += 7.5*self.salary_per_hour + (temp - 7.5)*self.salary_per_hour*1.3
            else:
                SumSalary += self.salary_per_hour*temp
        return int(SumSalary)
    """
    promote a cashier to manager it gets the cashier we want to promote and the slalry he is sappuse to get as a manager and we turn it into the object manager
    the function get the new salary
    """
    def promote(self, salary):
        m = Manager(self.name,salary)
        for i in range(len(self.get_shifts())):
            m.add_shift(self.get_shifts()[i])
        return m
    """
    print the object cashier
    """
    def __repr__(self):
        res = Employee.__repr__(self)
        res += "\nSalary: " + str(self.calculate_salary()) + "\nPosition: Cashier\n========================="
        return res


class Stocker(Employee):
    """
    bulding the object it gets name the the salary per an hour of work he gets. it inheratace from employee
    """
    def __init__(self, name, salary_per_hour):
        Employee.__init__(self,name)
        self.salary_per_hour = salary_per_hour
    """
    calculate the salary of a Stocker by the rules we were given
    """        
    def calculate_salary(self):
        SumSalary = 0
        for i in range(len(self.get_shifts())):
            temp = (self.get_shifts()[i].duration.hours + (self.get_shifts()[i].duration.minutes / 60))
            if temp>8:
                SumSalary += 8*self.salary_per_hour + (temp - 8)*self.salary_per_hour*1.25
            else:
                SumSalary += self.salary_per_hour*temp
        return int(SumSalary)        
    """
    promote a Stocker to cashier it gets the stocker we want to promote and upgrade his salary by adding to it 5 shekels and we turn it into the object cashier
    """
    def promote(self):
        m = Cashier(self.name,self.salary_per_hour+5)
        for i in range(len(self.get_shifts())):
            m.add_shift(self.get_shifts()[i])
        return m        
    """
    pront the object stocker
    """
    def __repr__(self):
        res = Employee.__repr__(self)
        res += "\nSalary: " + str(self.calculate_salary()) + "\nPosition: Stocker\n========================="
        return res