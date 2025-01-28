from persistence import *

def print_table(name, dao, order_by="id"):
    """Prints a database table sorted by a given column."""
    print(name)
    for row in sorted(dao.find_all(), key=lambda x: getattr(x, order_by)):
        print(row)

def print_employees_report():
    """Prints an employee report with total sales income."""
    print("Employees report")

    employees = sorted(repo.employees.find_all(), key=lambda e: e.name)
    for employee in employees:
        # Get all sales activities for this employee
        sales = [a for a in repo.activities.find(activator_id=employee.id) if a.quantity < 0]

        # Compute total sales income: sum of (quantity * price)
        total_sales_income = sum(abs(s.quantity) * repo.products.find(id=s.product_id)[0].price for s in sales)

        branch = repo.branches.find(id=employee.branche)[0].location
        print(f"{employee.name} {employee.salary} {branch} {total_sales_income}")

def print_activities_report():
    """Prints an activities report sorted by date."""
    print("Activities report")

    activities = sorted(repo.activities.find_all(), key=lambda a: a.date)
    for activity in activities:
        product = repo.products.find(id=activity.product_id)[0]
        seller = repo.employees.find(id=activity.activator_id)
        supplier = repo.suppliers.find(id=activity.activator_id)

        seller_name = seller[0].name if seller else "None"
        supplier_name = supplier[0].name if supplier else "None"

        print(f"{activity.date}, {product.description}, {activity.quantity}, {seller_name}, {supplier_name}")


def main():
    """Main function to print database tables and reports."""
    print_table("Activities", repo.activities, "date")
    print_table("Branches", repo.branches)
    print_table("Employees", repo.employees)
    print_table("Products", repo.products)
    print_table("Suppliers", repo.suppliers)

    print_employees_report()
    print_activities_report()

if __name__ == '__main__':
    main()