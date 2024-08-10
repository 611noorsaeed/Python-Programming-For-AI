def add_employee(employee_dict, emp_id, name, department):
    if emp_id not in employee_dict:
        employee_dict[emp_id] = {'Name': name, 'Department': department}
        print("Employee added successfully.....")
    else:
        print("Employee ID already exists.")


def remove_employee(employee_dict, emp_id):
    if emp_id in employee_dict:
        del employee_dict[emp_id]
        print("Employee removed successfully...")
    else:
        print("Employee ID not found.")


def update_employee(employee_dict, emp_id, name=None, department=None):
    if emp_id in employee_dict:
        if name:
            employee_dict[emp_id]['Name'] = name
        if department:
            employee_dict[emp_id]['Department'] = department
        print("Employee updated successfully...")
    else:
        print("Employee ID not found.")


def list_employees(employee_dict):
    print("\n\n Employee Records\n")
    if not employee_dict:
        print("No employees to display.")
    for emp_id, details in employee_dict.items():
        print(f"ID: {emp_id}, Name: {details['Name']}, Department: {details['Department']}")


# Main function
if __name__ == "__main__":
    employees = {}

    while True:
        print(
            "\n====================================Employee Management System============================================\n\n")
        print(" Press 1: To Add Employee.....")
        print("Press 2: To Remove Employee.....")
        print("Press 3: To Update Employee.....")
        print("Press 4: To List Employees.....")
        print("Press 5: To Exit.....")

        choice = int(input("\nEnter your choice (1, 2, 3, 4, 5)..............."))

        if choice == 1:
            id = int(input("Enter employee id........."))
            name = input("Enter employee name.........")
            department = input("Enter employee department.........")
            add_employee(employees, id, name, department)

        elif choice == 2:
            id = int(input("Enter employee id........."))
            remove_employee(employees, id)

        elif choice == 3:
            id = int(input("Enter employee id........."))
            name = input("Enter new employee name (leave blank to keep current).........")
            department = input("Enter new employee department (leave blank to keep current).........")
            update_employee(employees, id, name if name else None, department if department else None)

        elif choice == 4:
            list_employees(employees)

        elif choice == 5:
            print("Exiting the system...")
            break

        else:
            print("Please enter a valid choice...")
