from persistence import *

def print_table(name, table_name, order_by="id"):
    print(name + "\n")
    query = f"SELECT * FROM {table_name} ORDER BY {order_by};"
    results = repo.execute_command(query)
    for row in results:
        print(row, "\n")  

def print_employees_report():

    print("Employees report\n")

    query = """
        SELECT 
            employees.name,
            employees.salary,
            branches.location,
            IFNULL(SUM(ABS(activities.quantity) * products.price), 0) AS total_sales_income
        FROM employees
        JOIN branches ON employees.branche = branches.id
        LEFT JOIN activities ON employees.id = activities.activator_id AND activities.quantity < 0
        LEFT JOIN products ON activities.product_id = products.id
        GROUP BY employees.id
        ORDER BY employees.name;
    """

    results = repo.execute_command(query)
    for row in results:
        print(" ".join(map(str, row)) + "\n") 

def print_activities_report():
    """Prints an activities report using SQL SELECT with JOIN and ORDER BY."""
    print("Activities report\n")

    query = """
        SELECT 
            activities.date,
            products.description,
            activities.quantity,
            CASE WHEN activities.quantity < 0 THEN employees.name ELSE NULL END AS seller_name,
            CASE WHEN activities.quantity > 0 THEN suppliers.name ELSE NULL END AS supplier_name
        FROM activities
        LEFT JOIN products ON activities.product_id = products.id
        LEFT JOIN employees ON activities.activator_id = employees.id
        LEFT JOIN suppliers ON activities.activator_id = suppliers.id
        ORDER BY activities.date;
    """

    results = repo.execute_command(query)
    for activity in results:
        print(activity, "\n")  


def main():
    """Main function to print database tables and reports using SQL queries."""
    print_table("Activities", "activities", "date")
    print_table("Branches", "branches")
    print_table("Employees", "employees")
    print_table("Products", "products")
    print_table("Suppliers", "suppliers")

    print_employees_report()
    print_activities_report()

if __name__ == '__main__':
    main()
