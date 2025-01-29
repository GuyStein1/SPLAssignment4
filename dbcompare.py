import sqlite3

class DBCompare:
    def __init__(self, db1_path, db2_path):
        self.db1_conn = sqlite3.connect(db1_path)
        self.db2_conn = sqlite3.connect(db2_path)

    def _fetch_all_data(self, conn, table_name):
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()

    def compare_tables(self, table_name):
        db1_data = self._fetch_all_data(self.db1_conn, table_name)
        db2_data = self._fetch_all_data(self.db2_conn, table_name)
        return db1_data == db2_data

    def compare_all_tables(self):
        tables = ["employees", "suppliers", "products", "branches", "activities"]
        results = {}
        for table in tables:
            results[table] = self.compare_tables(table)
        return results

    def close(self):
        self.db1_conn.close()
        self.db2_conn.close()

if __name__ == '__main__':
    db1_path = "bgumart.db"
    db2_path = "bgumart_after_action.db"
    comparer = DBCompare(db1_path, db2_path)
    comparison_results = comparer.compare_all_tables()
    for table, result in comparison_results.items():
        print(f"Table {table}: {'Match' if result else 'Mismatch'}")
    comparer.close()
