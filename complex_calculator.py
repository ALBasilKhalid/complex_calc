#ALBASILAL-RAWAHI            138410
"""
Algorithm:
1. Define a class named Employee to represent employees with attributes and methods.
2. Implement the __init__ method to initialize an Employee object with default values for SID, name, workplace, and title.
3. Implement getter methods to retrieve the employee's name and workplace, and a method to update the workplace.
4. Define a main function to interactively prompt the user for employee SID and display employee information.
5. Inside the main function, create a list of Employee objects with predefined attributes.
6. Continuously prompt the user to enter an employee SID until 'q' is entered to quit.
7. For each entered SID, iterate through the list of employees to find a match by SID.
8. If an employee with the entered SID is found, display their title, name, SID, and workplace.
9. If no matching employee is found, notify the user that the employee with the entered SID was not found.
10. Exit the program when the user enters 'q' to quit.    

"""

class Employee:
  """
  This class represents an employee with attributes and methods.
  """

  def __init__(self, sid="00000", name="", workplace="SQU", title="Mr."):
    """
    Initializes an Employee object.

    Args:
      sid: The employee's ID (default: "00000").
      name: The employee's name (default: "").
      workplace: The employee's workplace (default: "SQU").
      title: The employee's title (default: "Mr.").
    """
    self.sid = sid
    self.name = name
    self.workplace = workplace
    self.title = title

  def get_name(self):
    """
    Returns the employee's name.
    """
    return self.name

  def get_workplace(self):
    """
    Returns the employee's workplace.
    """
    return self.workplace

  def update_workplace(self, new_workplace):
    """
    Updates the employee's workplace.

    Args:
      new_workplace: The new workplace for the employee.
    """
    self.workplace = new_workplace


def main():
  # Create a list of employees
  employees = [
      Employee("12345", "Basil", "HQ", "MR."),
      Employee("54321", "Ahmed", "R&D"),
      Employee("98765", "Ali", "Sales"),
      Employee("21098", "Masood", "Marketing"),
      Employee("76543", "Khatab", "Finance"),
      Employee("32109", "Omar", "IT"),
      Employee("87654", "Asma", "HR"),
      Employee("43210", "Yara", "Legal"),
      Employee("09876", "Samir", "Customer Service"),
      Employee("65432", "Ahmed", "Operations"),
  ]

  while True:
    # Get user input for SID
    sid = input("Enter employee SID (or 'q' to quit): ")
    if sid == 'q':
      break

    # Find employee by SID
    found_employee = None
    for employee in employees:
      if employee.sid == sid:
        found_employee = employee
        break

    # Display employee information if found
    if found_employee:
      print(f"{found_employee.title} {found_employee.name} (SID: {found_employee.sid}) works at {found_employee.get_workplace()}.")
    else:
      print(f"Employee with SID {sid} not found.")


if __name__ == "__main__":
  main()
