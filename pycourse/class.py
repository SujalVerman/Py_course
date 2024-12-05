class Employee:
    name = "Harry"
    language = "Py"
    salary = 120000
    def getinfo(out):
        print(f"The language is {out.language} and the salary is {out.salary}")

harry = Employee()
print(harry.name, harry.salary)
rohan = Employee()
harry.getinfo()
rohan.names = "Hello bhai" # This is an instance attribute
print(rohan.names)