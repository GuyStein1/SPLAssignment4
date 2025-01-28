from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            product_id = int(splittedline[0])
            quantity = int(splittedline[1])
            activator_id = int(splittedline[2])
            date = splittedline[3]

            # Get product info
            product = repo.products.find(id=product_id)
            if not product:
                continue  # Ignore if product doesn't exist

            product = product[0]  # Extract the Product object

            # Handle supply (supplier provides stock)
            if quantity > 0:
                supplier = repo.suppliers.find(id=activator_id)
                if supplier:  # Ensure the supplier exists
                    product.quantity += quantity  # Increase stock
                    repo.products.insert(product)  # Update product quantity
                    repo.activities.insert(Activitie(product_id, quantity, activator_id, date))

            # Handle sale (employee sells stock)
            elif quantity < 0:
                employee = repo.employees.find(id=activator_id)
                if employee and product.quantity >= abs(quantity):  # Ensure employee exists & enough stock
                    product.quantity += quantity  # Reduce stock
                    repo.products.insert(product)  # Update product quantity
                    repo.activities.insert(Activitie(product_id, quantity, activator_id, date))

if __name__ == '__main__':
    main(sys.argv)