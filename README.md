# BGUMart - Inventory Management System

**SPL Assignment 4, Fall 2024, Ben-Gurion University**

---

## Overview

This project implements a basic inventory and supply management system backed by an SQLite database. It provides functionality for initializing the database, populating it with initial data, performing actions (such as sales and restocking), and printing the database state.

The project follows the requirements of **SPL Assignment 4 (Fall 2024)** for the SPL course.

## Project Structure

- **`persistence.py`**: 
  - Defines the **DTOs** (Data Transfer Objects): `Employee`, `Supplier`, `Product`, `Branche`, and `Activitie`.
  - Defines the **Repository** class that manages the SQLite connection, table creation, and basic command execution.
  - Creates a singleton instance `repo` for global access.

- **`dbtools.py`**:
  - Provides an `orm` function to map database rows to DTO instances.
  - Defines a generic `Dao` class to perform CRUD operations (insert, find, delete) on each table.

- **`initiate.py`**:
  - Responsible for initializing the database from an input file.
  - Reads commands from a file to add `branches`, `suppliers`, `products`, and `employees`.

- **`action.py`**:
  - Reads an input file describing inventory activities (sales, restocking) and applies these actions to the database.

- **`printdb.py`**:
  - Prints the current content of all tables in the database in a human-readable format.

## Running the Project

1. **Initialize the database**

   ```bash
   python initiate.py <initialization_input_file>
   ```

2. **Apply actions**

   ```bash
   python action.py <actions_input_file>
   ```

3. **Print the database state**

   ```bash
   python printdb.py
   ```

## Notes
- The database file is named **`bgumart.db`**.
- Each module uses the shared `repo` instance from `persistence.py`.
- The system ensures proper database closure using `atexit`.

---

## Authors
- Guy Stein
- Guy Zilberstein
