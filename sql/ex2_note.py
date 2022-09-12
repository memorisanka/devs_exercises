import datetime
import sqlite3


class Notebook:

    @staticmethod
    def menu():
        menu = """ 
        Welcome to your notebook!
        ------------------------- 
        1: Add note
        2. See all notes
        3. Delete note
        4. Exit
        -------------------------
        """
        print(menu)

    @staticmethod
    def run():
        while True:
            Notebook.menu()
            choice = input("What do you want to do? Pick the number: ")
            with Database() as db:
                db.create_table()
                if choice == "1":
                    title = input("Title: ")
                    note = input("Note: ")
                    db.add_to_notebook(title, note)
                    print("Note has been added.")
                elif choice == "2":
                    db.preview_table()
                elif choice == "3":
                    title = input("Enter note's title to delete: ")
                    try:
                        db.delete_from_notebook(title)
                    except:
                        print("There isn't such note in your notebook.")
                    else:
                        print("Your note has been removed.")
                elif choice == "4":
                    exit()


class Database: # NotebookDatabaseHandler
    def __init__(self) -> None:
        self.con = sqlite3.connect('notebook.db')

    def create_table(self) -> None:
        query = "CREATE TABLE IF NOT EXISTS Notebook(id INTEGER PRIMARY KEY, title TEXT NOT NULL, note " \
                "TEXT NOT NULL, date DATE NOT NULL);"
        self.con.execute(query)

    def add_to_notebook(self, title: str, note: str, date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) -> None:
        query = "INSERT INTO Notebook(title, note, date) VALUES(?, ?, ?)"
        self.con.execute(query, (title, note, date))

    def preview_table(self) -> None:
        """XYZ"""
        query = f"SELECT * FROM Notebook"
        results = self.con.execute(query).fetchall()
        for result in results:
            print(f"id: {result[0]}, title: {result[1]}, note: {result[2]}, date: {result[3]}")

    def delete_from_notebook(self, title: str) -> None:
        query = f"DELETE FROM Notebook WHERE title='{title}'"
        self.con.execute(query)

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()

        self.con.close()


def main():
    notebook = Notebook()
    notebook.run()


if __name__ == "__main__":
    main()
