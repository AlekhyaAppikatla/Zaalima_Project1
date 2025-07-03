import json

# Base class
class Employee:
    def __init__(self, emp_id, name, dept, salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        try:
            self.salary = float(salary)
        except ValueError:
            raise ValueError("Salary must be a number")

    def yearly_salary(self):
        return self.salary * 12

    def display(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.dept}, Salary: {self.salary}"

# Manager subclass
class Manager(Employee):
    def __init__(self, emp_id, name, dept, salary, team_size):
        super().__init__(emp_id, name, dept, salary)
        self.team_size = int(team_size)

    def bonus(self):
        return 0.1 * self.yearly_salary() if self.team_size > 5 else 0

    def display(self):
        return f"{super().display()}, Team: {self.team_size}, Bonus: {self.bonus()}"

# Employee records
employees = {}

# Load from file
def load_data():
    try:
        with open("employees.txt", "r") as file:
            data = json.load(file)
            for eid, info in data.items():
                if info["type"] == "Manager":
                    emp = Manager(eid, info["name"], info["dept"], info["salary"], info["team_size"])
                else:
                    emp = Employee(eid, info["name"], info["dept"], info["salary"])
                employees[eid] = emp
    except:
        pass

# Save to file
def save_data():
    data = {}
    for eid, emp in employees.items():
        if isinstance(emp, Manager):
            data[eid] = {"type": "Manager", "name": emp.name, "dept": emp.dept, "salary": emp.salary, "team_size": emp.team_size}
        else:
            data[eid] = {"type": "Employee", "name": emp.name, "dept": emp.dept, "salary": emp.salary}
    with open("employees.txt", "w") as file:
        json.dump(data, file)

# Add employee
def add_employee():
    try:
        eid = input("ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        salary = input("Salary: ")
        emp = Employee(eid, name, dept, salary)
        employees[eid] = emp
        print("Employee added.")
    except ValueError as e:
        print(e)

# Add manager
def add_manager():
    try:
        eid = input("ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        salary = input("Salary: ")
        team_size = input("Team size: ")
        mgr = Manager(eid, name, dept, salary, team_size)
        employees[eid] = mgr
        print("Manager added.")
    except ValueError as e:
        print(e)

# Search
def search_employee():
    eid = input("Enter Employee ID: ")
    emp = employees.get(eid)
    if emp:
        print(emp.display())
    else:
        print("Employee not found.")

# Show all
def show_all():
    if not employees:
        print("No records.")
    for emp in employees.values():
        print(emp.display())

# Sort by salary
def sort_salary():
    sorted_list = sorted(employees.values(), key=lambda e: e.salary, reverse=True)
    for emp in sorted_list:
        print(emp.display())

# Menu
def menu():
    load_data()
    while True:
        print("\n--- Employee System ---")
        print("1. Add Employee")
        print("2. Add Manager")
        print("3. Search by ID")
        print("4. Display All")
        print("5. Sort by Salary")
        print("6. Save & Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            add_manager()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            show_all()
        elif choice == "5":
            sort_salary()
        elif choice == "6":
            save_data()
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

# Run
if __name__ == "__main__":
    menu()
