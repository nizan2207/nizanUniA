import Clock
import Shift
import Employee
class SuperMarket:
    """
    building the object supermarket
    """
    def __init__(self):
        self.employees = {}
    """
    adding an emplyee to the dictionary of emplyees that are hiered in th supermarket
    the function get the employee we want to add
    """
    def add_employee(self, employee):
        if employee.name in self.employees:
            return False
        else:
            self.employees[employee.name] = employee
        return True
    """
    remove an emplyee from the dictionary of the supermarket and return that emplyee
    the function get the name of the emplyee we want to remove
    """
    def remove_employee(self, employee_name):
        if employee_name in self.employees:
            m = self.employees.get(employee_name)
            self.employees.pop(employee_name)
            return m
        else:
            return None
    """
    the fucntion add a shift to an emplyee 
    the function get the name of the emplyee and a shift he did
    """
    def add_shift(self, name, shift):
        if name in self.employees:
            m = self.employees.get(name)
            m.add_shift(shift)
            temp = {name: m}
            self.employees.update(temp)
    """
    print the objct supermarket
    """
    def __repr__(self):
        res = ""
        lst = []
        for x in self.employees:
            lst.append(x)
        if len(lst) == 0:
            return "No employees found."
        lst.sort()
        for i in range(len(lst)):
            m = self.employees.get(lst[i])
            res += str(m) + "\n"
        return res



