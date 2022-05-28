import datetime

class Note:
    def __init__(self, author: str, text: str):
        self.author = author
        self.text = text
        self.created = datetime.datetime.now().hour, datetime.datetime.now().minute

    def __repr__(self):
        return f"{self.author}, {self.text}, {self.created[0]}:{self.created[1]}"

class Notebook:

    def __init__(self):
        self.notes: list[Note] = []

    def add_new_note(self, author: str, content: str) -> None:
        self.notes.append(Note(author, content))

    def add_note(self, note: Note) -> None:
        self.notes.append(note)

    def show_all(self) -> str:
        print("Masz następujące notatki:")
        for note in self.notes:
            print(note)

    def how_many_notes(self) -> str:
        print(f"Ilość notatek w notatniku: {len(self.notes)}")



def main():
    nb = Notebook()
    nb.add_new_note("Robert", "Umyć samochód")
    new_note = Note("Alicja", "Zadanie domowe - dokończyć")
    nb.add_note(new_note)
    nb.show_all()
    nb.how_many_notes()


if __name__ == "__main__":
    main()
