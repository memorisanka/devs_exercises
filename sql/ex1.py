import sqlite3


class Database:
    def __init__(self, path: str) -> None:
        self.con = sqlite3.connect(path)

    def create_table(self) -> None:
        query = "CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, name TEXT NOT NULL, surname " \
                "TEXT NOT NULL, date_joined DATE NOT NULL);"
        self.con.execute(query)

    def add_to_customers(self, name: str, surname: str, date_joined) -> None:
        query = "INSERT INTO Customers(name, surname, date_joined) VALUES(?, ?, ?)"
        self.con.execute(query, (name, surname, date_joined))

    def preview_table(self, table_name: str) -> None:
        query = f"SELECT * FROM {table_name}"
        results = self.con.execute(query).fetchall()
        print(results)

    def delete_from_customers(self, name: str, surname: str) -> None:
        query = f"DELETE FROM Customers WHERE name='{name}' AND surname='{surname}'"
        self.con.execute(query)

    def update_customers_name(self, new_name: str, old_name: str) -> None:
        query = f"UPDATE Customers SET name='{new_name}' WHERE name='{old_name}'"
        self.con.execute(query)

    def update_customers_surname(self, new_surname: str, old_surname: str) -> None:
        query = f"UPDATE Customers SET surname='{new_surname}' WHERE surname='{old_surname}'"
        self.con.execute(query)

    def update_customers_date(self, new_date: str, old_date: str) -> None:
        query = f"UPDATE Customers SET date_joined='{new_date}' WHERE date_joined='{old_date}'"
        self.con.execute(query)

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()

        self.con.close()


with Database('example2-data') as db:
    db.create_table()
    db.add_to_customers('John', 'Wick', '2000-09-02')
    db.add_to_customers('James', 'Bond', '2002-05-16')
    db.delete_from_customers('James', 'Bond')
    db.delete_from_customers('John', 'Wick')
    db.add_to_customers('John', 'Wick', '2000-09-02')
    db.update_customers_name('Barbara', 'John')
    db.update_customers_surname('Streissand', 'Wick')
    db.preview_table('Customers')
