class Employee():

    def __init__(self,empId,empName,DeptNo):
        self.empId = empId
        self.empName = empName
        self.deptNo = DeptNo

    def __hash__(self):
        return hash(str(self.deptNo)+str(self.empId))
    
    def __eq__(self, value):
        return self.__hash__() == value.__hash__()
    
def fun():
    pass
    
