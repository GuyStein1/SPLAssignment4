from persistence import *

import sys
import os

def add_branche(splittedline : list[str]):
    id, location, num_employees = splittedline
    repo.branches.insert(Branche(int(id), location, int(num_employees)))

def add_supplier(splittedline : list[str]):
    id, name, contact_info = splittedline

    # Ensure the ID is not already used by an employee
    if repo.employees.find(id=int(id)):
        return  # Ignore if the ID is already an employee
    
    repo.suppliers.insert(Supplier(int(id), name, contact_info))

def add_product(splittedline : list[str]):
    id, description, price, quantity = splittedline
    repo.products.insert(Product(int(id), description, float(price), int(quantity)))

def add_employee(splittedline : list[str]):
    id, name, salary, branch_id = splittedline

    # Ensure the ID is not already used by a supplier
    if repo.suppliers.find(id=int(id)):
        return  # Ignore if the ID is already a supplier
    
    repo.employees.insert(Employee(int(id), name, float(salary), int(branch_id)))

adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    inputfilename = args[1]

    # delete the database file if it exists
    repo._close()
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")

    # Reinitialize database
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)